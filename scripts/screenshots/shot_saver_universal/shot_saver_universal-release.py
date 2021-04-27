# -*- coding: utf-8 -*-
# <h3>Shot Saver Universal</h3><br>
#
# <code>
# Version: v3.2.4<br>
# Author: A.A.Trubilin, DSSL<br>
# E-mail: a.trubilin@dssl.ru<br>
# Help: https://scripts.page.link/shot_saver
# </code>
"""
<parameters>
    <company>AATrubilin</company>
    <title>ShotSaverUniversal</title>
    <version>3.2.4</version>

    <parameter>
        <type>caption</type>
        <name>Настройки скрипта</name>
    </parameter>
    <parameter>
        <id>SELECTED_SERVER</id>
        <type>server</type>
        <name>Сервер</name>
    </parameter>
    <parameter>
        <id>SELECTED_CHANNELS</id>
        <type>objects</type>
        <name>Каналы</name>
    </parameter>
    <parameter>
        <id>SAVE_FOLDER</id>
        <type>string</type>
        <name>Путь, относительно папки скриншотов</name>
        <value>{server.name}/%Y.%m.%d/{channel.name}</value>
    </parameter>
    <parameter>
        <id>SHOT_AWAITING_TIME</id>
        <type>integer</type>
        <name>Время ожидания скриншота, сек</name>
        <value>5</value>
        <min>1</min>
        <max>99</max>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Режим отладки</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Скриншоты онлайн</name>
    </parameter>
    <parameter>
        <id>SSO_DELAY</id>
        <type>integer</type>
        <name>Каждые n сек</name>
        <value>0</value>
        <min>0</min>
        <max>9999999</max>
    </parameter>
    <parameter>
        <id>SSO_SCHEDULE</id>
        <type>objects</type>
        <name>По расписанию (Red)</name>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Время ожидания загрузки расписания (сек)</name>
        <id>LOAD_SCHEDULE_TIMEOUT</id>
        <value>5</value>
        <min>5</min>
        <max>99999</max>
    </parameter>
    <parameter>
        <id>SSO_BUTTON_ALL</id>
        <type>string_from_list</type>
        <name>По нажатию клавиши (для выбранных каналов)</name>
        <value></value>
        <string_list>,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12</string_list>
    </parameter>
    <parameter>
        <id>SSO_BUTTON_ONE</id>
        <type>string_from_list</type>
        <name>По нажатию клавиши (для активного канала)</name>
        <value></value>
        <string_list>,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12</string_list>
    </parameter>
    <parameter>
        <type>string</type>
        <name>По событию</name>
        <id>EVENT_TYPE</id>
        <value></value>
    </parameter>
    <parameter>
        <id>EVENT_OBJECTS</id>
        <type>objects</type>
        <name>Только события с выбранных объектов</name>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Скриншоты из архива</name>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>SSA_INTERVAL</id>
        <name>Интервал между скриншотами, мин</name>
        <value>0</value>
        <min>0</min>
        <max>9999999</max>
    </parameter>
    <parameter>
        <type>date</type>
        <id>SSA_DAY_START</id>
        <name>Дата начала</name>
        <value>01.05.2019</value>
    </parameter>
    <parameter>
        <type>time</type>
        <id>SSA_TIME_START</id>
        <name>Время начала</name>
        <value>10:00:00</value>
    </parameter>
    <parameter>
        <type>date</type>
        <id>SSA_DAY_STOP</id>
        <name>Дата окончания</name>
        <value>01.05.2019</value>
    </parameter>
    <parameter>
        <type>time</type>
        <id>SSA_TIME_STOP</id>
        <name>Время окончания</name>
        <value>11:00:00</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>FIGURES</id>
        <name>Фигуры</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Настройка отправки</name>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>SENDING_METHOD</id>
        <name>Отправка скриншотов</name>
        <value>Отключено</value>
        <string_list>Отключено,Email,FTP</string_list>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>REMOVE</id>
        <name>Удалить после отправки</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Настройка Email</name>
    </parameter>
    <parameter>
        <id>EMAIL_ACCOUNT</id>
        <name>Учетная запись отправителя</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <id>EMAIL_SUBSCRIBERS</id>
        <name>Получатели</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>EMAIL_MAX_SIZE</id>
        <name>Максимальный размер вложения(МБ)</name>
        <value>25</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Настройка FTP</name>
    </parameter>
    <parameter>
        <type>string</type>
        <id>FTP_HOST</id>
        <name>IP адрес/имя хоста</name>
        <value>172.20.0.10</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>FTP_PORT</id>
        <name>Порт</name>
        <value>21</value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>FTP_USER</id>
        <name>Имя пользователя</name>
        <value>trassir</value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>FTP_PASSWORD</id>
        <name>Пароль пользователя</name>
        <value>12345</value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>FTP_WORK_DIR</id>
        <name>Рабочая папка</name>
        <value>/trassir/shots/</value>
    </parameter>
    <parameter>
        <id>FTP_ADD_RELATIVE_PATH</id>
        <type>boolean</type>
        <name>Учитывать относительный путь</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>FTP_PASSIVE_MODE</id>
        <name>Пассивный режим FTP</name>
        <value>True</value>
    </parameter>

    <resources>
        <resource>email_sender.py</resource>
        <resource>ftp.py</resource>
        <resource>helpers.py</resource>
        <resource>schedule.py</resource>
        <resource>shot_saver.py</resource>
    </resources>

</parameters>
"""

resources = {
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
    "ftp.py": """
        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
        l0U=
    """,
    "helpers.py": """
        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
        4+p7S3Xl7WOZBz5QD1O1/EpNMZf/H+cMA4M=
    """,
    "schedule.py": """
        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
        kIw=
    """,
    "shot_saver.py": """
        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
    """,
}
t1utils.resources_check(script_path, resources)
GLOBALS = globals()

# Script settings
SELECTED_SERVER = GLOBALS.get("SELECTED_SERVER", "") or None
SELECTED_CHANNELS = GLOBALS.get("SELECTED_CHANNELS", "")
SAVE_FOLDER = GLOBALS.get("SAVE_FOLDER", "{server.name}/%Y.%m.%d/{channel.name}")
SHOT_AWAITING_TIME = GLOBALS.get("SHOT_AWAITING_TIME", 5)
DEBUG = GLOBALS.get("DEBUG", False)

# Online screenshots
SSO_DELAY = GLOBALS.get("SSO_DELAY", 0) * 1000
SSO_SCHEDULE = GLOBALS.get("SSO_SCHEDULE", "")
LOAD_SCHEDULE_TIMEOUT = GLOBALS.get("LOAD_SCHEDULE_TIMEOUT", 5)
SSO_BUTTON_ALL = GLOBALS.get("SSO_BUTTON_ALL", "")
SSO_BUTTON_ONE = GLOBALS.get("SSO_BUTTON_ONE", "")
EVENT_TYPE = GLOBALS.get("EVENT_TYPE", "Input Low to High")
EVENT_OBJECTS = GLOBALS.get("EVENT_OBJECTS", "")

# Archive screenshots
SSA_INTERVAL = GLOBALS.get("SSA_INTERVAL", 0)
SSA_DAY_START = GLOBALS.get("SSA_DAY_START", "01.05.2019")
SSA_TIME_START = GLOBALS.get("SSA_TIME_START", "10:00:00")
SSA_DAY_STOP = GLOBALS.get("SSA_DAY_STOP", "01.05.2019")
SSA_TIME_STOP = GLOBALS.get("SSA_TIME_STOP", "11:00:00")
FIGURES = GLOBALS.get("FIGURES", False)

# Sender settings
SENDING_METHOD = GLOBALS.get("SENDING_METHOD", "Отключено")
REMOVE = GLOBALS.get("REMOVE", False)

# Email settings
EMAIL_ACCOUNT = GLOBALS.get("EMAIL_ACCOUNT", "")
EMAIL_SUBSCRIBERS = GLOBALS.get("EMAIL_SUBSCRIBERS", "")
EMAIL_MAX_SIZE = GLOBALS.get("EMAIL_MAX_SIZE", 25)

# FTP settings
FTP_HOST = GLOBALS.get("FTP_HOST", "172.20.0.10")
FTP_PORT = GLOBALS.get("FTP_PORT", 21)
FTP_USER = GLOBALS.get("FTP_USER", "trassir")
FTP_PASSWORD = GLOBALS.get("FTP_PASSWORD", "12345")
FTP_WORK_DIR = GLOBALS.get("FTP_WORK_DIR", "/trassir/shots/")
FTP_ADD_RELATIVE_PATH = GLOBALS.get("FTP_ADD_RELATIVE_PATH", False)
FTP_PASSIVE_MODE = GLOBALS.get("FTP_PASSIVE_MODE", True)

import re
import os
import datetime
import threading
from functools import wraps
from __builtin__ import object
import host
import helpers

helpers.set_script_name()
logger = helpers.init_logger("ShotSaver", debug=DEBUG)

from ftp import FTPClient, status as ftp_status
from schedule import ScheduleObject
from email_sender import EmailSender
from shot_saver import ShotSaver, status as shot_status

tr = host.tr

if not SELECTED_SERVER:
    SELECTED_SERVER = host.settings("").guid

if EVENT_OBJECTS:
    EVENT_OBJECTS = EVENT_OBJECTS.split(",")


def _is_channel_enabled(sett):
    info = sett.cd("info")
    try:
        if not sett["archive_zombie_flag"]:
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
    except KeyError:
        logger.warning("Can't check is channel enebled", exc_info=True)
    return False


def _parse_channel_names(channel_names):
    if channel_names:
        return set(channel_names.split(","))


def _run_as_thread(fn):
    @wraps(fn)
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
        return t

    return run


class TRObject(object):
    spec_symbols = re.compile(r'[|\\/:*?"<>]')

    def __init__(self, sett):
        self.sett = sett
        self.name = self.spec_symbols.sub("", sett.name.strip())

    def __getattr__(self, name):
        return getattr(self.sett, name)


class Server(TRObject):
    def __init__(self, sett):
        super(Server, self).__init__(sett)


class Channel(TRObject):
    def __init__(self, sett, server):
        super(Channel, self).__init__(sett)
        self.server = server

    @property
    def full_guid(self):
        return "{s.guid}_{s.server.guid}".format(s=self)


def get_channel(channel_guid):
    for _, guid, _, parent in host.objects_list("Channel"):
        if guid == channel_guid:
            server_settings = host.settings("/%s" % parent[:-1])
            channel_settings = server_settings.cd("channels").cd(guid)
            server = Server(server_settings)
            return Channel(channel_settings, server)


def get_channels(server_guid, channel_names=None):
    channels_ = []
    server = Server(host.settings("/%s" % server_guid))
    for sett in host.settings("/%s/channels" % server_guid).ls():
        if sett.type == "Channel":
            try:
                if channel_names is None or sett.name in channel_names:
                    if _is_channel_enabled(sett):
                        channels_.append(Channel(sett, server))
            except ValueError:
                logger.warning("Can't check channel, maybe user has no access", exc_info=True)
    return channels_


class Saver(object):
    default_shots_folder = host.settings("system_wide_options")["screenshots_folder"]

    def __init__(self, channel_guids, folder_tmpl):
        """

        Args:
            channel_guids (List[str]): Channels guid `channelGuid_serverGuid`
        """
        self.folder_tmpl = folder_tmpl
        self.channel_guids = channel_guids
        self.ss = ShotSaver(callback=self.save_shot_callback)
        self.ftp = None
        self.ftp_add_relative_path = False
        self.email = None
        self.email_subscribers = None
        self.remove = False
        self.shots_path_for_send_email = []
        self.working_tasks = {}

    def __get_folder(self, channel, dt=None):
        dt = dt or datetime.datetime.now()
        folder = dt.strftime(
            self.folder_tmpl.format(channel=channel, server=channel.server)
        )
        logger.debug("Folder: %s" % folder)
        return folder

    def ftp_callback(self, task_guid, state):
        logger.debug("%s: ftp %s", task_guid, state)
        if state in (ftp_status.success, ftp_status.error):
            task = self.working_tasks.pop(task_guid, None)
            host.stats()["run_count"] -= 1
            if task and self.remove:
                try:
                    os.remove(task["path"])
                except:
                    logger.exception("Unhandled exception while removing file", task)

    def remove_file(self, shot_path):
        try:
            os.remove(shot_path)
            logger.debug("remove file %s" % shot_path)
        except:
            logger.exception("Unhandled exception while removing file %s", shot_path)

    @_run_as_thread
    def sending_email(self):
        self.email.send(
            mails=self.email_subscribers, attachments=self.shots_path_for_send_email
        )
        if self.remove:
            for path in self.shots_path_for_send_email:
                self.remove_file(path)
        self.shots_path_for_send_email = []

    def save_shot_callback(self, task_guid, state):
        logger.debug("%s: shot %s", task_guid, state)
        if state == shot_status.success:
            task = self.working_tasks.get(task_guid, None)
            if task:
                if self.ftp:
                    try:
                        if self.ftp_add_relative_path:
                            remote_dir = task["folder"]
                        else:
                            remote_dir = None
                        self.ftp.send(
                            task["path"],
                            remote_dir=remote_dir,
                            task_guid=task_guid,
                            callback=self.ftp_callback,
                        )
                    except IOError:
                        logger.exception("Could not send file %s", task["path"])
                elif self.email:
                    self.shots_path_for_send_email.append(task["path"])
                    self.working_tasks.pop(task_guid, None)
                    host.stats()["run_count"] -= 1
                else:
                    self.working_tasks.pop(task_guid, None)
                    host.stats()["run_count"] -= 1

        elif state == shot_status.error:
            self.working_tasks.pop(task_guid, None)
            host.stats()["run_count"] -= 1
            logger.warning("Can't save shot %s" % task_guid)
        if self.email and not self.working_tasks and self.shots_path_for_send_email:
            logger.debug("Time to send email")
            self.sending_email()

    def save_shots(self, channels=None, dt=None):
        channels = channels or self.channel_guids
        paths = []
        for channel in channels:
            host.stats()["run_count"] += 1
            folder = self.__get_folder(channel, dt=dt)
            file_path = os.path.join(self.default_shots_folder, folder)
            task_guid, path = self.ss.save(
                channel.full_guid, dt=dt, file_path=file_path, figures=FIGURES
            )
            self.working_tasks[task_guid] = {
                "path": path,
                "folder": folder,
            }
            logger.debug("%s: task created (%s)", task_guid, path)
            paths.append(path)

        return paths


selected_channels = get_channels(
    SELECTED_SERVER, _parse_channel_names(SELECTED_CHANNELS)
)
saver = Saver(selected_channels, SAVE_FOLDER)
saver.ss.timeout_sec = SHOT_AWAITING_TIME
saver.remove = REMOVE

if SENDING_METHOD == "Email":
    saver.email = EmailSender(EMAIL_ACCOUNT)
    saver.email_subscribers = EmailSender.parse_mails(EMAIL_SUBSCRIBERS)
    saver.email.max_attachments_bytes = EMAIL_MAX_SIZE * 1024 * 1024

elif SENDING_METHOD == "FTP":
    saver.ftp = FTPClient(
        FTP_HOST,
        port=FTP_PORT,
        user=FTP_USER,
        passwd=FTP_PASSWORD,
        work_dir=FTP_WORK_DIR,
        passive_mode=FTP_PASSIVE_MODE,
    )
    saver.ftp_add_relative_path = FTP_ADD_RELATIVE_PATH
else:
    pass

if SSO_DELAY:
    assert SSO_DELAY > len(selected_channels), tr(
        "Delay is too short, for {length} channels you need more than {delay_min} seconds delay".format(
            length=len(selected_channels), delay_min=SSO_DELAY
        )
    )

    def make_shots_loop(delay):
        logger.info("Save shots by delay")
        saver.save_shots()
        host.timeout(delay, lambda: make_shots_loop(delay))

    make_shots_loop(SSO_DELAY)

if SSO_SCHEDULE:

    def color_change_handler(sched):
        if sched.color == "Red":
            saver.save_shots()

    schedule = ScheduleObject(SSO_SCHEDULE, color_change_handler=color_change_handler, tries=LOAD_SCHEDULE_TIMEOUT)

if SSO_BUTTON_ALL:
    host.activate_on_shortcut(SSO_BUTTON_ALL, saver.save_shots)

if SSO_BUTTON_ONE:

    class ActiveChannelHandler(object):
        def __init__(self, saver):
            self.saver = saver
            self.active_channel = ""

        def __call__(self, guid):
            logger.info("Focus Changed %s -> %s", self.active_channel, guid)
            self.active_channel = guid

        def save_shot(self):
            if not self.active_channel:
                host.alert(tr("Channel not selected!"))
            else:
                channel = get_channel(self.active_channel)
                if channel is not None:
                    paths = self.saver.save_shots([channel])
                    host.message(tr("Saving shot to <br><b>%s</b>") % paths[0])
                else:
                    host.error("Can't find channel %s" % self.active_channel)

    active_channel_handler = ActiveChannelHandler(saver)

    host.activate_on_gui_event("Focus Changed", active_channel_handler)
    host.activate_on_shortcut(SSO_BUTTON_ONE, active_channel_handler.save_shot)

if EVENT_TYPE:

    def handler(ev):
        if not EVENT_OBJECTS or ev.origin_object.name in EVENT_OBJECTS:
            saver.save_shots()

    host.activate_on_events(EVENT_TYPE, "", handler)

if SSA_INTERVAL:
    dt_start_ = datetime.datetime.strptime(
        "%s %s" % (SSA_DAY_START, SSA_TIME_START), "%d.%m.%Y %H:%M:%S"
    )
    dt_end_ = datetime.datetime.strptime(
        "%s %s" % (SSA_DAY_STOP, SSA_TIME_STOP), "%d.%m.%Y %H:%M:%S"
    )
    assert dt_start_ <= dt_end_, tr("Datetime end must be lower than datetime start")

    td = datetime.timedelta(minutes=SSA_INTERVAL)
    while dt_start_ <= dt_end_:
        saver.save_shots(dt=dt_start_)
        dt_start_ += td
