# -*- coding: utf-8 -*-
"""
<parameters>
    <company>d.gavrilov</company>
    <title>folder_cleaner</title>
    <version>1.0.4</version>
    <parameter>
        <id>FOLDER</id>
        <type>string</type>
        <name>Path to folder</name>
        <value>default</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Free space(mb)</name>
        <id>MIN_FREE_SPACE</id>
        <value>500</value>
        <min>0</min>
        <max>100000</max>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Check interval(min)</name>
        <id>CHECK_INTERVAL</id>
        <value>10</value>
        <min>1</min>
        <max>10000</max>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>File age(days)</name>
        <id>FILE_AGE</id>
        <value>10</value>
        <min>1</min>
        <max>100000</max>
    </parameter>
    <parameter>
        <id>FILTER_EXT</id>
        <type>string</type>
        <name>Filter ext</name>
        <value></value>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <name>Debug mode</name>
        <type>boolean</type>
        <value>False</value>
        </parameter>
    <resources>
        <resource>helpers.py</resource>
    </resources>
</parameters>
"""

GLOBALS = globals()
MIN_FREE_SPACE = GLOBALS.get("MIN_FREE_SPACE", 500)
FOLDER = GLOBALS.get("FOLDER", "")
CHECK_INTERVAL = GLOBALS.get("CHECK_INTERVAL", 1)
FILE_AGE = GLOBALS.get("FILE_AGE", 10)
FILTER_EXT = GLOBALS.get("FILTER_EXT", "")
DEBUG = GLOBALS.get("DEBUG", False)

import helpers

helpers.set_script_name()
logger = helpers.init_logger("folder_cleaner", debug=DEBUG)

logger.debug(
    "script started with params folder:%s, free space(Mb):%s, check interval(min):%s, file age(days):%s, "
    "filter ext: %s",
    FOLDER,
    MIN_FREE_SPACE,
    CHECK_INTERVAL,
    FILE_AGE,
    FILTER_EXT,
)

import psutil
import time
import os
import host


def _win_encode_path(path):
    if os.name == "nt":
        try:
            path = path.decode("utf8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return path


if FOLDER in ("default", ""):
    FOLDER = host.settings("system_wide_options")["screenshots_folder"]

clean_folder = _win_encode_path(FOLDER)
ext_list = None
if FILTER_EXT:
    ext_list = ["." + ext.strip() for ext in FILTER_EXT.split(",")]

if not os.path.exists(clean_folder):
    raise OSError("folder not found")


def folder_checker(folder_path, file_age, extension_list, disk_space, min_free_space):
    _file_count = 0
    _free_space = disk_space // 1024 // 1024
    for dir_path, dir_name, file_names in os.walk(folder_path):
        for file_name in file_names:
            _file_count += 1
            fp = os.path.join(dir_path, file_name)
            diff_time = time.time() - os.path.getctime(fp)
            file_name, extension = os.path.splitext(fp)
            if min_free_space == 0:
                if extension_list:
                    if extension in extension_list:
                        delete_file(diff_time, file_age, file_name, fp)
                    else:
                        continue
                else:
                    raise ValueError("Need to specify file extension")
            else:
                if extension_list:
                    if extension in extension_list:
                        delete_file(diff_time, file_age, file_name, fp)
                    else:
                        continue

                else:
                    delete_file(diff_time, file_age, file_name, fp)
        if _file_count == 0:
            logger.warning(
                "Nothing to delete, free disk space %s mb" % str(_free_space)
            )


def delete_file(diff_time, file_age, file_name, fp):
    if diff_time > file_age * 24 * 3600:
        try:
            logger.debug("remove file: %s", file_name)
            os.remove(fp)
        except OSError as e:
            logger.warning(str(e))


def loop():
    free_disk_space = int(psutil.disk_usage(clean_folder).free)
    if MIN_FREE_SPACE == 0:
        folder_checker(
            clean_folder, FILE_AGE, ext_list, free_disk_space, MIN_FREE_SPACE
        )
        host.timeout(CHECK_INTERVAL * 60000, loop)
    else:
        if free_disk_space < MIN_FREE_SPACE * 1024 * 1024:
            folder_checker(
                clean_folder, FILE_AGE, ext_list, free_disk_space, MIN_FREE_SPACE
            )
            host.timeout(CHECK_INTERVAL * 60000, loop)


loop()
