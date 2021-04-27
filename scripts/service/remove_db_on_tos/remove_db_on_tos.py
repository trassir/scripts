# -*- coding: utf-8 -*-
# Пересоздает БД на Trassir OS.
# После запуска скрипта его нужно выключить, перезагрузить сервер и создастся новая БД.
#
# ВНИМАНИЕ! Процесс  не обратим.
"""
<parameters>
    <company>DSSL</company>
    <title>DB</title>
    <version>1.0</version>
</parameters>
"""

import subprocess

subprocess.Popen(
    "service postgresql restart",
    stderr=subprocess.PIPE,
    stdout=subprocess.PIPE,
    shell=True,
).communicate()
subprocess.Popen(
    "sudo -u postgres dropdb postgres",
    stderr=subprocess.PIPE,
    stdout=subprocess.PIPE,
    shell=True,
).communicate()
subprocess.Popen(
    "sudo -u postgres createdb postgres",
    stderr=subprocess.PIPE,
    stdout=subprocess.PIPE,
    shell=True,
).communicate()
