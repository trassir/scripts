# -*- coding: utf-8 -*-

from script_object import ScriptObject

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger
logger = get_logger()


class FireEvent(ScriptObject):
    def __init__(self, name=None, guid=None, parent=None):
        super(FireEvent, self).__init__(name, guid, parent)

    def execute(self, channel_obj, ts, alarm_messages, *args, **kwargs):
        try:
            self.fire_event_v2(
                message="plate detected",
                channel=getattr(channel_obj, "full_guid"),
                data={"ts": ts, "alarm_messages": alarm_messages},
            )
        except Exception as err:
            logger.exception(err)
