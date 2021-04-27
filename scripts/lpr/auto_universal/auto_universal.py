# -*-coding: utf-8 -*-
# TRASSIR Auto universal v2.3.2
# Скрипт запускается на сервере

'''
<parameters>
    <company>DSSL Mitrofanov</company>
    <title>TRASSIR Auto universal</title>
    <version>2.3.2</version>
    <parameter>
        <type>caption</type>
        <name>Общие настройки</name>
    </parameter>
    <parameter>
        <id>CHANNELS_NAMES</id>
        <name>Каналы с АТ</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>LIST_TYPE</id>
        <name>Машина в списке</name>
        <type>string_from_list</type>
        <string_list>белом,чёрном,информационном,любом,нет в списках,любой номер,не распознан</string_list>
        <value>любом</value>
    </parameter>
    <parameter>
        <id>NAME_LIST</id>
        <type>string</type>
        <name>Работать со списками (имена через запятую)</name>
        <value></value>
    </parameter>
    <parameter>
        <id>REPEAT_EV_DELAY</id>
        <name>Задержка перед повторным распознаванием одинакового номера (сек)</name>
        <type>integer</type>
        <value>15</value>
        <min>1</min>
        <max>600</max>
    </parameter>
    <parameter>
        <id>DIRECTION</id>
        <name>Направление движения</name>
        <type>string_from_list</type>
        <string_list>вниз,вверх,любое</string_list>
        <value>вниз</value>
    </parameter>
    <parameter>
        <id>HW_DET_ENABLE</id>
        <name>Используется детектор HW</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
     <parameter>
        <name>""" Реакции по событиям """</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>OUTPUT_ON</id>
        <name>Выполнить операции с тревожными выходами</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>ACS_ENBL</id>
        <name>Выполнить операции с точкой доступа СКУД</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SHOW_CHAN</id>
        <name>Включить вывод канала на отображение</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SAVE_SCREEN</id>
        <name>Сохранить снимок локально</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_FTP</id>
        <name>Отправить снимок по FTP</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_SCREEN_EMAIL</id>
        <name>Отправить снимок на e-mail</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_SCREEN_TELEGRAM</id>
        <name>Снимок на Telegram</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_EMAIL</id>
        <name>Отправить уведомление на e-mail</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SHOW_MESSAGE</id>
        <name>Отображать текстовое сообщение</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SHOW_MESSAGE_DELAY</id>
        <name>Длительность отображения текcтового сообщения(сек)</name>
        <type>integer</type>
        <value>5</value>
        <min>1</min>
        <max>60</max>
    </parameter>
    <parameter>
        <id>PLAY_SOUND</id>
        <name>Проиграть звуковое оповещение</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SOUND_NAME</id>
        <name>Название звукового файла</name>
        <type>string_from_list</type>
        <string_list>alarm.wav,bell.wav,boxing-bell-1.wav,boxing-bell-3.wav,cardlock-open.wav,chime.wav,chip001.wav,chip019.wav,chip069.wav,cordless-phone-ring.wav,countdown.wav,dialtone.wav,ding.wav,horn-beep.wav,phone-beep.wav,police2.wav,ship-on-fog.wav,ships-bell.wav,SNES-startup.wav,spin-up.wav,tada1.wav,tape-slow9.wav</string_list>
        <value>bell.wav</value>
    </parameter>
    <parameter>
        <id>SHOW_POPUP</id>
        <name>Вывести всплывающее окно</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
      <parameter>
        <type>integer</type>
        <name>Номер монитора для перехода из всплывающих окон</name>
        <id>MON_POPUP</id>
        <value>1</value>
        <min>1</min>
        <max>15</max>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" Настройка e-mail """</name>
    </parameter>
    <parameter>
        <id>EMAIL_ACCOUNT</id>
        <name>Учетная запись отправителя, созданная в Trassir</name>
        <type>string</type>
    </parameter>
    <parameter>
        <id>EMAIL_ADDRESSES</id>
        <name>Список получателей через запятую</name>
        <type>string</type>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" Telegram """</name>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Telegram id пользователя</name>
        <id>TG_IDS</id>
        <value></value>
    </parameter>
    <parameter>
        <name>""" Дополнительно """</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <type>float</type>
        <name>Коррекция времени скриншота (до события), сек</name>
        <id>SAVE_SCREEN_DELTA</id>
        <value>0</value>
        <min>0</min>
        <max>7</max>
    </parameter>
    <parameter>
        <id>ONLINE_SHOT</id>
        <name>Скриншот с потока камеры</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
     <parameter>
        <id>FIGURES</id>
        <name>Скриншоты с фигурами</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SCHEDULE</id>
        <name>Расписание (опционально)(работает, когда расп. в красной зоне)</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" Настройки ftp """</name>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Хост</name>
        <id>FTP_HOST</id>
        <value>172.16.12.69</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Порт</name>
        <id>FTP_PORT</id>
        <value>21</value>
        <min>1</min>
        <max>999999</max>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Пользователь</name>
        <id>FTP_USER</id>
        <value>trassir</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Пароль</name>
        <id>FTP_PASSWD</id>
        <value>123456</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Папка на ftp сервере</name>
        <id>FTP_PATH</id>
        <value></value>
    </parameter>

     <parameter>
        <name>"""Тревожный монитор"""</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <name>Базовые настройки ТМ</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>AM_DISPLAY_DURATION</id>
        <name>Длительность отображения канала в тревожном шаблоне (сек)</name>
        <type>integer</type>
        <min>1</min>
        <max>9999</max>
        <value>30</value>
    </parameter>
    <parameter>
        <id>AM_ALARM_TEMPLATE</id>
        <name>Тревожный шаблон</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>AM_BASE_TEMPLATE</id>
        <name>Базовый шаблон (по окон-ю тревоги)</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>AM_MON</id>
        <name>Номер дисплея для тревожного шаблона</name>
        <type>integer</type>
        <value>1</value>
    </parameter>

    <parameter>
        <id>AM_TYPE</id>
        <name>Тип действия</name>
        <type>string_from_list</type>
        <string_list>Отобразить канал,Открыть момент в архиве</string_list>
        <value>Отобразить канал</value>
    </parameter>
    <parameter>
        <name>Опциональные настройки ТМ</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>AM_NO_MOTION_CHECK</id>
        <name>Сброс тревоги только при отуствии движения на канале</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>AM_MAX_CHANS</id>
        <name>Лимит одновременно отображаемых каналов</name>
        <type>integer</type>
        <value>24</value>
        <min>1</min>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" Операции со СКУД """</name>
    </parameter>
    <parameter>
        <id>ACS_TYPE</id>
        <name>Тип СКУД</name>
        <type>string_from_list</type>
        <string_list>Sigur,Orion</string_list>
        <value></value>
    </parameter>
    <parameter>
        <id>ACS_DOOR</id>
        <name>Название точки доступа СКУД</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>ACS_LOGIC</id>
        <name>Тип работы</name>
        <type>string_from_list</type>
        <string_list>открыть дверь,закрыть дверь</string_list>
        <value>открыть дверь</value>
    </parameter>
    <parameter>
        <id>ACS_DELAY</id>
        <name>Время открытого/закрытого состояния двери,(сек)</name>
        <type>integer</type>
        <value>5</value>
        <min>1</min>
        <max>3600</max>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <name>Клавиша для ручной активации операций</name>
        <id>ACS_MAN_ACTIV</id>
        <string_list>нет,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,F18,F19,F20,F21,F22,F23,F24,F25,F26,F27,F28,F29,F30,F31,F32,F33,F34,F35,F36,F37,F38,F39,F40,F41,F42,F43,F44,F45,F46,F47,F48,F49,Ctrl+F1,Ctrl+F2,Ctrl+F3,Ctrl+F4,Ctrl+F5,Ctrl+F6,Ctrl+F7,Ctrl+F8,Ctrl+F9,Ctrl+F10,Ctrl+F11,Ctrl+F12,Ctrl+F13,Ctrl+F14,Ctrl+F15,Ctrl+F16,Ctrl+F17,Ctrl+F18,Ctrl+F19,Ctrl+F20,Ctrl+F21,Ctrl+F22,Ctrl+F23,Ctrl+F24,Ctrl+F25,Ctrl+F26,Ctrl+F27,Ctrl+F28,Ctrl+F29,Ctrl+F30,Ctrl+F31,Ctrl+F32,Ctrl+F33,Ctrl+F34,Ctrl+F35,Ctrl+F36,Ctrl+F37,Ctrl+F38,Ctrl+F39,Ctrl+F40,Ctrl+F41,Ctrl+F42,Ctrl+F43,Ctrl+F44,Ctrl+F45,Ctrl+F46,Ctrl+F47,Ctrl+F48,Ctrl+F49</string_list>
        <value>нет</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" Операции с тревожными выходами """</name>
    </parameter>
    <parameter>
        <id>OUTPUTS</id>
        <name>Тревожные выходы</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>OUTPUT_ACTION_TYPE</id>
        <name>Тип работы</name>
        <type>string_from_list</type>
        <string_list>1.замкнуть,2.разомкнуть,3.замкнуть-разомкнуть,4.разомкнуть-замкнуть,5.замкнуть-замкнуть,6.разомкнуть-разомкнуть</string_list>
        <value>замкнуть-разомкнуть</value>
    </parameter>
    <parameter>
        <id>OUTPUT_DELAY</id>
        <name>Задержка между парными операциями (напр. замкнуть-разомкнуть) (сек)</name>
        <type>integer</type>
        <value>5</value>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>OUTPUT_ALGORITHM</id>
        <name>Алгоритм работы шлагбаума с очередью</name>
        <value>type_1</value>
        <string_list>type_1,type_2,type_3</string_list>
    </parameter>
    <parameter>
        <id>DELAY_BETWEEN_ITERATIONS</id>
        <name>Таймаут перед обработкой следующего авто для type_3 (сек)</name>
        <type>integer</type>
        <value>2</value>
        <min>1</min>
        <max>3600</max>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <name>Клавиша для ручной активации операций</name>
        <id>OUTPUT_MAN_ACTIV</id>
        <string_list>нет,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,F18,F19,F20,F21,F22,F23,F24,F25,F26,F27,F28,F29,F30,F31,F32,F33,F34,F35,F36,F37,F38,F39,F40,F41,F42,F43,F44,F45,F46,F47,F48,F49,Ctrl+F1,Ctrl+F2,Ctrl+F3,Ctrl+F4,Ctrl+F5,Ctrl+F6,Ctrl+F7,Ctrl+F8,Ctrl+F9,Ctrl+F10,Ctrl+F11,Ctrl+F12,Ctrl+F13,Ctrl+F14,Ctrl+F15,Ctrl+F16,Ctrl+F17,Ctrl+F18,Ctrl+F19,Ctrl+F20,Ctrl+F21,Ctrl+F22,Ctrl+F23,Ctrl+F24,Ctrl+F25,Ctrl+F26,Ctrl+F27,Ctrl+F28,Ctrl+F29,Ctrl+F30,Ctrl+F31,Ctrl+F32,Ctrl+F33,Ctrl+F34,Ctrl+F35,Ctrl+F36,Ctrl+F37,Ctrl+F38,Ctrl+F39,Ctrl+F40,Ctrl+F41,Ctrl+F42,Ctrl+F43,Ctrl+F44,Ctrl+F45,Ctrl+F46,Ctrl+F47,Ctrl+F48,Ctrl+F49</string_list>
        <value>нет</value>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <name>log</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <resources>
        <resource>base_utils.py</resource>
        <resource>delete_old_shots.py</resource>
        <resource>email_sender.py</resource>
        <resource>en.ts</resource>
        <resource>ftp.py</resource>
        <resource>helpers.py</resource>
        <resource>schedule.py</resource>
        <resource>script_object.py</resource>
        <resource>shot_saver.py</resource>
        <resource>tbot.py</resource>
        <resource>lpr_handler/lpr_handler.py</resource>
        <resource>lpr_handler/not_recognized_handler.py</resource>
        <resource>lpr_handler/__init__.py</resource>
        <resource>reactions/access_control.py</resource>
        <resource>reactions/alarm_mon.py</resource>
        <resource>reactions/executor.py</resource>
        <resource>reactions/fire_event.py</resource>
        <resource>reactions/output_reaction.py</resource>
        <resource>reactions/output_reaction_type_2.py</resource>
        <resource>reactions/output_reaction_type_3.py</resource>
        <resource>reactions/play_sound.py</resource>
        <resource>reactions/reactions.py</resource>
        <resource>reactions/reactions_with_screenshots.py</resource>
        <resource>reactions/show_message.py</resource>
        <resource>reactions/show_popup.py</resource>
        <resource>reactions/telegram_text_sender.py</resource>
        <resource>reactions/__init__.py</resource>
        <resource>senders/senders.py</resource>
        <resource>senders/__init__.py</resource>
    </resources>
    </parameters>
'''
import os
import re
from __builtin__ import object

from helpers import init_logger, set_script_name
import host
from tbot import *

GLOBALS = globals()

# Initialize logger before import another modules
DEBUG = GLOBALS.get("DEBUG", False)
logger = init_logger(name=host.stats().parent().name, debug=DEBUG)

logger.info(
    "SCRIPT START. Script info: %s, pc id %s, pc name: %s",
    set_script_name(),
    host.settings("").guid,
    host.settings("").name,
)


from reactions import Reactions
from reactions import PlaySound
from reactions import FireEvent


# """ Реакции по событиям """
SHOW_CHAN = GLOBALS.get("SHOW_CHAN", False)
SEND_FTP = GLOBALS.get("SEND_FTP")
SEND_SCREEN_EMAIL = GLOBALS.get("SEND_SCREEN_EMAIL", False)
SEND_EMAIL = GLOBALS.get("SEND_EMAIL", False)
SEND_SCREEN_TELEGRAM = GLOBALS.get("SEND_SCREEN_TELEGRAM", False)
PLAY_SOUND = GLOBALS.get("PLAY_SOUND", False)
SOUND_NAME = GLOBALS.get("SOUND_NAME", "bell.wav")
OUTPUT_ON = GLOBALS.get("OUTPUT_ON", False)
ACS_ENBL = GLOBALS.get("ACS_ENBL", False)
SHOW_MESSAGE = GLOBALS.get("SHOW_MESSAGE", False)
SHOW_POPUP = GLOBALS.get("SHOW_POPUP", False)
SHOW_MESSAGE_DELAY = GLOBALS.get("SHOW_MESSAGE_DELAY", 5)

CHANNELS_NAMES = GLOBALS.get("CHANNELS_NAMES")


# """Тревожный монитор"""
AM_ALARM_TEMPLATE = GLOBALS.get("AM_ALARM_TEMPLATE")
AM_MAX_CHANS = GLOBALS.get("AM_MAX_CHANS", 6)
AM_BASE_TEMPLATE = GLOBALS.get("AM_BASE_TEMPLATE")
AM_DISPLAY_DURATION = GLOBALS.get("AM_DISPLAY_DURATION", 30)

AM_TYPE = GLOBALS.get("AM_TYPE", host.tr("Отобразить канал"))
AM_NO_MOTION_CHECK = GLOBALS.get("AM_NO_MOTION_CHECK", False)
AM_CHANGE_TEMPLATE_CHECK = GLOBALS.get("AM_CHANGE_TEMPLATE_CHECK", False)
AM_MON = GLOBALS.get("AM_MON", 1)


# """ Операции со СКУД """
ACS_MAN_ACTIV = GLOBALS.get("ACS_MAN_ACTIV", host.tr("нет"))
ACS_TYPE = GLOBALS.get("ACS_TYPE", "Sigur")
ACS_DOOR = GLOBALS.get("ACS_DOOR")
ACS_DELAY = GLOBALS.get("ACS_DELAY", 5)
ACS_LOGIC = GLOBALS.get("ACS_LOGIC", "open the door")


# """ Настройка e-mail """
EMAIL_ACCOUNT = GLOBALS.get("EMAIL_ACCOUNT", "")
EMAIL_ADDRESSES = GLOBALS.get("EMAIL_ADDRESSES", "")

# """ Telegram """
TG_IDS = GLOBALS.get("TG_IDS", "")
TG_PROXY = GLOBALS.get("TG_PROXY", "")

# """ Настройки ftp """
FTP_HOST = GLOBALS.get("FTP_HOST", "172.16.12.69")
FTP_PORT = GLOBALS.get("FTP_PORT", 21)
FTP_USER = GLOBALS.get("FTP_USER", "trassir")
FTP_PASSWD = GLOBALS.get("FTP_PASSWD", "123456")
FTP_PATH = GLOBALS.get("FTP_PATH", "")
FTP_PASSIVE_MODE = GLOBALS.get("FTP_PASSIVE_MODE", True)

# """ Операции с тревожными выходами """
OUTPUTS = GLOBALS.get("OUTPUTS", "")
OUTPUT_MAN_ACTIV = GLOBALS.get("OUTPUT_MAN_ACTIV", host.tr("нет"))
OUTPUT_ALGORITHM = GLOBALS.get("OUTPUT_ALGORITHM", "type_1")
OUTPUT_DELAY = GLOBALS.get("OUTPUT_DELAY", 5)
DELAY_BETWEEN_ITERATIONS = GLOBALS.get("DELAY_BETWEEN_ITERATIONS", 5)

SCHEDULE = GLOBALS.get("SCHEDULE")


class TrassirError(Exception):
    """Exception if bad trassir version"""

    pass


def _is_channel_enabled(sett):
    info = sett.cd("info")
    if info and info["grabber_path"]:
        try:
            grabber = host.settings(info["grabber_path"])
        except KeyError:
            return False

        if grabber["grabber_enabled"]:
            n = info["grabber_channel_n"]
            return (
                grabber["channel%02d_main_enabled" % n]
                or grabber["channel%02d_ext_enabled" % n]
            )
    return False


class OutputObj(object):
    def __init__(self, obj, name, guid, parent_device_guid):
        self.obj = obj
        self.name = name
        self.guid = guid
        self.parent_device_guid = parent_device_guid

    def __repr__(self):
        return "{}({})".format(self.name, self.guid)

    def set_output_high(self):
        self.obj.set_output_high()

    def set_output_low(self):
        self.obj.set_output_low()


def parse_object_names(object_names):
    if object_names:
        return set(object_names.split(","))


def get_outputs(names=None):
    """

    Args:
        names (set):

    Returns:

    """
    _gpios = []
    for x in host.objects_list("GPIO Output"):
        if names and x[0] not in names:
            continue
        obj = host.object(x[1])
        if hasattr(obj, "set_output_high") and hasattr(obj, "set_output_low"):
            try:
                name = obj.name
                guid = obj.guid
            except EnvironmentError:
                raise EnvironmentError(
                    "Can't get access to %s, check script user rights" % x[0]
                )
            else:
                _gpios.append(OutputObj(obj, name, guid, x[3]))
    return _gpios


class TRObject(object):
    spec_symbols = re.compile(r'[|\\/:*?"<>]')

    def __init__(self, sett):
        self.sett = sett
        self.name = self.spec_symbols.sub("", sett.name.strip())

    def __getattr__(self, name):
        return getattr(self.sett, name)


class Server(TRObject):
    def __init__(self, sett):
        super(Server, self).__init__(sett)


class Channel(TRObject):
    def __init__(self, sett, server):
        super(Channel, self).__init__(sett)
        self.server = server

    @property
    def full_guid(self):
        return "{s.guid}_{s.server.guid}".format(s=self)


def get_channels(server_guid, channel_names=None):
    """
    Args:
        server_guid (str):
        channel_names (Set('name_1', 'name_2')):
    Returns: List[ Channel_1, Channel_2]

    """
    channels_ = []
    server = Server(host.settings("/%s" % server_guid))
    for sett in host.settings("/%s/channels" % server_guid).ls():
        if sett.type == "Channel" and not sett["archive_zombie_flag"]:
            if channel_names is None or sett.name in channel_names:
                if _is_channel_enabled(sett):
                    channels_.append(Channel(sett, server))
    return channels_


# ---------------------------------------------------------------------
#  Initializing starts here
# ---------------------------------------------------------------------

if __name__ == host.stats().parent().guid:
    if host.settings("").guid == "client":
        raise TrassirError("Script starts on Trassir server only, not client")

    schedule_ = None
    if SCHEDULE:
        from schedule import ScheduleObject

        schedule_ = ScheduleObject(SCHEDULE)

    reactions = Reactions(schedule_)

    # -------------------------------------------------------
    # Setup channels to work
    # -------------------------------------------------------
    SELECTED_SERVER = host.settings("").guid
    assert CHANNELS_NAMES, host.tr("Необходимо выбрать каналы для работы!")
    selected_channels = get_channels(
        SELECTED_SERVER, parse_object_names(CHANNELS_NAMES)
    )

    # -------------------------------------------------------
    # Play sound
    # -------------------------------------------------------
    if PLAY_SOUND:
        reactions.add_executor(PlaySound(SOUND_NAME))

    # -------------------------------------------------------
    # Output reactions
    # -------------------------------------------------------

    if OUTPUT_ON:

        assert OUTPUT_ALGORITHM in ["type_1", "type_2", "type_3"], host.tr(
            'Output algorithm not in ["type_1", "type_2", "type_3"] '
        )
        if OUTPUT_ALGORITHM == "type_1":
            from reactions import OutputReactions
        elif OUTPUT_ALGORITHM == "type_2":
            from reactions import OutputReactionsII as OutputReactions
        else:
            from reactions import OutputReactionsIII as OutputReactions

        assert OUTPUTS, host.tr("Необходимо выбрать тревожные выходы")
        _outputs = get_outputs(parse_object_names(OUTPUTS))
        logger.debug("outputs objects found: %s", _outputs)

        output_reactions = OutputReactions(
            gpios=_outputs,
            delay=OUTPUT_DELAY,
            reaction_type=GLOBALS.get("OUTPUT_ACTION_TYPE"),
            delay_between_iterations=DELAY_BETWEEN_ITERATIONS,
        )
        reactions.add_executor(output_reactions)
        if OUTPUT_MAN_ACTIV not in [host.tr("Нет"), host.tr("нет")]:
            logger.debug("Output manual activation key is %s", OUTPUT_MAN_ACTIV)
            host.activate_on_shortcut(
                OUTPUT_MAN_ACTIV, output_reactions.manual_activation_of_outputs
            )

    # -------------------------------------------------------
    # Operations with physical system control ("СКУД")
    # -------------------------------------------------------

    if ACS_ENBL:
        from reactions import AccessControlOperations

        assert ACS_TYPE in ["Sigur", "Orion"], "ACS_TYPE must be Sigur or Orion"
        assert ACS_DOOR, host.tr("Необходимо указать название точки доступа")

        acs_door_obj = host.object(ACS_DOOR)

        if ACS_TYPE == "Sigur":
            assert hasattr(
                acs_door_obj, "workmode_alwaysopen"
            ), "{} не является точкой доступа Sigur. Только одно имя м.б. указано".format(
                ACS_DOOR
            )
        if ACS_TYPE == "Orion":
            assert hasattr(
                acs_door_obj, "grant_access_once"
            ), "{} не является точкой доступа Orion. Только одно имя м.б. указано".format(
                ACS_DOOR
            )

        assert ACS_LOGIC in [
            host.tr("открыть дверь"),
            host.tr("закрыть дверь"),
        ], host.tr("Тип работы должен быть 'открыть дверь' или 'закрыть дверь'")

        assert 1 < ACS_DELAY < 3600, host.tr(
            "Время открытого/закрытого состояния двери должно быть в диапазоне [1, 3600] сек"
        )

        aco = AccessControlOperations(
            access_point_name=ACS_DOOR,
            access_point_type=ACS_TYPE,
            operation_type=ACS_LOGIC,
            delay_operations=ACS_DELAY,
        )
        reactions.add_executor(aco)

        if ACS_MAN_ACTIV not in [host.tr("Нет"), host.tr("нет")]:
            host.activate_on_shortcut(ACS_MAN_ACTIV, aco.manual_activation)

    # -------------------------------------------------------
    # Show channel in Alarm Monitor
    # -------------------------------------------------------

    def template_exists(template_name):
        for sett in host.settings("templates").ls():
            if sett.name == template_name:
                return True

    if SHOW_CHAN:
        from reactions import AlarmMonitorManager

        assert AM_ALARM_TEMPLATE, host.tr("Тревожный шаблон не выбран!")
        assert template_exists(AM_ALARM_TEMPLATE), "{txt}: {template_name}".format(
            txt=host.tr("Шаблон не найден"), template_name=AM_ALARM_TEMPLATE
        )
        if AM_TYPE == host.tr("Отобразить канал"):
            am_type = 1
        elif AM_TYPE == host.tr("Открыть момент в архиве"):
            am_type = 2
            AM_MAX_CHANS = 1
        else:
            logger.error("AM_TYPE wrong value: %s", AM_TYPE)
            am_type = 1

        am_manager = AlarmMonitorManager(
            AM_ALARM_TEMPLATE,
            am_type,
            AM_MAX_CHANS,
            display_duration=AM_DISPLAY_DURATION,
            base_template=AM_BASE_TEMPLATE,
            no_motion_check=AM_NO_MOTION_CHECK,
        )

        am_manager.create_monitor(AM_MON)

        reactions.add_executor(am_manager)
        if AM_CHANGE_TEMPLATE_CHECK:
            logger.debug("Drop template enabled")
            host.activate_on_gui_event("", am_manager.drop_template)

    # -------------------------------------------------------
    # Show message
    # -------------------------------------------------------
    if SHOW_MESSAGE:
        from reactions import ShowMessage

        reactions.add_executor(ShowMessage(show_message_delay=SHOW_MESSAGE_DELAY))

    # -------------------------------------------------------
    # Show popup window
    # -------------------------------------------------------
    if GLOBALS.get("SHOW_POPUP"):
        from reactions import ShowPopup

        mon_popup = GLOBALS.get("MON_POPUP", 1)
        reactions.add_executor(ShowPopup(monitor_to_show_archive_from_popup=mon_popup))

    # -------------------------------------------------------
    # Fire event
    # -------------------------------------------------------
    random_guid = host.random_guid()
    reactions.add_executor(
        FireEvent(name="AutoUniversal-{}".format(random_guid), guid=random_guid)
    )

    # -------------------------------------------------------
    # Al senders
    # -------------------------------------------------------
    ALL_SENDERS = []

    # -------------------------------------------------------
    # Initializing email sender
    # -------------------------------------------------------
    if SEND_SCREEN_EMAIL or SEND_EMAIL:
        from senders import AdoptedEmailSender
        from email_sender import EmailSender

        assert EMAIL_ACCOUNT, host.tr("Учетная запись e-mail в Trassir не задана")
        assert EMAIL_ADDRESSES, host.tr("Получатели почтовых уведомлений не заданы")
        mail_sender = EmailSender(EMAIL_ACCOUNT)

        if SEND_SCREEN_EMAIL:
            ALL_SENDERS.append(
                AdoptedEmailSender(
                    mail_sender=mail_sender, email_recipients=EMAIL_ADDRESSES
                )
            )
        else:
            from reactions import MailTextSender

            reactions.add_executor(MailTextSender(mail_sender, EMAIL_ADDRESSES))

    # -------------------------------------------------------
    # Initializing ftp sender
    # -------------------------------------------------------
    if SEND_FTP:
        from ftp import FTPClient
        from senders import AdoptedFTPSender

        ftp_c = FTPClient(
            FTP_HOST,
            FTP_PORT,
            FTP_USER,
            FTP_PASSWD,
            FTP_PATH,
            passive_mode=FTP_PASSIVE_MODE,
        )
        ALL_SENDERS.append(AdoptedFTPSender(ftp_c))

    # -------------------------------------------------------
    # Initializing Telegram sender
    # -------------------------------------------------------

    TG_IDS = GLOBALS.get("TG_IDS")

    if SEND_SCREEN_TELEGRAM:
        from senders import AdoptedTelegramSender

        assert TG_IDS, host.tr("Необходимо указать Ваш Telegram id")
        host.exec_encoded(tbot_service)
        tbot_api = TBotAPI()
        telegram_users = tbot_api.prepare_users(TG_IDS)
        ALL_SENDERS.append(AdoptedTelegramSender(tbot_api, telegram_users))

    # -------------------------------------------------------
    # Reactions with screenshots add here
    # -------------------------------------------------------

    BASE_SCREENSHOT_FOLDER = os.path.normpath(
        os.path.join(
            host.settings("system_wide_options")["screenshots_folder"],
            "AutoUniversal_{script_guid}".format(
                script_guid=host.stats().parent().guid
            ),
        )
    )
    DAYS_TO_STORE = int(GLOBALS.get("DAYS_TO_STORE", 5))
    SAVE_SCREEN = GLOBALS.get("SAVE_SCREEN", False)
    FIGURES = GLOBALS.get("FIGURES", False)

    if SEND_SCREEN_EMAIL or SEND_FTP or SAVE_SCREEN or SEND_SCREEN_TELEGRAM:
        from shot_saver import ShotSaver
        from reactions import ReactionsWithScreenshots

        SAVE_SCREEN_DELTA = GLOBALS.get("SAVE_SCREEN_DELTA", 0)
        assert 0 <= SAVE_SCREEN_DELTA <= 7, "save_screen_delta should be in [0, 7]"
        ONLINE_SHOT = GLOBALS.get("ONLINE_SHOT", False)
        reactions_with_screenshots = ReactionsWithScreenshots(
            delta=SAVE_SCREEN_DELTA,
            base_folder=BASE_SCREENSHOT_FOLDER,
            online_shot=ONLINE_SHOT,
            save_screen=SAVE_SCREEN,
            figures=FIGURES,
        )

        shot_saver_obj = ShotSaver()
        shot_saver_obj.max_tries = 4
        reactions_with_screenshots.shot_saver_obj = shot_saver_obj
        for sender in ALL_SENDERS:
            reactions_with_screenshots.add_sender(sender=sender)

        # Add all senders to send screenshots
        reactions.add_executor(reactions_with_screenshots)

        if DAYS_TO_STORE:
            from delete_old_shots import Worker

            shot_cleaner = Worker(BASE_SCREENSHOT_FOLDER, DAYS_TO_STORE)
            shot_cleaner.run()

    # -------------------------------------------------------
    # LPR handler
    # -------------------------------------------------------

    LIST_TYPE = GLOBALS.get("LIST_TYPE")
    direction = GLOBALS.get("DIRECTION")
    hw_det_enable = GLOBALS.get("HW_DET_ENABLE")
    list_name = GLOBALS.get("NAME_LIST")
    if list_name:
        list_name = [x.strip() for x in list_name.split(",")]
    repeat_ev_delay = GLOBALS.get("REPEAT_EV_DELAY")

    if LIST_TYPE == host.tr("не распознан"):
        from lpr_handler import NotRecognizedHandler as LprHandler
    else:
        from lpr_handler import LprHandler

    lpr_handler = LprHandler(
        channels_objs=selected_channels,
        direction=direction,
        hw_detector=hw_det_enable,
        list_type=LIST_TYPE,
        list_name=list_name,
        make_reactions=reactions.make_reactions,
        repeat_ev_delay=repeat_ev_delay,
    )
    # plates_from_files(lpr_handler.list_type)
    host.activate_on_lpr_events(lpr_handler.event_handler)
