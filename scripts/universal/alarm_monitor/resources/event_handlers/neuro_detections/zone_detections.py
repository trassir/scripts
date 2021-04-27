# -*- coding:utf-8 -*-


from __builtin__ import object as py_object
from base_utils import BaseUtils
from constants import EVENTS_TRANSLATION

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

import localization as loc

logger = get_logger()

EVENTS_TYPES = {
    "person": "Max count people",
    "head": "Max count people",
    "bicycle": "Max count bicycles",
    "vehicle": "Max count vehicles",
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
            text_2=loc.neuro.zone_name,
            zone_name=zone_name,
        ),
        "sms_message": "{event_description}. {text_1}: {channel_name},"
        "{text_2}: {zone_name}"
        "{text_3}: {event_time}".format(
            event_description=event_type,
            text_1=loc.main.channel,
            channel_name=channel_name,
            text_2=loc.neuro.zone_name,
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
            text_2=loc.neuro.zone_name,
            zone_name=zone_name,
        ),
    }
    return alarm_messages


class ObjectsInZoneDetector(py_object):
    """Handles deep events
        Args:
            obj_storage (ObjectsStorage): ObjectsStorage instance
            zones_names (list):
            confidence (int): integer in range [1 - 100]
            observable_types (dict): type and count of objects to rise event:
                {"person": 1, "head": 1, "vehicle": 1, "bicycle": 1}
            same_event_filter (same_event_filter.SameEvent object):
            callback:
     """

    def __init__(
        self, obj_storage, zones_names, confidence, observable_types, same_event_filter, callback=None
    ):
        self.obj_storage = obj_storage
        self.zones_names = zones_names
        self.confidence = confidence
        self.observable_types = {x: y for x, y in observable_types.iteritems() if y}
        self.same_event_filter = same_event_filter
        self.callback = callback
        logger.debug("observable types: %s", self.observable_types)

    def _objects_sum(self, zones):
        """Counts objects in each zone by it type

        Args:
            zones (list): список объектов зон

        Returns (dict): {'zone_1': {'person': 0, 'head': 0, 'bicycle': 0, 'vehicle': 0},
                         'zone_2': {'person': 5, 'head': 0, 'bicycle': 0, 'vehicle': 0}
                         }

        """
        counted_by_zones = {}

        for zone in zones:
            if zone.zone_type == 1:
                continue
            zone_name = getattr(zone, "zone_name", getattr(zone, "name", None))
            if zone_name not in self.zones_names:
                # logger.debug("zone name: %s not in zone names: %s break", zone_name, self.zones_names)
                continue
            counted_by_types = {x: 0 for x in self.observable_types.iterkeys()}
            counted_by_zones[zone_name] = counted_by_types
            for obj_inside in zone.objects_inside:
                if obj_inside.confidence * 100 < self.confidence:
                    logger.debug("bad confidence, break")
                    continue
                if obj_inside.class_id not in self.observable_types:
                    # logger.debug("class id (%s) not in observable types (%s)", obj_inside.class_id, self.observable_types)
                    continue
                counted_by_types[obj_inside.class_id] += 1
        logger.debug("counted_by_zones: %s", counted_by_zones)
        return counted_by_zones

    def _search_exceeding(self, counted_by_zones):
        exceeding_by_zones = {}
        for zone_id, count_by_type in counted_by_zones.iteritems():
            for _type, count in count_by_type.iteritems():
                if count >= self.observable_types[_type]:
                    exceeding_by_zones[zone_id] = {_type: count}
        if exceeding_by_zones:
            logger.debug("exceeding by zones: %s", exceeding_by_zones)
        return exceeding_by_zones

    def event_handler(self, event):
        channel_full = "{channel}_{server}".format(
            channel=event.channel_guid, server=event.server_guid
        )
        channel = event.channel_guid

        channel_obj = self.obj_storage.channels.get(event.channel_guid)
        if not channel_obj:
            logger.debug("channel object not found: %s, return", event.channel_guid)
            return

        exceed = self._search_exceeding(self._objects_sum(event.zones))
        events = []
        for zone_id, exceed_by_type in exceed.iteritems():
            for _type, count in exceed_by_type.iteritems():
                event_data = {channel_full: {zone_id: {_type: count}}}
                if not self.same_event_filter.is_same(event_data):
                    event_type = EVENTS_TRANSLATION.get(
                        EVENTS_TYPES.get(_type), "Unknown"
                    )
                    alarm_messages = make_alarm_message(
                        channel_obj.name, BaseUtils.ts_to_dt(event.event_ts), event_type, zone_id
                    )
                    events.append((channel_full, event.event_ts, alarm_messages, zone_id))

        if self.callback:
            for event in events:
                channel_full, event_ts, alarm_messages, zone_name = event
                self.callback(channel_full, event_ts, alarm_messages, zone_name=zone_name)
