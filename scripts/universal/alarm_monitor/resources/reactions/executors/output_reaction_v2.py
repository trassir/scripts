# -*- coding: utf-8 -*-

import time
from .output_reaction import OutputReactions
import host

from helpers import get_logger

logger = get_logger()


class OutputReactionsII(OutputReactions):
    def __init__(self, gpios, delay, reaction_type):
        super(OutputReactionsII, self).__init__(gpios, delay, reaction_type)
        self.task_count = 0
        self.channel = ""

    def _timer(self):
        if self.ts_to_come_back < time.time():
            logger.debug(
                "time to close the gate. %s < %s", self.ts_to_come_back, time.time()
            )
            self.last_method()
            self.open_flag = False
            self.task_count -= 1
            logger.debug(
                "gate task count decreased, task count is: %s", self.task_count
            )
            if self.task_count < 0:
                logger.warning("Task count couldn't be negative ")
                self.task_count = 0
            if self.task_count:
                host.timeout(2000, self.next_iteration)
        else:
            host.timeout(1000, self._timer)

    def next_iteration(self):

        self.open_flag = True
        self.ts_to_come_back = int(time.time()) + self.delay
        self.first_method()
        self._timer()

    def output_operation(self):
        self.task_count += 1
        logger.debug("gate task count increased, task count is: %s", self.task_count)
        if self.open_flag:
            return
        else:
            self.ts_to_come_back = int(time.time()) + self.delay
            logger.debug(
                "Setup timer, last operation will be after delay: %s seconds",
                self.delay,
            )
            self.open_flag = True
        self.first_method()
        self._timer()

    def execute(self, channel, *args, **kwargs):
        self.channel = channel
        self.output_operation()
