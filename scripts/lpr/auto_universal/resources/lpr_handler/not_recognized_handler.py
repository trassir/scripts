# -*-coding: utf-8 -*-

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

import time
from __builtin__ import object as py_object
import host
from base_utils import BaseUtils


def get_alarm_message(chan_name, tmstmp):
    event_time = BaseUtils.ts_to_dt(tmstmp)

    alarm_messages = {"alert_message": (
        "<br><b><font color='red'>{event_time} {event_type}</font></b>"       
        "<br>{on_channel}: {chan_name}"
    ).format(
        event_time=event_time.strftime("%H:%M:%S"),
        event_type=host.tr("Номер не распознан"),
        on_channel=host.tr("Канал"),
        chan_name=chan_name,
    ),

     "sms_message": (
        "{event_time}.{event_type}. {on_channel}:{chan_name}"
    ).format(
        event_time=event_time.strftime("%d-%m-%Y %H:%M:%S"),
        event_type=host.tr("Номер не распознан"),
        on_channel=host.tr("Канал"),
        chan_name=chan_name,
    ),

     "mail_message": (
        "{event_time}. {event_type}. {on_channel}: {chan_name}"
    ).format(
        event_time=event_time.strftime("%d-%m-%Y %H:%M:%S"),
        event_type=host.tr("Номер не распознан"),
        on_channel=host.tr("Канал"),
        chan_name=chan_name,

    )}
    return alarm_messages


def make_file_name(chan_name, tmstmp):
    event_time = BaseUtils.ts_to_dt(tmstmp)
    return r"{} ({}).jpg".format(
        chan_name, event_time.strftime("%Y.%m.%d %H-%M-%S"),
    )


class LprHandler(py_object):
    def __init__(
        self,
        channels_objs,
        direction,
        hw_detector,
        list_type,
        list_name="",
        make_reactions=None,
        repeat_ev_delay=10,
    ):
        self._channels = {}
        self.channels = channels_objs
        self._direction = ""
        self.direction = direction
        self.hw_detector = hw_detector
        self._list_type = []
        self.list_type = list_type
        self.list_name = list_name
        self.make_reactions = make_reactions
        self.repeat_ev_delay = repeat_ev_delay
        self.last_even_reaction = {"plate": 0, "time": 0}

        logger.debug(
            "Channels: %s, direction: %s"
            " list type: %s, repeat event delay: %s\n"
            " list types: 0 - black, 2 - white, 1 - info, -1 - not in list, [0, 1, 2] - any list,"
            " [-1, 0, 1, 2] - any plate",
            channels_objs,
            direction,
            self.list_type,
            self.repeat_ev_delay,
        )

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, _channels_objs):
        if not _channels_objs:
            raise ValueError("Channels can't be empty")
        self._channels = {chan_obj.guid: chan_obj for chan_obj in _channels_objs}
        logger.debug(
            "Channels_to_work: %s",
            {chan_obj.guid: chan_obj.name for chan_obj in _channels_objs},
        )

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction_to_work):
        if direction_to_work not in [
            host.tr("вниз"),
            host.tr("вверх"),
            host.tr("любое"),
        ]:
            raise ValueError(
                "{text}: {direction}".format(
                    text=host.tr("Не правильный тип направления движения авто"),
                    direction=direction_to_work,
                )
            )
        direction_types = {
            host.tr("вниз"): [2],
            host.tr("вверх"): [1],
            host.tr("любое"): [1, 2],
        }
        self._direction = direction_types[direction_to_work]
        logger.debug("direction to work: %s", self._direction)

    @property
    def list_type(self):
        return self._list_type

    @list_type.setter
    def list_type(self, list_type_to_react):
        all_types_of_lists = {
            host.tr("не распознан"): [-100],
        }
        _list_type = all_types_of_lists.get(list_type_to_react)
        if _list_type is None:
            raise ValueError(host.tr("Тип списка не установлен"))
        else:
            self._list_type = _list_type

    def is_direction_right(self, event_flag):
        direction = (event_flag & host.LPR_DOWN) or (event_flag & host.LPR_UP)
        if direction in self.direction:
            return True
        if self.hw_detector:
            return True

    def is_similar_event(self, plate, tmstmp):
        time_diff = (tmstmp - self.last_even_reaction["time"]) / 1e6
        similar_plate = False

        if (
            self.last_even_reaction["plate"] == plate
            and time_diff < self.repeat_ev_delay
        ):
            logger.debug("Time diff: %s, similar event detected, break.", time_diff)
            similar_plate = True
        self.last_even_reaction["plate"] = plate
        self.last_even_reaction["time"] = tmstmp

        return similar_plate

    def event_handler(self, event):
        plate = event.plate
        tmstmp = event.time_bestview
        channel = event.channel
        event_flag = event.flags
        dt_bw = BaseUtils.ts_to_dt(tmstmp)
        logger.debug("Plate in event: %s, time best_view: %s", plate, dt_bw)

        if channel not in self.channels:
            logger.debug("channel %s not in channels list", channel)
            return

        if time.time() - tmstmp / 1e6 > 60:
            logger.debug("Event ignoring, because it too old")
            return
        if len(plate) > 1:
            logger.debug("plate recognized")
            return
        if self.is_similar_event(plate, tmstmp):
            return
        if not self.is_direction_right(event_flag):
            logger.debug("Wrong direction, break. Event flag: %s", event_flag)
            return

        channel_full_guid = None
        if self.channels.get(channel):
            channel_full_guid = getattr(self.channels.get(channel), "full_guid")
        logger.debug("full guid %s", channel_full_guid)

        alarm_message = get_alarm_message(
                chan_name=getattr(self.channels.get(channel), "name"),
                tmstmp=tmstmp,
            )

        shot_name = make_file_name(
            getattr(self.channels.get(channel), "name"), tmstmp
        )
        logger.debug("shot_name: %s", shot_name)

        self.make_reactions(
            self.channels.get(channel), tmstmp, alarm_message, shot_name=shot_name
        )