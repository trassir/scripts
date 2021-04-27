# -*- coding: utf-8 -*-

from executor import Executor
from helpers import get_logger
logger = get_logger()


class TelegramSendText(Executor):
    def __init__(self, telegram_sender):
        self.telegram_sender = telegram_sender

    def execute(self, channel, tmstmp, alarm_messages, *args, **kwargs):
        if not isinstance(alarm_messages, dict):
            logger.error("alarm_messages is not dict: %s", alarm_messages)
            return
        alarm_message = alarm_messages.get("mail_message")
        if not alarm_message:
            logger.error("alarm_messages hasn't 'mail_message' key")
            return
        try:
            self.telegram_sender.text(alarm_message)
        except Exception as err:
            logger.exception(err)
