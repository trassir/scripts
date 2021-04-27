# -*- coding: utf-8 -*-
# users_rights_for_channels v1.0.1
"""
<parameters>
    <company>DSSL</company>
    <author>d.gavrilov</author>
    <title>users_rights_for_channels</title>
    <version>1.0.1</version>
    <parameter>
        <type>caption</type>
        <name>Main settings</name>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Folder path</name>
        <id>FOLDER_PATH</id>
        <value>default</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Other settings</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>DEBUG</id>
        <name>Debug mode</name>
        <value>False</value>
   </parameter>
    <resources>
        <resource>helpers.py</resource>
        <resource>localization/report.py</resource>
        <resource>localization/__init__.py</resource>
    </resources>
</parameters>
"""
GLOBALS = globals()
# Main settings
FOLDER_PATH = GLOBALS.get("FOLDER_PATH", "default") or None

# Other settings
DEBUG = GLOBALS.get("DEBUG", False)

import helpers

helpers.set_script_name()
logger = helpers.init_logger("user_rights_for_channels", debug=DEBUG)

import host
import os
import re
from datetime import datetime
import xlsxwriter
from __builtin__ import object
import localization as loc

shot_path = host.settings("system_wide_options")["screenshots_folder"]
host.stats()["run_count"] = 0


def _win_encode_path(path):
    if os.name == "nt":
        try:
            path = path.decode("utf8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return path


if FOLDER_PATH in ["default", None]:
    FOLDER_PATH = shot_path
else:
    if not os.path.isdir(_win_encode_path(FOLDER_PATH)):
        raise ValueError("Folder not found -> %s" % FOLDER_PATH)
    else:
        FOLDER_PATH = _win_encode_path(FOLDER_PATH)


class UserRightsChecker(object):
    max_bit = 32
    alc_regexp = re.compile(r"([\w/]+),(\d+)")

    def __init__(self, user_settings):
        assert user_settings
        assert user_settings.type == "User"
        self.__user_settings = user_settings
        self._base_rights = self.parse(user_settings["base_rights"], self.max_bit)
        self._acl_rights = self.collect_acl_rights(user_settings["acl"])
        self._group_acl_rights = None
        if user_settings.group_acl:
            self._group_acl_rights = self.collect_acl_rights(user_settings.group_acl)

    def collect_acl_rights(self, settings):
        acl_rights = {}
        if settings:
            for match in self.alc_regexp.finditer(settings):
                acl_rights[match.group(1)] = self.parse(match.group(2), 64)
        return acl_rights

    @classmethod
    def parse(cls, value, max_bits=32):
        return [
            bool(int(bit)) for bit in reversed(format(int(value), "0%sb" % max_bits))
        ]

    def _check(self, access, acl, check_path, key, key_):
        if access:
            access = not acl[check_path][key_]
        else:
            access = acl[check_path][key]
        return access

    def check_rights(self, setting_path, key):
        access = self._base_rights[key]
        key_ = key + 32
        split_setting_path = setting_path.split("/")[1:]
        check_path = ""
        for path in split_setting_path:
            check_path += "/%s" % path
            if self._group_acl_rights and check_path in self._group_acl_rights:
                access = self._check(
                    access, self._group_acl_rights, check_path, key, key_
                )

            if check_path in self._acl_rights:
                access = self._check(access, self._acl_rights, check_path, key, key_)
        return access

    def check_view_rights(self, setting_path):
        return self.check_rights(setting_path, 0)

    def check_archive_rights(self, setting_path):
        return self.check_rights(setting_path, 1)

    def check_modify_rights(self, setting_path):
        return self.check_rights(setting_path, 2)

    def check_setup_rights(self, setting_path):
        return self.check_rights(setting_path, 3)

    def check_bookmark_rights(self, setting_path):
        return self.check_rights(setting_path, 5)

    def check_users_and_script_rights(self, setting_path):
        return self.check_rights(setting_path, 6)

    def check_archive_export(self, setting_path):
        return self.check_rights(setting_path, 8)

    def check_ptz_rights(self, setting_path):
        return self.check_rights(setting_path, 9)

    def check_sound_rights(self, setting_path):
        return self.check_rights(setting_path, 10)

    @property
    def check_archive_speed_limit(self):
        return self.__user_settings["archive_speed_limit"]

    @property
    def check_ptz_priority(self):
        return self.__user_settings["ptz_priority"]


def collect_users():
    logger.debug("collect users")
    all_users = []
    for user in host.settings("users").ls():
        if user.type == "User" and user.name not in ("Admin", "Script"):
            user.group_acl = None
            if user["group"]:
                user.group_acl = host.settings("users/%s" % user["group"])["acl"]
            user.rights = UserRightsChecker(user)
            all_users.append(user)
    return all_users


def _check_permission(server):
    try:
        channels = server.cd("channels")
        for channel in channels.ls():
            channel_name = channel.name
            break
        return channels
    except ValueError:
        logger.warning("exception:", exc_info=True)


def generate_xlsx_report(folder_path):
    logger.debug("Starting create report...")
    try:
        xlsx_report_path = os.path.join(
            folder_path,
            "Users rights for channels %s .xlsx"
            % datetime.now().strftime("%Y.%m.%d %H-%M-%S"),
        )
        _row = 0
        workbook = xlsxwriter.Workbook(xlsx_report_path)
        worksheet = workbook.add_worksheet()
        header_format = workbook.add_format({"bold": True, "align": "center"})
        row_format = workbook.add_format({"align": "center", "valign": "vcenter"})
        headers_list = [
            loc.report.username,
            loc.report.server_name,
            loc.report.channel_name,
            loc.report.view,
            loc.report.archive,
            loc.report.sound,
            loc.report.ptz,
            loc.report.modify,
            loc.report.setup,
        ]

        for row_num, header in enumerate(headers_list):
            worksheet.write(0, row_num, header, header_format)

        users = collect_users()
        _row += 1
        for server in host.settings("/").ls():
            if server.type in ("LocalServer", "RemoteServer"):
                channels = _check_permission(server)
                if channels:
                    for channel in channels.ls():
                        if (
                            channel.type == "Channel"
                            and not channel["archive_zombie_flag"]
                        ):
                            host.stats()["run_count"] += 1
                            for user in users:
                                worksheet.write(_row, 0, user.name, row_format)
                                worksheet.write(_row, 1, server.name, row_format)
                                worksheet.write(_row, 2, channel.name, row_format)
                                worksheet.write(
                                    _row,
                                    3,
                                    str(user.rights.check_view_rights(channel.path)),
                                    row_format,
                                )
                                worksheet.write(
                                    _row,
                                    4,
                                    str(user.rights.check_archive_rights(channel.path)),
                                    row_format,
                                )
                                worksheet.write(
                                    _row,
                                    5,
                                    str(user.rights.check_sound_rights(channel.path)),
                                    row_format,
                                )
                                worksheet.write(
                                    _row,
                                    6,
                                    str(user.rights.check_ptz_rights(channel.path)),
                                    row_format,
                                )
                                worksheet.write(
                                    _row,
                                    7,
                                    str(user.rights.check_modify_rights(channel.path)),
                                    row_format,
                                )
                                worksheet.write(
                                    _row,
                                    8,
                                    str(user.rights.check_setup_rights(channel.path)),
                                    row_format,
                                )
                                _row += 1
        worksheet.freeze_panes(1, 0)
        worksheet.autofilter("A1:I%d" % _row)
        worksheet.set_column("A:C", 20)
        workbook.close()
        logger.debug("Report success exported to %s" % xlsx_report_path)
        raise ValueError("Report success exported to %s" % xlsx_report_path)
    except OSError as err:
        logger.warning("exception:", exc_info=True)
        raise err


generate_xlsx_report(FOLDER_PATH)
