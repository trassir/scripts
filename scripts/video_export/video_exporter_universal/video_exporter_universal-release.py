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

resources = {
    "ftp.py": """
        eNrVWv9v27gV/z1A/gdWh6By5ylJt2GH4DTsrpfegnXt0KQ43A6FKlt0rIss+iiqvszI/773
        SIoiKcp22hXYjKC1xfceyfceP+8LVa7WjAvCmuOjUn1diHVVzsxPseQ0L8r69vhowdmKLNp6
        LhirGqIJNjxfN3pwzqqKzkXJajNc0F9bOiV1vqKFaNcVPT4yspesEfjz+Ejw+4vjIwIfKWdJ
        qzXlRsYtFVnFbm8pPz6iv83pWpArOXLJOeM2I1LBWi3GV5KP5I0j5fhIfSOp9Tie4ECWfYSp
        YQtZBqPReXKenEUdfVLQWXsbRycN0VQX5KSJpiTLcIdZht8M/0Rt7lrkom1AWK+EOFIPgfPn
        qKE1Khi+RxQ3hF/ACpn50bTzOW2QOCrrDPTZ0ug9CG86wUpY/GmS9CoLuiBZwbKaiSXIiJ/l
        /LaZkmfP7jb4baLVvM6bxmLYgBhaz1lBs3UuljH+05GWC/CrBDdNUtBkLSI9gJ/e4t0HWWEv
        +B+oGUXGUSsWX+MCOxpt/fhdXSLB95JMesGU6GeXtXk2GcyAa8dvnIqW13IuazO8rbO8yZTL
        x4u644+i6G1bK9cHw6IzKRoYQGak+as8B8ikfqNAkDemRqkC2K05XsmNmlUAFRXpop4SpE8V
        u2JOtQxLRFLkdAVLSskNb6k9AM7BRWzR6j2LbsX6NyxSqWBegXrIy5t/St3Fl1LVsN2h5RXl
        iyWd371gda1OvOLq2MeYXor1u3XF8uKG5/M7ynsNq8dkzdktBxclkt5SsLRQVtalyLK4odVi
        SkTe3GW3bVlMyaKslAdOyaxi87usKf9Ns9m9oI7KkS+RQxteCkFRcWfJmUcAM4usWbJNnQEM
        zWmNlvKJzORoxe67R+MvBUj9R75UJvJKDgMtnB55GsAh8Ek8OG1m15OJq6Z5XlVGTTtcEPT7
        t7wuKkDCBeOkEYzPyjrn9504/FxTSr6tGuadpqUQ6+bi9LRgc1jnvViyOmH89vT5KcQPDjJO
        VShJlmJVfaW/g38k9izWQnZZ6XdpWKE9jzZUNmcrwFeB6uOsrYs4Hko79XU9Ic/I+dnZxN41
        oNeYMzxJB9N5uhl3I5/R5fOjjI4ursNNB0Im3gl+UZUwHLPZL3A2O3vfXP3j8s27G1jDufbl
        66vXP7y6vHnz2oGP7169efH37PrqX5fZdz/dXF5Lhud/VINZdvX66ubyexkcX+ZVQ4Pn07Xl
        tP+JId/6iVE6fX5uPWkbytMor1l9v2IYIC1i2N2mSCP72Ybxu6woefqa1dR6jgdgBgjjP5ch
        L1vlv1W0TsHkZzYPAhrotEO0FHXizV9+BG44f/aYd6BA/wBeaAAiGMGQLNGpsZ3rWziH/nEC
        zZC4EQCdiJI6OXLCF6Y0cVmLKWESmfNK0+LIFC2Qt5W4IB+en5MPLi+qVUof8OIIxmib39L/
        h2EI3RTjkhQB44URB9J8IZ3RwmJwFHM4IAA7MH5viUJresI6S5MYv+WzijoSr1VKhHFlLsOK
        Jre3G5Bq+8lQ551QSUWA5BYDTy8QHctfpudcJJ5BFu1IlQGVWCTwJ6O4zL59K3SeGBB0WaMa
        yFNN9pRIOgC0j3lFSkheXL+WH8j6KN+UDQW9N5Jdc0tme3Po+R9sZ34hYScXgpezFkDZc+wO
        d1CLuMt+f6JcUdYKUsI+IZOri8ZVoqfCHq7klo3GMM+sq3v4BzZZg8bqOSVzyKYELQILD4ac
        Du37OSAsqkc95Hkbk1l1tmpuAQpjT50o/yfWEoD/tioIwiJpwI6VtUS2INt51cjK4eGbGf9L
        FBCCUZkKizCxUVsiMC7+Hua6q9mGbJa5gMyRyicFgymfPPHkThKI9atcxJ3MVO9Txo8sS7pi
        ZuLy8RzdAzJhtJtK94wKLFITfxInWKgA4wX5TKJe6oGdGpJwl0ps84ck0qQScAZcCqBSjVT+
        sIGe1KBQSII5XKlz1gbrVwCQqio31mHFxo7JcMuQCQEHYs5gzGBZ2sMaOIBVlg3FyW2g5U08
        7sadZAKJ/fzGx6RQEuPTxF6myema60zTjoPBUxF9sx3xtIfY89Fo2/vHE/4A9ao3LjOHbe8p
        QSKZTGx7nwlLUmnFdlkWBa21AwUpTbKxdZ0pSGwykK1j2gClk5Ns7V+j6zVpyHbosw8+w8QG
        FnP4h7ZOvVwNP45S0uhZBJkyLCy2D9tkOh470/6YJOqJRTwsTsFtbPcaOJ/vZoDhJgYAwq4Z
        qAFjFyRemstB+WHTQR3GvjiJJ4PxREuKe4+cWhA17cKY2qqOdgExcBzLTnHojFMHsQIMgPs4
        +DEe2njYEtFbwLpPgnKDXQr4dhHC8GDpDsSTYUA0Tu4JGqrSqGtTxC6rtzd3xSqEQEWzGpG3
        utsjb+fEPSmS/NqWwkMw7P/t8TA9Cgkf+BWIsaW+lY7bDN1KO5TKaVUlNpJ7uEXfD1TIqfo1
        JUli98D+f5x4nw+N+9HBvvRIf3qUTx28CCSSbRm0W0qwa/n7r6NPPdABl2DCLgu6Jq6fnikI
        lf4ZVk0PDhfB6TY5r7H1G73I66eyey5dq586mqJEKPIXTBbA3gq6Zp85W/OKNXTf6UIaf57x
        44Hkjzwexg1xEih/IJWS6dejvNFISOSm4hF/8RbbG01yFWO26211sVOuZyEp9DD7LEqoDav7
        UIoXyEil9bB1kWHrYme71ZwJ16zXpsknicmmFEs1nQeggVZI31rV/ZAbeEDc/qrak16F6Zu0
        VaWmU519m9hpOgDtj/AbewxYZTtnxq8LDeO461hVRdezrSHLkj3aQE13un2Av6jLxLzKBBL+
        6DSyFOtVb4fEYctbAbw+Pw738hA5d2Dm6MS2J4LV1K2Q0dYsB2eDR1ZH22oJypuBTKgbA6xz
        vEuEOOyZci1+N9OSK12SrSGb3dFYh/ybz6IJZlNIStWJGDtGVm87ZPjrmzdvsaNLTnotTG25
        I4ueejoYeIS+g3JvsLyjDHoKwO+16U9iG0bdCO5OmTs4lbQBX/HhdgRqHb0R3d/3szHHcUIT
        jAhWNx2dVFV+rNm6ogsxhtxf9UzbMQqpM+Mb0YXlbTtZOF0xQfEkAE//YzdTVzECi2la7mQw
        pwA4+hMxxvIQUi1+AtgOOlHK+dna/fupeWjt731YaN92te/NOn6zVUtmv5v3Yysd3Mnr+2+5
        BX11YkGDuT0NS1PX1RKOykaGvV33bSOOh5/xJKL7YPqd6Iw7Pj87m5IqX82KvLe0DWnqmj/R
        m5tMdstWR6OP3Xui9pdYqMpxdi30wLx0p8F3k+IHayk9FaZgmyVmBmAdXcnJq5kTKGHy9bpD
        QXyuQHC6X/6+0+/tuM/L9tAfYmGFaWrl8eC9gHHHGKTkj/GA/ds81EfMWymTz1LFF1pd927M
        /sXtdXHzGkXXj0HsXd9XZS0uuquW9MezP5/94SDXlzo7yPUhU23rpbzcLwaHoAPKE/4/7Odf
        yLgHul2YgFYN3QFSfpn2EpV9wmXdsMDXESILhXes4RFb/29tO7hlZx1/wpn68EIH9URYN/uu
        KVy6XfgUrJC7g9F5eBy9C7g95LZ60bLVoF/f8jawR+ufo2mn54gL0TW1FZL7JEq9tOC9w9Bn
        MvK3l8bvqaiHlXK4SO7XMLybfyvHpPqcWzP87LmEf9m9OSfwdhJJEHw2S1pbKVtdNkvqVfhu
        J8CRaXoC1hWvNCAH47OV5HLrh7fY+/Y1c/VGvUSK6Z9MAMxRHdUvUCLRpyeLqgmvZ9Yg8fSk
        eWrBRFchapxwJu+VEq6u7Ax7t0ZG7hudCyubfqxCOqgmOrAKOqDu2VvpPIQvagfp0sCmLlaF
        kUaXG9f4ZgZRmOIDyQDy3JczexJdl9sYNwTRxycq3koV7uUVYt59935N5Oy/ezm0f5HxPydS
        l0U=
    """,
    "helpers.py": """
        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
        wYTfceCLK89o/wEf6+v+
    """,
    "video_exporter.py": """
        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
        86V0fPR/NheSRw==
    """,
}
t1utils.resources_check(script_path, resources)

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
