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

resources = {
    "helpers.py": """
        eNqlV19r21YUfw/kO1zuMEibrbZsjGLsjKx12kD+lMShlCwIxbp2tEq63r1XSUMIbPPexqCD
        MbbSjm19G2N0e9oG2172AZx9Az+07GPs3Ksr6Uqy28BssKXz//zOuedIr6HW6y00oH4Qj9oo
        EcPWdUlZXgqiMWUC8VOeXzOSX9KCGtLRCJSXl4aMRmApDMlABDTmSAv45IMENHOFI8qFvN29
        sbN+p+9urW72UFdRHS48wS3bGXuMxAIuYi8C1Zu9tdW9jb5raOyCytnyEoIPvkfiAPH7LBgL
        3NS0vViq+mh3UCLPJk9nk+9mk4ezyU+zyRezyaPZ5AlSpK9nk29nk69mk29mk+/hIteZfjl9
        9s/T6TN08dH094sPp79O/7r4OOemDlBMk0LhyfTP6S8Xn05/m69ixIt8yk89/vfPFWXQWKD8
        4vEPzz//4/nDz/795NGLxz9K+vnyUuQFsRtRPwkJAANFc9Ib7oyIsOZjO0oCv6lwt2U5lpd8
        MkQnYIfE0A/EHXviyJI/djv1HQyh7qokqNtFOBZYM+RHsFPjTn6kKgQj/xyfSJMWhga7ju1C
        jjwYEEDB2osDKXBTifUYo6yJNK0X5zS75oHzlMKISFisfKW5DELgoduQ3AYd3fZiPyTM0q3q
        6PvMnMybRIGwOAmHTbA1oMw3fSn8QNmNCOfeiChBZ0hZ5AlLi9um3zt0nIxf4RVj3GcgHDA0
        luLoKOUDXRqSIq5i8KLVlR4cgv76jdUN3E4DIwouQ2Bttf8Sbm9nZ3tnIffu6s5WxvQgGlFl
        rm/dWshf31rbzpgaKpN9s/fu3q2X8Le2+7u9/nyB8wyTVxYr4iN5BOoVKkQUU4O7n3KdkByT
        UPb2gQUWStXcPF0LQvKKct6FqvTc/vpmb3uv727K+XTt6tWrZtiuG8SBcF0d+hCMSodm8DwZ
        g4uSw6YK13Zy7VoirrTk6uNWPcDlEwPnV53H92kQV1h5o3MiBCTILQxzRJDIPQnAGB2roY7t
        fcwHjJCYH1HB3SENfejZgyKdslUj2HrcJywQhLknlN0HhxD8mhdyUhODeriwQhI52tQysSLv
        ATjrSoDtMsKpSYWwietJAODQMYmtKmRNhD1sI4/LRabIlSFzcgS0WijtOniZvqNisHCDvxdj
        1KipOtB4IRnCCL48Ipfs/Zorbww5+wvmVaYFcz2mYn4IlTwXhdlnSaXwqpVEEBGapPE61RPS
        LFszlpBqdHnOoJKypZqQ+WEy6iowsnzTPYTwmbw4R9aZ3GfnNs7ylORuqi053cVLUEOROgST
        2QmH1blRBJE3GtjPZrULoWo9R5P4fvvAXB1a0BmElBPz7Go1RiJ6nA+XTDx3pqXgTG7IAWXp
        IZrzZVau1oLQKwvPrgsVprI0lUXZBApkRADjHAI50U0jKbaiBNNaRjMGCm6kmHG037Dy0Wq3
        rvMDBIQgJjG1W29x1GlYwyQebCnhFdQCrh78NsepvQVJFG7LkZWq6Xi+n2NrGMjxU0vAALC0
        ue05MnX8JEYL4NMLs2TnshAOI9HFncOVEoD8oHPlcAVtAIDtAkjeOWQrnWClwM55+82rvHMl
        WCljWMukcFwJbiGKJRM5jFn6RuerCVsAW16iMBzlA5Ucj/pszVNb0KtV6csimqPasDw+kLPp
        f/Zns2zb9wRJ7d9rNaJWw0eN2+3GZruxa0q+JNci6HJe9alhFMQ0ktdDPw+n0sVghYmWzdVs
        jGpJ4IArZhkvErAZU1ncRFs0JjaCwVefjcbchhRcrt6HXAln7sOnAyjNfBeuC1zXNX1g3bQi
        EOp1hhEAx2ODI4vhjiKuWM4bdudKeg2qYMLOG1FRjUY8hqEMjy5VQ5qsTWV3JWOQk5eEpZzU
        xlEeztHxmdY6z5eO8T4kZbrq1xkxmoyta3Yzi6Wr/3OOjDuLU00Q/I4D3/LpBRnznRlWz7wX
        4+p7S3Xl7WOZBz5QD1O1/EpNMZf/H+cMA4M=
    """,
    "schedule.py": """
        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
        kIw=
    """,
}
t1utils.resources_check(script_path, resources)

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
