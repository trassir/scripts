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

resources = {
    "helpers.py": """
        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
    """,
    "schedule_object.py": """
        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
        kIw=
    """,
}
t1utils.resources_check(script_path, resources)

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
