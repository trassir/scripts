import re
import os
import host

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger


logger = get_logger()

__version__ = "1.0.1"
logger.debug("%s version: %s", __name__, __version__)

_email_valid_regexp = re.compile(r"[^@]+@[^@]+\.[^@]+")


class EmailError(Exception):
    pass


class EmailAccountNotFound(EmailError):
    pass


class EmailNotValid(EmailError):
    pass


def _win_encode_path(path):
    if os.name == "nt":
        try:
            path = path.decode("utf8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return path


class EmailSender(object):
    default_subject = "{server_name} -> {script_name}".format(
        server_name=host.settings("").name or "Client",
        script_name=host.stats().parent().name,
    )

    def __init__(self, account):
        self.__account = self.get_email_account(account)
        self.max_attachments_bytes = 25 * 1024 * 1024

    @staticmethod
    def get_email_account(account):
        if not account:
            raise ValueError("Empty account")

        for sett in host.settings("scripts").ls():
            if sett.type == "EmailAccount" and (sett.name == account or sett.guid == account):
                return sett

        raise EmailAccountNotFound(account)

    @staticmethod
    def email_is_valid(email):
        return bool(_email_valid_regexp.match(email))

    @classmethod
    def parse_mails(cls, emails):
        if not emails:
            raise ValueError("Empty emails")
        else:
            parsed_emails = []
            if isinstance(emails, (str, unicode)):
                emails = emails.split(",")

            for email in emails:
                if cls.email_is_valid(email):
                    parsed_emails.append(email)
                else:
                    raise EmailNotValid(email)
            return parsed_emails

    def _group_files_by_max_size(self, file_paths):
        """Split files to groups. Size of each group is less then max_size

        Args:
            file_paths (list): List of files
        """
        if not file_paths:
            return []

        group = []
        cur_size = 0
        for idx, file_path in enumerate(file_paths):
            encoded_file_path = _win_encode_path(file_path)
            if not os.path.isfile(encoded_file_path):
                logger.warning("File not found: %s", file_path)
                continue
            file_size = os.stat(encoded_file_path).st_size
            logger.debug("Add attachment %s: %s", file_size, file_path)
            if file_size >= self.max_attachments_bytes:
                logger.warning(
                    "%s size %s but max_attachments_bytes=%s",
                    file_path,
                    file_size,
                    self.max_attachments_bytes,
                )
            if not cur_size or (cur_size + file_size) < self.max_attachments_bytes:
                cur_size += file_size
                group.append(file_path)
            else:
                break
        else:
            return [group]

        return [group] + self._group_files_by_max_size(file_paths[idx:])

    def send(self, mails, text="", attachments=None, subject=None):
        logger.debug(
            "Sending email %r, text=%r, attachments=%r, subject=%r",
            mails,
            text,
            attachments,
            subject,
        )
        if subject is None:
            subject = self.default_subject

        if attachments:
            for grouped_attachments in self._group_files_by_max_size(attachments):
                host.send_mail_from_account(
                    self.__account.guid,
                    self.parse_mails(mails),
                    subject,
                    text,
                    grouped_attachments,
                )
        else:
            host.send_mail_from_account(
                self.__account.guid, self.parse_mails(mails), subject, text, []
            )
