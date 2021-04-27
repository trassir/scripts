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
    "schedule.py": """
        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
        4J8=
    """,
}
t1utils.resources_check(script_path, resources)

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
