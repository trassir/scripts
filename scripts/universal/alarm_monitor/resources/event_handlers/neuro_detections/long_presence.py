# -*- coding: utf-8 -*-

import datetime

import numpy as np
import time
from __builtin__ import object as py_object

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()
from base_utils import BaseUtils
from constants import EVENTS_TRANSLATION
import localization as loc


EVENTS_TYPES = {
    "person": "Max count people",
    "head": "Max count people",
    "bicycle": "Max count bicycles",
    "vehicle": "Max count vehicles",
}


def make_alarm_message(channel_name, dt, event_type, zone_name, count, level_to_react):

    event_time = dt.strftime("%H:%M:%S")

    alarm_messages = {
        "alert_message": "{event_time}<br><b><font color='red'>{event_description}</font></b>"
        "<br>{text_1}: {channel_name}"
        "<br>{text_2}: {zone_name}"
        "<br>{text_4}: {count}. {text_5}: {level_to_react}".format(
            event_time=event_time,
            event_description=event_type,
            text_1=loc.main.channel,
            channel_name=channel_name,
            text_2=loc.neuro.zone_name,
            zone_name=zone_name,
            text_4=loc.neuro.last_detection_quantity,
            count=count,
            text_5=loc.neuro.level_to_react,
            level_to_react=level_to_react,
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
        "\n{text_1}: {channel_name}."
        "\n{text_2}: {zone_name}."
        "\n{text_4}: {count}."
        "\n{text_5}: {level_to_react}.".format(
            event_time=event_time,
            event_description=event_type,
            text_1=loc.main.channel,
            channel_name=channel_name,
            text_2=loc.neuro.zone_name,
            zone_name=zone_name,
            text_4=loc.neuro.last_detection_quantity,
            count=count,
            text_5=loc.neuro.level_to_react,
            level_to_react=level_to_react,
        ),
    }
    return alarm_messages


class LongPresence(py_object):
    """Handles deep events
        Args:
            obj_storage (ObjectsStorage): ObjectsStorage instance
            zones_names (list):
            confidence (int): integer in range [1 - 100]
            observable_types (Ordered dict): dict with 4 elements: type and count of each objects to rise event:
                {"person": 1, "head": 1, "vehicle": 1, "bicycle": 1}
            observation_duration (int): observation of the object time
             period in seconds to rise alarm
            match_level (float): ratio of true to all elements in 'zone_array'
            same_event_filter (same_event_filter.SameEvent object):
            callback:
     """

    def __init__(
        self,
        obj_storage,
        zones_names,
        confidence,
        observable_types,
        observation_duration,
        match_level,
        same_event_filter,
        callback=None,
    ):
        self.obj_storage = obj_storage
        self.zones_names = zones_names
        self.confidence = confidence
        self.observable_types = observable_types
        self.observation_duration = observation_duration
        self.match_level = float(match_level)
        self.same_event_filter = same_event_filter
        self.callback = callback

        self.all_detections = {}
        self._alarm_level = np.array(list(observable_types.values()))
        self._base_types = np.array(list(observable_types.keys()))
        self._norm_base_types = self._base_types[np.nonzero(self._alarm_level)[0]]
        self._columns_to_work_array = np.nonzero(self._alarm_level)[0] + 1
        self._constant = (
            self.observation_duration / 3 if self.observation_duration <= 20 else 20
        )  # поправочная константа
        self.previous_event_time = {}
        self._obj_type_column_no = {"person": 1, "head": 2, "bicycle": 3, "vehicle": 4}
        logger.debug("observable types: %s", self.observable_types)

    def _initialize_cell(self, channel, zone_name, counted_array):
        """
        Если событие по каналу или зоне пришло впервые, то нужно создать
         соответствующую ячейку в словаре
        Args:
            channel (str):
            zone_name (str):
            counted_array (np.array)

        Returns: (bool)

        """
        if not self.all_detections.get(channel):
            self.all_detections[channel] = {}
            self.all_detections[channel][zone_name] = np.array([counted_array])
            logger.debug(
                "initialized cell. chan: %s, zone name: %s" % (channel, zone_name)
            )
            return True
        if self.all_detections[channel].get(zone_name) is None:
            self.all_detections[channel][zone_name] = np.array([counted_array])
            logger.debug(
                "chan already initialized: %s, new zone add, name: %s"
                % (channel, zone_name)
            )
            return True

    def zones_with_detections(self, zones, channel):
        """Counts objects in each zone by it type
        При событии считает объекты по всем зонам на канале и результат кладет
        в виде вектора  в массив данных в data_by_channel
        Возвращает список имен зон с детекциями

        Args:
            zones (List): список объектов зон
            channel (str): имя канала

        Returns : List(str)
        """
        zones_with_detections = []
        for zone in zones:
            if zone.zone_type == 1:
                continue
            zone_name = getattr(zone, "zone_name", getattr(zone, "name", None))
            if zone_name not in self.zones_names:
                # logger.debug("zone name: %s not in zone names: %s break", zone_name, self.zones_names)
                continue
            _counted = np.array([int(time.time()), 0, 0, 0, 0])
            for obj_inside in zone.objects_inside:
                if obj_inside.confidence * 100 < self.confidence:
                    logger.debug("bad confidence, break")
                    continue
                if obj_inside.class_id not in self.observable_types:
                    continue
                _counted[self._obj_type_column_no[obj_inside.class_id]] += 1
                if zone_name not in zones_with_detections:
                    zones_with_detections.append(zone_name)
            if self._initialize_cell(channel, zone_name, _counted):
                continue
            self.all_detections[channel][zone_name] = np.vstack(
                (self.all_detections[channel][zone_name], _counted)
            )
        return zones_with_detections

    def _event_recorder(self, channel, zone_name, obj_type):
        """
        Records time for each alarm raised to avoid spam
        Args:
            channel (str):
            zone_name (str):
            obj_type (str):

        Returns:

        """
        if not self.previous_event_time.get(channel):
            self.previous_event_time[channel] = {}
        if not self.previous_event_time[channel].get(zone_name):
            self.previous_event_time[channel][zone_name] = {
                "person": 0,
                "head": 0,
                "bicycle": 0,
                "vehicle": 0,
            }
        self.previous_event_time[channel][zone_name][obj_type] = time.time()

    def check_long_presence_objects(self, channel, zone_name):
        """
        Counts detected objects in zone for period, if percentage of
         'successful events' reaches match_level for object
         put it in dictionary, for example {person: 3}, where 3 is last count
        Args:
            channel (str): full_guid
            zone_name (str):

        Returns: Dict
        """
        min_ts = time.time() - self.observation_duration - self._constant
        zone_array = self.all_detections[channel][zone_name]

        def is_long_exceeding_detected(obj_events, object_type, time_to_rise_event):
            """

            Args:
                obj_events (ndarray): numpy array
                object_type (str):
                time_to_rise_event ():
            Returns: Dict

            """

            if obj_events.shape[0] < 2:
                return
            duration = obj_events[-1, 0] - obj_events[0, 0]
            if duration < time_to_rise_event:
                logger.debug(
                    "duration %s is less %s, break", duration, time_to_rise_event
                )
                return
            comparison = obj_events >= self.observable_types[object_type]
            non_zeroes = np.count_nonzero(comparison[:, [1]])
            ratio = 100 * non_zeroes / obj_events.shape[0]
            match_level_reached = ratio >= self.match_level
            logger.debug(
                "ratio is: %s, match level reached: %s", ratio, match_level_reached
            )
            return match_level_reached

        # Make selection for each type of objects and check long presence
        long_lasting_exceeding = {}

        for obj_type in self._norm_base_types:
            column_no = self._obj_type_column_no[obj_type]
            try:
                start_ts = self.previous_event_time[channel][zone_name][obj_type]
                start_ts = start_ts if start_ts > min_ts else min_ts
            except KeyError:
                start_ts = min_ts
            object_events = zone_array[:, [0, column_no]][zone_array[:, 0] >= start_ts]
            logger.debug(
                "for %s, prev event_ts: %s, events is %s",
                obj_type,
                start_ts,
                object_events,
            )
            if is_long_exceeding_detected(
                object_events, obj_type, self.observation_duration
            ):
                long_lasting_exceeding[obj_type] = object_events[-1][1]
                self._event_recorder(channel, zone_name, obj_type)
        return long_lasting_exceeding

    def clean_old_detections(self, channel, zone_name):
        start_ts = time.time() - 3 * self.observation_duration
        zone_array = self.all_detections[channel][zone_name]
        self.all_detections[channel][zone_name] = zone_array[
            zone_array[:, 0] >= start_ts
        ]

    def event_handler(self, event):
        try:
            channel_full = "{channel}_{server}".format(
                channel=event.channel_guid, server=event.server_guid
            )

            channel_obj = self.obj_storage.channels.get(event.channel_guid)
            if not channel_obj:
                logger.debug("channel object not found: %s, return", event.channel_guid)
                return

            zones_with_detections = self.zones_with_detections(
                event.zones, channel_full
            )
            events = []
            logger.debug("all events: %s" % self.all_detections)
            for zone in zones_with_detections:
                long_lasting_exceeding = self.check_long_presence_objects(
                    channel_full, zone
                )
                if not long_lasting_exceeding:
                    continue
                logger.debug(
                    "long lasting exceeding is detected for channel: %s, zone: %s, types-count: %s",
                    channel_full,
                    zone,
                    long_lasting_exceeding,
                )
                for _type, count in long_lasting_exceeding.iteritems():
                    event_type = EVENTS_TRANSLATION.get(
                        EVENTS_TYPES.get(_type), "Unknown"
                    )
                    alarm_messages = make_alarm_message(
                        channel_obj.name,
                        datetime.datetime.now(),
                        event_type,
                        zone,
                        count,
                        self.observable_types.get(_type),
                    )
                    events.append(
                        (channel_full, long(int(time.time()) * 1e6), alarm_messages, zone)
                    )

            if self.callback:
                for event in events:
                    channel_full, event_ts, alarm_messages, zone_name = event
                    self.callback(channel_full, event_ts, alarm_messages, zone_name=zone_name)

            for zone in zones_with_detections:
                self.clean_old_detections(channel_full, zone)
        except Exception:
            logger.exception("unhandled exception")
