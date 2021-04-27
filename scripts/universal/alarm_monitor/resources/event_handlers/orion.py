# -*- coding:utf-8 -*-

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()


import host
from base_utils import BaseUtils
from constants import EVENTS_TRANSLATION
import localization as loc


# -----------------------------------------------------------------------------------------------------------
# Orion events handler module
# -----------------------------------------------------------------------------------------------------------


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


def make_alarm_message(channel_name, event_type, tmstmp):
    ev_translation = EVENTS_TRANSLATION.get(event_type, "Unknown")
    event_time = BaseUtils.ts_to_dt(tmstmp)

    alarm_messages = {
        "alert_message": "<b><font color='red'>{text_1}: '{ev_translation}'</font></b><br>{text2}: {channel_name}".format(
            event_time=event_time,
            text_1=loc.main.alarm,
            ev_translation=ev_translation,
            text2=loc.main.channel,
            channel_name=channel_name,
        ),
        "sms_message": "{event_time}.{text_1}: '{ev_translation}'. {text2}: {channel_name}".format(
            event_time=event_time,
            text_1=loc.main.alarm,
            ev_translation=ev_translation,
            text2=loc.main.channel,
            channel_name=channel_name,
        ),
        "mail_message": "{event_time}.{text_1}: '{ev_translation}'. {text2}: {channel_name}".format(
            event_time=event_time,
            text_1=loc.main.alarm,
            ev_translation=ev_translation,
            text2=loc.main.channel,
            channel_name=channel_name,
        ),
    }

    return alarm_messages


class OrionEventsHandler:
    def __init__(self, obj_storage, orion_alarm_nodes, callback=None):
        self.obj_storage = obj_storage
        self.orion_alarm_nodes = orion_alarm_nodes
        self.callback = callback

    def check_channel(self, channel):
        res = False
        if not self.obj_storage.all_channels_in_work:
            res = channel in self.obj_storage.channels
        return self.obj_storage.all_channels_in_work or res

    def event_handler(self, event):
        logger.debug("event type: %s, origin: %s, ts: %s", event.type, event.origin, event.ts)
        try:
            node_name = event.origin_object.name
            logger.debug("node name: %s", node_name)
        except EnvironmentError as err:
            node_name = event.origin
            logger.debug("Can't get name of orion node, node origin (%s) --> node name. Err: %s", node_name, err)

        if self.orion_alarm_nodes and node_name not in self.orion_alarm_nodes:
            logger.debug(
                "node name (%s) not in alarm nodes list: %s", node_name, self.orion_alarm_nodes
            )
            return

        channel_full = getattr(event.origin_object, "associated_channel", None)
        if not channel_full:
            logger.warning(
                "node_name: %s hasn't an associated channel, break", node_name
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

        ts = event.ts - utc_offset(channel_obj.server) * 60 * 1e6

        if self.callback:
            alarm_messages = make_alarm_message(channel_obj.name, event.type, ts)
            self.callback(channel_full, ts, alarm_messages)
