# -*- coding: utf-8 -*-

import abc
from __builtin__ import object as py_object


class Executor(py_object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self, channel_obj, ts, alarm_messages, shot_name):  #
        """
        args, kwars
        Args:
            channel_obj (:obj: 'Channel'):
            ts (int): (Trassir 16 digit timestamp)
            alarm_messages:
            shot_name (str):

        Returns:

        """
        pass