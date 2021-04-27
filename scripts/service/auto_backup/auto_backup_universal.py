# -*- coding: utf-8 -*-
# auto_backup_universal v1.1.0
"""
<parameters>
    <company>DSSL</company>
    <author>d.gavrilov</author>
    <title>auto_backup_universal</title>
    <version>1.1.0</version>

    <parameter>
        <type>caption</type>
        <name>Schedule settings</name>
    </parameter>
    <parameter>
        <id>WORK_MODE</id>
        <name>Work mode</name>
        <type>string_from_list</type>
        <string_list>weekly,monthly</string_list>
        <value>weekly</value>
    </parameter>
    <parameter>
        <id>DAYS</id>
        <type>string</type>
        <name>Working days</name>
        <value>1,2,3,4,5,6,7</value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>SCHEDULE_TIME</id>
        <name>Save at(hours:minutes)</name>
        <value>10:00</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Script settings</name>
    </parameter>
    <parameter>
      <type>string</type>
      <id>BACKUP_SAVE_DIR</id>
      <name>Backup save directory</name>
      <value>default</value>
    </parameter>
    <parameter>
        <id>DELETE_BACKUP</id>
        <name>Delete backup after send</name>
        <type>boolean</type>
        <value>True</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>DEBUG</id>
        <name>Debug mode</name>
        <value>False</value>
   </parameter>

    <parameter>
        <type>caption</type>
        <name>E-mail settings</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SEND_EMAIL</id>
        <name>Send backup on e-mail</name>
        <value>True</value>
   </parameter>
    <parameter>
        <id>EMAIL_ACCOUNT</id>
        <name>Email account name</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <id>EMAIL_SUBSCRIBERS</id>
        <name>Email subscribers</name>
        <type>string</type>
        <value></value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>FTP Settings</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SEND_FTP</id>
        <name>Send backup on FTP</name>
        <value>False</value>
   </parameter>
    <parameter>
        <id>FTP_HOST</id>
        <name>Host</name>
        <type>string</type>
        <value>127.0.0.1</value>
    </parameter>
    <parameter>
        <id>FTP_PORT</id>
        <type>integer</type>
        <name>Port</name>
        <value>21</value>
        <min>1</min>
        <max>999999</max>
    </parameter>
    <parameter>
        <id>FTP_LOGIN</id>
        <name>Username</name>
        <type>string</type>
        <value>trassir</value>
    </parameter>
    <parameter>
        <id>FTP_PASS</id>
        <name>Password</name>
        <type>string</type>
        <value>12345</value>
    </parameter>
    <parameter>
        <id>FTP_WD</id>
        <name>Working directory</name>
        <type>string</type>
        <value>/trassir_backup</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>FTP_PASSIVE_MODE</id>
        <name>Passive mode</name>
        <value>True</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>FTP_CHECK_CONNECTION</id>
        <name>Check connection</name>
        <value>False</value>
    </parameter>

    <resources>
        <resource>email_sender.py</resource>
        <resource>ftp.py</resource>
        <resource>schedule.py</resource>
    </resources>
</parameters>
"""

GLOBALS = globals()

# Schedule settings
WORK_MODE = GLOBALS.get("WORK_MODE", "weekly")
DAYS = GLOBALS.get("DAYS", "1,2,3,4,5,6,7")
SCHEDULE_TIME = GLOBALS.get("SCHEDULE_TIME", "10:00")

# Script settings
BACKUP_SAVE_DIR = GLOBALS.get("BACKUP_SAVE_DIR", "default")
DELETE_BACKUP = GLOBALS.get("DELETE_BACKUP", True)
DEBUG = GLOBALS.get("DEBUG", False)

# E-mail settings
SEND_EMAIL = GLOBALS.get("SEND_EMAIL", True)
EMAIL_ACCOUNT = GLOBALS.get("EMAIL_ACCOUNT", "")
EMAIL_SUBSCRIBERS = GLOBALS.get("EMAIL_SUBSCRIBERS", "")

# FTP Settings
SEND_FTP = GLOBALS.get("SEND_FTP", False)
FTP_HOST = GLOBALS.get("FTP_HOST", "127.0.0.1")
FTP_PORT = GLOBALS.get("FTP_PORT", 21)
FTP_LOGIN = GLOBALS.get("FTP_LOGIN", "trassir")
FTP_PASS = GLOBALS.get("FTP_PASS", "12345")
FTP_WD = GLOBALS.get("FTP_WD", "/trassir_backup")
FTP_PASSIVE_MODE = GLOBALS.get("FTP_PASSIVE_MODE", True)
FTP_CHECK_CONNECTION = GLOBALS.get("FTP_CHECK_CONNECTION", False)

import os
import zipfile
import datetime
import host
import schedule
from email_sender import EmailSender
from ftp import FTPClient, status as ftp_status

SETTINGS_NAME = host.settings("").name
WORKING_TASKS = {}

ftp = None
mail = None


def _win_encode_path(path):
    if os.name == "nt":
        try:
            path = path.decode("utf8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return path


def write_log(row, debug=False):
    if debug:
        host.log_message(row)


def check_days_range(day, start, end):
    if start <= day <= end:
        return True
    else:
        raise ValueError("Day must be in range [%d, %d]" % (start, end))


def collect_working_days(selected_days, mode):
    if not selected_days:
        raise ValueError("Working days not selected")

    days = set()
    for day in selected_days.split(","):
        try:
            day = int(day)
        except ValueError:
            raise ValueError("Expected int for days, got %s" % day)

        if mode == "weekly":
            if check_days_range(day, 1, 7):
                days.add(day)

        else:
            if check_days_range(day, 1, 31):
                days.add(day)
    write_log("mode: %s, work days --> %s, " % (mode, days), debug=DEBUG)

    return days


WORK_DAYS = collect_working_days(DAYS, WORK_MODE)


def backup_work_directory(folder_name):
    screenshots_folder = host.settings("system_wide_options")["screenshots_folder"]
    if folder_name in ["default", ""]:
        work_dir = screenshots_folder
    else:
        work_dir = os.path.join(screenshots_folder, folder_name)
        if not os.path.isdir(work_dir):
            try:
                os.mkdir(work_dir)
            except:
                raise IOError("Backup dir creation error: %s", work_dir)
    write_log("Backup work directory %s" % work_dir, debug=DEBUG)
    return work_dir


BACKUP_WORK_FOLDER = backup_work_directory(BACKUP_SAVE_DIR)


def _client(settings_directory):
    settings_path = os.path.join(settings_directory, "_t1client.settings")
    return settings_path, None


def _server(settings_directory):
    settings_path = os.path.join(settings_directory, "_t1server.settings")
    license_path = os.path.join(settings_directory, " Trassir 3 License.txt")
    return settings_path, license_path


def get_settings_path():
    if os.name == "nt":
        settings_directory = os.getcwd()
        if host.settings("").guid == "client":
            settings_path, license_path = _client(settings_directory)
        else:
            settings_path, license_path = _server(settings_directory)
    else:
        if host.settings("health")["architecture"] == "x86_64":
            settings_directory = "/home/trassir"
            settings_path, license_path = _server(settings_directory)
        else:
            # ARM
            settings_path = os.path.join("/data/userdata/", "_t1server.settings")
            license_path = os.path.join("/data/", " Trassir 3 License.txt")
    return settings_path, license_path


SETTINGS_PATH, LICENSE_PATH = get_settings_path()


def create_backup():
    backup_name = "{name}_{dt}_backup.zip".format(
        name=SETTINGS_NAME, dt=datetime.datetime.today().strftime("%d-%m-%Y_%H%M%S")
    )
    path_to_backup_zip = os.path.join(BACKUP_WORK_FOLDER, backup_name)
    with zipfile.ZipFile(path_to_backup_zip, "w") as _file:
        if LICENSE_PATH:
            _file.write(SETTINGS_PATH, arcname="_t1server.settings")
            _file.write(LICENSE_PATH, arcname=" Trassir 3 License.txt")
        else:
            _file.write(SETTINGS_PATH, arcname="_t1client.settings")
    return path_to_backup_zip


def remove_backup(backup_path):
    if os.path.isfile(backup_path):
        try:
            os.remove(backup_path)
            write_log("remove file %s" % backup_path, debug=DEBUG)
        except:
            write_log(
                "Unhandled exception while removing file %s" % backup_path, debug=DEBUG
            )
    else:
        write_log("%s is not exists" % backup_path, debug=DEBUG)


def ftp_callback(task_guid, state):
    write_log("%s: ftp %s" % (task_guid, state), debug=DEBUG)
    if state in (ftp_status.success, ftp_status.error):
        task = WORKING_TASKS.pop(task_guid, None)
        host.stats()["run_count"] -= 1
        if task and state == ftp_status.success:
            if DELETE_BACKUP:
                remove_backup(_win_encode_path(task))

        elif state == ftp_status.error:
            WORKING_TASKS.pop(task_guid, None)
            write_log("Can't send file %s" % task_guid, debug=DEBUG)


def total_days_in_month(date):
    total_days = (
        date.replace(month=date.month % 12 + 1, day=1) - datetime.timedelta(days=1)
    ).day
    return total_days


def push_backup(backup_path):
    if backup_path:
        if not mail and not ftp:
            return
        if mail:
            mail.send(
                EMAIL_SUBSCRIBERS,
                attachments=[backup_path],
                subject="{name} -> AutoBackup Universal".format(name=SETTINGS_NAME),
            )
        if ftp:
            task_guid = host.random_guid()
            WORKING_TASKS[task_guid] = backup_path
            host.stats()["run_count"] += 1
            ftp.send(backup_path, task_guid=task_guid)
        if DELETE_BACKUP and not ftp:
            remove_backup(_win_encode_path(backup_path))


def check_current_day():
    count = 0
    total_month_days = total_days_in_month(datetime.datetime.now())

    if WORK_MODE == "weekly":
        current_day = datetime.datetime.today().isoweekday()
    else:
        current_day = datetime.datetime.today().day

    if current_day in WORK_DAYS:
        push_backup(create_backup())

    else:
        if current_day == total_month_days:
            for day in WORK_DAYS:
                if day > current_day and not count:
                    count += 1
                    push_backup(create_backup())


if __name__ == host.stats().parent().guid:
    if SEND_FTP:
        ftp = FTPClient(
            host=FTP_HOST,
            port=FTP_PORT,
            user=FTP_LOGIN,
            passwd=FTP_PASS,
            work_dir=FTP_WD,
            callback=ftp_callback,
            check_connection=FTP_CHECK_CONNECTION,
            passive_mode=FTP_PASSIVE_MODE,
        )
    if SEND_EMAIL:
        EMAIL_SUBSCRIBERS = EmailSender.parse_mails(EMAIL_SUBSCRIBERS)
        mail = EmailSender(EMAIL_ACCOUNT)

    schedule.every().day.at(SCHEDULE_TIME).do(check_current_day)
    schedule.run_continuously()
