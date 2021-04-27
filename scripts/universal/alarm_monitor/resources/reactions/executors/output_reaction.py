# -*- coding: utf-8 -*-

import host
import time
from executor import Executor

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger
logger = get_logger()


class OutputReactions(Executor):
    """
    Args:
        gpios (List[:class: 'TrObject']): Список объектов TrObject укзанных выходов
        delay (int): значение в секундах, 5 сек
        type (str): одно из возможных событий:
        '1.замкнуть,2.разомкнуть,3.замкнуть-разомкнуть,4.разомкнуть-замкнуть,5.замкнуть-замкнуть,6.разомкнуть-разомкнуть'
    """

    def __init__(self, gpios, delay, reaction_type, *args, **kwargs):
        self.gpios = gpios
        self.delay = delay
        self.logic = {
            1: (self._set_output_high, self.do_nothing),
            2: (self._set_output_low, self.do_nothing),
            3: (self._set_output_high, self._set_output_low),
            4: (self._set_output_low, self._set_output_high),
            5: (self.high_high, self.high_high),
            6: (self.low_low, self.low_low),
        }
        self.first_method = None
        self.last_method = None
        self.open_flag = False
        self.ts_to_come_back = 0
        self.output_logic(reaction_type)

        logger.debug(
            "gpios: %s, delay: %s, reaction_type: %s",
            self.gpios,
            self.delay,
            reaction_type,
        )

    def output_logic(self, oper_type):
        if not isinstance(oper_type, str):
            logger.error("Type is not str. Can't initialize logic.")
            raise ValueError("{} is not string!".format(oper_type))
        reaction_code = oper_type.split(".")[0]
        if not reaction_code.isdigit():
            logger.error("Reaction code must be digit. Can't initialize logic.")
            raise ValueError(
                "Reaction code must be digit. {} is not digit!".format(reaction_code)
            )
        reaction_code = int(reaction_code)
        _methods = self.logic.get(reaction_code)
        if _methods is None:
            logger.error("Can't get associated methods. Can't initialize logic.")
            raise ValueError("Can't get associated methods. Can't initialize logic.")

        self.first_method = _methods[0]
        self.last_method = _methods[1]

        logger.debug(
            "Output logic initialized successful. Methods are: %s, %s",
            self.first_method.__name__,
            self.last_method.__name__,
        )

    def do_nothing(self):
        pass

    def _set_output_low(self):
        logger.debug("Start setting low")
        for gpio in self.gpios:
            gpio.set_output_low()

    def _set_output_high(self):
        logger.debug("Start setting high")
        for gpio in self.gpios:
            gpio.set_output_high()

    def low_low(self):
        # low - high - low
        logger.debug("start setting low_high_low operation")
        self._set_output_low()
        host.timeout(500, self._set_output_high)

    def high_high(self):
        # high - low - high
        logger.debug("start setting high-low-high operations")
        self._set_output_high()
        host.timeout(500, self._set_output_low)

    def _timer(self):
        if self.ts_to_come_back < time.time():
            logger.debug(
                "Timer is stopping. %s < %s", self.ts_to_come_back, time.time()
            )
            self.open_flag = False
            self.last_method()
            self.ts_to_come_back = 0
        else:
            host.timeout(1000, self._timer)

    def output_operation(self):
        """
        - Если шлагбаум закрыт (open_flag == False), то выполняет первый метод,
         а второй метод запустится когда ts_to_come_back == time.time()
        - Если шлагбаум поднят на данный момент, то first_method -не запускается,
        а ts_to_come_back увеличивается на delay
        - Таймер _timer следит, когда нужно запустить last_method

        """
        if self.open_flag:
            self.ts_to_come_back += self.delay
            logger.debug(
                "Increase timer, last operation will be after: %s seconds.",
                self.ts_to_come_back - int(time.time()),
            )
            return
        else:
            self.ts_to_come_back = int(time.time()) + self.delay
            logger.debug("Setup timer, last operation will be after: %s", self.delay)
            self.open_flag = True
        self.first_method()
        self._timer()

    def manual_activation_of_outputs(self):
        logger.debug("Manual activation of outputs starting.")
        host.stats()["run_count"] += 1
        self.output_operation()

    def execute(self, *args, **kwargs):
        self.output_operation()
