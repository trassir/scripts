# -*-coding: utf-8 -*-

from __builtin__ import object as py_object
from base_utils import BaseUtils
import host

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()


from constants import EVENTS_TRANSLATION
import localization as loc

OBJECT_TYPES_TRANSLATION = {
    "person": loc.neuro.person,# host.tr("Человек"),
    "head": loc.neuro.person,
    "vehicle": loc.neuro.vehicle,
    "bicycle": loc.neuro.bicycle,
}


def make_alarm_message(channel_name, dt, event_type, zone_name):
    event_time = dt.strftime("%H:%M:%S")

    alarm_messages = {
        "alert_message": "{event_time}<br><b><font color='red'>{event_description}</font></b>"
        "<br>{text_1}: {channel_name}"
        "<br>{text_2}: {zone_name}".format(
            event_time=event_time,
            event_description=event_type,
            text_1=loc.main.channel,
            channel_name=channel_name,
            text_2=loc.neuro.border,
            zone_name=zone_name,
        ),
        "sms_message": "{event_description}. {text_1}: {channel_name},"
        "{text_2}: {zone_name}"
        "{text_3}: {event_time}".format(
            event_description=event_type,
            text_1=loc.main.channel,
            channel_name=channel_name,
            text_2=loc.neuro.border,
            zone_name=zone_name,
            text_3=loc.neuro.event_time,
            event_time=event_time,
        ),
        "mail_message": "{event_time}. {event_description}"
        "\n{text_1}: {channel_name}"
        "\n{text_2}: {zone_name}".format(
            event_time=event_time,
            event_description=event_type,
            text_1=loc.main.channel,
            channel_name=channel_name,
            text_2=loc.neuro.border,
            zone_name=zone_name,
        ),
    }
    return alarm_messages


class CrossLineDetector(py_object):
    def __init__(
        self, obj_storage, ab_borders, ba_borders, observable_types, same_event_filter, callback=None
    ):
        """

        Args:
            obj_storage (ObjectsStorage): ObjectsStorage instance
            ab_borders (list):
            ba_borders (list):
            observable_types (list| dict): либо список, либо слооварь с ключами:
                                        {"person", "head", "vehicle", "bicycle"}
            same_event_filter:
            callback:

        """
        self.obj_storage = obj_storage
        self._ab_borders = []
        self.ab_borders = ab_borders
        self._ba_borders = []
        self.ba_borders = ba_borders
        self.observable_types = observable_types
        self.same_event_filter = same_event_filter
        self.callback = callback
        self.cross_detections = {}

    @property
    def ab_borders(self):
        return self._ab_borders

    @ab_borders.setter
    def ab_borders(self, borders_names):
        if isinstance(borders_names, str) and not borders_names:
            self._ab_borders = []
        elif isinstance(borders_names, str):
            self._ab_borders = [bn.strip() for bn in borders_names.split(",")]
        elif borders_names is None:
            self._ab_borders = []
        elif isinstance(borders_names, list):
            self._ab_borders = borders_names
        else:
            raise ValueError("Wrong parameter for A->B borders")
        logger.debug("Initialized A->B borders: %s", self._ab_borders)

    @property
    def ba_borders(self):
        return self._ba_borders

    @ba_borders.setter
    def ba_borders(self, borders_names):
        if isinstance(borders_names, str) and not borders_names:
            self._ba_borders = []
        elif isinstance(borders_names, str):
            self._ba_borders = [bn.strip() for bn in borders_names.split(",")]
        elif borders_names is None:
            self._ba_borders = []
        elif isinstance(borders_names, list):
            self._ba_borders = borders_names
        else:
            raise ValueError("Wrong parameter for B->A borders")
        logger.debug("Initialized B->A borders: %s", self._ba_borders)

    def _is_first(self, channel, border, direction, count_by_classes):
        """

        Args:
            channel (str): channel guid
            border (str): border name
            direction (str): 'a_to_b' or 'b_to_a'
            count_by_classes (dict):  {'person': 241}
        Returns:
            bool
        """

        if not self.cross_detections.get(channel):
            self.cross_detections[channel] = {border: {direction: count_by_classes}}
            return True
        if not self.cross_detections[channel].get(border):
            self.cross_detections[channel][border] = {direction: count_by_classes}
            return True
        if not self.cross_detections[channel][border].get(direction):
            self.cross_detections[channel][border][direction] = count_by_classes
            return True

    def ab_handler(self, a_to_b, channel_guid, border_name):
        """
        Args:
            a_to_b (dict): a_to_b_unique_count_by_classes
            channel_guid (str):
            border_name (str):
        Returns (list):

        """

        if not (border_name in self.ab_borders):
            logger.debug("%s not in ab_borders: %s", border_name, self.ab_borders)
            return

        if self._is_first(channel_guid, border_name, "a_to_b", a_to_b):
            return

        a_to_b_previous = self.cross_detections[channel_guid][border_name]["a_to_b"]
        objects_which_crossed = []

        for obj_type, count in a_to_b.iteritems():
            if obj_type in self.observable_types:
                count_diff = count - a_to_b_previous.get(obj_type, 0)
                if count_diff:
                    logger.debug(
                        "A->B: channel: %s, border: %s, crossing detected for object type: %s,"
                        " crossing count diff: %s, new count: %s",
                        channel_guid,
                        border_name,
                        obj_type,
                        count_diff,
                        count,
                    )
                    a_to_b_previous[obj_type] = count
                    objects_which_crossed.append(obj_type)
        return objects_which_crossed

    def ba_handler(self, b_to_a, channel_guid, border_name):
        """
         Args:
             b_to_a (dict): b_to_a_unique_count_by_classes
             channel_guid (str):
             border_name (str):

         Returns:
         """

        if not (border_name in self.ab_borders):
            logger.debug("%s not in ab_borders: %s", border_name, self.ba_borders)
            return

        if self._is_first(channel_guid, border_name, "b_to_a", b_to_a):
            return

        b_to_a_previous = self.cross_detections[channel_guid][border_name]["b_to_a"]
        objects_which_crossed = []

        for obj_type, count in b_to_a.iteritems():
            if obj_type in self.observable_types:
                count_diff = count - b_to_a_previous.get(obj_type, 0)
                if count_diff:
                    logger.debug(
                        "B->A. channel: %s, border: %s  crossing detected for object type: %s,"
                        " crossing count diff: %s, new count: %s",
                        channel_guid,
                        border_name,
                        obj_type,
                        count_diff,
                        count,
                    )
                    b_to_a_previous[obj_type] = count
                    objects_which_crossed.append(obj_type)
        return objects_which_crossed

    def event_handler(self, event):

        channel_full = "{channel}_{server}".format(
            channel=event.channel_guid, server=event.server_guid
        )
        channel = event.channel_guid

        channel_obj = self.obj_storage.channels.get(event.channel_guid)
        if not channel_obj:
            logger.debug("channel object not found: %s, return", event.channel_guid)
            return

        events = []

        for zone in event.zones:
            if zone.zone_type != 1:
                continue
            border_name = getattr(zone, "zone_name", getattr(zone, "name", None))

            if self.ab_borders:
                a_to_b = zone.tracking_state.a_to_b_unique_count_by_classes
                _types_a_b = self.ab_handler(a_to_b, channel, border_name)
                if _types_a_b:
                    for _type in _types_a_b:
                        event_data = {channel_full: {border_name: {_type: 0}}}
                        if not self.same_event_filter.is_same(event_data):
                            event_type = "{direction}: {object_type}".format(
                                direction=EVENTS_TRANSLATION.get(
                                    "Border Crossed A -> B"
                                ),
                                object_type=OBJECT_TYPES_TRANSLATION.get(_type),
                            )
                            alarm_messages = make_alarm_message(
                                channel_obj.name,
                                BaseUtils.ts_to_dt(event.event_ts),
                                event_type,
                                border_name,
                            )
                            events.append(
                                (channel_full, event.event_ts, alarm_messages)
                            )

            if self.ba_borders:
                b_to_a = zone.tracking_state.b_to_a_unique_count_by_classes
                _types_b_a = self.ba_handler(b_to_a, channel, border_name)
                if _types_b_a:
                    for _type in _types_b_a:
                        event_data = {channel_full: {border_name: {_type: 0}}}
                        if not self.same_event_filter.is_same(event_data):
                            event_type = "{direction}: {object_type}".format(
                                direction=EVENTS_TRANSLATION.get(
                                    "Border Crossed B -> A"
                                ),
                                object_type=OBJECT_TYPES_TRANSLATION.get(_type),
                            )
                            alarm_messages = make_alarm_message(
                                channel_obj.name,
                                BaseUtils.ts_to_dt(event.event_ts),
                                event_type,
                                border_name,
                            )
                            events.append(
                                (channel_full, event.event_ts, alarm_messages)
                            )

        if self.callback and events:
            for event in events:
                self.callback(*event)
