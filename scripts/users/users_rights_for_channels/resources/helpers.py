# -*- coding: utf-8 -*-
import sys
import re
import os
import logging
from collections import deque

import host

__version__ = "2.0.0"

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
finalizers = []


def win_encode_path(path):
    if os.name == "nt":
        try:
            path = path.decode("utf8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return path


class DuplicateFilter(logging.Filter):
    """Suppressing multiple messages with same content.

    Tracking last logged record and filter out any
    repeated (similar) records.

    Example:
        --- The last message repeated 3 times
    """

    def __init__(self):
        super(DuplicateFilter, self).__init__()
        self._last_log = None
        self._last_log_count = 1

    def filter(self, record):
        record.duplicates = ""
        current_log = (record.module, record.levelno, record.msg)
        if current_log == self._last_log:
            self._last_log_count += 1
            return False
        else:
            if self._last_log_count > 1:
                record.duplicates = (
                        "--- The last message repeated %s times\n" % self._last_log_count
                )
            self._last_log = current_log
            self._last_log_count = 1
            return True


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
    WRITE_TIMEOUT_MS = 2000
    MAX_LOG_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB

    def __init__(self, filename):
        super(MyFileHandler, self).__init__()
        self.__file_path = win_encode_path(
            os.path.join(
                host.settings("system_wide_options")["screenshots_folder"], filename
            )
        )
        self.__writer_working = False
        self.__msg_queue = deque(maxlen=1000)
        finalizers.append(self.__writer)

    @property
    def filepath(self):
        return self.__file_path

    def __check_log_size(self):
        if os.path.isfile(self.__file_path):
            if os.path.getsize(self.__file_path) > self.MAX_LOG_SIZE_BYTES:
                old_filename = self.__file_path + '.old'
                if os.path.isfile(old_filename):
                    os.remove(old_filename)
                os.rename(self.__file_path, self.__file_path + '.old')

    def __writer(self):
        self.__check_log_size()
        with open(self.__file_path, "a") as log_file:
            while self.__msg_queue:
                log_file.write("%s\n" % self.__msg_queue.popleft())
        self.__writer_working = False

    def emit(self, record):
        self.__msg_queue.append(self.format(record))
        if not self.__writer_working:
            self.__writer_working = True
            host.timeout(self.WRITE_TIMEOUT_MS, self.__writer)


def init_logger(name, debug=False, duplicate_filter=False):
    script_ = host.stats().parent()
    name = "{name}_({guid})".format(name=name.replace(" ", "_"), guid=script_.guid)
    logger = logging.getLogger(name)
    logger.filepath = None

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
        fmt = "%(asctime)s [%(levelname)-8s] %(lineno)-4s <%(funcName)s> - %(message)s"
        file_handler = MyFileHandler("%s.log" % name)
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")
        if duplicate_filter:
            fmt = "%(duplicates)s" + fmt
            file_formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")
            file_handler.addFilter(DuplicateFilter())
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        logger.filepath = file_handler.filepath

    logger.info("Starting script %s (%s), helpers v%s", script_.name, script_.guid, __version__)
    logger.debug("Script parameters\n%s", script_["parameters"])

    return logger


def get_logger():
    return getattr(main_module, "logger", None) or logging.getLogger()


def set_script_name(name=None):
    """Set script name

    Args:
        name (str, optional): Script name, if None - parse name from parameters

    Returns:
        str: Script name
    """
    if name:
        default_script_name = str(name)
    else:
        doc = getattr(main_module, "__doc__", None) or ""
        title = re.search(r"<title>(.+)</title>", doc)
        version = None
        if title:
            version = re.search(r"<version>(.+)</version>", doc)
        default_script_name = "{title} v{version}".format(
            title=title.group(1), version=version.group(1) if version else "?.?.?"
        )
    if SCRIPT_NAME in DEFAULT_SCRIPT_NAMES:
        host.stats().parent()["name"] = default_script_name
    return default_script_name


def __finalizer():
    for finalizer in finalizers:
        finalizer()


host.register_finalizer(__finalizer)
