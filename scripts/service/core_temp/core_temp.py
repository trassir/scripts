# -*- coding: utf-8 -*-

"""
<parameters>
    <company>DSSL</company>
    <title>Coretemp</title>
    <version>2.0</version>
    <parameter>
    <type>integer</type>
    <name>Период сбора данных, сек</name>
    <id>DELAY</id>
    <value>60</value>
    <min>1</min>
    <max>100000</max>
</parameter>
</parameters>
"""

GLOBALS = globals()
DELAY = GLOBALS.get("DELAY", 60)

import os
from datetime import datetime
import time
import commands
import host


class Log:
    # Initialization
    def __init__(
        self,
        file_name="%s.log"
        % host.settings("scripts/%s" % __name__).name.split("\\")[-1],
        write_log=True,
    ):
        self.dir_path = host.settings("system_wide_options")["screenshots_folder"]
        self.file_name = file_name
        self.file_path = os.path.join(self.dir_path, self.file_name)
        self.write_log = write_log
        self.max_rows = 500

    # Old rows removal
    def remove_old_lines(self):
        with open(self.file_path, "rb") as f:
            text = f.read().split("\n")
        if len(text) > self.max_rows:
            text = text[len(text) - self.max_rows :]
            with open(self.file_path, "wb") as f:
                f.write("\n".join(text))

    # Write to log
    def write(self, string):
        if not self.write_log:
            return 0
        with open(self.file_path, "a") as f:
            f.write(
                time.strftime(
                    "%d.%m.%Y %H:%M:%S: {0}\n".format(str(string)), time.localtime()
                )
            )
        self.remove_old_lines()
        return 0


log = Log()
log_path = os.path.join(
    host.settings("system_wide_options")["screenshots_folder"], "coretemp.log"
)


def start():
    res = commands.getoutput("cat /sys/class/thermal/thermal_zone0/temp | cut -c 1-2")
    dt_str = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    # raise ValueError(res)
    log.write(res + "°C")
    host.stats()["run_count"] += 1
    host.timeout(1000 * DELAY, start)


start()
