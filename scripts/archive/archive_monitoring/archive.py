# -*- coding: utf-8 -*-
# Archive stat v1.9
"""
<parameters>
    <company>MNRudkovskyi</company>
    <title>Archive stat</title>
    <version>1.9</version>
    <parameter>
        <id>CHANNELS</id>
        <name>Channels(all channels if there is no choice)</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>MAIL_ACCOUNT</id>
        <name>E-mail account</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <id>MAILING_LIST</id>
        <name>E-Mail Recipients</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <id>MAIL_SUBJECT</id>
        <name>E-Mail subject</name>
        <type>string</type>
        <value>Archive monitoring on server {server_name}</value>
    </parameter>
    <parameter>
        <type>objects</type>
        <id>WORK_SCHEDULE</id>
        <name>Work schedule (red)</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>DEBUG</id>
        <name>DEBUG</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>Check archive by days</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>DAY_MAIN</id>
        <name>Check main stream</name>
        <value>True</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>DAY_SUB</id>
        <name>Check sub stream</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>DAY_VALUE</id>
        <name>Last N days</name>
        <value>1</value>
        <min>1</min>
        <max>6</max>
    </parameter>
    <parameter>
        <type>string</type>
        <id>TIME_REPORT_DAY</id>
        <name>Check daily at(hours:minutes)</name>
        <value>10:00</value>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>Check archive for the last hours</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>HOURS_MAIN</id>
        <name>Check main stream</name>
        <value>True</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>HOURS_SUB</id>
        <name>Check sub stream</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>HOURS_VALUE</id>
        <name>Last N hours</name>
        <value>1</value>
        <min>1</min>
        <max>23</max>
    </parameter>
    <resources>
        <resource>date_utils.py</resource>
        <resource>email_sender.py</resource>
        <resource>helpers.py</resource>
        <resource>schedule.py</resource>
        <resource>schedule_object.py</resource>
        <resource>script_object.py</resource>
    </resources>
</parameters>
"""
GLOBALS = globals()
CHANNELS = GLOBALS.get("CHANNELS", None)
MAIL_ACCOUNT = GLOBALS.get("MAIL_ACCOUNT", "")
MAILING_LIST = GLOBALS.get("MAILING_LIST", "")
MAIL_SUBJECT = GLOBALS.get("MAIL_SUBJECT", "Archive monitoring on server {server_name}")
WORK_SCHEDULE = GLOBALS.get("WORK_SCHEDULE", "")

DAY_MAIN = GLOBALS.get("DAY_MAIN", True)
DAY_SUB = GLOBALS.get("DAY_SUB", False)
DAY_VALUE = GLOBALS.get("DAY_VALUE", 1)
TIME_REPORT_DAY = GLOBALS.get("TIME_REPORT_DAY", "10:00")

HOURS_MAIN = GLOBALS.get("HOURS_MAIN", True)
HOURS_SUB = GLOBALS.get("HOURS_SUB", False)
HOURS_VALUE = GLOBALS.get("HOURS_VALUE", 1)
TIME_REPORT_HOURS = ":15"

DEBUG = GLOBALS.get("DEBUG", False)

import json
import datetime
from functools import wraps
import host

import helpers

default_script_name = helpers.set_script_name()
logger = helpers.init_logger("Archive_stat", debug=DEBUG)

from script_object import ScriptObject
from date_utils import ts_to_dt
import schedule
from schedule_object import ScheduleObject
from email_sender import EmailSender

MAIL = None
if MAIL_ACCOUNT:
    MAIL = EmailSender(MAIL_ACCOUNT)

if MAIL_SUBJECT:
    MAIL_SUBJECT = MAIL_SUBJECT.format(server_name=host.settings("").name)
else:
    MAIL_SUBJECT = None
scr_obj = ScriptObject()

if WORK_SCHEDULE:
    WORK_SCHEDULE = ScheduleObject(WORK_SCHEDULE)
else:
    WORK_SCHEDULE = None

channels = []
selected_channels = None
if CHANNELS:
    selected_channels = set(CHANNELS.split(","))


def _is_channel_enabled(sett):
    info = sett.cd("info")
    if info and info["grabber_path"]:
        try:
            grabber = host.settings(info["grabber_path"])
        except KeyError:
            return False

        if grabber["grabber_enabled"]:
            n = info["grabber_channel_n"]
            return (
                    grabber["channel%02d_main_enabled" % n]
                    or grabber["channel%02d_ext_enabled" % n]
            )
    return False


for sett in host.settings("channels").ls():
    if sett.type == "Channel" and not sett["archive_zombie_flag"]:
        if selected_channels is None or sett.name in selected_channels:
            if _is_channel_enabled(sett):
                channels.append(sett)
                if selected_channels:
                    selected_channels.remove(sett.name)

assert not selected_channels, "Channels not found: " + ", ".join(selected_channels)
assert channels, "No channels to monitoring"


def cam_list():
    list_cam = {}
    for cam in channels:
        logger.debug("cam: %s", cam.name)
        try:
            stat_archive = cam.cd("arch_stats")
            logger.debug("stat_archive: %s", stat_archive["archive_stat_data"])
            if stat_archive:
                list_cam[cam] = json.loads(stat_archive["archive_stat_data"])
        except KeyError:
            logger.warning(
                "Can't get archive_stat_data for %s", cam.name, exc_info=True
            )
        except ValueError:
            logger.warning("No archive_stat_data for %s", cam.name, exc_info=True)
    return list_cam


def check_archive(list_cam, stream_type, interval_type, interval_value):
    logger.debug(
        "stream_type: %s, interval_type: %s, interval_value: %s",
        stream_type,
        interval_type,
        interval_value,
    )
    alarm_list = []
    if interval_type == "hours":
        reference_value = set(
            (datetime.datetime.now() - datetime.timedelta(hours=i)).hour
            for i in range(0, interval_value)
        )
    else:
        reference_value = set(
            (datetime.datetime.now() - datetime.timedelta(days=i)).day
            for i in range(0, interval_value)
        )
    logger.debug("reference_value: %s", reference_value)
    for cam, arch_stat in list_cam.iteritems():
        cam_stat = set()
        try:
            for data in arch_stat["write"][stream_type][interval_type]:
                if data["size"]:
                    if interval_type == "days":
                        cam_stat.add(ts_to_dt(data["ts"]).day)
                    else:
                        cam_stat.add(ts_to_dt(data["ts"]).hour)
            logger.debug("cam: %s, cam_stat: %s", cam.name, cam_stat)
            if cam_stat:
                if reference_value - cam_stat == reference_value:
                    alarm_list.append(cam.name)
            else:
                alarm_list.append(cam.name)
        except KeyError:
            alarm_list.append(cam.name)
            logger.debug("No data for %s in cam %s", interval_type, cam.name)
    logger.debug("alarm_list: %s", alarm_list)
    return alarm_list


def report(interval_type=None, interval_value=None, main=False, sub=False):
    result = {}
    list_cam = cam_list()

    if main:
        result["main"] = check_archive(
            list_cam,
            stream_type="main",
            interval_value=interval_value,
            interval_type=interval_type,
        )
    if sub:
        result["sub"] = check_archive(
            list_cam,
            stream_type="sub",
            interval_value=interval_value,
            interval_type=interval_type,
        )

    text = ""

    for stream, data in result.iteritems():
        for cam in data:
            scr_obj.fire_event_v2(
                "No archive of the %s stream, on the %s channel for the last %s %s"
                % (stream, cam, interval_value, interval_type),
                channel=cam,
            )
        if data:
            text += (
                    "No archive of the %s stream, on the channel: %s for the last %s %s. \n"
                    % (
                        stream,
                        ", ".join(str(cam) for cam in data),
                        interval_value,
                        interval_type,
                    )
            )
    if MAIL:
        if text:
            if WORK_SCHEDULE and WORK_SCHEDULE.color == "Red" or WORK_SCHEDULE is None:
                MAIL.send(MAILING_LIST, text=text, subject=MAIL_SUBJECT)


def day_report():
    logger.debug("Start days report")
    report(interval_type="days", interval_value=DAY_VALUE, main=DAY_MAIN, sub=DAY_SUB)


def hours_report():
    logger.debug("Start hours report")
    report(
        interval_type="hours",
        interval_value=HOURS_VALUE,
        main=HOURS_MAIN,
        sub=HOURS_SUB,
    )


schedule.every().day.at(TIME_REPORT_DAY).do(day_report)
schedule.every().hours.at(TIME_REPORT_HOURS).do(hours_report)

schedule.run_continuously()
