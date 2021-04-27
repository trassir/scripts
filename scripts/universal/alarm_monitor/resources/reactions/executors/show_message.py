# -*- coding: utf-8 -*-

from executor import Executor
import host
from helpers import get_logger
logger = get_logger()
logger.debug('show message logger imported')


class ShowMessage(Executor):
    def __init__(self, show_message_delay):
        self.show_message_delay = show_message_delay

    def execute(self, channel, ts, alarm_messages, *args, **kwargs):
        if not isinstance(alarm_messages, dict):
            logger.error("alarm_messages is not dict: %s", alarm_messages)
            return
        alarm_message = alarm_messages.get("alert_message")
        if not alarm_message:
            logger.error("alarm_messages hasn't 'alert_message key'")
            return
        host.message(alarm_messages["alert_message"], self.show_message_delay * 1000)
