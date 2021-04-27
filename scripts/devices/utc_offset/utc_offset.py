# -*- coding: utf-8 -*-
# Скрипт для смены UTC на IP устройствах
#
# 1. Выбрать IP устройствах
# 2. Задать параметр в зависимости от часового пояса(Москва = 180, это +3 часа)

"""
<parameters>
    <company>My Company</company>
    <title>My Script</title>
    <version>1.0</version>
    <parameter>
        <id>NAME</id>
        <name>Выберите ip устройства</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>UTCOFFSET</id>
        <name>UTC offset</name>
        <type>integer</type>
        <value>0</value>
        <min>0</min>
        <max>1440</max>
    </parameter>
</parameters>
"""

NAMELIST = NAME.split(',')
message(NAMELIST)

for ip in settings('/' + settings('').guid + '/ip_cameras/').ls():
    # alert(ip.path)
    if 'ip_camera_add' not in ip.path:
        for IPNAME in NAMELIST:
            if ip['name'] == IPNAME and 'ip_camera_add' not in ip.path:
                message('Камера найдена, попытка смены настройки на ' + str(UTCOFFSET))
                ip['utc_offset_minutes'] = str(UTCOFFSET)