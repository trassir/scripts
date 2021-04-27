# -*- coding: utf-8 -*-
"""
<parameters>
    <company>DSSL</company>
    <author>d.gavrilov</author>
    <title>display_text</title>
    <version>1.0.1</version>
    <parameter>
        <id>CHANNELS</id>
        <name>Channels</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Custom string</name>
        <id>CUSTOM_STRING</id>
        <value></value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>DEBUG</id>
        <name>Debug</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>Display parameters</name>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>x1</name>
        <id>X1</id>
        <value>40</value>
        <min>1</min>
        <max>100000</max>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>y1</name>
        <id>Y1</id>
        <value>50</value>
        <min>1</min>
        <max>100000</max>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>x2</name>
        <id>X2</id>
        <value>50</value>
        <min>1</min>
        <max>100000</max>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>y2</name>
        <id>Y2</id>
        <value>50</value>
        <min>1</min>
        <max>100000</max>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Font color</name>
        <id>FONT_COLOR</id>
        <value>#CE2424</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Background color</name>
        <id>BACKGROUND_COLOR</id>
        <value>#FFFFFF</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Font size(px)</name>
        <id>FONT_SIZE</id>
        <value>30</value>
        <min>1</min>
        <max>100000</max>
    </parameter>
    <resources>
        <resource>figures.py</resource>
        <resource>helpers.py</resource>
    </resources>
</parameters>
"""

GLOBALS = globals()
CHANNELS = GLOBALS.get("CHANNELS", "")
CUSTOM_STRING = GLOBALS.get("CUSTOM_STRING", "")
DEBUG = GLOBALS.get("DEBUG", False)
# Display parameters
X1 = GLOBALS.get("X1", 20)
Y1 = GLOBALS.get("Y1", 30)
X2 = GLOBALS.get("X2", 30)
Y2 = GLOBALS.get("Y2", 30)
FONT_COLOR = GLOBALS.get("FONT_COLOR", "")
BACKGROUND_COLOR = GLOBALS.get("BACKGROUND_COLOR", "")
FONT_SIZE = GLOBALS.get("FONT_SIZE", "")

import host
import helpers

helpers.set_script_name()
logger = helpers.init_logger("display_text", debug=DEBUG)
from figures import draw, text_ext

if CHANNELS:
    CHANNELS = CHANNELS.split(",")
else:
    CHANNELS = None


def get_channel_grabber(sett):
    info = sett.cd("info")
    if info:
        try:
            grabber = host.settings(info["grabber_path"])
        except KeyError:
            return
        return grabber


def get_channels(select_channels):
    for sett in host.settings("channels").ls():
        if sett.type == "Channel" and not sett["archive_zombie_flag"]:
            if select_channels is None or sett.name in select_channels:
                grabber = get_channel_grabber(sett)
                if grabber and grabber["grabber_enabled"]:
                    yield sett.guid


def draw_figures():
    for guid in get_channels(CHANNELS):
        draw(
            guid,
            text_ext(
                X1, Y1, X2, Y2, CUSTOM_STRING, BACKGROUND_COLOR, FONT_COLOR, FONT_SIZE
            ),
        )
    host.timeout(30000, draw_figures)


def clear_figures():
    for guid in get_channels(CHANNELS):
        logger.debug("clear figures on channel with guid %s", guid)
        host.figure_remove(guid)


if not CUSTOM_STRING:
    raise ValueError("Empty string to display")
draw_figures()

host.register_finalizer(clear_figures)
