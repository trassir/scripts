# -*- coding: utf-8 -*-

from datetime import timedelta
from executor import Executor
from base_utils import BaseUtils
import host
try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger
logger = get_logger()


class ShowPopup(Executor):
    def __init__(self, monitor_to_show_archive_from_popup):
        self.monitor_to_show_archive_from_popup = monitor_to_show_archive_from_popup
        self._gui = host.object("operatorgui_" + host.settings('').guid)

    def open_archive(self, channel, tmstmp):
        logger.debug("Start show archive, channel is: %s, tmstmp: %s", channel, tmstmp)
        ts_start = BaseUtils.ts_to_dt(tmstmp)-timedelta(seconds=5)
        ts_end = BaseUtils.ts_to_dt(tmstmp)

        start_str = ts_start.strftime("%Y%m%d_%H%M%S")
        end_str = ts_end.strftime("%Y%m%d_%H%M%S")
        logger.debug(
            "open_arhive - chan: %s, mon: %s, start: %s, end: %s",
            channel,
            self.monitor_to_show_archive_from_popup,
            start_str,
            end_str
        )
        try:
            self._gui.show_archive(  # pylint:disable=E1101
                channel,
                self.monitor_to_show_archive_from_popup,
                start_str,
                end_str
            )
        except EnvironmentError as err:
            logger.debug("Can't show archive. Error occur: %s", err)

    @staticmethod
    def cancel_function():
        pass

    def show_popup(self, channel, ts, alrm_msg):
        logger.debug("Start show popup window")

        host.question(
            alrm_msg,
            host.tr("Отмена"),
            self.cancel_function,
            host.tr("Посмотреть событие в архиве"),
            lambda: self.open_archive(channel, ts),
            60 * 60,
        )

    def execute(self, channel_obj, ts, alarm_messages, *args, **kwargs):
        if not isinstance(alarm_messages, dict):
            logger.error("alarm_messages is not dict: %s", alarm_messages)
            return
        alarm_message = alarm_messages.get("alert_message")
        if not alarm_message:
            logger.error("alarm_messages hasn't 'alert_message key'")
            return
        channel = getattr(channel_obj, 'guid')
        if not channel:
            logger.warning("Can't get guid to show popup")
            return
        self.show_popup(channel, ts, alarm_message)

