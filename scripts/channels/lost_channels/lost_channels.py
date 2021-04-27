# -*- coding: utf-8 -*-
# Активируется нажатием клавиши F2
"""
<parameters>
    <company>AATrubilin</company>
    <title>LostChannels</title>
    <version>1.0.1</version>
    <parameter>
        <type>server</type>
        <id>SERVER</id>
        <name>Сервер, откуда брать потерянный канал</name>
        <value></value>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>LOST_CHANNEL</id>
        <name>Имя потерянного канала</name>
        <value></value>
        <string_list></string_list>
    </parameter>
    <parameter>
        <type>channel</type>
        <id>CHANNEL</id>
        <name>Канал куда будет привязан потерянный</name>
        <value></value>
    </parameter>
</parameters>
"""

import re
import host

GLOBALS = globals()
SERVER = GLOBALS.get("SERVER", "")
CHANNEL = GLOBALS.get("CHANNEL", "")
LOST_CHANNEL = GLOBALS.get("LOST_CHANNEL", "")

_lost_channels_regexp = re.compile(r"""\s<string_list>(.*)</string_list>""")
_bad_chars_regexp = re.compile(r"[\[\]&,]")

if not SERVER:
    raise ValueError("Выберите сервер!")

try:
    srv_channels = host.settings("/%s/channels" % SERVER)
except KeyError:
    raise ValueError("Сервер '%s' недоступен!" % SERVER)

lost_channels = []
for channel in sorted(srv_channels.ls(), key=lambda ch: ch.name):
    try:
        archive_zombie_flag = channel["archive_zombie_flag"]
    except KeyError:
        archive_zombie_flag = None

    if archive_zombie_flag:
        # lost_channels.append('%s_%s (d%s)' %(x.guid, SERVER, x.name.replace('_', '-').replace(' ', '-')))
        lost_channels.append(
            "{name} [{guid}_{server}]".format(
                name=_bad_chars_regexp.sub("_", channel.name),
                guid=channel.guid,
                server=SERVER,
            )
        )

lost_channels_list = ",".join(lost_channels)

found_lost_channels = _lost_channels_regexp.search(host.stats().parent()["script"])
if found_lost_channels and found_lost_channels.group(1) != lost_channels_list:
    host.stats().parent()["script"] = _lost_channels_regexp.sub(
        "<string_list>{string_list}</string_list>".format(
            string_list=lost_channels_list
        ),
        host.stats().parent()["script"],
    )

if not LOST_CHANNEL:
    raise ValueError("Выберите потерянный канал")
if not CHANNEL:
    raise ValueError("Выберите канал привязки")

change_channel, change_srv = CHANNEL.split("_")
changer_channel, changer_srv = LOST_CHANNEL.split("[")[1][:-1].split("_")

if change_srv != changer_srv:
    raise ValueError(
        "Канал привязки находится не на сервере привязываемой камеры!\nВыберите другой канал!"
    )


def restore_lost():
    for device in host.settings("/{srv}/ip_cameras".format(srv=SERVER)).ls():
        if device.type == "Grabber":
            for x in xrange(31):
                if device["channel%02d_guid" % x] == change_channel:
                    host.message("Replace!")
                    device["channel%02d_guid" % x] = changer_channel
                    host.settings("/{}/channels/{}".format(changer_srv, changer_channel))[
                        "archive_zombie_flag"
                    ] = 0
                    host.settings("/{}/channels/{}".format(change_srv, change_channel))[
                        "archive_zombie_flag"
                    ] = 1
                    return

    host.error("Can't find channel to replace")


host.activate_on_shortcut('F2', restore_lost)
