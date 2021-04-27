import time

import host

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

__version__ = "1.0.0"
logger.debug("%s version: %s", __name__, __version__)


class LongEventHandler(object):
    def __init__(self, event_types, callback, event_filter=None, duration=5, mode=2):
        """

        Args:
            event_types (Tuple[str, str]): Events tuple. For example ("Motion Start", "Motion Stop")
            callback (callable(ev)): Callback function with event as argument
            event_filter (callable(ev), optional): Callable event filter function, must return bool
            duration (int, optional): Min. event duration, seconds. Default 5 seconds
            mode (int, optional): Callback event index (0 | 1). If index is out of range - callback all events.
        """
        if isinstance(event_types, (list, tuple)):
            self.__event_types = tuple(event_types)
            if len(self.__event_types) != 2:
                raise ValueError("Expected 2 event types, got %s" % len(self.__event_types))
        else:
            raise TypeError("Expect list or tuple for event_types, got %s" % type(event_types).__name__)
        try:
            self.__callback_events = (self.__event_types[mode],)
        except IndexError:
            self.__callback_events = self.__event_types
        self.__current_events = {}
        self.__working_now = False

        self.duration = duration
        self.callback = callback
        self.event_filter = event_filter

    def __events_checker(self):
        if not self.__current_events:
            self.__working_now = False
            return

        ts_now = time.time()
        for guid in self.__current_events.keys():
            if ts_now > self.__current_events[guid].callback_ts:
                self.__callback(self.__current_events.pop(guid))

        host.timeout(self.duration * 100, self.__events_checker)

    def __callback(self, ev):
        if ev.type in self.__callback_events:
            self.callback(ev)

    def activate_on_events(self):
        """Add activate on selected events handler"""
        host.activate_on_events(self.__event_types[0], "", self)
        host.activate_on_events(self.__event_types[1], "", self)

    def __call__(self, ev):
        """Events handler

        You can use host.activate_on_events to handle custom events.
        All events that not in selected event types ignored.

        Args:
            ev (host.SE_Event): Trassir event
        """
        if ev.type in self.__event_types:
            if not callable(self.event_filter) or self.event_filter(ev):
                popped_event = self.__current_events.pop(ev.origin, None)
                if popped_event is None:
                    ev.callback_ts = time.time() + self.duration
                    self.__current_events[ev.origin] = ev

                    if self.__working_now is False:
                        self.__working_now = True
                        self.__events_checker()
