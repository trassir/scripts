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
