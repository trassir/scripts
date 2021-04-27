# -*- coding: utf-8 -*-
import host

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

__version__ = "1.0.1"
logger.debug("%s version: %s", __name__, __version__)


class ScheduleObject(object):
    __obj = None
    __prev_color = None

    def __init__(self, name, color_change_handler=None):
        """

        Args:
            name (str): Имя расписания или его guid
            color_change_handler (callable, optional): Хендлер смены цвета, по умолчанию `None`
                Можно задать функцию, которая будет вызываться при каждой смене цвета.
                В качестве аргумента в данную функцию передается `self`


        Public attributes:
            name (str): Возвращает имя расписания
            guid (str): Возвращает guid расписания
            color (str): Возвращает текущий цвет расписания
            prev_color (str): Возвращает цвет расписания до последней смены цвета
        """
        self.color_change_handler = color_change_handler
        self.prev_color = self.__prev_color
        self._name = name
        self._load_object()

    def __repr__(self):
        return "<ScheduleObject({self._name}, {self.color})>".format(self=self)

    def __del__(self):
        del self.__obj

    def _load_object(self, tries=5):
        logger.debug("Loading schedule object('%s')...", self._name)
        for sett in host.settings("scripts").ls():
            if sett.type == "Schedule" and sett.name == self._name and sett["enable"]:
                obj = host.object(sett.guid)
                logger.debug("Found local schedule %s", sett.guid)
                break
        else:
            logger.warning("Local schedule not found, get random global object with name %r", self._name)
            obj = host.object(self._name)

        try:
            self._name = obj.name
            try:
                obj.state("color")
                logger.info("Schedule %s (%s) loaded success", obj.name, obj.guid)
            except KeyError:
                raise RuntimeError(
                    "Object {obj.name} ({obj.guid}) is not schedule".format(obj=obj)
                )

            self.__obj = obj
            self.__prev_color = self.color

            if callable(self.color_change_handler):
                logger.info("Add handler on color changed")
                host.register_finalizer(self.__del__)

                # Call handler with timeout need to fix bug:
                # Restarting schedule with not Green color
                # calls state changes handler twice:
                # with Green color and current color
                self.__obj.activate_on_state_changes(
                    lambda: host.timeout(1, self._state_changes)
                )
        except EnvironmentError:
            if tries:
                logger.warning("Schedule %s not found, next try after 1000ms", self._name)
                host.timeout(1000, lambda: self._load_object(tries - 1))
            else:
                raise EnvironmentError(
                    "Schedule with name {} not found".format(self._name)
                )

    def _state_changes(self):
        if self.__prev_color != self.color:
            self.prev_color, self.__prev_color = self.__prev_color, self.color
            logger.debug("%s color changed: %s -> %s", self, self.prev_color, self.color)
            if callable(self.color_change_handler):
                self.color_change_handler(self)
            else:
                logger.warning("%s color_change_handler is not callable", self)

    def __getattr__(self, item):
        try:
            return super(ScheduleObject, self).__getattr__(item)
        except AttributeError:
            return getattr(self.__obj, item)

    @property
    def color(self):
        if self.__obj:
            return self.__obj.state("color")
