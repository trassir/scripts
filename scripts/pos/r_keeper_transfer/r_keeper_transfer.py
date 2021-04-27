# -*- coding: utf-8 -*-
# Перемещение файла R-keeper на Trassir OS
"""
<parameters>
    <company>DSSL</company>
    <title>R-keeper transfer</title>
    <version>1.0</version>
    <parameter>
        <type>server</type>
        <id>server_id</id>
        <name>Сервер</name>
        <value></value>
    </parameter>
</parameters>
"""
import os
import shutil

rs = settings("system_wide_options")["screenshots_folder"] + "/pos-rkeeper.ini"


def dele(guid, nume):
    settings("/" + nume + "/scripts")["script_erase"] = guid


def update_script(guid, nume):
    settings("/" + nume + "/scripts/" + guid)["script"] = (
        """import os
import shutil
import subprocess
subprocess.call(['mount -o remount,rw /'], shell=True, close_fds=True)
rt = settings("system_wide_options")["screenshots_folder"]+"/pos-rkeeper.ini"
cop = %r
open(rt, "w").write(cop)
subprocess.call(['sudo mount -o remount,rw /'], shell=True, close_fds=True)
subprocess.call(['sudo cp /mnt/LocalStorage/shots/pos-rkeeper.ini /opt/trassir/tech1/pos-rkeeper.ini'], shell=True, close_fds=True)
subprocess.call(['sudo mount -o remount,r /'], shell=True, close_fds=True)
subprocess.call(['sudo rm /mnt/LocalStorage/shots/pos-rkeeper.ini'], shell=True, close_fds=True)"""
        % open(rs, "r").read()
    )
    timeout(1000, lambda: dele(guid, nume))


def upp(guid, nume):
    timeout(1000, lambda: update_script(guid, nume))


def start():
    guid = settings("/" + server_id + "/scripts")["script_new_guid"]
    nume = settings("/" + server_id)["name"]
    settings("/" + nume + "/scripts")["script_create_now"] = 1
    upp(guid, nume)


start()
