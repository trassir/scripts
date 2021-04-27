# -*- coding: utf-8 -*-

import abc
from __builtin__ import object as py_object


class Executor(py_object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self, channel, ts, alarm_messages, shot_name, *args, **kwargs):
        """
        args, kwargs
        Args:
            channel (full guid):
            ts (long): Trassir 16-digit timestamp
            alarm_messages (dict):
            shot_name (str):

        Returns:

        """
        pass