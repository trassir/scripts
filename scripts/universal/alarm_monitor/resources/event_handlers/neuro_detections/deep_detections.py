# -*- coding:utf-8 -*-

from __builtin__ import object as py_object

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()


class DeepDetections(py_object):
    def __init__(
            self,
            obj_storage,
            zone_detector,
            cross_line_detector,
    ):
        """

        Args:
            obj_storage (ObjectsStorage): ObjectsStorage instance
            zone_detector (deep_detection.ObjectsInZoneDetector object):
            cross_line_detector(deep_detection.CrossLineDetector object):
        """
        self.obj_storage = obj_storage
        self.zone_detector = zone_detector
        self.cross_line_detector = cross_line_detector

    def check_channel(self, channel):
        res = False
        if not self.obj_storage.all_channels_in_work:
            res = channel in self.obj_storage.channels
        return self.obj_storage.all_channels_in_work or res

    def event_handler(self, event):
        channel = event.channel_guid
        if not self.check_channel(channel):
            logger.debug(
                "channel %s not in channels list, return", channel
            )
            return
        if self.zone_detector:
            self.zone_detector.event_handler(event)
        if self.cross_line_detector:
            self.cross_line_detector.event_handler(event)
