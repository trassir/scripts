# -*- coding: utf-8 -*-

import time
import itertools
from output_reaction import OutputReactions
import host

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger
logger = get_logger()


class OutputReactionsIII(OutputReactions):
    def __init__(
        self, gpios, delay, reaction_type, delay_between_iterations, *args, **kwargs
    ):
        super(OutputReactionsIII, self).__init__(gpios, delay, reaction_type)
        self.delay_between_iterations = delay_between_iterations
        self.loop_working = False
        self.count = 0
        self.prev_oper_ts = 0
        self._method_to_work = None
        self.method_to_work = [self.first_method, self.last_method]
        self.prev_method = self.last_method

    @staticmethod
    def _methods_iterator(methods):
        for m in itertools.cycle(methods):
            yield m

    @property
    def method_to_work(self):
        return self._method_to_work

    @method_to_work.setter
    def method_to_work(self, methods):
        self._method_to_work = self._methods_iterator(methods)

    def output_manager_loop(self):
        diff = time.time() - self.prev_oper_ts
        if diff > self.delay and self.prev_method == self.first_method:
            # внутри одной итерации, время вызвать второй метод (закрыть шлагбаум)
            logger.debug(
                "Inside the iteration. Time to close gate. Time passed since the last operation (%s) > delay (%s) ",
                time.time() - self.prev_oper_ts,
                self.delay,
            )

            self.count -= 1
            logger.debug("count decreased. count: %s", self.count)

            self.prev_oper_ts = time.time()
            _method_to_work = self.method_to_work.next()
            logger.debug(
                "method name: %s", _method_to_work.__name__,
            )
            self.prev_method = _method_to_work
            _method_to_work()

            if self.count < 0:
                logger.warning("something goes wrong, count is: %s", self.count)
                self.count = 0
            if self.count <= 0:
                logger.debug("all iterations were made, stop loop")
                self.loop_working = False
            else:
                logger.debug("host.timeout -- 1")
                host.timeout(1000, self.output_manager_loop)
        elif diff > self.delay_between_iterations and self.prev_method == self.last_method:
            # между итерациями, время вызвать первый метод (открыть шлагбаум)
            logger.debug("Between two iterations. Time passed since the last iteration (%s)"
                         " > delay_between_iterations (%s)",
                         diff,
                         self.delay_between_iterations
                         )
            self.prev_oper_ts = time.time()
            _method_to_work = self.method_to_work.next()
            logger.debug(
                "method name: %s", _method_to_work.__name__,
            )
            self.prev_method = _method_to_work
            _method_to_work()
            logger.debug("host.timeout -- 2")
            host.timeout(1000, self.output_manager_loop)

        else:
            # waiting
            logger.debug("host.timeout -- 3. delay in action, going to check next loop")
            host.timeout(1000, self.output_manager_loop)

    def execute(self, *args, **kwargs):
        self.count += 1
        logger.debug("count increased. count: %s", self.count)
        if self.loop_working:
            return
        else:
            self.loop_working = True
            logger.debug("loop_working --> True")
            self.output_manager_loop()
