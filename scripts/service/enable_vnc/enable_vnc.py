# -*- coding: utf-8 -*-
# Только для серверов на Trassir OS
#
# Данный скрипт включает на сервере под TOS возможность
# подключения по VNC
"""
<parameters>
<parameter>
    <type>server</type>
    <id>SERVER</id>
    <name>Выбор сервера</name>
    <value></value>
</parameter>
<parameter>
    <type>string</type>
    <name>Пароль для vnc</name>
    <id>PSWD</id>
    <value></value>
</parameter>
</parameters>
"""

assert SERVER, 'Укажите сервер!'
assert PSWD, 'Укажите, пароль!'


def enable_vnc(srv, pswd):
    settings("/{}/system_wide_options".format(srv))["enable_vnc"] = pswd


enable_vnc(SERVER, PSWD)

raise ValueError("ОК! Пароль установлен: {}".format(settings("/{}/system_wide_options".format(SERVER))["enable_vnc"]))