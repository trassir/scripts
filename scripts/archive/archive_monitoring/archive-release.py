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

resources = {
    "date_utils.py": """
        eNp1kMEOgyAMhu8mvkOP4DKmlx2WuFcxRmpCJmKgvv+ojKnJVgKU9u/XUGMX5wnIWCwLkx66
        J0wBXhpH0NSR6ygITfJRFhDNI61+BjOT4M16ZV98RZHim9ZlQiGlhAoavMMlYpQ1g3cBBzdr
        ufMpMF9HTMh8w1F4xsqm/oTYojJWQ7s1joIbo+Upb8OevuaC6qDDKeB/5A9YffpyHo/6OqN3
        lp1AvV1E4kn+bxbwoXGiXuzwwyRCu3VKOfkGy7B19Q==
    """,
    "email_sender.py": """
        eNqVV1tr5DYUfg/kPwhDQNOdmmRpoQydJaHNQmHZl9C+pKnw2JoZtbZkJHk32aX/vedIsi3b
        mkl3ArFH5/6di86IplXaEs0vL4R/VWZ4PSpjLy8uL6x+2VxeEPjstWrIkdct14YErgO3rFaH
        A9eXF/y55K0lvznKvdZKx4LIJeQhEvzg5EhhJlrwz7+TbUSgKyQw9gmMCyUZA2p2k1/nN1nP
        n1d81x1odmVI4NqQK5OtCWOyaDhj+DbIe328KUTNPhW1qJjmB/7cgl7N81I1rag51dnjX7dP
        b27d/z9z98hW3suyLowh96jBRUvvHQCgfRUCb4FhwXtXlqqT9qOy7+FZ0VHBWTHg/wPdPMtf
        8T1hn4VkXJaq4qwt7JHiv55V7CHHOcJBtgCgtFkg4GdMdf9BUQAEH4AuqqRZZ/c/IQQ9T0g7
        /V0KZPjVsTn/1iSc3cvhbLWwgL7jm+a209LZWgT/wGUFNaB2f/PS9iog2KKrLTOdO8aC+Gq4
        hgy7fP9Lvn9HvppSi9b6gyzfK90Ulo4uRPxbrPjccGuhTA3NspXHSWmS/VILDlitI8FRbxC0
        hTV0lbeFBlbqhYOAK5jgMtSgkMIyRg2v92tS+HKIcUFCzligQFzuAHvBl2sg0F50JtkUz6yw
        tiiPDXhi2O7FcgNa3v5IviM3129/CI/eqVt0XZQNt0dVjX6ethe5CvUkle2DmOVWF8JwAlXb
        +dzT7L5p7UvPnQ2wuCEBOCP4REgyy4TH2kBCakB4ZgQ8QM7cvrS+puMmy0ghK0IdQ1/0PazB
        Xn7oRBWdz/VHpYnsscs+vmRTj6k5i7HHVxg/gaj7GjsQDO+UqmliVkGqbXkMYqMt1zhzU1CX
        hjPkNLSszdrbNolkesL/zKVnnsyD2vBFk4PtygeAlfj4tMihMEICRrLkPhxwkBoLI6TzI2SV
        ysug0L/kpq2Fpdl6Wll9dTkmLK9kgMEPgCZ/LSsnQ8uLtoVJFSQS/i6hSdTSMOlTaoYpGZmd
        TJeDVl3L9nB5YeczHAZGfOFh2uC5uxUmic+y7AGhc2RDrCJOi8nJA4gSBYUK08QfQqYIMAHX
        kUvSq4/xvtOHObijWUJrYaDJyAd4oGZncuLKoiBH6U0SDCynkeC9nBZZ2WnnJhxfT0eOqJ4j
        VFx1yK7hurCcpsFyiXQXWsVGwe3y3h2Iq0W1Y1RwD7t7VRhkpAuVqYoLi87nQksYjTR7D8we
        Ipw6Yd05ZdcBoSQM1Y4n0hPwAbdwViX8gfOQ64RLYfe6qyoy3j3gT+wTCp92T+wjP95tz9xl
        rwOT7jHcDJ12eO46S5LKt+hvWn7w/BzdBZmmn44oIZAumqGQoXTp8OXNaHpFfv425EYl21HL
        ks11VT/fTqXwxHzbaV78c/aC6BvZWZl085QCkfrl6NSUG1v2ETp78zTZvAz67udguGIsf7bb
        DOozQmr7UUko07BVum9xK07qfRpFhmsq/sbxN82VDgbwJTaA33v1V3pebd616RmqmR1FCmeU
        oDo6XU1Gar8vwyDH4DZJ6X7rnC3ZcWpAVeTEZnnhuiTBCIm4cMCez2DEnJqAYTWUlVtlGP60
        HPbTM103bNNu3TvXn/Ge5DekU9wLmF/J2KSVprCc7/9Ew3wbDCkITkY7BOZjWCxr4Nh/udOX
        +Q==
    """,
    "helpers.py": """
        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
        4+p7S3Xl7WOZBz5QD1O1/EpNMZf/H+cMA4M=
    """,
    "schedule.py": """
        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
        4J8=
    """,
    "schedule_object.py": """
        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
        kIw=
    """,
    "script_object.py": """
        eNq9V1tr4zgUfg/kPwjBEBs8ppl9CwS2U8JSZrcdpmVfSnEUW0k840hGkkNLt/99ji625UvS
        MgObl9g653xH5/uOLs4PJRcKfZecTSe5fdlzqaaT6USJ58V0guC3FfyA9rQoqZDIee2oSgq+
        21ExndCnlJYKXRvLSggu/EDtlbOdF/i3iUNEdlCmE/uElt5wEGpDkhwhdc5ZkoAVz+OL+ALX
        /nFGN9UuwB8kcl4L9EHiCCUJIweaJPqpiTd4d1ffrr/eJzeX/6wATxccS0WUDMK4JIIyBQ86
        VvtOJ2lBpER3qchLdbv5TlMVmJB7AeO5sEMR4uY/dKVjjJ0dSRPp7BpQ2y/FTjpX/dPZUCCV
        AJxSwUxJES6QhTbGCGV0S6pCoQUALdY3nNF1G7+r8uxkvDa+EW/LHiJ8teP8XUBQc10e+ADr
        OctVkgSSFtvIVLHU3pHBcY82sXkJPT5kBc0W+JxHSMOEcYOKrRWHdU4Tl4rE1XJC2I43IMam
        S8Db/HGBvOboeUpoS+0VtHEjcEaKpVUE4PDL60dLH463XByICtpJxtorHEmjx4MWbyRNU6V7
        gFS2XqoULDcZYBwa+BF0x4UPNJJhy4vMLMdW1ta4p6RQe228/YL7xnRP0x+JYfVeVHQQreeg
        VcxJkWh9aPDgo0Y9mMfO5EyVltGEZJalkdmDR90C1vksnSlnij4pSMYqCHt4rD3+LAWHVlTP
        bV/bSdq8i5O8NLOIbYXYWrCntqCqEqwT2KS1r0ZNvTmO5I7QkRRVZ9XkWzuGcoYetDARwmY/
        xo+eV0cGR78JG+N9ENRWaGJaD1pI2ssiSC4p+lf7mWkEePVUghQ0Q7PbLzPdszNjmMGewBWa
        vbzOmlViqwvPCFHP84QUXhfmTbd7gtR2HA412XBeBF2Ydib1yECdzoTG9cllziA/S2ngONep
        Qk1FK908Qhd9xax1ieboY5/5MUG768kEjMvpsfRbguoydBXz/y5+ScxmY/UJ66yQ+kQ2APpl
        wH+D8V7u4bgLT60MA2Zhxnhzp8ZvcWZOW83Vy2vDlHou67RxfYM5S5zdps9TZ30aEPs6oM9D
        GieQwVTN+JslejcPlBI2U2hDET2U6rl7Xr9XFfDzK+lZ2218T9iOOqdR8UYE6qh+JrR3Kv7P
        ypv9xTulkk2lFGdOLT0cAdNFsSHpD589uJRdZlkdimwUUry+02ksX5HexVT/TGBgVEGfXTwM
        dZ3q3CjYVizVF0jwvqoH6zE/0zfTof1k9lZ5t0qu7IyviIItSqwBzJVgzmgQOivaljZ4mu4+
        XMv+Al1vbSm5tK3Y9bwH+p0jdFtTDjjrttfvZFPQDrGDxaHh32yCG278BgvBTxOMSdnCNXMN
        8IDi/oy7eTaK1dciAu5HOCwS+C7yO8u7KA0a68y1KSZlSVkWBN2QuP0Mg9xjR61ifo9vc0ET
        eoQraXL85Lr7QKUkO9gZ9PpmtFhiuNlkRBF46PX6X5RRAUUh5b6+DNQbDe7w6x5f6ZB2cL0u
        5+t1bzNwMxl+MdlgyM3TnOil3ngCzqcBjq7iFIi1QdgfnbCxxvM2UR01uocauKX52I+z6lBK
        4zq8C7cK1N9Y8EE9x0MZrAYA8BMTvrha
    """,
}
t1utils.resources_check(script_path, resources)
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
