# -*- coding: utf-8 -*-
from collections import namedtuple

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

import time
from __builtin__ import object as py_object
import host
from base_utils import BaseUtils


def get_alarm_message(chan_name, tmstmp, plate, plate_comment, list_name):
    """
    Args:
        chan_name (str): channel name
        tmstmp (long): Trassir timestamp
        plate (str): plate from event or recognized plate
        plate_comment (str): plate comment
        list_name (str): list_name
    Returns:
           'dict'
    """
    alarm_messages = {}
    event_time = BaseUtils.ts_to_dt(tmstmp)
    plate = plate.upper()

    if plate_comment:
        plate_comment_alarm_message = "<br>Комментарий: {}.".format(plate_comment)
        plate_comment_mail_message = " Комментарий: {}.".format(plate_comment)
    else:
        plate_comment_alarm_message = ""
        plate_comment_mail_message = ""

    if list_name:
        list_name_alarm_message = "<br>Имя списка: {list_name}.".format(
            list_name=list_name
        )
        list_name_mail_message = " Имя списка: {list_name}.".format(list_name=list_name)
    else:
        list_name_alarm_message = ""
        list_name_mail_message = ""

    alarm_messages["alert_message"] = (
        "<br><b><font color='red'>{event_time} {event_type}</font></b>"
        "<br>{plate}{plate_comment}{list_name}"
        "<br>{on_channel}: {chan_name}"
    ).format(
        event_time=event_time.strftime("%H:%M:%S"),
        event_type=host.tr("Распознан номер"),
        plate=plate,
        plate_comment=plate_comment_alarm_message,
        on_channel=host.tr("Канал"),
        chan_name=chan_name,
        list_name=list_name_alarm_message,
    )

    alarm_messages["sms_message"] = (
        "{event_time}.{event_type}:{plate}{plate_comment}.{on_channel}:{chan_name}"
    ).format(
        event_time=event_time.strftime("%d-%m-%Y %H:%M:%S"),
        event_type=host.tr("Распознан номер"),
        plate=plate,
        plate_comment=plate_comment,
        on_channel=host.tr("Канал"),
        chan_name=chan_name,
    )

    alarm_messages["mail_message"] = (
        "{event_time}. {event_type}: {plate}.{plate_comment}{list_name} {on_channel}: {chan_name}"
    ).format(
        event_time=event_time.strftime("%d-%m-%Y %H:%M:%S"),
        event_type=host.tr("Распознан номер"),
        plate=plate,
        plate_comment=plate_comment_mail_message,
        on_channel=host.tr("Канал"),
        chan_name=chan_name,
        list_name=list_name_mail_message,
    )
    return alarm_messages


def make_file_name(chan_name, tmstmp, plate):
    event_time = BaseUtils.ts_to_dt(tmstmp)
    plate = plate.replace("?", "_")
    plate = plate.upper()
    return r"{} ({})({}).jpg".format(
        chan_name, event_time.strftime("%Y.%m.%d %H-%M-%S"), plate
    )


SearchResult = namedtuple(
    "SearchResult",
    ["FOUND_IN_A_LIST", "NOT_FOUND_IN_ANY_LIST", "FOUND_IN_THE_DESIRED_LIST"],
)
search_result = SearchResult(
    FOUND_IN_A_LIST="Plate found in a list",
    NOT_FOUND_IN_ANY_LIST="Not found in any list",
    FOUND_IN_THE_DESIRED_LIST="Found in the desired list",
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
            host.tr("чёрном"): [0],
            host.tr("белом"): [2],
            host.tr("информационном"): [1],
            host.tr("любом"): [0, 1, 2],
            host.tr("нет в списках"): [-1],
            host.tr("любой номер"): [-1, 0, 1, 2],
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

    def which_list(self, ev):
        found = search_result.NOT_FOUND_IN_ANY_LIST
        emblist_names = []

        if not hasattr(ev, "matched_embrecords_history"):
            logger.error(
                "The software version is outdated, update the software for script 'Auto universal' to work correctly."
            )
            return
        if ev.matched_embrecords_history or ev.matched_extlists_history:
            # found in any list
            found = search_result.FOUND_IN_A_LIST

        # check internal list
        for embrecord, emblist in ev.matched_embrecords_history:
            if emblist.reaction in self.list_type:
                if self.list_name and emblist.name not in self.list_name:
                    logger.debug(
                        "list name (%s) not in list: %s", emblist.name, self.list_name
                    )
                    continue
                # if here found in desired list
                logger.debug(
                    "found in desired internal list: %s with reaction: %s",
                    emblist.name,
                    emblist.reaction,
                )
                return (
                    search_result.FOUND_IN_THE_DESIRED_LIST,
                    emblist.reaction,
                    embrecord.comment,
                    emblist.name,
                )
            else:
                logger.debug(
                    "name: %s, emblist.reaction (%s) not in: %s",
                    emblist.name,
                    emblist.reaction,
                    self.list_type,
                )
                emblist_names.append(emblist.name)

        # not found in internal list
        logger.debug("in internal list not found")

        # check external lists
        for extlists in ev.matched_extlists_history:
            try:
                emblist_names.append(extlists["list_name"])
                if extlists["reaction"] in self.list_type:
                    if self.list_name and extlists["list_name"] not in self.list_name:
                        logger.debug(
                            "list name (%s) not in list: %s",
                            extlists["list_name"],
                            self.list_name,
                        )

                        continue
                    # if here found in desired list
                    logger.debug(
                        "found in desired external list: %s with reaction: %s",
                        extlists["list_name"],
                        extlists["reaction"],
                    )
                    return (
                        search_result.FOUND_IN_THE_DESIRED_LIST,
                        extlists.get("reaction"),
                        extlists.get("comment"),
                        extlists.get("list_name"),
                    )
                else:
                    logger.debug(
                        "name: %s, emblist.reaction (%s) not in: %s",
                        extlists["list_name"],
                        extlists["reaction"],
                        self.list_type,
                    )
            except Exception as err:
                logger.error(err)

        logger.debug("in external list not found")
        return found, "", "", emblist_names

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
        if len(plate) <= 3:
            logger.debug("plate to short, break")
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

        found, reaction, comment, list_name = self.which_list(event)

        if found == search_result.NOT_FOUND_IN_ANY_LIST and self.list_type[0] == -1:
            """Не найдено в списках, так и надо. Вызываем реакцию"""
            alarm_message = get_alarm_message(
                chan_name=getattr(self.channels.get(channel), "name"),
                tmstmp=tmstmp,
                plate=plate,
                plate_comment="",
                list_name="",
            )

        elif found == search_result.FOUND_IN_THE_DESIRED_LIST:
            """ Найден в списке который удовлетворяет заданному"""

            alarm_message = get_alarm_message(
                chan_name=getattr(self.channels.get(channel), "name"),
                tmstmp=tmstmp,
                plate=plate,
                plate_comment=comment,
                list_name=list_name,
            )
        elif self.list_type == [-1, 0, 1, 2]:
            alarm_message = get_alarm_message(
                chan_name=getattr(self.channels.get(channel), "name"),
                tmstmp=tmstmp,
                plate=plate,
                plate_comment=comment,
                list_name=list_name,
            )
        else:
            logger.debug("found result: %s, break", found)
            return

        shot_name = make_file_name(
            getattr(self.channels.get(channel), "name"), tmstmp, plate
        )
        logger.debug("shot_name: %s", shot_name)

        self.make_reactions(
            self.channels.get(channel), tmstmp, alarm_message, shot_name=shot_name
        )
