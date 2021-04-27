# -*- coding: utf-8 -*-

from __builtin__ import object as py_object

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

import host
from base_utils import BaseUtils
from constants import EVENTS_TRANSLATION
import localization as loc


def utc_offset(server_guid):
    _utc_offset = 0
    try:
        _utc_offset = host.settings(
            "/{server_guid}/system_wide_options".format(server_guid=server_guid)
        )["utc_offset_minutes"]
        logger.debug("utc offset: %s", _utc_offset)
    except (IndexError, KeyError) as err:
        logger.error("can't get utc offset. Error: %s", err)
    return _utc_offset


def make_alarm_message(channel_name, event_type, tmstmp, code):

    event_translation = "{event_name}: {code}".format(
        event_name=EVENTS_TRANSLATION.get(event_type, "Unknown"), code=code
    )

    event_time = BaseUtils.ts_to_dt(tmstmp)
    dt = event_time.strftime("%d-%m-%Y %H:%M:%S")

    alarm_messages = {
        "alert_message": "{event_time}<br><b><font color='red'>{text_1}: {event_name}"
        "</font></b><br>{text2}: {channel_name}".format(
            event_time=dt,
            text_1=loc.main.alarm,
            event_name=event_translation,
            text2=loc.main.channel,
            channel_name=channel_name,
        ),
        "sms_message": "{event_time}.{text_1}: {event_name}"
        ". {text2}: {channel_name}".format(
            event_time=dt,
            text_1=loc.main.alarm,
            event_name=event_translation,
            text2=loc.main.channel,
            channel_name=channel_name,
        ),
        "mail_message": "{event_time}.{text_1}: {event_name}"
        ". {text2}: {channel_name}".format(
            event_time=dt,
            text_1=loc.main.alarm,
            event_name=event_translation,
            text2=loc.main.channel,
            channel_name=channel_name,
        ),
    }
    return alarm_messages


class ArucoEventsHandler(py_object):
    def __init__(
        self,
        obj_storage,
        aruco_codes,
        ignoring_mode=False,
        entered=True,
        leave=False,
        callback=None,
    ):
        """

        Args:
            obj_storage (ObjectsStorage): ObjectsStorage instance
            aruco_codes (list):
            ignoring_mode (bool):
            entered (bool):
            leave (bool):
            callback:
        """
        self.obj_storage = obj_storage
        self.aruco_codes = aruco_codes
        self.ignoring_mode = ignoring_mode
        self.entered = entered
        self.leave = leave
        self.callback = callback

    def check_channel(self, channel):
        res = False
        if not self.obj_storage.all_channels_in_work:
            res = channel in self.obj_storage.channels
        return self.obj_storage.all_channels_in_work or res

    def event_handler(self, event):
        logger.debug("event type: %s, origin: %s, aruco code: %s, zone name: %s, ts: %s",
                     event.type, event.origin, event.p1, event.p2, event.ts)

        code = event.p1
        zone_name = event.p2

        channel_full = getattr(event.origin_object, "associated_channel", None)
        if not channel_full:
            logger.debug(
                "Can't get associated channel for origin: %s, break.", event.origin
            )
            return
        logger.debug("associated channel is %s", channel_full)

        channel = channel_full.split("_")[0]
        if not self.check_channel(channel):
            logger.debug("channel %s not in channels list, return", channel)
            return

        channel_obj = self.obj_storage.channels.get(channel)
        if not channel_obj:
            logger.debug("channel object not found: %s, return", channel)
            return

        if "Entered Zone" in event.type:
            if not self.entered:
                return
            event_type = "Aruco entered the zone"
        else:
            if not self.leave:
                return
            event_type = "Aruco left the zone"

        ts = event.ts - utc_offset(channel_obj.server) * 60 * 1e6

        if self.ignoring_mode and code in self.aruco_codes:
            logger.debug("ignoring mode and code: %s in ignoring codes: %s", code,
                         self.aruco_codes)
            return
        if not self.ignoring_mode and code not in self.aruco_codes:
            logger.debug("code %s not in aruco codes: %s", code, self.aruco_codes)
            return

        if self.callback:
            alarm_messages = make_alarm_message(
                channel_obj.name, event_type, ts, code
            )
            self.callback(channel_full, ts, alarm_messages)
