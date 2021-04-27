# -*- coding: utf-8 -*-
# <h3>Script changes screenshot folder on
# <span style="color: #dd042b">TrassirOS.</span></h3>
#
# <p style="color: #dd042b">Don't disable script if you select 'Network' or 'HDD' folder.</p>
#
# <p style="color: #074c80">
# Use "Custom" folder at your own risk
# </p><br>
#
# <code>Version: 0.2<br>
# Author: A.A.Trubilin, DSSL<br>
# E-mail: a.trubilin@dssl.ru<br>
# Help: https://scripts.page.link/change_screenshot_folder
# </code>
"""
<parameters>
    <company>AATrubilin</company>
    <title>change_screenshot_folder</title>
    <version>0.2</version>

    <parameter>
        <id>SHOTS_PATH</id>
        <type>string_from_list</type>
        <name>Screenshot folder</name>
        <value>Default</value>
        <string_list>Default,HDD,Network (CIFS),Custom</string_list>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>CHECK_WRITE_ACCESS</id>
        <name>Check write access</name>
        <value>True</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>DEBUG</id>
        <name>Debug mode</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Network folder settings</name>
    </parameter>
    <parameter>
        <id>NET_SOURCE</id>
        <type>string</type>
        <name>Source</name>
        <value>//172.20.0.10/shots</value>
    </parameter>
    <parameter>
        <id>NET_USERNAME</id>
        <type>string</type>
        <name>Username</name>
        <value>guest</value>
    </parameter>
    <parameter>
        <id>NET_PASSWORD</id>
        <type>string</type>
        <name>Password</name>
        <value></value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Custom folder settings</name>
    </parameter>
    <parameter>
        <id>CUSTOM_FOLDER</id>
        <type>string</type>
        <name>Full path</name>
        <value>/media/TrassirArchive/shots</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>CUSTOM_CREATE</id>
        <name>Create if not exist</name>
        <value>True</value>
    </parameter>

    <resources>
        <resource>ru.ts</resource>
        <resource>en.ts</resource>
    </resources>
</parameters>
"""

resources = {
    "ru.ts": """
        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
    """,
    "en.ts": """
        eAG9Vt9P2zAQfkfifzgyaXkZSceQNnWhGmpBTNoALd2kPSE3uTZWXTuyL5QK8b/vnB8tE7CX
        KTxUSZ3zfee7775zcjC5Gk9/X5/BNB3t7yXTFG7ROmn0SXAUDQJegyQzmvCO/DskWqxwlGZW
        lgT+PYnrlfrbCp0Ti+YPJM5UNsPRW0Wfiw/dlqwQeoEOXGYRtSsMwdyoHC0Yzdu8sSuFBkcb
        hSdBZpSxQ3iT54Pjo1kwmlrhnLRXaeQtY29aA8SMsL/XOihf2j0xOiTIpRMzhT4EH5Gcw8ZU
        4FBhRhBeIq2NXYZgLIQXk0nYxtcAlv9AGXw8zj41KfvpEIJx5cisgu58gjwOn3OtwUq3bN2w
        S/+Y2Z3nzOQ4+tWUYQiD6GhrAKcVFR7sNDqNpraaSSX1O5ik6bedzdnhSkg1BBFRa/Eld05F
        ttrZXKAqh1AQlW4Yx00mXFRy8SK2X8ZNmW52VbppTtEFXYeYxG2Jm3qTFdopQRw10KbkzFR6
        LrV0BeZB3DAkfkyR5/nCRPmbGf3AjAvMlrC2khBElrFJPzgTnFULWHG++vHf8rVjmUMiqRc9
        HSatH/345p6xjaD04f2adYPzlPdEprrVX6cG55VSUAoqejqKRcEtwaqouQPxTjrqB4i1FS4Z
        4txUOj9opem7WLIwV5Z7kkChcATvwVtKx11K8hZrHWbLH+hIWGpVPIKvnYwjUMHWLSaIhZAa
        DsEPMfYAa0kFI5SlsdTp4muQwmeTidETlPCDjYXTl64FDO8fwjZXZ9byNPOaDfcPQ/71xMwG
        +P5hR52uWinyaH2GWiGcAM+xnpr+qcYDmcf5gTlPSsxfSlO7Pq6H4faeYrc3iPApQNjPSaae
        0u2FxWi14WAsJ669DP0nZsLjvLvhJXF9EfwDecxBvg==
    """,
}


import os
import logging
import threading
import subprocess

from functools import wraps
from abc import ABCMeta, abstractmethod
from __builtin__ import object as py_object

import host

GLOBALS = globals()

SHOTS_PATH = GLOBALS.get("SHOTS_PATH", "HDD")
CHECK_WRITE_ACCESS = GLOBALS.get("CHECK_WRITE_ACCESS", True)
DEBUG = GLOBALS.get("DEBUG", False)

NET_SOURCE = GLOBALS.get("NET_SOURCE", "//172.20.0.10/trassirShots")
NET_USERNAME = GLOBALS.get("NET_USERNAME", "trassir")
NET_PASSWORD = GLOBALS.get("NET_PASSWORD", "12345")

CUSTOM_FOLDER = GLOBALS.get("CUSTOM_FOLDER", "/media/TrassirArchive/shots")
CUSTOM_CREATE = GLOBALS.get("CUSTOM_CREATE", True)


def run_as_thread(func):
    """Run function as thread"""

    @wraps(func)
    def run(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread

    return run


def raise_from_thread(e):
    def raise_(err):
        raise err

    host.timeout(1, lambda: raise_(e))


def set_script_name(name):
    _scr_default_names = (
        "Yeni skript",
        "Unnamed Script",
        "უსახელო სკრიპტი",
        "Жаңа скрипт",
        "Script nou",
        "Новый скрипт",
        "Yeni skript dosyası",
        "Новий скрипт",
        "未命名脚本",
    )
    if host.stats().parent().name in _scr_default_names:
        host.stats().parent()["name"] = name  # pylint: disable=E1137
        return True
    return False


class HostLogHandler(logging.Handler):
    """Trassir main log handler"""

    def __init__(self):
        super(HostLogHandler, self).__init__()

    def emit(self, record):
        msg = self.format(record)
        # noinspection PyBroadException
        try:
            host.log_message(msg)
        except:  # pylint: disable=W0702
            # Handle NameError trassir error if logger in finalizer function
            pass


class PopupHandler(logging.Handler):
    """Trassir popup handler"""

    def __init__(self, host_api=host):
        super(PopupHandler, self).__init__()
        self._host_api = host_api
        self._popups = {
            "CRITICAL": host_api.error,
            "FATAL": host_api.error,
            "ERROR": host_api.error,
            "WARN": host_api.alert,
            "WARNING": host_api.alert,
            "INFO": host_api.message,
            "DEBUG": host_api.message,
            "NOTSET": host_api.message,
        }

    def emit(self, record):
        msg = self.format(record)
        self._popups[record.levelname](msg)


def get_logger(host_log="WARNING", popup_log="ERROR"):
    """Prepare and returns logger

    Args:
        host_log (str, optional): HostLogHandler level. Default "WARNING"
        popup_log (str, optional): PopupHandler level. Default "ERROR"

    Returns:
        logging.logger: Logger
    """
    logger_ = logging.getLogger(__name__)
    logger_.setLevel("DEBUG")

    def _remove_handlers():
        """Close and remove handlers on disable script"""
        for handler in logger_.handlers[:]:
            handler.close()
            logger_.removeHandler(handler)

    host.register_finalizer(_remove_handlers)

    if host_log:
        host_handler = HostLogHandler()
        host_handler.setLevel(host_log)
        host_formatter = logging.Formatter(
            "[%(levelname)-8s] %(lineno)-4s <%(funcName)s> - %(message)s"
        )
        host_handler.setFormatter(host_formatter)
        logger_.addHandler(host_handler)

    if popup_log:
        popup_handler = PopupHandler()
        popup_handler.setLevel(popup_log)
        popup_formatter = logging.Formatter(
            fmt="<b>[%(levelname)s]</b> Line: %(lineno)s<br><i>%(message).630s</i>"
        )
        popup_handler.setFormatter(popup_formatter)
        logger_.addHandler(popup_handler)

    return logger_


if DEBUG:
    logger = get_logger(host_log="DEBUG", popup_log="WARNING")
else:
    logger = get_logger(host_log="INFO", popup_log="ERROR")


class NetworkFolderError(Exception):
    """Raises when script has error while mount"""

    pass


class ShotsFolder(py_object):
    __metaclass__ = ABCMeta
    _DEFAULT = "/home/trassir/shots"
    rollback = False

    @abstractmethod
    def mount(self):
        """Method calls on start script and retunrs new shots folder path"""
        pass

    def umount(self):
        """Method calls when user disable script and must return default folder"""
        return self._DEFAULT


class DefaultFolder(ShotsFolder):
    """Default shots folder"""

    def mount(self):
        return self._DEFAULT


class HDDFolder(ShotsFolder):
    """Create and returns path on HDD"""

    def mount(self):
        """This script use host.path_arbitrary_data method

        And returns /media/TrassirArchive*/TrassirArbitraryData/shots

        Note:
            If there are several HDDs in the system, the path /media/TrassirArchive*
            is mounted dynamically and change at each boot.

        Returns:
            str: ...path_arbitrary_data/shots path

        Raises:
            EnvironmentError: if HDD not found
        """
        data_path = host.path_arbitrary_data()
        logger.debug("data_path = %r", data_path)
        if not data_path:
            logger.error("HDD Not Found")
            raise EnvironmentError(
                host.tr(
                    "HDD Not Found!<br>"
                    "Make sure at least 1 HDD is active.<br>"
                    "Restart script. If you see this message again - contact with support@dssl.ru"
                )
            )

        shots_path = os.path.join(data_path, "shots")
        if not os.path.isdir(shots_path):
            os.makedirs(shots_path)

        return shots_path


class CustomFolder(ShotsFolder):
    def __init__(self, folder, create_if_not_exists=False):
        """Create if need and return your path

        Args:
            folder (str): Full path to your custom shots folder
            create_if_not_exists (bool, optional): If True - script trying
                to create folder if it not exists. Default: False

        Raises:
            ValueError: if custom folder not set
        """
        if not folder:
            logger.warning("Custom folder not set")
            raise ValueError(host.tr("Custom folder not set"))

        self.folder = folder
        self.create_if_not_exists = create_if_not_exists

    def mount(self):
        """Check, create and return custom folder

        Returns:
            str: Full path to your custom shots folder

        Raises:

            OSError: if cant' crate folder
            EnvironmentError: if folder not exist and CUSTOM_CREATE is False
        """
        if not os.path.isdir(self.folder):
            if self.create_if_not_exists:
                try:
                    os.makedirs(self.folder)
                except OSError as err:
                    logger.exception("Can't create folder %r", self.folder)
                    raise OSError(
                        host.tr(
                            "Can't create folder '{}'<br>" "Error code {}: {}"
                        ).format(self.folder, err.errno, err.strerror)
                    )
            else:
                raise EnvironmentError(
                    host.tr("Folder {} not exist.<br>Set 'Create if not exist' = True")
                )

        return self.folder


class NetworkFolder(ShotsFolder):
    """Mount shared network folder by CIFS protocol

    More info: https://ru.bmstu.wiki/CIFS_(Common_Internet_File_System)
    """

    _UMOUNT = "sudo umount {target}"
    _CHMOD = "sudo chmod 777 {target}"
    _MOUNT = "sudo mount -t cifs {source} {target} -o username='{username}'"

    def __init__(
        self, source, target="/mnt/LocalStorage/shared", username="", password=""
    ):
        self.source = source
        self.target = target
        self.username = username
        self.password = password

        self.rollback = True

    @staticmethod
    def _popen(cmd):
        sp = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        out, err = sp.communicate()
        if err:
            logger.warning("ERROR Popen(%r): %s", cmd, err)
        else:
            if out:
                out = ": %s" % out
            logger.debug("SUCCESS Popen(%r)%s", cmd, out)
        return out, err

    def mount(self):
        """Mount network shared path

        - Create or umount target path
        - Change the access permissions to 777
        - Mount shared folder with username and pass

        Returns:
            str: Full path mounted folder

        Raises:
            NetworkFolderError: if mount command finished with error
        """
        if os.path.exists(self.target):
            self._popen(self._UMOUNT.format(target=self.target))

        else:
            logger.info("makedirs(%r)", self.target)
            os.makedirs(self.target)

        self._popen(self._CHMOD.format(target=self.target))

        mount = self._MOUNT.format(
            source=self.source, target=self.target, username=self.username
        )
        if self.password:
            mount += ",password='{password}'".format(password=self.password)

        _, err = self._popen(mount)
        if err:
            raise NetworkFolderError(err)
        else:
            return self.target

    def umount(self):
        """Unmounts a mounted network folder and returns default"""
        if os.path.exists(self.target):
            self._popen(self._UMOUNT.format(target=self.target))
            os.removedirs(self.target)

        return self._DEFAULT


class FolderSetter(py_object):
    def __init__(self, shots_folder_obj):
        if not issubclass(shots_folder_obj.__class__, ShotsFolder):
            raise TypeError(
                "{} is not subclass of ShotsFolder".format(
                    shots_folder_obj.__class__.__name__
                )
            )
        logger.info("FolderSetter(%s)", shots_folder_obj.__class__.__name__)
        self.folder = shots_folder_obj
        self._prev_folder = host.settings("system_wide_options")["screenshots_folder"]

    @staticmethod
    def _check_path(path):
        """Check write access to folder

            Args:
                path (str): Full folder path

            Raises:
                IOError: if can't write test file to folder
            """
        test_file = os.path.join(path, "write_test")
        try:
            with open(test_file, "w") as opened_file:
                opened_file.write("Test write access")
            os.remove(test_file)
        except IOError as err:
            logger.exception("No write access to folder %r", path)
            raise IOError(
                host.tr(
                    "Check write access to folder '{}' failed<br>"
                    "Error code {}: {}<br>"
                    "Change folder or disable 'Check write access'"
                ).format(path, err.errno, err.strerror)
            )

    @staticmethod
    def _set_screenshots_folder(path):
        logger.info("screenshots_folder = %r", path)
        host.settings("system_wide_options")["screenshots_folder"] = path

    def rollback(self):
        """Run umount and set default settings path"""
        rollback_path = self.folder.umount()
        self._set_screenshots_folder(rollback_path)

    def set_folder(self, tries=3, check_access=True):
        """Set folder to trassir settings

        Args:
            tries (int, optional): Numbers of tris to set folder. Default 3.
            check_access (bool, optional): Check write access if True. Default True.
        """
        host.stats()["run_count"] = tries
        try:
            new_folder = self.folder.mount()
            if check_access:
                self._check_path(new_folder)
            host.stats()["run_count"] = 0
        except Exception as err:  # pylint: disable=W0703
            if tries:
                logger.warning("%s attempt failed with error: %s", tries, err)
                host.timeout(
                    1000,
                    lambda: self.set_folder(
                        tries=(tries - 1), check_access=check_access
                    ),
                )
            else:
                logger.error("%s attempt failed with error: %s", tries, err)
                raise_from_thread(err)

            return

        self._set_screenshots_folder(new_folder)

        if self.folder.rollback is True:
            host.register_finalizer(self.rollback)


if __name__ == host.stats().parent().guid:
    t1utils.resources_check(script_path, resources)
    name_changed = set_script_name("Screenshot Folder Changer")

    if not name_changed:
        if os.name == "nt":
            raise OSError(host.tr("This script only for TrassirOS"))

        if SHOTS_PATH in (host.tr("Default"), "Default"):
            folder_obj = DefaultFolder()

        elif SHOTS_PATH == host.tr("HDD"):
            folder_obj = HDDFolder()

        elif SHOTS_PATH == host.tr("Network (CIFS)"):
            logger.info(
                "NET_SOURCE, NET_USERNAME, NET_PASSWORD = %r, %r, %r",
                NET_SOURCE,
                NET_USERNAME,
                NET_PASSWORD,
            )
            folder_obj = NetworkFolder(NET_SOURCE)
            folder_obj.username = NET_USERNAME
            folder_obj.password = NET_PASSWORD

        elif SHOTS_PATH == host.tr("Custom"):
            logger.info(
                "CUSTOM_FOLDER, CUSTOM_CREATE = %r, %r", CUSTOM_FOLDER, CUSTOM_CREATE
            )
            folder_obj = CustomFolder(CUSTOM_FOLDER, create_if_not_exists=CUSTOM_CREATE)

        else:
            logger.critical("Unknown shots path: %s", SHOTS_PATH)
            raise RuntimeError(host.tr("Unknown shots path: {}".format(SHOTS_PATH)))

        folder_setter = FolderSetter(folder_obj)
        folder_setter.set_folder(
            tries=3,
            check_access=CHECK_WRITE_ACCESS
        )
