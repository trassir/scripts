# -*- coding: utf-8 -*-
# Carousel Universal v0.4
#
# F1 - Запуск Auto Carousel
# F2 - Остановка Auto Carousel (ручной режим)
#
# Ручной режим:
# F5 - Следующий канал
# F6 - Предыдущий канал

"""
<parameters>
    <company>AATrubilin</company>
    <title>Carousel Universal</title>
    <version>0.4</version>
    <parameter>
        <type>caption</type>
        <name>Выберите каналы или шаблоны для циклического показа</name>
    </parameter>
    <parameter>
        <id>CHOICE</id>
        <name>Каналы или Шаблоны</name>
        <type>string_from_list</type>
        <value>Каналы</value>
        <string_list>Каналы,Шаблоны</string_list>
    </parameter>
    <parameter>
        <id>CHAN</id>
        <name>Выберите Каналы или Шаблоны</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>CHAN_BAD</id>
        <name>Каналы или шаблоны игноррирования</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>MONITOR</id>
        <name>Монитор для вывода каналов или шаблонов</name>
        <type>integer</type>
        <value>1</value>
    </parameter>
    <parameter>
        <id>TIMEOUT</id>
        <name>Таймаут перед следующим каналом или шаблоном</name>
        <type>integer</type>
        <value>5</value>
    </parameter>
    <parameter>
        <id>MOUSE_TIME</id>
        <name>Таймаут после остановки цикла клика мышью</name>
        <type>integer</type>
        <value>10</value>
    </parameter>
    <parameter>
        <id>HAND_USING</id>
        <name>Ручное управление при запуске</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>Выберите параметры и тревожные события для тревожного монитора</name>
    </parameter>
    <parameter>
        <id>ALARM_TEMPLATE</id>
        <name>Тревожный шаблон</name>
        <type>string</type>
    </parameter>
    <parameter>
        <id>ATTENTION_MONITOR</id>
        <name>Тревожный монитор</name>
        <type>integer</type>
        <value>2</value>
    </parameter>
    <parameter>
        <id>ATTENTION_TIMEOUT</id>
        <name>Таймаут перед очисткой тревожного шаблона</name>
        <type>integer</type>
        <value>2</value>
    </parameter>
    <parameter>
        <id>MOTION_REACTION</id>
        <name>События появления движения</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>LEFT_OBJECT_REACTION</id>
        <name>События от детектора оставленных предметов</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SABOTAGE_REACTION</id>
        <name>События от детектора саботажа</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>FIRE_REACTION</id>
        <name>События от детектора огня</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>USER</id>
        <name>Запуск циклического просмотра по логированию пользователя (имя пользователя)</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <name>Режим отладки</name>
        <id>DEBUG</id>
        <value>False</value>
    </parameter>
    <resources>
        <resource>helpers.py</resource>
        <resource>tr.ts</resource>
    </resources>
</parameters>
"""

GLOBALS = globals()
CHOICE = GLOBALS.get("CHOICE", "Каналы")  # [Каналы, Шаблоны]
CHAN = GLOBALS.get("CHAN", "")
CHAN_BAD = GLOBALS.get("CHAN_BAD", "")
MONITOR = GLOBALS.get("MONITOR", 1)
TIMEOUT = GLOBALS.get("TIMEOUT", 5)
MOUSE_TIME = GLOBALS.get("MOUSE_TIME", 10)
HAND_USING = GLOBALS.get("HAND_USING", False)
ALARM_TEMPLATE = GLOBALS.get("ALARM_TEMPLATE", "")
ATTENTION_MONITOR = GLOBALS.get("ATTENTION_MONITOR", 2)
ATTENTION_TIMEOUT = GLOBALS.get("ATTENTION_TIMEOUT", 2)
MOTION_REACTION = GLOBALS.get("MOTION_REACTION", False)
LEFT_OBJECT_REACTION = GLOBALS.get("LEFT_OBJECT_REACTION", False)
SABOTAGE_REACTION = GLOBALS.get("SABOTAGE_REACTION", False)
FIRE_REACTION = GLOBALS.get("FIRE_REACTION", False)
USER = GLOBALS.get("USER", "")
DEBUG = GLOBALS.get("DEBUG", False)

import helpers

helpers.set_script_name()
logger = helpers.init_logger("Carousel Universal", debug=DEBUG)

import host

import time
import threading
from functools import wraps

choice_dict = {
    host.tr("Каналы"): "Channel",
    host.tr("Шаблоны"): "Template",
}


def _run_as_thread(fn):
    @wraps(fn)
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
        return t

    return run


class Event:
    def __init__(self):
        self.MOTION_REACTION = MOTION_REACTION
        self.FIRE_REACTION = FIRE_REACTION
        self.LEFT_OBJECT_REACTION = LEFT_OBJECT_REACTION
        self.SABOTAGE_REACTION = SABOTAGE_REACTION

        if self.MOTION_REACTION:
            motion_event = ["Motion Start", "CrossLine Detected"]
        if self.FIRE_REACTION:
            fire_event = ["Smoke Detected", "Fire Detected"]
        if self.LEFT_OBJECT_REACTION:
            left_object_event = [
                "Left Object Detected",
                "Item Abandoned",
                "Item Missing",
                "Slow Down Detected",
            ]
        if self.SABOTAGE_REACTION:
            sabotage_event = [
                "Tamper Alert: Defocus",
                "Tamper Alert: Covered",
                "Tamper Alert: Flashlight",
                "Tamper Alert: Shift",
            ]
        self.loc = locals()

    def compil_event(self):
        event_collect = [self.loc["%s" % x] for x in self.loc if "event" in x]
        event_full = []
        for x in event_collect:
            event_full += x
        return event_full


event = Event()


class Carousel:
    def __init__(self, carousel_dict, hand_using, func):
        self.chan_on_template = []
        self.gui = host.object("operatorgui_" + host.settings("").guid)
        self.carousel_dict = carousel_dict
        self.hand_using = hand_using
        self.func = func
        self.idx = 0
        self.carousel_go()

    def attention(self, ev):
        guid = ev.origin
        if (
            host.object(guid).name not in self.carousel_dict
            and guid in self.chan_on_template
        ):
            return
        self.chan_on_template.append(ev.origin)
        self.show_chans()
        pass

    def show_chans(self):
        self.gui.show_template(ALARM_TEMPLATE, ATTENTION_MONITOR)
        try:
            self.gui.show("gui7(-1, '')", ATTENTION_MONITOR)
            self.gui.assign_channels(",".join(self.chan_on_template), ATTENTION_MONITOR)
        except Exception as e:
            host.alert("ERROR: %s" % e)
        host.timeout(1000 * ATTENTION_TIMEOUT, self.del_old)

    def del_old(self):
        if not self.chan_on_template:
            return
        self.chan_on_template.pop(0)
        self.show_chans()

    def show_channel(self):
        logger.debug("show %s" % self.carousel_dict[self.idx])
        self.gui.show_channel(self.carousel_dict[self.idx], MONITOR)

    def show_template(self):
        logger.debug("show %s" % self.carousel_dict[self.idx])
        self.gui.show_template_by_guid(self.carousel_dict[self.idx], MONITOR)

    def hand_using_carousel(self, stat):
        self.hand_using = stat
        logger.info("hand using: %s" % self.hand_using)

    def hand_using_go(self, x):
        if x == "up":
            self.idx += 1
        if x == "down":
            self.idx -= 1
        if self.idx >= len(self.carousel_dict):
            self.idx = 0
        if self.idx < 0:
            self.idx = len(self.carousel_dict) - 1
        getattr(self, self.func)()

    def carousel_go(self):
        if not self.hand_using:
            if self.idx >= len(self.carousel_dict):
                self.idx = 0
            getattr(self, self.func)()
            self.idx += 1
        host.timeout(1000 * TIMEOUT, self.carousel_go)

    @_run_as_thread
    def mous_handler(self, ev):
        logger.debug("mouse catch")
        self.hand_using = True
        time.sleep(MOUSE_TIME)
        self.hand_using = False
        logger.debug("mouse no catch")


def initialization():
    if CHAN_BAD:
        bad_list = [host.object(x).guid for x in CHAN_BAD.split(",")]
    else:
        bad_list = []
    logger.debug(bad_list)
    logger.debug(choice_dict[CHOICE])
    if CHAN:
        carousel_list = [
            host.object(x).guid
            for x in CHAN.split(",")
            if not host.object(x).guid in bad_list
        ]
    else:
        carousel_list = [
            x[1] for x in host.objects_list(choice_dict[CHOICE]) if not x[1] in bad_list
        ]
    logger.debug(carousel_list)
    for x in [z[1] for z in host.objects_list("IP Device")]:
        if x in carousel_list:
            raise ValueError(
                host.tr("Имеется IP устройство с именем канала %s") % host.object(x).name
            )
    logger.debug("list %s done!" % carousel_list)
    return {x: z for x, z in enumerate(carousel_list)}


def user_login(ev):
    if ev.username == USER:
        slide.hand_using_carousel(False)


slide = Carousel(
    initialization(), HAND_USING, ("show_%s" % choice_dict[CHOICE]).lower()
)
if ALARM_TEMPLATE:
    for event_type in event.compil_event():
        host.activate_on_events(event_type, "", slide.attention)

host.activate_on_shortcut("F1", lambda: slide.hand_using_carousel(False))
host.activate_on_shortcut("F2", lambda: slide.hand_using_carousel(True))
host.activate_on_shortcut("F5", lambda: slide.hand_using_go("up"))
host.activate_on_shortcut("F6", lambda: slide.hand_using_go("down"))
host.activate_on_gui_event("Focus Changed", slide.mous_handler)
if USER:
    host.activate_on_events("Login Successful, %1 from %2", "", user_login)
