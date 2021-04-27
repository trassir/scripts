# -*- coding: utf-8 -*-

from datetime import timedelta
from reactions.executors.executor import Executor
from base_utils import BaseUtils
import host
from helpers import get_logger
import localization as loc

logger = get_logger()


class ShowPopup(Executor):
    def __init__(self, monitor_to_show_archive_from_popup, display_duration):
        self.monitor_to_show_archive_from_popup = monitor_to_show_archive_from_popup
        self.display_duration = display_duration
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

    def show_popup(self, channel, tmstmp, alrm_msg):
        logger.debug("Start show popup window")

        host.question(
            alrm_msg,
            loc.popup.cancel,
            self.cancel_function,
            loc.popup.show_event_in_archive,
            lambda: self.open_archive(channel, tmstmp),
            self.display_duration,
        )

    def execute(self, channel, ts, alarm_messages, *args, **kwargs):
        if not isinstance(alarm_messages, dict):
            logger.error("alarm_messages is not dict: %s", alarm_messages)
            return
        alarm_message = alarm_messages.get("alert_message")
        if not alarm_message:
            logger.error("alarm_messages hasn't 'alert_message key'")
            return
        self.show_popup(channel, ts, alarm_message)

