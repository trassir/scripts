# More info: https://confluence.trassir.com/pages/viewpage.action?pageId=42467986

import json

import host

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

__version__ = "1.0.0"
logger.debug("%s version: %s", __name__, __version__)

script = host.stats().parent()
server = host.settings("")


class Event(object):
    def __init__(self, type):
        """

        Args:
            type (str): Event type
        """
        self.__type = str(type)

    @property
    def type(self):
        return self.__type

    def __repr__(self):
        return "<Event({s.type})>".format(s=self)

    def __str__(self):
        return self.type


class State(object):
    class Value(object):
        def __init__(self, value, icon=None):
            self.__value = str(value)
            self.__icon = icon if icon else None

        def __repr__(self):
            return "<State.Value({s.value}, icon={s.icon})>".format(s=self)

        @property
        def value(self):
            return self.__value

        @property
        def icon(self):
            return self.__icon

    def __init__(self, name, values=None):
        """

        Args:
            name (str): State name
            values (Tuple(State.Value), optional): State values
        """
        self.__name = str(name)

        assert values, "No state values specified"
        if isinstance(values, list):
            values = tuple(values)
        elif isinstance(values, self.Value):
            values = (values,)
        self.__values = values

    def __repr__(self):
        return "<State({s.name}, values={s.values})>".format(s=self)

    def __getitem__(self, item):
        return self.values[item].value

    @property
    def name(self):
        return self.__name

    @property
    def values(self):
        return self.__values


class BaseObject(host.TrassirObject, object):
    classname = None
    events = None
    states = None

    default_icon = ":/archer/any_object.png"

    def __new__(cls, *args, **kwargs):
        if cls.events and isinstance(cls.events, Event):
            cls.events = (cls.events,)

        if cls.states and isinstance(cls.states, State):
            cls.states = (cls.states,)

        if cls.states:
            # Creating state props
            for state in cls.states:
                if getattr(cls, state.name, None) is None:
                    def getter(self, name=state.name):
                        return self.__obj.state(name)

                    def setter(self, value, name=state.name):
                        self.set_state(
                            [
                                value if st.name == name else getattr(self, st.name)
                                for st in self.states
                            ]
                        )

                    setattr(cls, state.name, property(getter, fset=setter))

        return super(BaseObject, cls).__new__(cls, *args, **kwargs)

    def __init__(self, name=None, guid=None, parent="", folder="", associated_channel="", **kwargs):
        self.__obj = None
        self.classname = self.classname or self.__class__.__name__

        self._folder = ""
        self._name = name or script.name
        self._guid = guid or "{}-object".format(script.guid)
        self._parent = parent

        self.__register_class_if_not_exists()
        super(BaseObject, self).__init__(self.classname)

        initial_state = getattr(self, "initial_state", None)
        if initial_state is None:
            initial_state = []
            if self.states:
                for state in self.states:
                    initial_state.append(state.values[0].value)

        self.set_name(self._name)
        self.set_guid(self._guid)
        self.set_parent(self._parent)
        self.set_initial_state(initial_state)
        if associated_channel:
            self.set_associated_channel(str(associated_channel))

        host.object_add(self)

        self.__obj = host.object(self._guid)

        if folder:
            self.folder = folder

        self.context_menu = []

    def __register_class_if_not_exists(self):
        check_object = host.TrassirObject(self.classname)
        try:
            check_object.set_initial_state([0])
            logger.debug("class %s already registered", self.classname)
        except RuntimeError as err:
            if err.message.endswith("not exist"):
                logger.debug("Register new class %s ...", self.classname)
                new_object_class = host.TrassirObjectClass()
                new_object_class.set_class_name(self.classname)

                if self.events:
                    for event in self.events:
                        assert isinstance(event, Event), (
                            "Unexpected event class %s" % event.__class__.__name__
                        )
                        new_object_class.create_event(event.type)

                if self.states:
                    for state in self.states:
                        assert isinstance(state, State), (
                            "Unexpected state class %s" % state.__class__.__name__
                        )
                        new_object_class.create_state(state.name)
                        for state_value in state.values:
                            assert isinstance(state_value, State.Value), (
                                "Unexpected state value class %s"
                                % state_value.__class__.__name__
                            )
                            new_object_class.add_state_description(
                                state.name,
                                state_value.value,
                                state_value.icon or self.default_icon,
                            )

                new_object_class.register_class_in_trassir()
                logger.info("New class %s registered success", self.classname)
            else:
                logger.debug("class %s already registered!", self.classname)

    def __getattr__(self, item):
        if self.__obj:
            return getattr(self.__obj, item)
        raise AttributeError(
            "'%s' object has no attribute '%s'" % (self.__class__.__name__, item)
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.set_name(value)
            self._name = value
        else:
            raise ValueError("Expected str, got {}".format(type(value).__name__))

    @property
    def folder(self):
        return self._folder

    @folder.setter
    def folder(self, value):
        if not value:
            raise ValueError("Object guid can't be empty")

        if isinstance(value, str):
            if self._folder:
                self.change_folder(value)
            else:
                self.set_folder(value)
            self._folder = value
        else:
            raise ValueError("Expected str, got {}".format(type(value).__name__))

    def context_menu_button(self, text, callback):
        """Add context button to object menu

        Args:
            text (str): Button text
            callback (function): Callback function

        Returns:
            :obj:`SE_ContextCatcher`: Context menu handler

        Raises:
            ValueError: If text is empty
            TypeError: if callback is not callable
        """
        if not text:
            raise ValueError("No text")

        if not callable(callback):
            raise TypeError("Callback function is not callable")

        btn = host.activate_on_context_menu(self._guid, text, callback)
        self.context_menu.append((text, callback.__name__, btn))
        return btn

    def fire_event_(self, event_type, message="", channel="", data=""):
        """Generate trassir event

        Args:
            event_type (str): Event type
            message (str, optional): Event message (``p1``)
            channel (str, optional): Event associated channel (``p2``)
            data (str, optional): Event data (``p3``)
        """
        if not isinstance(data, str):
            data = json.dumps(data)

        self.fire_event(str(event_type), str(message), str(channel), str(data))
