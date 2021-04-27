# -*- coding: utf-8 -*-
import sys
import re
import os
import logging
from collections import deque

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


def win_encode_path(path):
    if os.name == "nt":
        try:
            path = path.decode("utf8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return path


class HostLogHandler(logging.Handler):
    def emit(self, record):
        host.log_message(self.format(record))


class PopupHandler(logging.Handler):
    """Trassir popup handler"""

    _popups = {
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


class MyFileHandler(logging.Handler):
    WRITE_TIMEOUT_MS = 1000

    def __init__(self, filename):
        super(MyFileHandler, self).__init__()
        self.__file_path = win_encode_path(
            os.path.join(
                host.settings("system_wide_options")["screenshots_folder"], filename
            )
        )
        self.__writer_working = False
        self.__msg_queue = deque(maxlen=1000)

    def __writer(self):
        with open(self.__file_path, "a") as log_file:
            while self.__msg_queue:
                log_file.write("%s\n" % self.__msg_queue.popleft())
        self.__writer_working = False

    def emit(self, record):
        self.__msg_queue.append(self.format(record))
        if not self.__writer_working:
            self.__writer_working = True
            host.timeout(self.WRITE_TIMEOUT_MS, self.__writer)


def init_logger(name, debug=False):
    name = "{name} ({guid})".format(name=name, guid=host.stats().parent().guid)
    logger = logging.getLogger(name)

    for handler_ in logger.handlers[:]:
        handler_.close()
        logger.removeHandler(handler_)

    logger.setLevel("DEBUG")

    host_handler = HostLogHandler()
    host_handler.setLevel(logging.DEBUG if debug else logging.INFO)
    host_formatter = logging.Formatter(
        "%(name)s [%(levelname)-8s] %(lineno)-4s <%(funcName)s> - %(message)s"
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

    if debug:
        file_handler = MyFileHandler("%s.log" % name)
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            fmt="%(asctime)s [%(levelname)-8s] %(lineno)-4s <%(funcName)s> - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger


def get_logger():
    return getattr(main_module, "logger", None) or logging.getLogger()


def set_script_name():
    doc = getattr(main_module, "__doc__", None) or ""
    title = re.search(r"<title>(.+)</title>", doc)
    if title:
        version = re.search(r"<version>(.+)</version>", doc)
    default_script_name = "{title} v{version}".format(
        title=title.group(1), version=version.group(1) if version else "?.?.?"
    )
    if SCRIPT_NAME in DEFAULT_SCRIPT_NAMES:
        host.stats().parent()["name"] = default_script_name
    return default_script_name
