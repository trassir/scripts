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

resources = {
    "helpers.py": """
        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
        tpxmGmQOAOD//vCkWQ==
    """,
    "tr.ts": """
        eNq9WEtv20YQvgfIf5gGCGAfGqVB20PBGgjyaIseEkDuIceVtDAYvgKSMmqfZBdNUjiwgR7a
        IijiJpf2KLmWogctHyTfl/+o3yxFi1RsqlGEADawjyF3vpn5vlnK+OTugzvrjx7eo/Xy2tUr
        xnqZNqUfmJ779bVbN25ewxoZVc8N5Y8hj8lwhSPXylXffBISj42SXtF7jgwCsZFMyAi8ul+V
        a+qlaqoT/A/iPaM0WUwsQl+4gS1CHLf2vXCFbQvfKGVX9WtL2fdecsg/OKClBmqoTgqPOXsl
        KrbnLn7QHypSbdWOd+Od+IC+e0jxTxjtxg0c3eOROlJDindIdbXlCf4jUv00CKpJ14MCB68H
        ZHEoyAwck0xbUsX0+RyxtTFuheTIzWo9XMz5O8L36oG06QfX5DTjlM2bNz6/egVW9z+jT0n9
        DhdPGZHq0+166FH6CFvcYotXGiODGQIpYOXtaCVu4Plner9HCEtbdTgUq/oU9deFm1/x67/g
        179GhNrqGFb78S/Y6mVCx0ZfstGhfvI43tOGs2YFwZ0bgAeh58DUotqo426Moq1RRBVxdojn
        0whcZFKr+/ijFWkjXxbo4nt2AvheZoUcr1Y/h1r2XF9YZpLtFNroN7cq08UFK/RXxKWFCm2o
        LjLVzkQm3uOqHKguxc+zfCF1jM0Dip9iu88GyFGbiwD7/6Kc1SkG/Jq3qlkQ3rtJRMgc/W26
        kzLelFuCzg5T1o1bFEjeNrcXhPfyXTT/m/2pyMx6taxIf7Bvl4ZrecGaTX0XGQYfQVuG0dC0
        5oe68UGBt9+MOtvCr8E/WYNIoWiTfC8vuH+ygzqw8C2tUHWEkENgMW1mRRVOX4SP198r5JPS
        dTzXDEedRV1/Aw96UP8m1GmXydNOBAttYUbeojyI6BIQUQGInI7kwNSES2CkFpRgFPlyWXCG
        CQ7iQa4ZdKcSotMz0BMMo3gvfh6/iPcLgNwXvtQN7x1hrdWtEFiCCdJt4WAGVR63nHFrQVDT
        RtRGC0fTawDHkU4Pqo7B8RL4+3baElW7wP2s0i9LT04Rc/Yr0heOhqYr6ctGW7OgwxRmADuY
        tBDjXabtuZznDFMpj7K8KpTz2yCvc84FZIOlSLrSsqUPAUetkdAmni22tFi5H6pXb2ag9XJM
        mOtrbRRtS9dc2uH5YL1HqJYtHDj+GdxgtvWTu9NFuc2pxvzMTqKFTAam7cianMrFUij2Ol+U
        rBsHU4oldXoErnXShQKPv4U4WDKkUAZPzNCcltxyfBtyuI+ZZfCln3JjKnCp1yiL+OdEGpCW
        hJdzmsy69C3dJB3z7JC8ymP5kUFAHLgqhhpIp7AuyqLiheLxR48yX0EK0/9IuPj6cZfmWPY7
        p+DWy9chLETseeLqKa8PtEH+srSfXJIH8Qt0DL2sUbIOr3CjnzDgIoPVoitKHVcqyGoVyrpi
        ZSYCd69Vsr0NG1QNsDDTOSdfLY5YtD+m32Y6bdzQkTl0+EKOhgKfqeOWxT7pr505hxul6W8L
        Rkn/BPEfXCGsHw==
    """,
}
t1utils.resources_check(script_path, resources)

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
