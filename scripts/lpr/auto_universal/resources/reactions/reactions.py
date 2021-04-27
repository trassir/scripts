# -*- coding: utf-8 -*-

import host
from __builtin__ import object as py_object
from executor import Executor
from script_object import ScriptObject


try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger
logger = get_logger()


class Reactions(py_object):
    """Класс диспетчер для вызова всех 'зарегестрирвоанных'
    в нем реакций.

    Examples:
        >>> reactions = Reactions()
        >>> reactions.add_executor(PlaySound(sound_name))
        >>> reactions.make_reactions(channel, tmstmp, alarm_messages, images=None)

        Объект PlaySound(sound_name) наследуется от класса Executor и необходимо,
        чтобы он имел метод execute(channel, tmstmp, alarm_messages, images=None),
        где channel (str) - гуид канала, tmstmp - Trassir timestamp,
        alarm_messages (dict) - словарь с ключами "alert_message",
         "sms_message", "mail_message",
        значение это сформированное сообщение в соответстии с типом.

        Args:
            schedule_color (str): цвет расписания для работы скрипта
    """

    WORKING_COLOR = "Red"

    def __init__(self, schedule):
        self.schedule = schedule
        self.executors = {}

    def add_executor(self, executor):
        if not (issubclass(executor.__class__, Executor) or issubclass(
            executor.__class__, ScriptObject
        )):
            raise TypeError(
                "{} is not subclass of Executor".format(executor.__class__.__name__)
            )
        logger.info("Reactions.add executor: %s", executor.__class__.__name__)
        self.executors[executor.__class__.__name__] = executor

    def make_reactions(self, channel_obj, ts, alarm_messages, *args, **kwargs):
        """

        Args:
            channel_obj (:obj: 'Channel'):
            ts (int): (Trassir 16 digit timestamp)
            alarm_messages:
            *args:
            **kwargs:

        Returns:

        """
        if self.schedule is not None and self.schedule.color != self.WORKING_COLOR:
            logger.debug(
                "Event don't call reaction: schedule color %s, to react must be: %s",
                self.schedule.color,
                self.WORKING_COLOR,
            )
            return
        host.stats()["run_count"] += 1

        for e_name, executor in self.executors.iteritems():
            logger.debug("Start make reaction: %s", e_name)

            executor.execute(channel_obj, ts, alarm_messages, *args, **kwargs)


