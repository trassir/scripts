# -*- coding: utf-8 -*-

import host
from __builtin__ import object as py_object

from helpers import get_logger

logger = get_logger()
from executors import Executor


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
            schedule (ScheduleObject|None): объкт класса из модуля schedule
    """

    WORKING_COLOR = "Red"

    def __init__(self, schedule, input_filter_obj, input_state_to_react):
        self.schedule = schedule
        self.input_filter_obj = input_filter_obj
        self.input_state_to_react = input_state_to_react
        self.executors = {}

    def add_executor(self, executor):
        if not issubclass(executor.__class__, Executor):
            raise TypeError(
                "{} is not subclass of Executor".format(executor.__class__.__name__)
            )
        logger.info("Reactions.add executor: %s", executor.__class__.__name__)
        self.executors[executor.__class__.__name__] = executor

    def make_reactions(self, channel, tmstmp, alarm_messages, *args, **kwargs):
        """

        Args:
            channel (str):
            tmstmp (long): Trassir 16 digit timestamp
            alarm_messages (dict):

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

        if self.input_filter_obj:
            try:
                current_state = self.input_filter_obj.state("gpio_input_level")
                if self.input_state_to_react not in current_state:
                    logger.debug(
                        "Current state of input is: %s, to react must be %s",
                        current_state,
                        self.input_state_to_react
                    )
                    return
            except EnvironmentError:
                logger.warning("Can't get state for input to filter reaction work")

        host.stats()["run_count"] += 1
        for e_name, executor in self.executors.iteritems():
            logger.debug("Start make reaction: %s", e_name)
            executor.execute(channel, tmstmp, alarm_messages, *args, **kwargs)
