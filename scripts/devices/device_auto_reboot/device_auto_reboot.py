# DeviceAutoReboot v0.0.6
"""
<parameters>
    <company>DSSL</company>
    <author>AATrubilin</author>
    <title>DeviceAutoReboot</title>
    <version>0.0.6</version>
    
    <parameter>
        <id>DEVICES</id>
        <type>objects</type>
        <name>Devices, optional</name>
        <value></value>
    </parameter>
    <parameter>
        <id>MIN_TIMEOUT_BETWEEN_REBOOTS</id>
        <type>integer</type>
        <name>Min timeout between reboots, min</name>
        <value>15</value>
        <min>1</min>
        <max>3600</max>
    </parameter>
    
    <parameter>
        <type>caption</type>
        <name>Reboot on Signal Lost event</name>
    </parameter>
    <parameter>
        <id>SIGNAL_LOST_ENABLE</id>
        <type>boolean</type>
        <name>Enable</name>
        <value>True</value>
    </parameter>
    <parameter>
        <id>SIGNAL_LOST_TIMEOUT</id>
        <type>integer</type>
        <name>Signal Lost timeout, sec</name>
        <value>5</value>
        <min>1</min>
        <max>3600</max>
    </parameter>
    
    <parameter>
        <type>caption</type>
        <name>Reboot by Schedule</name>
    </parameter>
    <parameter>
        <id>SCHEDULE_REBOOT_ENABLE</id>
        <type>boolean</type>
        <name>Enable</name>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SCHEDULE_NAME</id>
        <type>objects</type>
        <name>Schedule (reboot on change to Red zone)</name>
        <value></value>
    </parameter>
    
    <parameter>
        <type>caption</type>
        <name>Other settings</name>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Debug mode</name>
        <value>False</value>
    </parameter>

    <resources>
        <resource>helpers.py</resource>
        <resource>long_event_handler.py</resource>
        <resource>schedule.py</resource>
    </resources>
</parameters>
"""

GLOBALS = globals()

DEVICES = GLOBALS.get("DEVICES", "")
MIN_TIMEOUT_BETWEEN_REBOOTS = GLOBALS.get("MIN_TIMEOUT_BETWEEN_REBOOTS", 15) * 60

SIGNAL_LOST_ENABLE = GLOBALS.get("SIGNAL_LOST_ENABLE", True)
SIGNAL_LOST_TIMEOUT = GLOBALS.get("SIGNAL_LOST_TIMEOUT", 5)

SCHEDULE_REBOOT_ENABLE = GLOBALS.get("SCHEDULE_REBOOT_ENABLE", False)
SCHEDULE_NAME = GLOBALS.get("SCHEDULE_NAME", "")

DEBUG = GLOBALS.get("DEBUG", False)

APP_NAME = "DeviceAutoReboot"

import time
import host
import helpers

default_script_name = helpers.set_script_name()
logger = helpers.init_logger(APP_NAME, debug=DEBUG)

from schedule import ScheduleObject
from long_event_handler import LongEventHandler


logger.info("Starting script %s (%s)", default_script_name, __name__)
logger.debug("DEVICES='%s'", DEVICES)
logger.debug("SIGNAL_LOST_ENABLE=%s", SIGNAL_LOST_ENABLE)
logger.debug("SIGNAL_LOST_TIMEOUT=%s", SIGNAL_LOST_TIMEOUT)
logger.debug("SCHEDULE_REBOOT_ENABLE=%s", SCHEDULE_REBOOT_ENABLE)
logger.debug("SCHEDULE_NAME='%s'", SCHEDULE_NAME)


_ip_cameras = host.settings("ip_cameras")
_channels = host.settings("channels")


def get_ip_cameras(names):
    if names:
        names = set(names.split(","))
    else:
        names = None

    ip_cameras = []
    for sett in _ip_cameras.ls():
        if sett.type == "Grabber" and sett["grabber_enabled"]:
            if names is None or sett.name in names:
                sett.prev_reboot_ts = 0
                ip_cameras.append(sett)
                if names:
                    names.remove(sett.name)
                    if not names:
                        break
    if names:
        raise RuntimeError("Not found ip cameras: %s" % ", ".join(names))

    return ip_cameras


devices = {dev.guid: dev for dev in get_ip_cameras(DEVICES)}


def reboot_device(dev):
    if time.time() - dev.prev_reboot_ts > MIN_TIMEOUT_BETWEEN_REBOOTS:
        logger.info("Reboot device %s", dev.name)
        dev["reboot"] = 1
        dev.prev_reboot_ts = time.time()
    else:
        logger.debug("Device %s not rebooted, timeout", dev.name)


def reboot_channel_device(ev):
    channel = _channels.cd(ev.origin)
    if channel:
        info = channel.cd("info")
        if info:
            reboot_device(info["grabber_path"].rsplit('/', 1)[-1])
        else:
            logger.warning("Channel %s (%s) has no info", channel.name, channel.guid)
    else:
        logger.debug("Channel %s not found", ev.origin)


if SIGNAL_LOST_ENABLE:
    leh = LongEventHandler(
        (
            "Signal Lost",
            "Signal Restored",
        ),
        reboot_channel_device,
        duration=SIGNAL_LOST_TIMEOUT,
        mode=0
    )


if SCHEDULE_REBOOT_ENABLE:
    assert SCHEDULE_NAME, "Please, select schedule..."

    def reboot_all_devices(sched):
        logger.info("Reboot all devices")
        if sched.color == "Red":
            for dev in devices.itervalues():
                reboot_device(dev)

    schedule = ScheduleObject(SCHEDULE_NAME, color_change_handler=reboot_all_devices)
