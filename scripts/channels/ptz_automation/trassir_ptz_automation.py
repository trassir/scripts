# -*- coding: utf-8 -*-
# PTZAutomation v3.0.2
"""
<parameters>
    <company>AATrubilin</company>
    <title>PTZAutomation</title>
    <version>3.0.2</version>

    <parameter>
        <id>CHANNEL</id>
        <type>channel</type>
        <name>Channel</name>
        <value></value>
    </parameter>
    <parameter>
        <id>SCHEDULE</id>
        <type>objects</type>
        <name>Work by schedule</name>
        <value></value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Workmode</name>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>WORKMODE_GREED</id>
        <name>Default mode (Green or without schedule)</name>
        <value>Patrol</value>
        <string_list>Patrol,Preset</string_list>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>WORKMODE_RED</id>
        <name>Alarm mode (Red)</name>
        <value>Off</value>
        <string_list>Patrol,Preset,Off</string_list>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>WORKMODE_BLUE</id>
        <name>Other mode (Blue)</name>
        <value>Off</value>
        <string_list>Patrol,Preset,Off</string_list>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Patrol settings</name>
    </parameter>
    <parameter>
        <id>DEFAULT_PRESET</id>
        <type>integer</type>
        <name>Default preset</name>
        <value>1</value>
        <min>1</min>
        <max>99</max>
    </parameter>
    <parameter>
        <id>PATROL_PATH</id>
        <type>string</type>
        <name>Patrol path</name>
        <value>1,2,3,4</value>
    </parameter>
    <parameter>
        <id>PATROL_PRESET_TIMEOUT</id>
        <type>integer</type>
        <name>Preset timeout, sec</name>
        <value>30</value>
        <min>15</min>
        <max>9999</max>
    </parameter>
    <parameter>
        <id>PATROL_PRESET_TIMEOUT_RAND_MAX</id>
        <type>integer</type>
        <name>Max random preset timeout, sec</name>
        <value>30</value>
        <min>15</min>
        <max>9999</max>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>ActiveDome</name>
    </parameter>
    <parameter>
        <id>ACTIVEDOME_TIMEOUT</id>
        <type>integer</type>
        <name>ActiveDome timeout, sec</name>
        <value>15</value>
        <min>15</min>
        <max>999</max>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Other</name>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Debug mode</name>
        <value>False</value>
    </parameter>

    <resources>
        <resource>helpers.py</resource>
        <resource>schedule.py</resource>
    </resources>
</parameters>
"""

GLOBALS = globals()

CHANNEL = GLOBALS.get("CHANNEL", None)
SCHEDULE = GLOBALS.get("SCHEDULE", "")

WORKMODE_GREED = GLOBALS.get("WORKMODE_GREED", "Patrol")
WORKMODE_RED = GLOBALS.get("WORKMODE_RED", "Off")
WORKMODE_BLUE = GLOBALS.get("WORKMODE_BLUE", "Off")

DEFAULT_PRESET = GLOBALS.get("DEFAULT_PRESET", 1)
PATROL_PATH = GLOBALS.get("PATROL_PATH", "1,2,3,4")
PATROL_PRESET_TIMEOUT = GLOBALS.get("PATROL_PRESET_TIMEOUT", 30)
PATROL_PRESET_TIMEOUT_RAND_MAX = GLOBALS.get("PATROL_PRESET_TIMEOUT_RAND_MAX", 30)

ACTIVEDOME_TIMEOUT = GLOBALS.get("ACTIVEDOME_TIMEOUT", 10)

DEBUG = GLOBALS.get("DEBUG", False)

APP_NAME = "PTZAutomation"

import time
import random
from itertools import cycle
from __builtin__ import object

import host

import helpers

helpers.set_script_name()
logger = helpers.init_logger(APP_NAME, debug=DEBUG)

from schedule import ScheduleObject

assert CHANNEL, "Channel not selected"
channel = host.object(CHANNEL.split("_")[0])
try:
    channel.state("signal")
except EnvironmentError:
    raise EnvironmentError("Channel %s not found or disabled" % CHANNEL)


def __get_random_timout():
    return random.randint(PATROL_PRESET_TIMEOUT, PATROL_PRESET_TIMEOUT_RAND_MAX)


if PATROL_PRESET_TIMEOUT == PATROL_PRESET_TIMEOUT_RAND_MAX:

    def get_timeout():
        return PATROL_PRESET_TIMEOUT


else:
    assert (
        PATROL_PRESET_TIMEOUT < PATROL_PRESET_TIMEOUT_RAND_MAX
    ), "Random max timeout must be lower then preset timeout"

    def get_timeout():
        return __get_random_timout()


class PTZAutomation(object):
    def __init__(self, channel):
        self.channel = channel
        self.get_timeout = lambda: 30
        self.default_preset = 1
        self.ad_timeout = 15
        self.__patrol_path = cycle([1, 2, 3, 4])

        self.__workmode = {
            "Green": self.patrol,
            "Red": self.do_nothing,
            "Blue": self.do_nothing,
        }

        self.__last_ad_activity_ts = 0
        self.__current_work_mode = "patrol"

    @property
    def patrol_path(self):
        return next(self.__patrol_path)

    @patrol_path.setter
    def patrol_path(self, value):
        if isinstance(value, str):
            assert value, "Patrol path is empty"
            value = [int(v) for v in value.split(",")]
        self.__patrol_path = cycle(value)
        logger.debug("Set new patrol path: cycle(%r)", value)

    def set_mode(self, color, mode):
        mode = mode.lower()
        if mode == "patrol":
            self.__workmode[color] = self.patrol
        elif mode == "preset":
            self.__workmode[color] = self.preset
        else:
            self.__workmode[color] = self.do_nothing
        logger.debug("Change mode: %s", self.__workmode)

    def set_preset(self, preset):
        logger.debug("%s go to %s", channel.name, preset)
        self.channel.ptz_preset(preset)

    def patrol(self):
        if self.__current_work_mode == "patrol":
            if time.time() - self.__last_ad_activity_ts > self.ad_timeout:
                self.set_preset(self.patrol_path)
                timeout = self.get_timeout()
                logger.debug("Go next preset after %s", timeout)
                host.timeout(timeout * 1000, self.patrol)
            else:
                host.timeout(1000, self.patrol)

    def preset(self):
        if time.time() - self.__last_ad_activity_ts > self.ad_timeout:
            self.set_preset(self.default_preset)
            host.timeout(1000 * 15, self.preset)
        else:
            host.timeout(1000 * 15, self.preset)

    def do_nothing(self):
        pass

    def color_change_handler(self, sched):
        work = self.__workmode[sched.color]
        self.__current_work_mode = work.__name__
        logger.info("Start %s mode %s", sched.color, self.__current_work_mode)
        work()

    def run_default(self):
        work = self.__workmode["Green"]
        self.__current_work_mode = work.__name__
        logger.info("Start default mode %s", self.__current_work_mode)
        work()

    def ptz_handler(self, ev):
        logger.debug("ptz_handler: ev %s", ev.type)
        if ev.channel == self.channel.guid:
            if (
                "PRESET" not in ev.type
                and "ACQUIRE" not in ev.type
                and "RELEASE" not in ev.type
            ):
                self.__last_ad_activity_ts = time.time()


ptz = PTZAutomation(channel)
ptz.get_timeout = get_timeout
ptz.default_preset = DEFAULT_PRESET
ptz.patrol_path = PATROL_PATH
ptz.patrol_path = PATROL_PATH
ptz.ad_timeout = ACTIVEDOME_TIMEOUT

ptz.set_mode("Green", WORKMODE_GREED)
ptz.set_mode("Red", WORKMODE_RED)
ptz.set_mode("Blue", WORKMODE_BLUE)

if SCHEDULE:
    schedule = ScheduleObject(SCHEDULE, color_change_handler=ptz.color_change_handler, on_ready_handler=ptz.color_change_handler)
else:
    schedule = None
    ptz.run_default()

host.activate_on_ptz_events(ptz.ptz_handler)
