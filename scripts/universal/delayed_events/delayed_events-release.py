# -*- coding: utf-8 -*-
# <h3>delayed_events</h3><br>
#
# <code>Version: v1.7.9<br>
# Author: A.A.Trubilin, DSSL<br>
# E-mail: a.trubilin@dssl.ru<br>
# Help: https://scripts.page.link/delayed_events
# </code>
"""
<parameters>
    <company>AATrubilin</company>
    <title>delayed_events</title>
    <version>1.7.9</version>

    <parameter>
        <type>caption</type>
        <name>Required</name>
    </parameter>

    <parameter>
        <type>string_from_list</type>
        <id>EVENTS</id>
        <name>Events</name>
        <value>Motion Start/Stop</value>
        <string_list>Signal Lost/Restored,Motion Start/Stop,Fire Detected/Stopped,Connection Lost/Established,Disconnected From/Connected To,Object Entered/Left the Zone,Output Low to High/High to Low,Input Low to High/High to Low,DP Objects Inside More/Less than</string_list>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>DP_MAX_OBJECTS_INSIDE</id>
        <name>DP Objects Inside More/Less than</name>
        <value>5</value>
        <min>1</min>
        <max>50</max>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>INFORM_ABOUT</id>
        <name>Inform about</name>
        <value>First event</value>
        <string_list>Both events,First event,Second event</string_list>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>EVENT_DURATION</id>
        <name>Event duration, sec</name>
        <value>15</value>
        <min>1</min>
        <max>999999</max>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Optional</name>
    </parameter>

    <parameter>
        <type>objects</type>
        <id>SELECTED_OBJECTS</id>
        <name>Only selected objects</name>
        <value></value>
    </parameter>
    <parameter>
        <type>objects</type>
        <id>SCHEDULE</id>
        <name>Work by schedule (Red)</name>
        <value></value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>ADD_IMAGE</id>
        <name>Add screenshot</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>ONLINE_IMAGE</id>
        <name>Make online screenshot</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>DEBUG</id>
        <name>Debug mode</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Simple notifications</name>
    </parameter>

    <parameter>
        <type>boolean</type>
        <id>SIMPLE_PLAY_SOUND</id>
        <name>Play sound</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>SOUND_FILE</id>
        <name>Sound file</name>
        <value>SNES-startup.wav</value>
        <string_list>screenshots_folder/my_sound.wav,SNES-startup.wav,alarm.wav,bell.wav,boxing-bell-1.wav,boxing-bell-3.wav,cardlock-open.wav,chime.wav,chip001.wav,chip019.wav,chip069.wav,cordless-phone-ring.wav,countdown.wav,dialtone.wav,ding.wav,horn-beep.wav,phone-beep.wav,police2.wav,ship-on-fog.wav,ships-bell.wav,spin-up.wav,tada1.wav,tape-slow9.wav</string_list>
    </parameter>

    <parameter>
        <type>boolean</type>
        <id>SIMPLE_POPUP</id>
        <name>Pop-up</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>POPUP_IMG_WIDTH</id>
        <name>Image width, px</name>
        <value>400</value>
        <min>100</min>
        <max>4320</max>
    </parameter>

    <parameter>
        <type>boolean</type>
        <id>SIMPLE_POPUP_WITH_BUTTON</id>
        <name>Pop-up with button</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>POPUP_WITH_BUTTON_IMG_WIDTH</id>
        <name>Image width, px</name>
        <value>800</value>
        <min>100</min>
        <max>4320</max>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Telegram notification</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>TELEGRAM</id>
        <name>Enable</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Telegram id's</name>
        <id>TELEGRAM_IDS</id>
        <value></value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>PUSH notification</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>PUSH</id>
        <name>Enable</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Token</name>
        <id>PUSH_TOKEN</id>
        <value></value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Email notification</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>EMAIL</id>
        <name>Enable</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>EMAIL_ACCOUNT</id>
        <name>Email account name</name>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>EMAIL_SPAMLIST</id>
        <name>Send to emails</name>
        <value></value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>SMSC.ru notification</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SMSC</id>
        <name>Enable</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>SMSC_LOGIN</id>
        <name>SMSC Login</name>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>SMSC_PASSWORD</id>
        <name>SMSC Password</name>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>SMSC_PHONES</id>
        <name>SMSC Phones</name>
        <value>79999999999,78888888888</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SMSC_TRANSLIT</id>
        <name>Translit messages</name>
        <value>1</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>GPIO settings</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>GPIO</id>
        <name>Enable</name>
        <value>False</value>
    </parameter>
    <parameter>
        <id>GPIO_GUID</id>
        <type>gpio_out</type>
        <name>GPIO Out</name>
    </parameter>
    <parameter>
        <id>GPIO_WORK_MODE</id>
        <name>Work mode</name>
        <type>string_from_list</type>
        <string_list>high,high-low,low,low-high</string_list>
        <value>high-low</value>
    </parameter>
    <parameter>
        <id>GPIO_DELAY</id>
        <name>Delay, sec</name>
        <type>integer</type>
        <value>1</value>
        <min>1</min>
        <max>15</max>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>FTP notification</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SEND_FTP</id>
        <name>Enable</name>
        <value>False</value>
   </parameter>
    <parameter>
        <id>FTP_HOST</id>
        <name>Host</name>
        <type>string</type>
        <value>127.0.0.1</value>
    </parameter>
    <parameter>
        <id>FTP_PORT</id>
        <type>integer</type>
        <name>Port</name>
        <value>21</value>
        <min>1</min>
        <max>999999</max>
    </parameter>
    <parameter>
        <id>FTP_LOGIN</id>
        <name>Username</name>
        <type>string</type>
        <value>trassir</value>
    </parameter>
    <parameter>
        <id>FTP_PASS</id>
        <name>Password</name>
        <type>string</type>
        <value>12345</value>
    </parameter>
    <parameter>
        <id>FTP_WD</id>
        <name>Working directory</name>
        <type>string</type>
        <value>/delayed_events</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>FTP_PASSIVE_MODE</id>
        <name>Passive mode</name>
        <value>True</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>FTP_CHECK_CONNECTION</id>
        <name>Check connection</name>
        <value>False</value>
    </parameter>

    <resources>
        <resource>base_alarm.py</resource>
        <resource>ftp.py</resource>
        <resource>helpers.py</resource>
        <resource>tbot.py</resource>
    </resources>
</parameters>
"""

resources = {
    "base_alarm.py": """
        eNqFVt9r2zAQfg/kf9AMYXYJYX0ty2CDbQzGHvZailDts6vVlowkpw2l//vuJNuR3aT2Q+Lo
        vvvu9ymyabVx7EFbt16tV84cb9Yrhk9pdMMeoG7BWCYDqgLHa11VYNYreM6hdeyXl3w3RptY
        kVBSVZHib6/HhJ2wrFfhje2j4zQjAecHNC214hylyfXu0+46GfC7Au67Kk02lvWoG7axyZZx
        rkQDnNPbqO/51qu8Ftayb8LC11qYJtX3/yB3We+304+gyFJCWDppjdRGuiMe/tEKwqF1wnV2
        clSAzY1sHdqanOe6aUC5yZk7tsBFfgarHGKnxK3ROVhLiZzaO8gceNXJYsphQDgo+JxFGGTm
        M7BBEnjymY8NykaYIzqY627meS0PwBtdwHgazjnXPnRRc7SEyXfUMXuWBjE9aTKkEiuUWme2
        rFMyR64s28awkNwFUJTuBWRfgAVUVJJFvlAkgtXSui1zXVvDlhUS+2iKPdVuMZyxmkvmx/oS
        UCq0X9Za4FetVTW3P1QdsQidCofiLxictcMCemwQxN1rXQ/SbOiUAkrsFqmk4zy1UJfbYfbo
        SZKERpMJmk3mZzWhWRzk/eBLVeo0ud3Yux5JfEBREuPOT/HMooHW9BZjgwZcZxRLPr94Tc69
        Tc53ww55TYMkargP5jX7kuxKbRrhPOPe08YGS2kghMeuhKksfl09PtHbLNyfoMBgRS1T8NRH
        Awdq2DNx9wvPB44WaCd4jfOB0yNLprSLpJF1H7+QmO6/WFjZgN/gtE8DlEnLoGlxYNmGXUjP
        xFjwfs9eEq+f3ER2X2Mgpo6Ne4JaE2deYf/TFOKvwdiZnTJz/yDqDsK9IZwzfcYjalpS2VQH
        UxLUMDzKDUFmtD1M2sGz1GvMPM3OaI1puB2duEP/vPpbNNQWLpD0FQdfkvMQ30E/MJV4AcJz
        i9cYFPReYVB0D17WOiXoMmYS6js4Eof0ZGNXXIBn8dzR9UD/OHY0KtznLPWf2aR7oxp46Q5L
        HS3hDPceLuF5KUIJTjCqwS39Curkc5L5NqRDark3GnfvTl+L+wSXaxH0+v8dp27fsiGUSTAY
        9czRtwuN0tHTMtvldH/Mx/ud9un5cNMo3A49ZS7UR+eJl9ZFvw7Rz/XqP9tj11k=
    """,
    "ftp.py": """
        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
        l0U=
    """,
    "helpers.py": """
        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
    """,
    "tbot.py": """
        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
        vjPSjg==
    """,
}
t1utils.resources_check(script_path, resources)

GLOBALS = globals()

# Required
EVENTS = GLOBALS.get("EVENTS", "Motion Start/Stop")
DP_MAX_OBJECTS_INSIDE = GLOBALS.get("DP_MAX_OBJECTS_INSIDE", 5)
INFORM_ABOUT = GLOBALS.get("INFORM_ABOUT", "First event")
EVENT_DURATION = GLOBALS.get("EVENT_DURATION", 15)

# Optional
SELECTED_OBJECTS = GLOBALS.get("SELECTED_OBJECTS", "")
SCHEDULE = GLOBALS.get("SCHEDULE", "")
ADD_IMAGE = GLOBALS.get("ADD_IMAGE", False)
ONLINE_IMAGE = GLOBALS.get("ONLINE_IMAGE", False)
DEBUG = GLOBALS.get("DEBUG", False)

# Simple notifications
SIMPLE_PLAY_SOUND = GLOBALS.get("SIMPLE_PLAY_SOUND", False)
SOUND_FILE = GLOBALS.get("SOUND_FILE", "SNES-startup.wav")
SIMPLE_POPUP = GLOBALS.get("SIMPLE_POPUP", False)
POPUP_IMG_WIDTH = GLOBALS.get("POPUP_IMG_WIDTH", 400)
SIMPLE_POPUP_WITH_BUTTON = GLOBALS.get("SIMPLE_POPUP_WITH_BUTTON", False)
POPUP_WITH_BUTTON_IMG_WIDTH = GLOBALS.get("POPUP_WITH_BUTTON_IMG_WIDTH", 800)

# Telegram notification
TELEGRAM = GLOBALS.get("TELEGRAM", False)
TELEGRAM_IDS = GLOBALS.get("TELEGRAM_IDS", "")

# PUSH notification
PUSH = GLOBALS.get("PUSH", False)
PUSH_TOKEN = GLOBALS.get("PUSH_TOKEN", "")

# Email notification
EMAIL = GLOBALS.get("EMAIL", False)
EMAIL_ACCOUNT = GLOBALS.get("EMAIL_ACCOUNT", "")
EMAIL_SPAMLIST = GLOBALS.get("EMAIL_SPAMLIST", "")

# SMSC.ru notification
SMSC = GLOBALS.get("SMSC", False)
SMSC_LOGIN = GLOBALS.get("SMSC_LOGIN", "")
SMSC_PASSWORD = GLOBALS.get("SMSC_PASSWORD", "")
SMSC_PHONES = GLOBALS.get("SMSC_PHONES", "79999999999,78888888888")
SMSC_TRANSLIT = GLOBALS.get("SMSC_TRANSLIT", True)

# GPIO settings
GPIO = GLOBALS.get("GPIO", False)
GPIO_GUID = GLOBALS.get("GPIO_GUID", "")
GPIO_WORK_MODE = GLOBALS.get("GPIO_WORK_MODE", "high-low")
GPIO_DELAY = GLOBALS.get("GPIO_DELAY", 1)

# FTP notification
SEND_FTP = GLOBALS.get("SEND_FTP", False)
FTP_HOST = GLOBALS.get("FTP_HOST", "127.0.0.1")
FTP_PORT = GLOBALS.get("FTP_PORT", 21)
FTP_LOGIN = GLOBALS.get("FTP_LOGIN", "trassir")
FTP_PASS = GLOBALS.get("FTP_PASS", "12345")
FTP_WD = GLOBALS.get("FTP_WD", "/delayed_events")
FTP_PASSIVE_MODE = GLOBALS.get("FTP_PASSIVE_MODE", True)
FTP_CHECK_CONNECTION = GLOBALS.get("FTP_CHECK_CONNECTION", False)

import ssl
import time
import urllib2
import httplib
import mimetools
import mimetypes
import itertools


import re
import os
import json
import time
import base64
import urllib
import threading
from functools import wraps
from collections import deque, namedtuple
from datetime import datetime, timedelta
from ftp import FTPClient, status as ftp_status
from __builtin__ import object as py_object

import host

if os.name == "nt":
    import winsound

import helpers

default_script_name = helpers.set_script_name()
logger = helpers.init_logger("delayed_events", debug=DEBUG)

from tbot import tbot_service

host.exec_encoded(tbot_service)

from base_alarm import BaseAlarm

VERSION = {"TITLE": "delayed_events", "VERSION": 1.7}
UTC_OFFSET = timedelta(
    minutes=host.settings("system_wide_options")["utc_offset_minutes"]
)
WORKING_TASKS = {}

host.exec_encoded(tbot_service)


def run_as_thread(fn):
    """Run function as thread"""

    @wraps(fn)
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
        return t

    return run


def _win_encode_path(path):
    if os.name == "nt":
        try:
            path = path.decode("utf8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return path


def ts_to_dt(ts):
    if ts > 1e10:
        ts_sec = int(ts / 1e6)
        ts_ms = int(ts - ts_sec * 1e6)
    else:
        ts_sec = int(ts)
        ts_ms = 0
    return datetime.fromtimestamp(ts_sec) + timedelta(
        microseconds=ts_ms
    ) - UTC_OFFSET


def remove_screenshot(file_path):
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            logger.debug("remove file %s" % file_path)
        except:
            logger.debug(
                "Unhandled exception while removing file %s" % file_path)
    else:
        logger.debug("%s is not exists" % file_path)


def ftp_callback(task_guid, state):
    logger.debug("%s: ftp %s" % (task_guid, state))
    if state in (ftp_status.success, ftp_status.error):
        task = WORKING_TASKS.pop(task_guid, None)
        host.stats()["run_count"] -= 1
        if task and state == ftp_status.success:
            logger.debug("Send file successfully %s" % task_guid)
            remove_screenshot(_win_encode_path(task))

        elif state == ftp_status.error:
            WORKING_TASKS.pop(task_guid, None)
            logger.debug("Can't send file %s" % task_guid)
            remove_screenshot(_win_encode_path(task))


class ScriptError(Exception):
    """Base exception for EventListener class"""

    pass


class NotificatorError(ScriptError):
    """Raises with Notificator class"""

    pass


class ScheduleError(NotificatorError):
    """Raises if cant load schedule object"""

    pass


class Notificator(py_object):
    """Send notification for all events in queue

    Args:
        schedule (str, optional) : Schedule name, default: ""
        add_image (bool, optional) : Make/send screenshot, default: False
        online_image (bool, optional) : Make online shot (ts="0"), default: False
        figures_delay (int, optional) : Delay before make shot, default: 3 sec
        queue_len (int, optional) : max queue length, default: 100
        host_api (Trassir module, optional) : Trassir host module, default: host
    """

    _AWAITING_IMAGE = 10  # How long to await screenshot creation, sec
    _SCREENSHOT_OFFSET = (
        1  # Offset for screenshot from event time (only for shot from archive), sec
    )

    def __init__(
        self,
        schedule="",
        add_image=False,
        online_image=False,
        figures_delay=3,
        queue_len=100,
        host_api=host,
    ):
        self._host_api = host_api
        self._base_path = self._host_api.settings("system_wide_options")[
            "screenshots_folder"
        ]

        self.queue = deque(maxlen=queue_len)
        self.senders = {}
        self.add_image = add_image
        self.online_image = online_image
        self.figures_delay = figures_delay
        self._schedule = self._load_schedule(schedule)
        self._sender()

        logger.info(
            "Notificator(schedule='{schedule}', add_image={add_image}, online_image={online_image}, "
            "figures_delay={figures_delay}, queue_len={queue_len}".format(
                schedule=schedule,
                add_image=add_image,
                online_image=online_image,
                figures_delay=figures_delay,
                queue_len=queue_len,
            )
        )

    def add_event(self, data):
        """Add event data to queue

        Args:
            data (dict) : Event data
        """
        if self._schedule is None or self._schedule.state("color") == "Red":
            self.queue.append(data)

    def _load_schedule(self, name):
        """Returns schedule object

        Returns None if name is empty

        Args:
            name (str) : Schedule name

        Raises ScheduleError if cant load object
        """
        if name:
            obj = self._host_api.object(name)
            try:
                obj.name
                obj.state("color")
            except EnvironmentError:
                raise ScheduleError("Object '{}' not found".format(name))
            except KeyError:
                raise ScheduleError("Object '{}' is not schedule".format(name))
            return obj

    def _get_shots_path(self):
        """Returns ...{shots_path}/delayed_events

        Make dir if is not exists
        """
        full_path = os.path.join(self._base_path, "delayed_events")

        if not os.path.isdir(full_path):
            os.mkdir(full_path)

        return full_path

    def _get_channel_full_guid(self, origin_guid):
        """Returns full channel guid

        Args:
            origin_guid (str) : Event origin guid
        """
        all_objects = {
            obj[1]: {"name": obj[0], "type": obj[2], "parent": obj[3]}
            for obj in self._host_api.objects_list("")
        }

        def get_parent(child_guid):
            child = all_objects.get(child_guid, None)
            if child and child["type"] != "Server":
                if child["type"] == "Channel":
                    return "%s_%s" % (child_guid, child["parent"][:-1])
                else:
                    return get_parent(child["parent"])

        return get_parent(origin_guid)

    def _get_object_name(self, obj_guid):
        """Returns Trassir object name

        Returns obj_guid if object not found

        Args:
            obj_guid (str) : Trassir obj guid
        """
        try:
            obj_name = self._host_api.object(obj_guid).name
        except EnvironmentError:
            """Object {obj_guid} not found"""
            obj_name = obj_guid
        return obj_name

    def _check_file(self, full_path):
        """Check if file exists, run only in thread!

        Args:
            full_path (str) : Full path to file
        """
        if os.name == "nt":
            full_path = full_path.decode("utf8").encode("cp1251")

        for x in xrange(self._AWAITING_IMAGE):
            if os.path.isfile(full_path):
                return True
            time.sleep(1)
        return False

    def make_shot(self, ev, dt=None, online=False):
        """Making screenshot for channel

        Returns full shot path or None

        Args:
            ev (ScriptHost.SE_Event): Trassir event object
            dt (datetime, optional): Datetime for screenshot
            online (bool, optional): If True - make online shot
        """

        channel_guid = getattr(ev, "channel_guid", None)
        if channel_guid:
            if dt is None:
                dt = datetime.fromtimestamp(ev.ts / 1e6)

            if online:
                ts = "0"
            else:
                if self.figures_delay > 0:
                    time.sleep(self.figures_delay)
                ts = (dt + timedelta(seconds=self._SCREENSHOT_OFFSET)).strftime(
                    "%Y%m%d_%H%M%S"
                )

            ev_type = ev.type
            ev_type = ev_type.replace("%1", ev.p1)
            ev_type = ev_type.replace("%2", ev.p2)

            dt_format = "{ev.origin_object.name} - {ev_type} (%Y.%m.%d %H-%M-%S).jpg".format(
                ev=ev, ev_type=ev_type
            )

            file_name = dt.strftime(dt_format)
            file_path = self._get_shots_path()

            self._host_api.screenshot_v2_figures(channel_guid, file_name, file_path, ts)

            full_path = os.path.join(file_path, file_name)

            if os.name == "nt":
                try:
                    full_path = full_path.decode("utf8")
                except (UnicodeDecodeError, UnicodeEncodeError):
                    pass

            if self._check_file(full_path):
                return full_path
            else:
                if online:
                    return self.make_shot(ev, online=False)

        else:
            logger.warning("No channel guid for {}".format(ev.origin_object.name))

    @run_as_thread
    def notify(self, data):
        """Send all notification

        Args:
            data (dict) : Event data - {"ev": ScriptHost.SE_Event, "dt": datetime}
        """
        try:
            text = "{ev.type} ({obj})".format(
                ev=data["ev"], obj=data["ev"].origin_object.name
            )
            text = text.replace("%1", data["ev"].p1)
            text = text.replace("%2", data["ev"].p2)
            image = False

            channel_guid = getattr(data["ev"], "channel_guid", None)
            if channel_guid is None:
                data["ev"].channel_guid = self._get_channel_full_guid(data["ev"].origin)
            if self.add_image:
                image = self.make_shot(
                    data["ev"], dt=data["dt"], online=self.online_image
                )

            for key, sender in self.senders.iteritems():
                args = [text]
                kwargs = {}
                if key == "ftp":
                    method = sender.send
                else:
                    method = sender.text

                if image is None:
                    args[0] += " (Can't make screenshot)"
                elif image:
                    if key == "ftp":
                        task_guid = host.random_guid()
                        WORKING_TASKS[task_guid] = image
                        host.stats()["run_count"] += 1
                        method(image, task_guid=task_guid)
                        continue
                    else:
                        method = sender.text_with_image
                        kwargs["image_path"] = image

                if key == "popup_with_button" and getattr(data["ev"], "channel_guid", None):
                    kwargs["ev"] = data["ev"]

                logger.debug("Call %s", key)
                method(*args, **kwargs)

            if image and not SEND_FTP:
                time.sleep(1)
                remove_screenshot(_win_encode_path(image))

            self._host_api.stats()["run_count"] += 1
        except:
            logger.critical("Critical error while making notify", exc_info=True)

    def _sender(self):
        """Send notification from queue loop"""
        if self.queue:
            self.notify(self.queue.popleft())

        self._host_api.timeout(1000, self._sender)


class EventTypeError(ScriptError):
    """Raises with event type errors"""

    pass


class EventListener(py_object):
    """Listen Trassir events, alarm to long duration events

    Args:
        event_type (str): Selected event type
        callback (function): Callback function for alarm
        event_mode (str, optional): Event mode
            default: Both events
        event_duration (int, optional): Event duration for event
            default: event_duration=15
        selected_objects (str, optional): Working objects, empty == all objects
            default: selected_objects=""
        dp_max_objects_inside (str, optional): Maximum objects inside zone. Default 5
        host_api (Trassir module, optional): Trassir host module, default - host
            default: host_api=host
    """

    _EVENT_TYPES = {
        "Signal Lost/Restored": ("Signal Lost", "Signal Restored"),
        "Motion Start/Stop": ("Motion Start", "Motion Stop"),
        "Fire Detected/Stopped": ("Fire Detected", "Fire Stopped"),
        "Connection Lost/Established": ("Connection Lost", "Connection Established"),
        "Disconnected From/Connected To": (
            "Disconnected From %1",
            "Connected To %1 under %2",
        ),
        "Object Entered/Left the Zone": (
            "Object Entered the Zone",
            "Object Left the Zone",
        ),
        "Output Low to High/High to Low": ("Output Low to High", "Output High to Low"),
        "Input Low to High/High to Low": ("Input Low to High", "Input High to Low"),
        "DP Objects Inside More/Less than": (
            "DP %1 Objects Inside More than %2",
            "DP %1 Objects Inside Less than %2",
        ),
    }

    _EVENT_MODES = {"Both events": (0, 1), "First event": (0,), "Second event": (1,)}

    def __init__(
        self,
        event_type,
        callback,
        event_mode="Both events",
        event_duration=15,
        selected_objects="",
        dp_max_objects_inside=5,
        host_api=host,
    ):
        self._event_types = self._EVENT_TYPES.get(event_type)
        if self._event_types is None:
            raise EventTypeError("Unknown event type '%s'" % event_type)

        self._active_events = self._get_active_events(event_mode)

        self._callback = callback
        self.event_duration = event_duration
        self._selected_objects = self._parse_objects(selected_objects)
        self._host_api = host_api

        self.current_events = {}

        self.dp_max_objects_inside = dp_max_objects_inside
        self.dp_zones = {}
        self.dp_origin_obj = namedtuple("DP_Origin", ["guid", "name"])
        self.dp_event = namedtuple(
            "DP_Event",
            ["origin", "origin_object", "p1", "p2", "ts", "type", "channel_guid"],
        )

        self._start(event_type)

        logger.info(
            "EventListener('{event_type}', callback, event_mode='{event_mode}', "
            "event_duration={event_duration}, selected_objects='{selected_objects}', "
            "dp_max_objects_inside={dp_max_objects_inside}) initialized".format(
                event_type=event_type,
                callback=callback,
                event_mode=event_mode,
                event_duration=event_duration,
                selected_objects=selected_objects,
                dp_max_objects_inside=dp_max_objects_inside,
            )
        )

    @staticmethod
    def _parse_objects(str_objects):
        """Parse objects name from string

        Args:
            objects (str) : Comma spaced object names
        """
        if str_objects:
            return str_objects.split(",")

    def _get_active_events(self, event_mode):
        """Returns list of active event types

        Args:
            event_mode (str) : Event mode
        """
        active_events = []
        for idx in self._EVENT_MODES.get(event_mode, (0, 1)):
            active_events.append(self._event_types[idx])
        return active_events

    def check_current_events(self):
        dt_now = datetime.now()
        for guid in self.current_events.keys():
            data = self.current_events[guid]
            if (dt_now - data["dt"]).seconds > self.event_duration:
                data = self.current_events.pop(guid)
                if data["ev"].type in self._active_events:
                    self._callback(data)

        self._host_api.timeout(1000, self.check_current_events)

    def _start(self, event_type):
        if self._callback is None:
            raise ScriptError("Set callback function first!")

        def event_handler(ev):
            origin = ev.origin_object
            if self._selected_objects is None or origin.name in self._selected_objects:
                logger.debug("Got new event %s (%s)", ev.type, origin.guid)
                pop_obj = self.current_events.pop(origin.guid, None)
                if pop_obj is None:
                    self.current_events[origin.guid] = {"ev": ev, "dt": datetime.now()}

        if event_type == "DP Objects Inside More/Less than":

            def dp_event_handler(ev):
                deep_people_sett = self._host_api.settings(
                    "/{0.server_guid}/channels/{0.channel_guid}/deep_people".format(ev)
                )

                for zone in ev.zones:
                    if zone.zone_type != 0:
                        continue

                    zone_guid = deep_people_sett["{0.tree_zone_name}_guid".format(zone)]

                    prev_objects_too_much = self.dp_zones.get(zone_guid)

                    cur_objects_len = len(zone.objects_inside)
                    cur_objects_too_much = cur_objects_len >= self.dp_max_objects_inside

                    if prev_objects_too_much != cur_objects_too_much:
                        self.dp_zones[zone_guid] = cur_objects_too_much
                        zone_name = getattr(zone, "zone_name", None) or zone.name
                        logger.debug(
                            "{} -> {} {}".format(
                                zone_name, cur_objects_len, cur_objects_too_much
                            )
                        )

                        if cur_objects_too_much:
                            ev_type = "DP %1 Objects Inside More than %2"
                        else:
                            ev_type = "DP %1 Objects Inside Less than %2"

                        logger.debug("Got new event %s (%s)", ev_type, zone_guid)

                        origin = self.dp_origin_obj(zone_guid, zone_name)
                        event = self.dp_event(
                            zone_guid,
                            origin,
                            str(cur_objects_len),
                            str(self.dp_max_objects_inside),
                            ev.event_ts,
                            ev_type,
                            "{ev.channel_guid}_{ev.server_guid}".format(ev=ev),
                        )

                        event_handler(event)

            self._host_api.activate_on_deep_detection_events(dp_event_handler)
        else:
            self._host_api.activate_on_events(self._event_types[0], "", event_handler)
            self._host_api.activate_on_events(self._event_types[1], "", event_handler)

        self.check_current_events()


class SenderError(Exception):
    """Base Sender Exception"""

    pass


class EmailSenderError(SenderError):
    """Exceptions for EmailSender"""

    pass


class Sender(py_object):
    _HTML_IMG_TEMPLATE = """<img src="data:image/png;base64,{img}" {attr}>"""

    def __init__(self, host_api=host):
        self._host_api = host_api

    @staticmethod
    def _encode_filename(image_path):
        if os.name == "nt":
            image_path = image_path.decode("utf8").encode("cp1251")

        return image_path

    def _get_base64(self, image_path):
        """Returns base64 image

        Args:
            image_path (str) : Image full path
        """
        image_path = self._encode_filename(image_path)
        if os.path.isfile(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read())

    def _get_html_img(self, image_base64, **kwargs):
        """Returns html with img

        Args:
            image_base64 (str) : Base64 image
        """
        html_img = self._HTML_IMG_TEMPLATE.format(
            img=image_base64,
            attr="".join('%s="%s"' % (key, value) for key, value in kwargs.iteritems()),
        )
        return html_img

    def text(self, message):
        """Send only text

        Args:
            message (str) : Text message
        """
        pass

    def image(self, image_path=None, image_base64=None):
        """Send only image

        Args:
            image_path (str) : Image path
            image_base64 (str) : Base64 image
        """
        pass

    def text_with_image(self, message, image_path=None, image_base64=None):
        """Send text with image

        Args:
            message (str) : Text message
            image_path (str, optional) : Image path
            image_base64 (str, , optional) : Base64 image
        """
        pass


class PopupSender(Sender):
    """Show trassir popup

    Args:
        width (int) : Image width, default: 400
    """

    def __init__(self, width=400):
        super(PopupSender, self).__init__()
        self._attr = {"width": width}
        logger.info("PopupSender({}) initialized".format(width))

    def text(self, message, popup_type=1):
        """Call trassir alert/message/error with text

        Args:
            message (str) : Text message
            popup_type (int, optional) Popup type
                1 - message, default
                2 - alert
                3 - error
        """
        if popup_type == 1:
            self._host_api.message(message)
        elif popup_type == 2:
            self._host_api.alert(message)
        else:
            self._host_api.error(message)

    def image(self, image_path=None, image_base64=None, popup_type=1):
        """Call trassir alert/message/error with image

        Args:
            image_path (str) : Image path
            image_base64 (str) : Base64 image
            popup_type (int, optional) Popup type
                1 - message, default
                2 - alert
                3 - error
        """
        if image_path:
            image_base64 = self._get_base64(image_path)

        if image_base64:
            html_image = self._get_html_img(image_base64, **self._attr)
            self.text(html_image, popup_type)

    def text_with_image(
        self, message, image_path=None, image_base64=None, popup_type=1
    ):
        """Call trassir alert/message/error with text and image

        Args:
            message (str) : Text message
            image_path (str, optional) : Image path
            image_base64 (str, , optional) : Base64 image
            popup_type (int, optional) Popup type
                1 - message, default
                2 - alert
                3 - error
        """
        if image_path:
            image_base64 = self._get_base64(image_path)

        if not message:
            self.image(
                image_path=image_path, image_base64=image_base64, popup_type=popup_type
            )
        else:
            html = "<b>{}</b><br> {}".format(
                message, self._get_html_img(image_base64, **self._attr)
            )
            self.text(html, popup_type)


class PopupWithBtnSender(Sender):
    """Show trassir popup with button

    Args:
        width (int) : Image width, default: 800
    """
    try:
        gui = host.object('operatorgui_%s' % host.settings('').guid)
        gui.name
    except EnvironmentError:
        gui = None
    archive_delta = timedelta(seconds=5)

    def __init__(self, width=800):
        super(PopupWithBtnSender, self).__init__()
        self._attr = {"width": width}
        logger.info("PopupWithBtnSender({}) initialized".format(width))

    @staticmethod
    def _ok():
        pass

    def text(self, message, ev=None):
        """Call Trassir question method with text

        Args:
            message (str) : Message to show
        """
        args = ["<pre>{}</pre>".format(message), "Ok", self._ok]
        if ev and self.gui:
            dt = ts_to_dt(ev.ts)
            dt_start, dt_end = dt - self.archive_delta, dt + self.archive_delta
            args.extend([
                "Open archive",
                lambda: self.gui.show_archive(ev.channel_guid, 1, dt_start.strftime("%Y-%m-%d %H:%M:%S"), dt_end.strftime("%Y-%m-%d %H:%M:%S"))
            ])
        self._host_api.question(*args)

    def image(self, image_path=None, image_base64=None):
        """Call Trassir question method with image

        Args:
            image_path (str, optional) : Image path
            image_base64 (str, , optional) : Base64 image
        """
        if image_path:
            image_base64 = self._get_base64(image_path)
        html_image = self._get_html_img(image_base64, **self._attr)
        self.text(html_image)

    def text_with_image(self, message, image_path=None, image_base64=None, ev=None):
        """Call Trassir question method with text and image

        Args:
            message (str) : Text message
            image_path (str, optional) : Image path
            image_base64 (str, , optional) : Base64 image
        """
        if image_path:
            image_base64 = self._get_base64(image_path)

        if not message:
            self.image(image_path=image_path, image_base64=image_base64)
        else:
            html = "<b>{}</b><br><br> {}".format(
                message, self._get_html_img(image_base64, **self._attr)
            )
            self.text(html, ev=ev)


class EmailSender(Sender):
    """Send email message

    Args:
        account (str) : Trassir E-Mail Account
        spam_list (str) : Comma spaced emails to send event
        subject (str) : E-Mail default subject
    """

    _EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def __init__(self, account="", spam_list="", subject=None):
        super(EmailSender, self).__init__()
        self._account = self._check_account(account)
        self._spam_list = self._parse_emails(spam_list)

        self._subject_default = subject or self._generate_subject()

        logger.info(
            "EmailSender('{0._account}', {0._spam_list}, '{0._subject_default}') initialized".format(
                self
            )
        )

    def _generate_subject(self):
        """Returns `server name` -> `script name`"""
        subject = "{} -> {}".format(
            self._host_api.settings("").name, self._host_api.stats().parent()["name"]
        )
        return subject

    @staticmethod
    def _check_account(account):
        """Check Trassir E-Mail account

        Args:
            account (str) : Trassir E-Mail Account

        Raise EmailSenderError if can't find account or account is empty
        """
        if account:
            for obj in host.settings("scripts").ls():
                if obj.type == "EmailAccount":
                    if obj.name == account:
                        break
            else:
                raise EmailSenderError("Can't find account '%s'" % account)

        else:
            raise EmailSenderError("Empty account name")

        return account

    def _parse_emails(self, spam_list):
        """Parse comma spaced emails to list

        And check if email valid

        Args:
            spam_list (str) : Comma spaced emails to send event
        """
        if spam_list:
            for mail in spam_list.split(","):
                if not self._EMAIL_REGEX.match(mail):
                    raise EmailSenderError("E-mail '{}' is not valid".format(mail))
        else:
            raise EmailSenderError("No emails to send")

        return spam_list.split(",")

    def text(self, message, subject=None, attachments=None):
        """Send email text

        Args:
            message (str) : Text message
            subject (str, optional) : E-Mail default subject
                default: subject=None, if None - subject={script_name}
            attachments (list, optional) : Files to send
                default: attachments=None
        """
        if attachments is None:
            attachments = []
        self._host_api.send_mail_from_account(
            self._account,
            self._spam_list,
            subject or self._subject_default,
            message,
            attachments,
        )

    def image(self, image_path=None, image_base64=None):
        """Send email image

        Args:
            image_path (str, optional) : Image path
            image_base64 (str, , optional) : Base64 image
        """
        if not image_path:
            if image_base64:
                with open("temp.jpeg", "wb") as fh:
                    fh.write(base64.b64decode(image_base64))
                image_path = "temp.jpeg"
        self.text("", attachments=[image_path])

    def text_with_image(self, message, image_path=None, image_base64=None):
        """Send email text with image

        Args:
            message (str) : Text message
            image_path (str, optional) : Image path
            image_base64 (str, , optional) : Base64 image
        """
        if not image_path:
            if image_base64:
                with open("temp.jpeg", "wb") as fh:
                    fh.write(base64.b64decode(image_base64))
                image_path = "temp.jpeg"
        self.text(message, attachments=[image_path])


class TelegramSender(Sender):
    """Send telegram message

    Args:
        telegram_ids (str) : Comma spaced telegram id's
    """

    def __init__(self, telegram_ids):
        super(TelegramSender, self).__init__()
        self._tbot_api = TBotAPI()
        if not telegram_ids:
            raise ValueError("No telegram id's to send")

        self._tg_users = []
        for tg_id in telegram_ids.split(","):
            try:
                self._tg_users.append(int(tg_id))
            except ValueError:
                raise ValueError("Bad telegram id: %s" % tg_id)

        logger.info("TelegramSender('{}') initialized".format(telegram_ids))

    def text(self, message):
        """Send email text

        Args:
            message (str) : Text message
        """

        self._tbot_api.send_message(self._tg_users, message)

    def image(self, image_path=None, image_base64=None, caption=""):
        """Send email image

        Args:
            image_path (str, optional) : Image path
            image_base64 (str, , optional) : Base64 image
            caption (str, optional) : Cation to sending image
        """
        if not image_path:
            with open("temp.jpeg", "wb") as fh:
                fh.write(base64.b64decode(image_base64))
            image_path = "temp.jpeg"

        self._tbot_api.send_image(self._tg_users, image_path, caption=caption)

    def text_with_image(self, message, image_path=None, image_base64=None):
        """Send email text with image

        Args:
            message (str) : Text message
            image_path (str, optional) : Image path
            image_base64 (str, , optional) : Base64 image
        """
        if not image_path:
            if image_base64:
                with open("temp.jpeg", "wb") as fh:
                    fh.write(base64.b64decode(image_base64))
                image_path = "temp.jpeg"

        self._tbot_api.send_image(self._tg_users, image_path, caption=message)


class SMSCSenderError(SenderError):
    """Raises with SMSCSender errors"""

    pass


class SMSCSender(Sender):
    """Class to send message with smsc.ru service

    See Also:
        `https://smsc.ru/api/http/ <https://smsc.ru/api/http/>`_

    Args:
        login (:obj:`str`): SMSC Login
        password (:obj:`str`): SMSC Password
        phones (:obj:`str`): Comma spaced phone list
        translit(:obj:`1` | :obj:`0`, optional): Translate message, Default :obj:`1`

    Raises:
        SMSCSenderError: With any errors with sending sms
    """

    _PHONE_REGEXP = re.compile(r"[^\d,;]")
    _BASE_URL = "https://smsc.ru/sys/send.php?{params}"
    _ERROR_CODES = {
        1: "URL Params error",
        2: "Invalid login or password",
        3: "Not enough money",
        4: "Your IP is temporary blocked. More info: https://smsc.ru/faq/99",
        5: "Bad date format",
        6: "Message is denied (by text or sender name)",
        7: "Bad phone format",
        8: "Can't send message to this number",
        9: "Too many requests",
    }

    def __init__(self, login, password, phones, translit=True):
        super(SMSCSender, self).__init__()
        if not login:
            raise SMSCSenderError("Empty login")
        if not password:
            raise SMSCSenderError("Empty password")

        self._params = {
            "login": urllib.quote(login),  # Login
            "psw": urllib.quote(password),  # Password or MD5 hash
            "phones": urllib.quote(
                self._check_phones(phones)
            ),  # Comma or semicolon spaced phone list
            "fmt": 3,  # Response format: 0 - string; 1 - integers; 2 - xml; 3 - json
            "translit": 1 if translit else 0,  # If 1 - transliting message
            "charset": "utf-8",  # Message charset: "windows-1251"|"utf-8"|"koi8-r"
            "cost": 3,  # Message cost in response: 0 - msg; 1 - cost; 2 - msg+cost, 3 - msg+cost+balance
        }

        self._check_account()

    def _check_phones(self, phones):
        """Check phones"""
        if not phones:
            raise ValueError("No phones!")

        bad_chars = self._PHONE_REGEXP.findall(phones)
        if bad_chars:
            raise ValueError(
                "Bad chars in phone list: `{}`".format(", ".join(bad_chars))
            )
        return phones

    def _get_link(self, **kwargs):
        """Returns get link"""
        params = self._params.copy()
        params.update(kwargs)
        url = self._BASE_URL.format(params=urllib.urlencode(params))

        return url

    def _request_callback(self, code, result, error):
        """Callback for async_get"""
        if code != 200:
            raise SMSCSenderError("RequestError [{}]: {}".format(code, error))
        else:
            try:
                data = json.loads(result)
            except ValueError:
                data = {"error_code": 0, "error": "JSON loads error: {}".format(result)}

            error_code = data.get("error_code")
            if error_code is not None:
                error = self._ERROR_CODES.get(error_code)
                if not error:
                    error = data.get("error", "Unknown error")
                raise SMSCSenderError(
                    "ResponseError [{}]: {}".format(error_code, error)
                )

    def _check_account(self):
        """Send test request to smsc server"""
        url = self._get_link(cost=1, mes=urllib.quote("Hello world!"))
        self._host_api.async_get(url, self._request_callback)

    def text(self, text):
        """Отправка текстового сообщения

        Args:
            text (:obj:`str`): Текст сообщения.
        """

        url = self._get_link(mes=urllib.quote(text))

        self._host_api.async_get(url, self._request_callback)


class PlaySound(py_object):
    """"""

    def __init__(self, sound_file, host_api=host):
        self._host_api = host_api
        self.sound_file = self._check_file(sound_file)

    def _check_file(self, sound_file):
        if "my_sound.wav" in sound_file:
            base_path = self._host_api.settings("system_wide_options")[
                "screenshots_folder"
            ]
            sound_file = "my_sound.wav"
        else:
            if os.name == "nt":
                base_path = "sounds"
            else:
                base_path = "/opt/trassir/tech1/sounds"

        sound_file = os.path.join(base_path, sound_file)

        if not os.path.isfile(sound_file):
            raise ValueError("File {} not found".format(sound_file))
        return sound_file

    def play_sound(self):
        if os.path.isfile(self.sound_file):
            if os.name == "nt":
                winsound.PlaySound(
                    self.sound_file,
                    winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NOWAIT,
                )
            else:
                os.system('aplay -D "sysdefault:CARD=PCH" %s &' % self.sound_file)

    def text(self, *args, **kwargs):
        self.play_sound()

    def text_with_image(self, *args, **kwargs):
        self.play_sound()


class GPIOWorker(py_object):
    """"""

    def __init__(self, guid, work_mode, delay, host_api=host):
        modes = {
            host_api.tr("high"): self.set_high,
            host_api.tr("low"): self.set_low,
            host_api.tr("high-low"): self.set_high_low,
            host_api.tr("low-high"): self.set_high_low,
        }

        self._host_api = host_api
        self.gpio = None
        self.delay = delay * 1000
        self.__load_object(guid)
        self.__work = modes[work_mode]

    def __load_object(self, guid, tries=5):
        obj = host.object(guid.split("_")[0])
        try:
            obj.state("gpio_output_level")
        except EnvironmentError:
            if tries:
                host.timeout(100, lambda: self.__load_object(guid, tries=tries - 1))
            else:
                raise EnvironmentError("Object %s not found" % guid)
        except KeyError:
            raise EnvironmentError("Object %s is not gpio out" % obj.name)
        else:
            logger.info("Loaded gpio success %s", obj.name)
            self.gpio = obj

    def set_high(self):
        self.gpio.set_output_high()

    def set_low(self):
        self.gpio.set_output_low()

    def set_high_low(self):
        self.set_high()
        self._host_api.timeout(self.delay, self.set_low)

    def set_low_high(self):
        self.set_low()
        self._host_api.timeout(self.delay, self.set_high)

    def work(self):
        if self.gpio:
            self.__work()
        else:
            logger.warning("GPIO Object not loaded to work...")

    def text(self, *args, **kwargs):
        self.work()

    def text_with_image(self, *args, **kwargs):
        self.work()


def bytes_to_base64(shot_bytes):
    return base64.b64encode(shot_bytes)


class PushAlarm(BaseAlarm, Sender):
    token = PUSH_TOKEN
    priority = "high"

    def text(self, message):
        self.contents = [
            {
                "type": "html",
                "html": (
                    "<!doctype html><head><meta charset='utf-8'></head><body>"
                    ""
                    "<p>{message}</p>"
                    ""
                    "</body></html>"
                ).format(message=message),
            },
        ]
        self.description = message
        super(PushAlarm, self).fire()

    def text_with_image(self, message, image_path=None, image_base64=None):
        self.contents = [
            {
                "type": "html",
                "html": (
                    "<!doctype html><head><meta charset='utf-8'></head><body>"
                    ""
                    "<p>{message}</p>"
                    ""
                    "</body></html>"
                ).format(message=message),
            },
            {
                "type": "image",
                "format": "jpg",
                "image_base64": self._get_base64(image_path),
            },

        ]
        self.description = message
        super(PushAlarm, self).fire()


ntf = Notificator(
    schedule=SCHEDULE,
    add_image=ADD_IMAGE,
    online_image=ONLINE_IMAGE,
    figures_delay=(host.settings("archive")["prebuffer"] + 1 - EVENT_DURATION),
)


if SIMPLE_PLAY_SOUND:
    ntf.senders["sound"] = PlaySound(SOUND_FILE)
    ntf.senders["sound"].play_sound()

if SIMPLE_POPUP:
    ntf.senders["popup"] = PopupSender(POPUP_IMG_WIDTH)

if SIMPLE_POPUP_WITH_BUTTON:
    ntf.senders["popup_with_button"] = PopupWithBtnSender(POPUP_WITH_BUTTON_IMG_WIDTH)

if TELEGRAM:
    ntf.senders["telegram"] = TelegramSender(TELEGRAM_IDS)

if EMAIL:
    ntf.senders["email"] = EmailSender(EMAIL_ACCOUNT, EMAIL_SPAMLIST)

if SMSC:
    ntf.senders["smsc"] = SMSCSender(
        SMSC_LOGIN, SMSC_PASSWORD, SMSC_PHONES, SMSC_TRANSLIT
    )

if GPIO:
    assert GPIO_GUID, "GPIO not selected"
    ntf.senders["gpio"] = GPIOWorker(GPIO_GUID, GPIO_WORK_MODE, GPIO_DELAY)

if PUSH:
    ntf.senders["push"] = PushAlarm()

if SEND_FTP:
    assert ADD_IMAGE, "Need to enable checkbox 'Add screenshot'"
    ntf.senders["ftp"] = FTPClient(
        host=FTP_HOST,
        port=FTP_PORT,
        user=FTP_LOGIN,
        passwd=FTP_PASS,
        work_dir=FTP_WD,
        callback=ftp_callback,
        check_connection=FTP_CHECK_CONNECTION,
        passive_mode=FTP_PASSIVE_MODE,
    )

ev_listener = EventListener(
    event_type=EVENTS,
    callback=ntf.add_event,
    event_mode=INFORM_ABOUT,
    event_duration=EVENT_DURATION,
    selected_objects=SELECTED_OBJECTS,
    dp_max_objects_inside=DP_MAX_OBJECTS_INSIDE,
)
