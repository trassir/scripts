# -*- coding: utf-8 -*-
# shutdown_by_schedule v1.0.0
"""
<parameters>
    <company>DSSL</company>
    <author>d.gavrilov</author>
    <title>shutdown_by_schedule</title>
    <version>1.0.0</version>
    <parameter>
        <id>RESTART_TYPE</id>
        <type>string_from_list</type>
        <name>Restart type</name>
        <value>HW Reboot</value>
        <string_list>Shutdown Trassir only,SW reboot,HW Reboot,Power off,Reset monitor settings</string_list>
    </parameter>
    <parameter>
        <id>STARTUP_DELAY_SEC</id>
        <type>integer</type>
        <name>Startup delay(sec)</name>
        <value>180</value>
        <min>60</min>
        <max>604800</max>
    </parameter>
    <parameter>
        <id>SCHEDULE</id>
        <name>Schedule (red zone)</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>SCHEDULE_LOAD_TIME</id>
        <type>integer</type>
        <name>Schedule load time(sec)</name>
        <value>10</value>
        <min>0</min>
        <max>100000</max>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>DEBUG</id>
        <name>Debug</name>
        <value>False</value>
   </parameter>
    <resources>
        <resource>helpers.py</resource>
        <resource>schedule_object.py</resource>
    </resources>
</parameters>
"""

GLOBALS = globals()
RESTART_TYPE = GLOBALS.get("RESTART_TYPE", "HW Reboot")
STARTUP_DELAY_SEC = GLOBALS.get("STARTUP_DELAY_SEC", 180)
SCHEDULE = GLOBALS.get("SCHEDULE", "")
SCHEDULE_LOAD_TIME = GLOBALS.get("SCHEDULE_LOAD_TIME", 10)
DEBUG = GLOBALS.get("DEBUG", False)

import helpers

helpers.set_script_name()
logger = helpers.init_logger("shutdown_by_schedule", debug=DEBUG)

import os
import sys
import time
import host
from __builtin__ import object
from schedule_object import ScheduleObject

if os.name == "nt" and RESTART_TYPE == "Reset monitor settings":
    raise EnvironmentError(host.tr("Reset monitor settings is not available for WinOS"))

EXIT_CODES = {
    "Shutdown Trassir only": 0,
    "SW reboot": 102,
    "HW Reboot": 103,
    "Power off": 104,
    "Reset monitor settings": 103,
}

MONITOR_SETTINGS_FILE = "/home/trassir/nvr-system-settings.ini"


def get_uptime_sec():
    return int(time.time() - (int(host.settings("health")["startup_ts"]) / 1e6))


class Worker(object):
    def __init__(self, exit_codes, restart_type, startup_delay):
        self.exit_codes = exit_codes
        self.monitor_settings_file = None
        self.restart_type = restart_type
        self.startup_delay = startup_delay

    def schedule_change_handler(self, schedule):
        if schedule.color == "Red":
            uptime = get_uptime_sec()
            if uptime > self.startup_delay:
                logger.debug("Time to push restart command -> %s", self.restart_type)
                if self.restart_type == "Reset monitor settings":
                    if os.path.isfile(self.monitor_settings_file):
                        os.remove(self.monitor_settings_file)
                    else:
                        raise RuntimeError(
                            "%s file not found" % self.monitor_settings_file
                        )
                host.stats()["run_count"] = self.exit_codes[self.restart_type]
                sys.exit(self.exit_codes[self.restart_type])
            else:
                logger.debug("Ignore restart event")


wr = Worker(EXIT_CODES, RESTART_TYPE, STARTUP_DELAY_SEC)
wr.monitor_settings_file = MONITOR_SETTINGS_FILE
if SCHEDULE:
    working_schedule = ScheduleObject(
        SCHEDULE,
        color_change_handler=wr.schedule_change_handler,
        tries=SCHEDULE_LOAD_TIME,
    )
else:
    assert SCHEDULE, host.tr("Schedule not selected")
