# -*- coding: utf-8 -*-
import json

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

try:
    from constants import EVENTS_TRANSLATION
except ImportError as err:
    logger.error("Can't import EVENTS_TRANSLATION")

from base_utils import BaseUtils
import host
import localization as loc


# --------------------------------------------------------------------------------------------------------------------
# simple events handler module
# --------------------------------------------------------------------------------------------------------------------

SIMPLE_EVENTS_LIST = [
    "Motion Start",
    "Sound Detected",
    "Smoke Detected",
    "Fire Detected",
    "Fire Stopped",
    "Face Detected",
    "CrossLine Detected",
    "Intrusion Detected",
    "Left Object Detected",
    "Item Abandoned",
    "Item Missing",
    "Slow Down Detected",
    "Tamper Alert",
    "Tamper Alert: Defocus",
    "Tamper Alert: Covered",
    "Tamper Alert: Flashlight",
    "Tamper Alert: Shift",
    "Person without helmet detected",
    "Person without uniform detected",
    "Warning: Thermal Signal",
    "Plate detected",
    "People Detected",  # HW detector Hikvision
    "BOPOH event",
    "Person without mask found",
    "Social distance violation detected",
    "Suspicious pose",
]


def utc_offset(server_guid):
    utc_offset = 0
    try:
        utc_offset = host.settings(
            "/{server_guid}/system_wide_options".format(server_guid=server_guid)
        )["utc_offset_minutes"]
    except KeyError as err:
        logger.error(
            "Can't get utc_offset for server: %s, error occurred: %s", utc_offset, err
        )

    try:
        utc_offset = host.settings(
            "system_wide_options".format(server_guid=server_guid)
        )["utc_offset_minutes"]
    except KeyError as err:
        logger.error("Can't get local utc_offset, error occurred: %s", err)

    return utc_offset


def make_alarm_message(channel_name, dt, event_type):
    event_name = EVENTS_TRANSLATION.get(event_type, "Unknown")
    dt = dt.strftime("%d-%m-%Y %H:%M:%S")
    alarm_messages = {
        "alert_message": "{event_time}<br><b><font color='red'>{text_1}: '{event_name}'"
        "</font></b><br>{text2}: {channel_name}".format(
            event_time=dt,
            text_1=loc.main.alarm,
            event_name=event_name,
            text2=loc.main.channel,
            channel_name=channel_name,
        ),
        "sms_message": "{event_time}.{text_1}: '{event_name}'"
        ". {text2}: {channel_name}".format(
            event_time=dt,
            text_1=loc.main.alarm,
            event_name=event_name,
            text2=loc.main.channel,
            channel_name=channel_name,
        ),
        "mail_message": "{event_time}.{text_1}: '{event_name}'"
        ". {text2}: {channel_name}".format(
            event_time=dt,
            text_1=loc.main.alarm,
            event_name=event_name,
            text2=loc.main.channel,
            channel_name=channel_name,
        ),
    }

    return alarm_messages


class SimpleEventsHandler:
    def __init__(self, obj_storage, callback=None):
        """Обработка событий из SIMPLE_EVENTS_LIST

        Args:
            obj_storage (ObjectsStorage): ObjectsStorage instance
            callback (`function`, optional):
        """
        self.obj_storage = obj_storage
        self.callback = callback

    def check_channel(self, channel):
        res = False
        if not self.obj_storage.all_channels_in_work:
            res = channel in self.obj_storage.channels
        return self.obj_storage.all_channels_in_work or res

    def event_handler(self, event):
        try:
            logger.debug("event type: %s", event.type)
            if event.type == "Left Object Detected":
                channel = getattr(event.origin_object, "associated_channel", None)
            else:
                channel = event.origin
            logger.debug("channel: %s", channel)
            channel = channel.split("_")[0]

            if not self.check_channel(channel):
                logger.debug("channel %s not in channels list, return", channel)
                return

            channel_obj = self.obj_storage.channels.get(channel)
            if not channel_obj:
                logger.debug("channel object not found: %s, return", channel)
                return
            channel_full = channel_obj.full_guid
            server_guid = channel_obj.server

            ts = event.ts - utc_offset(server_guid) * 60 * 1e6
            dt = BaseUtils.ts_to_dt(ts)

            logger.debug(
                "Trassir timestamp: %s, Trassir dt is : %s, corrected dt: %s",
                event.ts,
                BaseUtils.ts_to_dt(event.ts),
                dt,
            )

            alarm_messages = None
            if getattr(event, "data", None):
                alarm_messages = json.loads(getattr(event, "data")).get(
                    "alarm_messages"
                )
                logger.debug("alarm message in data")

            if not alarm_messages:
                alarm_messages = make_alarm_message(channel_obj.name, dt, event.type)
            if event.type == "Plate detected":
                ts = event.ts

            if self.callback:
                self.callback(channel_full, ts, alarm_messages)

        except Exception as err:
            logger.exception("simple_events_handler: error occurred: %s", err)
