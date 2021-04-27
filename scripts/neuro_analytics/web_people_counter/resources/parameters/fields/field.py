import abc

import host

from helpers import get_logger

logger = get_logger()


class Field(object):
    __metaclass__ = abc.ABCMeta

    default = None

    def __init__(self, key, name, *args, **kwargs):
        self.key = key
        self.name = host.tr(name)
        self.multiple = kwargs.get("multiple", False)
        self.description = kwargs.get("description", "")
        self.onchange = kwargs.get("onchange")
        self.kwargs = kwargs
        self.__value = self.default

        if callable(self.onchange):
            self.onchange(self, None)

    def __repr__(self):
        return "<{self.__class__.__name__}({self.name!r}, {self.value!r})>".format(
            self=self
        )

    def clear_value(self, value):
        return value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        value = self.clear_value(val)
        prev_val = self.__value
        self.__value = value
        if prev_val != self.__value and callable(self.onchange):
            logger.debug("Value changed: %s -> %s", prev_val, value)
            self.onchange(self, prev_val)

    @abc.abstractmethod
    def get_html(self):
        pass

    def serialize(self):
        data = {"key": self.key, "type": self.__class__.__name__, "value": self.value}
        return data

    @classmethod
    def deserialize(cls, instance, data):
        kwargs = instance.kwargs
        kwargs["default"] = data["value"]
        return cls(instance.key, instance.name, **kwargs)

