# -*- coding: utf-8 -*-
# VideoExporterUniversal v3.1.2
"""
<parameters>
    <company>DSSL</company>
    <authors>d.gavrilov, a.trubilin</authors>
    <title>video_exporter_universal</title>
    <version>3.1.2</version>

    <parameter>
        <type>caption</type>
        <name>Настройки скрипта</name>
    </parameter>
    <parameter>
        <id>SELECTED_SERVER</id>
        <type>server</type>
        <name>Сервер с каналами</name>
        <value></value>
    </parameter>
    <parameter>
        <id>SELECTED_CHANNELS</id>
        <type>objects</type>
        <name>Каналы</name>
    </parameter>
    <parameter>
        <id>SAVE_FOLDER</id>
        <type>string</type>
        <name>Сохранить в папку</name>
        <value>{server_name}/%Y.%m.%d/{channel_name}</value>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Режим отладки</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Экспорт видео</name>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>EXPORT_ACTIVATE</id>
        <name>Режим работы</name>
        <value>Разовый экспорт</value>
        <string_list>Разовый экспорт,Ежедневный экспорт</string_list>
    </parameter>
    <parameter>
        <id>EXPORT_WEEKDAYS</id>
        <type>string</type>
        <name>Дни недели для ежедневного экспорта</name>
        <value>1,2,3,4,5,6,7</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>PREFER_SUBSTREAM</id>
        <name>Экспортировать субпоток</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>IS_HARDWARE</id>
        <name>Архив с HDD устройства</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>date</type>
        <id>EXPORT_DATE_START</id>
        <name>Дата начала экспортируемого фрагмента</name>
        <value>21.04.2020</value>
    </parameter>
    <parameter>
        <type>time</type>
        <id>EXPORT_TIME_START</id>
        <name>Время начала экспортируемого фрагмента</name>
        <value>10:00:00</value>
    </parameter>
    <parameter>
        <type>date</type>
        <id>EXPORT_DATE_END</id>
        <name>Дата окончания экспортируемого фрагмента</name>
        <value>21.04.2020</value>
    </parameter>
    <parameter>
        <type>time</type>
        <id>EXPORT_TIME_END</id>
        <name>Время окончания экспортируемого фрагмента</name>
        <value>10:01:00</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Настройка отправки</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>FTP</id>
        <name>Отправить на FTP</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>REMOVE</id>
        <name>Удалить после отправки</name>
        <value>False</value>
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
        <min>10</min>
        <max>99999</max>
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
        <value>/trassir/exported/</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>FTP_PASSIVE_MODE</id>
        <name>Пассивный режим FTP</name>
        <value>True</value>
    </parameter>
    <resources>
        <resource>ftp.py</resource>
        <resource>helpers.py</resource>
        <resource>video_exporter.py</resource>
    </resources>
</parameters>
"""

GLOBALS = globals()
# Script settings
SELECTED_SERVER = GLOBALS.get("SELECTED_SERVER", "")
SELECTED_CHANNELS = GLOBALS.get("SELECTED_CHANNELS", "")
SAVE_FOLDER = GLOBALS.get("SAVE_FOLDER", "{server_name}/%Y.%m.%d/{channel_name}")
DEBUG = GLOBALS.get("DEBUG", False)
# Export settings
EXPORT_ACTIVATE = GLOBALS.get("EXPORT_ACTIVATE", "Разовый экспорт")
EXPORT_WEEKDAYS = GLOBALS.get("EXPORT_WEEKDAYS", "1,2,3,4,5,6,7")
PREFER_SUBSTREAM = GLOBALS.get("PREFER_SUBSTREAM", False)
IS_HARDWARE = GLOBALS.get("IS_HARDWARE", False)
EXPORT_DATE_START = GLOBALS.get("EXPORT_DATE_START", "01.06.2020")
EXPORT_DATE_END = GLOBALS.get("EXPORT_DATE_END", "04.06.2020")
EXPORT_TIME_START = GLOBALS.get("EXPORT_TIME_START", "10:00:00")
EXPORT_TIME_END = GLOBALS.get("EXPORT_TIME_END", "10:01:00")
# FTP
FTP = GLOBALS.get("FTP", False)
REMOVE = GLOBALS.get("REMOVE", False)
FTP_HOST = GLOBALS.get("FTP_HOST", "172.20.0.10")
FTP_PORT = GLOBALS.get("FTP_PORT", 21)
FTP_USER = GLOBALS.get("FTP_USER", "trassir")
FTP_PASSWORD = GLOBALS.get("FTP_PASSWORD", "12345")
FTP_WORK_DIR = GLOBALS.get("FTP_WORK_DIR", "/trassir/exported/")
FTP_PASSIVE_MODE = GLOBALS.get("FTP_PASSIVE_MODE", True)

import os
from datetime import datetime, timedelta

import host

import helpers

helpers.set_script_name()
logger = helpers.init_logger("video_exporter_universal", debug=DEBUG)

from video_exporter import VideoExporter, status
from ftp import FTPClient, status as ftp_status

if not SELECTED_SERVER:
    raise ValueError("Server not selected")
if not SELECTED_CHANNELS:
    raise ValueError("No channels selected")

DELETE_EMPTY_FOLDERS = "{server_name}" in SAVE_FOLDER
if REMOVE and not DELETE_EMPTY_FOLDERS:
    logger.warning(
        "Folder path does not start with the server name, empty folders will not be deleted."
    )

DT_START = datetime.strptime(EXPORT_DATE_START + EXPORT_TIME_START, "%d.%m.%Y%H:%M:%S")
DT_END = datetime.strptime(EXPORT_DATE_END + EXPORT_TIME_END, "%d.%m.%Y%H:%M:%S")
SELECTED_CHANNELS = SELECTED_CHANNELS.split(",")

SERVER_NAME = host.settings("/{}".format(SELECTED_SERVER)).name


def _win_encode_path(path):
    if os.name == "nt":
        try:
            path = path.decode("utf8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return path


class VideoSaver:
    default_shots_folder = host.settings("system_wide_options")["screenshots_folder"]
    full_channels_guid = {}

    def __init__(
        self,
        server_guid,
        server_name,
        selected_channels,
        folder_tmpl,
        remove_file,
        prefer_substream,
        is_hardware,
    ):
        self.server_guid = server_guid
        self.server_name = server_name
        self.selected_channels = selected_channels
        self.ve = VideoExporter(callback=self.video_export_callback)
        self.folder_tmpl = folder_tmpl
        self.prefer_substream = prefer_substream
        self.is_hardware = is_hardware
        self.ftp = None
        self.ftp_add_relative_path = False
        self.remove_file = remove_file
        self.delete_empty_folders = False
        self.working_tasks = {}

    def get_full_channels_guid(self):
        for sett in host.settings("/%s/channels" % self.server_guid).ls():
            if sett.type == "Channel" and sett.name in self.selected_channels:
                self.full_channels_guid[sett.name] = "{}_{}".format(
                    sett.guid, self.server_guid
                )
        logger.debug(self.full_channels_guid)

    def __get_folder(self, channel, dt=None):
        if dt is None:
            dt = datetime.now()
        folder = dt.strftime(
            self.folder_tmpl.format(channel_name=channel, server_name=self.server_name)
        )
        logger.debug("Folder: %s" % folder)
        return folder

    def ftp_callback(self, task_guid, state):
        logger.debug("%s: ftp %s", task_guid, state)
        if state in (ftp_status.success, ftp_status.error):
            task = self.working_tasks.pop(task_guid, None)
            host.stats()["run_count"] -= 1
            if task and self.remove_file:
                try:
                    os.remove(_win_encode_path(task["path"]))
                    logger.debug("remove file %s", task["path"])
                except:
                    logger.exception("Unhandled exception while removing file", task)
                if not host.stats()["run_count"] and self.delete_empty_folders:
                    self._remove_all_empty_folders()

    def _remove_all_empty_folders(self):
        _work_dir = os.path.join(self.default_shots_folder, self.server_name)
        for dir_path, dir_names, file_names in os.walk(_work_dir, topdown=False):
            for dir_name in dir_names:
                try:
                    os.rmdir(_win_encode_path(os.path.join(dir_path, dir_name)))
                    logger.debug("remove folder %s", dir_name)
                except OSError:
                    logger.debug(
                        "can't remove folder %s, because it is not empty", dir_path
                    )

    def video_export_callback(self, task_guid, state):
        logger.debug("%s: video %s", task_guid, state)
        if state == status.success:
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
                else:
                    self.ftp_callback(task_guid, ftp_status.success)
        elif state == status.error:
            self.working_tasks.pop(task_guid, None)
            logger.warning("Can't save file %s" % task_guid)

    def video_export(self, dt_start, dt_end):
        paths = []
        self.get_full_channels_guid()
        for (
            key,
            value,
        ) in (
            self.full_channels_guid.iteritems()
        ):  # "ChannelName": "ChannelGuid_ServerGuid"
            host.stats()["run_count"] += 1
            folder = self.__get_folder(key, dt_start)
            file_path = os.path.join(self.default_shots_folder, folder)
            task_guid, path = self.ve.export(
                value,
                dt_start,
                dt_end,
                prefer_substream=self.prefer_substream,
                file_path=file_path,
                options={"is_hardware": self.is_hardware},
            )
            self.working_tasks[task_guid] = {
                "path": path,
                "folder": folder,
            }
            logger.debug("%s: task created (%s)", task_guid, path)
            paths.append(path)
        return paths


saver = VideoSaver(
    SELECTED_SERVER,
    SERVER_NAME,
    SELECTED_CHANNELS,
    SAVE_FOLDER,
    REMOVE,
    PREFER_SUBSTREAM,
    IS_HARDWARE,
)
saver.delete_empty_folders = DELETE_EMPTY_FOLDERS

if FTP:
    saver.ftp = FTPClient(
        FTP_HOST,
        port=FTP_PORT,
        user=FTP_USER,
        passwd=FTP_PASSWORD,
        work_dir=FTP_WORK_DIR,
        passive_mode=FTP_PASSIVE_MODE,
    )
    saver.ftp_add_relative_path = FTP_WORK_DIR

if EXPORT_ACTIVATE == "Разовый экспорт":
    if DT_START > DT_END:
        raise ValueError("Export start time exceeds export end time")
    else:
        saver.video_export(DT_START, DT_END)

else:

    class EveryDayExporter:

        _DELAY = timedelta(seconds=15)  # sec
        _day = timedelta(days=1)

        def __init__(self, dt_start, dt_end, weekdays=None):
            dt_now = datetime.now()

            self.weekdays = weekdays
            self.dt_start = dt_start.replace(
                year=dt_now.year, month=dt_now.month, day=dt_now.day
            )
            self.dt_end = dt_end.replace(
                year=dt_now.year, month=dt_now.month, day=dt_now.day
            )

            if self.dt_end <= self.dt_start:
                self.dt_end += self._day

        def start(self):
            now = datetime.now()
            if now - self.dt_end > self._DELAY:
                if self.weekdays:
                    weekday = now.weekday() + 1
                    if weekday in self.weekdays:
                        saver.video_export(self.dt_start, self.dt_end)
                else:
                    saver.video_export(self.dt_start, self.dt_end)

                self.dt_start += self._day
                self.dt_end += self._day
                host.timeout(120 * 1000, self.start)
            else:
                host.timeout(60 * 1000, self.start)

    weekdays = set()
    for d in EXPORT_WEEKDAYS.split(","):
        try:
            day = int(d)
        except ValueError:
            raise ValueError("Expected int for weekdays, got %s" % d)

        if 1 <= day <= 7:
            weekdays.add(day)
        else:
            raise ValueError("Weekday must be in [1, 7]")

    every_day_exporter = EveryDayExporter(DT_START, DT_END, weekdays=weekdays)
    every_day_exporter.start()
