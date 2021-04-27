# -*- coding: utf-8 -*-

import abc
from __builtin__ import object as py_object
from helpers import get_logger
from shot_saver import status as STATUS


logger = get_logger()


class AdoptedSender(py_object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def send(self, status, shot_path, alarm_messages, *args, **kwargs):
        """Абстрактный базовый класс.
           Создаёт адаптеры к различным сендерам
           для отправки скриншотов.

        Args:
            status (str): one of "saving", "error", "success", "in_queue"
            shot_path (List['str']): ['Shot path 1', 'Shot path 2']
            alarm_messages (dict): dict with three types of messages generated in event handler:
                                   each type has it key: alert_message, sms_message, mail_message

        Returns:

        """
        pass


class AdoptedEmailSender(AdoptedSender):
    def __init__(self, mail_sender, email_recipients):
        self.mail_sender = mail_sender
        self._email_recipients = []
        self.email_recipients = email_recipients

    @property
    def email_recipients(self):
        return self._email_recipients

    @email_recipients.setter
    def email_recipients(self, all_recipients):
        """
        Args:
            all_recipients (str| list):

        Returns:

        """
        if not all_recipients:
            raise ValueError("No email recipients to send")
        if isinstance(all_recipients, list):
            self._email_recipients = all_recipients
            logger.debug("E-mail recipients: %s", self._email_recipients)
        elif isinstance(all_recipients, str):
            self._email_recipients = [i.strip() for i in all_recipients.split(",")]
            logger.debug("E-mail recipients: %s", self._email_recipients)
        else:
            logger.debug("Wrong e-mail recipients: %s", all_recipients)
            raise ValueError("Wrong e-mail recipients: %s" % all_recipients)

    def send(self, status, shot_path, alarm_messages, *args, **kwargs):
        """

        Args:
            status (str): one of "saving", "error", "success", "in_queue"
            shot_path (List['str']): ['Shot path 1', 'Shot path 2']
            alarm_messages (dict):

        Returns:

        """
        logger.debug("adopted email sender: %s, shot path: %s", status, shot_path)
        alarm_message = alarm_messages["mail_message"].encode("utf-8")
        try:
            self.mail_sender.send(
                self.email_recipients,
                text=alarm_message,
                attachments=shot_path if status == STATUS.success else None,
            )

        except Exception as err:
            logger.error(err)


class AdoptedFTPSender(AdoptedSender):
    def __init__(self, ftp_sender):
        self.ftp_sender = ftp_sender

    def send(self, status, shot_path, *args, **kwargs):
        """
         Args:
            status (str): one of "saving", "error", "success", "in_queue"
            shot_path (List['str']): ['Shot path 1', 'Shot path 2']

        Returns:
        """
        if status == STATUS.success:
            logger.debug("start to send to ftp")
            try:
                self.ftp_sender.send(shot_path[0])
            except IndexError as err:
                logger.error("No file to send to FTP, %s", err)
            except AttributeError as err:
                logger.error(err)
        else:
            logger.info("FTP sender. Nothing to send, status: %s", status)


class AdoptedFTPSender(AdoptedSender):
    def __init__(self, ftp_sender):
        self.ftp_sender = ftp_sender

    def send(self, success, shot_path, *args, **kwargs):
        if success:
            logger.debug("start try to send to ftp")
            try:
                self.ftp_sender.files(shot_path)
            except Exception as err:
                logger.exception(err)
        else:
            logger.debug("FTP sender. Nothing to send")


class AdoptedTelegramSender(AdoptedSender):
    def __init__(self, tbot_api, telegram_users):
        """
        Args:
            tbot_api (tbot_api object):
            telegram_users (List['str',]):
        """
        self.tbot_api = tbot_api
        self.telegram_users = telegram_users

    def send(self, status, shot_path, alarm_messages, *args, **kwargs):
        """
                Args:
                   status (str): one of "saving", "error", "success", "in_queue"
                   shot_path (List['str']): ['Shot path 1', 'Shot path 2']
                   alarm_messages (dict):

               Returns:
        """
        if status == STATUS.success:
            logger.debug("start try to send images to telegram (status = %s)", status)
            try:
                message = alarm_messages["mail_message"].encode("utf-8")
            except KeyError as err:
                logger.error("No mail message")
                message = ""
            logger.debug("Telegram shots: %s", shot_path)
            self.tbot_api.send_image_album(
                self.telegram_users, shot_path, captions=[message]
            )

            # self.tbot_api.send_image(self.telegram_users, shot_path[0], captions=message)
        elif status == STATUS.error:
            try:
                message = alarm_messages["mail_message"].encode("utf-8")
            except KeyError as err:
                logger.error("No mail message")
                message = ""
            self.tbot_api.send_message(self.telegram_users, message)
        else:
            logger.debug("status of shot is %s, nothing send to Telegram)", status)
