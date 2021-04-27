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
