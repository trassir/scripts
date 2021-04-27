# -*- coding: utf-8 -*-

from executor import Executor

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()


class MailTextSender(Executor):
    def __init__(self, mail_sender, email_recipients):
        self.mail_sender = mail_sender
        self.email_recipients = email_recipients

    def execute(self, channel, ts, alarm_messages, *args, **kwargs):
        alarm_message = alarm_messages.get("mail_message")
        if not alarm_message:
            logger.error("alarm_messages hasn't 'mail_message' key")
            return
        try:
            self.mail_sender.send(mails=self.email_recipients, text=alarm_message)
        except Exception as err:
            logger.error(err)
