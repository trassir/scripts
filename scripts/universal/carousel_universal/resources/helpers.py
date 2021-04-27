# -*- coding: utf-8 -*-
import sys
import re
import json
import logging

import host

SCRIPT_NAME = host.stats().parent().name
DEFAULT_SCRIPT_NAMES = {
    "Yeni skript",
    "Unnamed Script",
    "უსახელო სკრიპტი",
    "Жаңа скрипт",
    "Script nou",
    "Новый скрипт",
    "Yeni skript dosyası",
    "Новий скрипт",
    "未命名脚本",
}
main_module = sys.modules.get(host.stats().parent().guid, host)


class HostLogHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        host.log_message(self.format(record))


class PopupHandler(logging.Handler):
    """Trassir popup handler"""

    def __init__(self):
        super(PopupHandler, self).__init__()
        self._popups = {
            "CRITICAL": host.error,
            "FATAL": host.error,
            "ERROR": host.error,
            "WARN": host.alert,
            "WARNING": host.alert,
            "INFO": host.message,
            "DEBUG": host.message,
            "NOTSET": host.message,
        }

    def emit(self, record):
        msg = self.format(record)
        self._popups[record.levelname](msg)


def init_logger(name, debug=False):
    logger = logging.getLogger(name)

    for handler_ in logger.handlers[:]:
        handler_.close()
        logger.removeHandler(handler_)

    logger.setLevel("DEBUG")

    host_handler = HostLogHandler()
    host_handler.setLevel(logging.DEBUG if debug else logging.INFO)
    host_formatter = logging.Formatter(
        "[%(levelname)-8s] %(lineno)-4s <%(funcName)s> - %(message)s"
    )
    host_handler.setFormatter(host_formatter)
    logger.addHandler(host_handler)

    popup_handler = PopupHandler()
    popup_handler.setLevel(logging.INFO if debug else logging.WARNING)
    popup_formatter = logging.Formatter(
        fmt="<b>[%(levelname)s]</b> Line: %(lineno)s<br><i>%(message).630s</i>"
    )
    popup_handler.setFormatter(popup_formatter)
    logger.addHandler(popup_handler)

    return logger


def get_logger():
    return (
        getattr(main_module, "logger", None)
        or logging.getLogger()
    )


def set_script_name():
    if SCRIPT_NAME in DEFAULT_SCRIPT_NAMES:
        doc = getattr(main_module, "__doc__", None) or ""
        title = re.search(r"<title>(.+)</title>", doc)
        if title:
            version = re.search(r"<version>(.+)</version>", doc)
            host.stats().parent()["name"] = "{title} v{version}".format(
                title=title.group(1),
                version=version.group(1) if version else "?.?.?"
            )


class ScriptObject(host.TrassirObject, object):
    """Trassir script object

    Args:
        name (str, optional): Object name, default :obj:`None`
        guid (str, optional): Object guid, default :obj:`None`
        parent (str, optional): Parent object guid, default :obj:`None`
    """

    def __init__(self, name=None, guid=None, parent=None):
        super(ScriptObject, self).__init__("Script")

        scr_parent = host.stats().parent()

        self._name = name or SCRIPT_NAME
        self.set_name(self._name)

        self._guid = guid or "{}-object".format(scr_parent.guid)
        self.set_guid(self._guid)

        self._parent = parent or host.settings("").guid
        self.set_parent(self._parent)

        self._folder = ""

        self._health = "OK"
        self._check_me = True

        self.set_initial_state([self._health, self._check_me])

        host.object_add(self)

        self._obj = host.object(self._guid)

        self.context_menu = []

    @property
    def health(self):
        self._health = self._obj.state("health")
        return self._health

    @health.setter
    def health(self, value):
        if value in ["OK", "Error"]:
            self.set_state([value, self._check_me])
            self._health = value
        else:
            raise ValueError("Expected 'OK' or 'Error', got '{}'".format(value))

    @property
    def check_me(self):
        self._check_me = int(self._obj.state("check_me"))
        return bool(self._check_me)

    @check_me.setter
    def check_me(self, value):
        if isinstance(value, bool) or value in [1, 0]:
            value = 1 - value
            self.set_state([self._health, value])
            self._check_me = value
        else:
            raise ValueError("Expected bool or 1|0, got '{}'".format(value))

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

    def fire_event_v2(self, message, channel="", data=""):
        """Generate trassir event

        Args:
            message (str): Event message (``p1``)
            channel (str, optional): Event associated channel (``p2``)
            data (str, optional): Event data (``p3``)
        """
        if not isinstance(data, str):
            data = json.dumps(data)

        self.fire_event("Script: %1", message, channel, data)
