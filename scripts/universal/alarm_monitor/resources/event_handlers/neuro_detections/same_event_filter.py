# -*-coding: utf-8 -*-

import time
from __builtin__ import object as py_object

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()


class SameEvent(py_object):
    """
    Check is event same.
    events (dict): {channel: {zone_id: {_type: timestamp}}}
    """

    def __init__(self, same_event_delay):
        self.events = {}
        self.same_event_delay = same_event_delay
        self.working = False

    def is_same(self, data):
        """
        Args:
            data (dict): {channel: {zone_id: {_type: count}}}
        Returns:

        """

        now = time.time()
        for channel, _d1 in data.iteritems():
            if not self.events.get(channel):
                for zone_id, _d2 in _d1.iteritems():
                    for _type, _ in _d2.iteritems():
                        self.events[channel] = {zone_id: {_type: time.time()}}
                logger.debug("not same: 1st")
                return

            for zone_id, _d2 in _d1.iteritems():
                if not self.events[channel].get(zone_id):
                    for _type, _ in _d2.iteritems():
                        self.events[channel] = {zone_id: {_type: time.time()}}
                    logger.debug("not same 2nd")
                    return
                for _type, _ in _d2.iteritems():
                    if not self.events[channel][zone_id].get(_type):
                        self.events[channel][zone_id][_type] = time.time()
                        logger.debug("not same 3rd")
                        return
                    if now - self.events[channel][zone_id][_type] < self.same_event_delay:
                        logger.debug(
                            "Same event detected, break: %s, diff: %s",
                            self.events[channel][zone_id][_type],
                            now - self.events[channel][zone_id][_type],
                        )
                        return True
                    else:
                        self.events[channel][zone_id][_type] = now