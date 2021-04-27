# -*- coding: utf-8 -*-
# This script set new parameters in nvr-system-settings.ini
#
# Script is available only for TrassirOS
#
# Version: 2.1
# Author: A.A.Trubilin, DSSL
# E-mail: a.trubilin@dssl.ru
"""
<parameters>
    <company>AATrubilin</company>
    <title>nvr-system-settings</title>
    <version>2.1</version>
</parameters>
"""

import os
import ConfigParser as configparser

from __builtin__ import object as py_object

import host


class ResultMessage(Exception):
    pass


class TrassirConfigParser(configparser.ConfigParser):
    def write(self, fp):
        """Write an .ini-format representation of the configuration state.

        Redefines parent method to write without spaces around the equal sign.
        Not sure that it's important, but trassir saves settings without spaces.
        """
        if self._defaults:
            fp.write("[%s]\n" % configparser.DEFAULTSECT)
            for (key, value) in self._defaults.items():
                fp.write("%s=%s\n" % (key, str(value).replace("\n", "\n\t")))
            fp.write("\n")
        for section in self._sections:
            fp.write("[%s]\n" % section)
            for (key, value) in self._sections[section].items():
                if key == "__name__":
                    continue
                if (value is not None) or (self._optcre == self.OPTCRE):
                    key = "=".join((key, str(value).replace("\n", "\n\t")))
                fp.write("%s\n" % (key))
            fp.write("\n")


class NvrSystemSettings(py_object):
    _SETTINGS_PATH = "/home/trassir/nvr-system-settings.ini"

    def __init__(self, setting_path=None):
        """Set/update parameters in nvr-system-settings.ini

        Args:
            setting_path (str, optional): Full path to setting file
        """
        if setting_path is None:
            setting_path = self._SETTINGS_PATH
        self.setting_path = setting_path

        if not os.path.isfile(setting_path):
            raise IOError("File {!r} not found".format(self.setting_path))

        self.config = TrassirConfigParser()
        self.config.read(setting_path)

    def _set_parameter(self, section, key, value):
        """Set parameter to section

        Args:
            section (str): Parameter section
            key (str): Parameter key
            value (str): Parameter value
        """
        if not self.config.has_section(section):
            self.config.add_section(section)

        self.config.set(section, key, value)

    def set_from_dict(self, settings):
        """Set settings from dict object

        Args:
            settings (Dict[Dict[str: str]]): Settings to update

        Examples:
            settings = {
                "hidden": {
                    "skip_edid_check": "true"
                },
                "keyboard": {
                    keyboard_layouts: 0,
                    keyboard_switch: 1
                }
            }
            This setting will update nvr-system-settings.ini file with:
                [hidden]
                skip_edid_check = true

                [keyboard]
                keyboard_layouts = 0
                keyboard_switch = 1

        Returns:
            str: Full path of setting file
        """
        if not isinstance(settings, dict):
            raise TypeError("Expected 'dict' got {!r}".format(type(settings).__name__))

        for section, config in settings.iteritems():
            if not isinstance(config, dict):
                raise TypeError(
                    "Expected 'dict' got {!r}".format(type(config).__name__)
                )

            for key, value in config.iteritems():
                self._set_parameter(section, key, value)

        tmp_file = self.setting_path + ".tmp"
        with open(tmp_file, "w") as setting_file:
            self.config.write(setting_file)

        # If successful, the renaming will be an atomic operation
        os.rename(tmp_file, self.setting_path)

        return self.setting_path


if __name__ == host.stats().parent().guid:
    if os.name == "nt":
        raise OSError("This script is unavailable for WinOS")

    nvr_system_settings = NvrSystemSettings()
    nvr_system_settings.set_from_dict({"hidden": {"skip_edid_check": "true"}})

    raise ResultMessage("""<span style="color: #009900">Success</span>""")
