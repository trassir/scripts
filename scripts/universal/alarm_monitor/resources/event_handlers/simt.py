# -*- coding:utf-8 -*-

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

try:
    from constants import EVENTS_TRANSLATION
except ImportError as err:
    logger.error("Can't import EVENTS_TRANSLATION")


import time
from datetime import datetime
from __builtin__ import object as py_object
import host
from base_utils import BaseUtils
import localization as loc


# ---------------------------------------------------------------------
# simt events handler module
# ---------------------------------------------------------------------


def utc_offset(server_guid):
    _utc_offset = 0
    try:
        _utc_offset = host.settings(
            "/{server_guid}/system_wide_options".format(server_guid=server_guid)
        )["utc_offset_minutes"]
    except (IndexError, KeyError) as err:
        logger.error("can't get utc offset. Error: %s", err)
    return _utc_offset


def make_alarm_message(channel_name, event_type, zone_or_border, tmstmp):
    zone_or_border_name = zone_or_border.name
    dt = datetime.fromtimestamp(tmstmp / 1e6)
    ev_translation = EVENTS_TRANSLATION.get(event_type, "Unknown")

    if "Border" in event_type:
        zone_or_border_text = loc.simt.border_name
    else:
        zone_or_border_text = loc.simt.zone_name

    alarm_messages = {
        "alert_message": "<br><b><font color='red'>{event_type}</font></b><br>{event_time}"
        "<br>{zone_or_border_text}:<br>{zone_or_border_name}. <br>{on_channel}: {chan_name}".format(
            event_time=dt.strftime("%H:%M:%S"),
            event_type=ev_translation,
            zone_or_border_text=zone_or_border_text,
            zone_or_border_name=zone_or_border_name,
            on_channel=loc.simt.associated_channel,
            chan_name=channel_name,
        ),
        "sms_message": "{event_type}: {zone_or_border_name}. {on_channel}: {chan_name}".format(
            event_type=ev_translation,
            zone_or_border_name=zone_or_border_name,
            on_channel=loc.simt.associated_channel,
            chan_name=channel_name,
        ),
        "mail_message": "{event_time}. {event_type}. {zone_or_border_text}: {zone_or_border_name}."
        " {on_channel}: {channel_name}.".format(
            event_time=dt.strftime("%Y.%m.%d %H:%M:%S"),
            zone_or_border_text=zone_or_border_text,
            zone_or_border_name=zone_or_border_name,
            event_type=ev_translation,
            on_channel=loc.simt.associated_channel,
            channel_name=channel_name,
        ),
    }
    return alarm_messages


class SpamEvent(py_object):
    def __init__(self, same_event_delay):
        self.events = {}
        self.same_event_delay = same_event_delay

    def is_pam(self, event):
        now = time.time()
        if not self.events.get(event.origin_object.associated_channel):
            logger.debug(
                "new channel in spam: %s", event.origin_object.associated_channel
            )
            self.events[event.origin_object.associated_channel] = {}

        if not self.events[event.origin_object.associated_channel].get(event.type):
            logger.debug("new event type: %s", event.type)
            self.events[event.origin_object.associated_channel][event.type] = {}

        if not self.events[event.origin_object.associated_channel][event.type].get(
            event.origin_object.guid
        ):
            logger.debug("new zone: %s", event.origin_object.guid)
            self.events[event.origin_object.associated_channel][event.type][
                event.origin_object.guid
            ] = now
            return

        diff = (
            now
            - self.events[event.origin_object.associated_channel][event.type][
                event.origin_object.guid
            ]
        )
        logger.debug("event diff: %s, event_delay: %s", diff, self.same_event_delay)
        if diff < self.same_event_delay:
            return True
        else:
            logger.debug("event time: %s", now)
            self.events[event.origin_object.associated_channel][event.type][
                event.origin_object.guid
            ] = now


class SimtHandler(py_object):
    """Класс для работы по событиям от SIMT детектора,
     этот же хендлер используется для обработки событий "Object Entered the Zone"
     и Object Left the Zone от нейродетектора

             Args:
                 obj_storage (ObjectsStorage): ObjectsStorage instance
                 simt_borders_guid_list (:obj:`list['str']`, optional): гуиды границ SIMT,
                    пересечение которых обрабатывается в event_handler
                 border_alarm_dir (str): направление пересечения, может быть:
                     A -> B, B -> A или любое.
                 check_zones(:obj:`str`): имена зон для работы, поле может быть пустым.
                 size_alarm(bool): тревога по размеру объекта.
                 speed_alarm(bool): тревога по скорости объекта.
                 length_alarm(bool): тревога по размеру объекта.
                 enter_alarm(:obj:`str`): имена зон при вхождении объекта в которые
                    вызывается реакция.
                 leave_alarm(:obj:`str`): имена зон при выходе объекта из
                    которых вызывается реакция.
                 presence_check(bool): тревога при длительном присутствии объекта в зоне.
                 presence_delay(int): длительность нахождения объекта в зоне
                    перед вызовом реакции
                 events_translation(dict): словарь соответствия английских
                  названий событий русским
                 callback(): функция вызываемая при наступлении события, туда передаётся
                                    метод Reaction.make_reactions()

             self.events_info - dict для хранения timestamp события, события делятся по типу,
              каналу, зоне (если событие связано с зоной).
             Образец вида переменонной:
             self.events_info = {"channnel_guid":
                                        {"Object Entered the Zone": {"zone_name": "timestamp"},
                                         "Object Left the Zone": {"zone_name": "timestamp"},
                                         "Border Crossed": {"border_name": "timestamp"},
                                         "Object Track Length Alarm": "timestamp",
                                         "Object Size Alarm": "timestamp",
                                         },
                                    "channel_2_guid": {"Object Entered the Zone": "e.t.c..."}
                                    }
             """

    def __init__(
        self,
        obj_storage,
        simt_borders_guid_list=None,
        border_alarm_dir=None,
        size_alarm=False,
        speed_alarm=False,
        length_alarm=False,
        presence_check=False,
        presence_delay=10,
        events_translation=None,
        callback=None,
        similar_events_delay=5,
    ):

        self.obj_storage = obj_storage
        self._simt_borders_guid_list = None
        self.simt_borders_guid_list = simt_borders_guid_list
        self.border_alarm_dir = border_alarm_dir
        self.size_alarm = size_alarm
        self.size_alarm = size_alarm
        self.speed_alarm = speed_alarm
        self.length_alarm = length_alarm

        self.presence_check = presence_check
        self.presence_delay = presence_delay
        self._events_translation = None
        self.events_translation = events_translation
        self.callback = callback
        self.is_spam = SpamEvent(similar_events_delay).is_pam

        self.zones_with_objects_presense = []
        self._zones_check_enter_names = []
        self._zones_check_leave_names = []
        self._zones_check_names = []
        self.events_info = {}

    @property
    def simt_borders_guid_list(self):
        if self._simt_borders_guid_list:
            return self._simt_borders_guid_list
        else:
            return []

    @simt_borders_guid_list.setter
    def simt_borders_guid_list(self, _borders):
        if _borders:
            self._simt_borders_guid_list = _borders
        else:
            self._simt_borders_guid_list = []

    @property
    def zones_check_enter_names(self):
        return self._zones_check_enter_names

    @zones_check_enter_names.setter
    def zones_check_enter_names(self, zones_names):
        if zones_names:
            self._zones_check_enter_names = zones_names.split(",")
        else:
            self._zones_check_enter_names = []
        logger.debug("Zones to check enter: {}".format(self.zones_check_enter_names))

    @property
    def zones_check_leave_names(self):
        return self._zones_check_leave_names

    @zones_check_leave_names.setter
    def zones_check_leave_names(self, zones_names):
        if zones_names:
            self._zones_check_leave_names = zones_names.split(",")
        else:
            self._zones_check_leave_names = []
        logger.debug("Zones to check leave: {}".format(self.zones_check_leave_names))

    @property
    def zones_check_names(self):
        return self._zones_check_names

    @zones_check_names.setter
    def zones_check_names(self, zones_check_names):
        if zones_check_names:
            self._zones_check_names = zones_check_names.split(",")
        else:
            self._zones_check_names = []

    def check_channel(self, channel):
        res = False
        if not self.obj_storage.all_channels_in_work:
            res = channel in self.obj_storage.channels
        return self.obj_storage.all_channels_in_work or res

    def does_zone_already_exists(self, guid):
        for some_zone in self.zones_with_objects_presense:
            if some_zone.get("guid", "unknown") == guid:
                return True

    def append_new_zone_for_observe(self, event):
        if (
            not self.does_zone_already_exists(event.origin_object.guid)
            and not hasattr(event.origin_object, "objects_crossing")
            and (
                not self.zones_check_names
                or event.origin_object.name in self.zones_check_names
            )
        ):
            self.zones_with_objects_presense.append(
                {
                    "zone_guid": event.origin_object.guid,
                    "timer": 0,
                    "channel_guid": event.origin_object.associated_channel.split("_")[
                        0
                    ],
                }
            )

    def check_zones_with_objects_presence(self):
        """ Check long presence of an objects on the zones.
        Works in a loop

        """
        if not self.presence_check:
            return
        logger.debug("simt_zones:: {}".format(self.zones_with_objects_presense))

        for zone in self.zones_with_objects_presense:
            try:
                if (
                    host.object(zone["guid"]).state("objects_inside")
                    != "No Objects in Zone"
                ):
                    zone["timer"] += 1
                    if zone["timer"] > self.presence_delay:

                        channel = zone["channel_guid"]
                        event_type = "Object presence alarm"
                        zone_or_border = zone["zone_guid"]
                        tmstmp = int(time.time())
                        zone["timer"] = 0

                        logger.debug(
                            "Object long-lasting presence alarm on channel: {}, zone: {}".format(
                                host.object(channel).name,
                                host.object(zone_or_border).name,
                            )
                        )

                        alarm_messages = make_alarm_message(
                            channel, event_type, zone_or_border, tmstmp
                        )
                        if self.callback:
                            self.callback(channel, tmstmp, event_type, alarm_messages)

                else:
                    zone["timer"] = 0
            except KeyError:
                self.zones_with_objects_presense.remove(zone)
        host.timeout(1000, self.check_zones_with_objects_presence)

    def handle_border_crossed(self, event):
        if event.origin_object.guid not in self.simt_borders_guid_list:
            logger.debug("Zone guid {} not in list".format(event.origin_object.guid))
            return
        if event.type == "Border Crossed A -> B" and self.border_alarm_dir == "A -> B":
            return True
        if event.type == "Border Crossed B -> A" and self.border_alarm_dir == "B -> A":
            return True
        if self.border_alarm_dir == loc.simt.any:
            return True

    def event_handler(self, event):
        """Принмает события от SIMT и
        события Object Entered the Zone и Object Left the Zone от нейродетектора
        Проверка для событий Entered the Zone и Object Left the Zone осуществляется по
        имени зоны, а не по гуиду. Т.е. если есть нескольколько зон с одинаковыми
        названиями на разных каналах, то событие от разных зон с одинаковыми
        названиями будет пропущено через фильтр.
        """
        # logger.debug("Start handle SIMT events, event type is: {}".format(event.type))
        try:
            make_reaction = False
            event_type = event.type
            channel = event.origin_object.associated_channel.split("_")[0]
            server = event.origin_object.associated_channel.split("_")[1]
            zone_or_border = event.origin_object

            if not self.check_channel(channel):
                logger.debug("channel %s not in channels list", channel)
                return

            logger.debug(
                "SIMT event. type: %s, channel: %s, zone or border: %s %s",
                event.type,
                event.origin_object.associated_channel,
                event.origin_object.name,
                event.origin_object.guid,
            )

            channel_obj = self.obj_storage.channels.get(channel)
            if not channel_obj:
                logger.debug("channel object not found: %s, return", channel)
                return

            if (
                event_type == "Object Entered the Zone"
                and event.origin_object.name in self.zones_check_enter_names
            ):
                make_reaction = True

            if (
                event_type == "Object Left the Zone"
                and event.origin_object.name in self.zones_check_leave_names
            ):
                make_reaction = True

            if "Border Crossed" in event_type:
                make_reaction = self.handle_border_crossed(event)

            if event.origin_object.name in self.zones_check_names:
                logger.debug(
                    "object name: %s in working zones: %s",
                    event.origin_object.name,
                    self.zones_check_names,
                )

                if event_type == "Object presence alarm":
                    self.append_new_zone_for_observe(event)

                if event_type == "Object Track Length Alarm" and self.length_alarm:
                    make_reaction = True

                if event_type == "Object Size Alarm" and self.size_alarm:
                    make_reaction = True

                if event_type == "Object Speed Alarm" and self.speed_alarm == True:
                    make_reaction = True

            if make_reaction and self.callback:
                _spam_event = self.is_spam(event)
                logger.debug("spam event: %s", _spam_event)
                if _spam_event:
                    logger.debug("Spam event detected, ignoring")
                    return

                ts = event.ts - utc_offset(server) * 60 * 1e6

                channel_full = event.origin_object.associated_channel
                alarm_messages = make_alarm_message(
                    channel_obj.name, event_type, zone_or_border, ts
                )
                self.callback(channel_full, ts, alarm_messages)
        except Exception as err:
            logger.exception("Error occurred in simt handler: %s", err)
