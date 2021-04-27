# -*- coding: utf-8 -*-

from __builtin__ import object
import host
import time

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

from base_utils import BaseUtils
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


alert_message = (
    "{event_time}<br><b><font color='red'>{text_1}"
    "</font></b><br>"
    "{event_name}<br>"
    "{text2}: {channel_name}"
)
sms_message = "{event_time}.{text_1}:{event_name}.{text2}:{channel_name}"
mail_message = "{event_time}.{text_1}\n{event_name}\n{text2}: {channel_name}"

all_formats = {
    "alert_message": alert_message,
    "sms_message": sms_message,
    "mail_message": mail_message,
}


def make_alarm_message(channel_name, tmstmp, event_type):

    event_name = "{}".format(event_type)
    event_time = BaseUtils.ts_to_dt(tmstmp)
    dt = event_time.strftime("%d-%m-%Y %H:%M:%S")

    alarm_messages = {
        name: _frmt.format(
            event_time=dt,
            text_1=loc.gate.pacs_gate_event,
            event_name=event_name,
            text2=loc.gate.channel,
            channel_name=channel_name,
        )
        for name, _frmt in all_formats.iteritems()
    }
    return alarm_messages


# -----------------------------------------------------------------------------------------------------------
# Gate (physical access control system events) handler module
# -----------------------------------------------------------------------------------------------------------


class GatePacs(object):
    def __init__(self, obj_storage, callback=None):
        self.obj_storage = obj_storage
        self.callback = callback

    def check_channel(self, channel):
        res = False
        if not self.obj_storage.all_channels_in_work:
            res = channel in self.obj_storage.channels
        return self.obj_storage.all_channels_in_work or res

    def event_handler(self, event):
        logger.debug(
            "event type: %s, text: %s, p1: %s, origin: %s, ts: %s, time: %s",
            event.type,
            event.text,
            event.p1,
            event.origin,
            event.ts,
            time.time(),
        )

        channel_full = getattr(event.origin_object, "associated_channel", None)
        if not channel_full:
            logger.debug("Can't get associated channel for: %s, break", event.origin)
            return

        channel = channel_full.split("_")[0]
        if not self.check_channel(channel):
            logger.debug("channel %s not in channels list, return", channel)
            return

        channel_obj = self.obj_storage.channels.get(channel)
        if not channel_obj:
            logger.debug("channel object not found: %s, return", channel)
            return

        utc_offset(channel_obj.server)

        ts = event.ts
        event_type = event.text

        alarm_messages = make_alarm_message(
            channel_obj.name, ts, event_type
        )
        if self.callback:
            self.callback(channel_full, ts, alarm_messages)
