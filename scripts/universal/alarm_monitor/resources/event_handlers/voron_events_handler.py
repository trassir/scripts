# -*- coding: utf-8 -*-

import json

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

try:
    from constants import EVENTS_TRANSLATION
except ImportError as err:
    logger.error("Can't import EVENTS_TRANSLATION")

from base_utils import BaseUtils
import host


VORORON_CODES_TO_EVENTS = {
    -1: host.tr("Рубеж: {boundary}. Зона {zone}. Зона снята с охраны."),
    0: host.tr("Рубеж: {boundary}. Зона {zone}. Зона поставлена на охрану"),
    1: host.tr("Рубеж: {boundary}. Зона {zone}. Тревога 1."),
    2: host.tr("Рубеж: {boundary}. Зона {zone}. Тревога 2."),
    3: host.tr("Рубеж: {boundary}. Зона {zone}. Тревога 3."),
    4: host.tr("Рубеж: {boundary}. Зона {zone}. Тревога 4."),
    5: host.tr("Рубеж: {boundary}. Зона {zone}. Тревога 5."),
    11: host.tr("Рубеж: {boundary}. Зона {zone}. Ручное подтверждение тревоги 1."),
    12: host.tr("Рубеж: {boundary}. Зона {zone}. Ручное подтверждение тревоги 2."),
    13: host.tr("Рубеж: {boundary}. Зона {zone}. Ручное подтверждение тревоги 3."),
    14: host.tr("Рубеж: {boundary}. Зона {zone}. Ручное подтверждение тревоги 4."),
    15: host.tr("Рубеж: {boundary}. Зона {zone}. Ручное подтверждение тревоги 5."),
    21: host.tr("Рубеж: {boundary}. Зона {zone}. Авт. подтверждение тревоги 1."),
    22: host.tr("Рубеж: {boundary}. Зона {zone}. Авт. подтверждение тревоги 2."),
    23: host.tr("Рубеж: {boundary}. Зона {zone}. Авт. подтверждение тревоги 3."),
    24: host.tr("Рубеж: {boundary}. Зона {zone}. Авт. подтверждение тревоги 4."),
    25: host.tr("Рубеж: {boundary}. Зона {zone}. Авт. подтверждение тревоги 5."),
    255: host.tr("Рубеж: {boundary}. Зона {zone}. Неисправность зоны."),
}


def make_alarm_message(channel_name, dt, event_code, zone, boundary):
    """

    Args:
        channel: str
        dt: DateTime
        event_code: int
        zone: int
        boundary: int

    Returns: dict

    """
    dt = dt.strftime("%d-%m-%Y %H:%M:%S")
    event_description = VORORON_CODES_TO_EVENTS.get(int(event_code))
    message = event_description.format(
        zone=zone, boundary=boundary
    )

    text_channel = host.tr("Канал")

    alarm_messages = {
        "alert_message": "{event_time}<br><b><font color='red'>{message}"
        "</font></b><br>{text_channel}: {channel_name}".format(
            event_time=dt,
            message=message,
            text_channel=text_channel,
            channel_name=channel_name,
        ),
        "sms_message": "{event_time}. {message}"
        ". {text_channel}:{channel_name}".format(
            event_time=dt,
            message=message,
            text_channel=text_channel,
            channel_name=channel_name,
        ),
        "mail_message": "{event_time}. {message}"
        ". {text_channel}: {channel_name}".format(
            event_time=dt,
            message=message,
            text_channel=text_channel,
            channel_name=channel_name,
        ),
    }

    return alarm_messages


class VoronEventsHandler:
    def __init__(self, voron_codes_to_react, obj_storage, callback=None):
        """Обработка событий скрипта интеграции с системой ворон

        Args:
            voron_codes_to_react (Set):
            obj_storage (ObjectsStorage): ObjectsStorage instance
            callback (`function`, optional):
        """
        self.voron_codes_to_react = voron_codes_to_react
        self.obj_storage = obj_storage
        self.callback = callback

    def check_channel(self, channel):
        res = False
        if not self.obj_storage.all_channels_in_work:
            res = channel in self.obj_storage.channels
        return self.obj_storage.all_channels_in_work or res

    def event_handler(self, event):
        logger.debug("event type: %s, origin: %s, p1: %s, p2: %s ts: %s",
                     event.type, event.origin, event.p1, event.p2, event.ts)

        channel_full = event.p2

        channel = channel_full.split("_")[0]
        if not self.check_channel(channel):
            logger.debug("channel %s not in channels list, return", channel)
            return

        channel_obj = self.obj_storage.channels.get(channel)
        if not channel_obj:
            logger.debug("channel object not found: %s, return", channel)
            return

        ev_data = json.loads(event.data)
        logger.debug("channel_full: %s, event data: %s", channel_full, ev_data)
        try:
            event_code = int(ev_data["event_code"])
            zone = int(ev_data["zone"])
            boundary = int(ev_data["boundary"])
            event_ts = int(ev_data["ts"])
        except KeyError as err:
            logger.error(err)
            return

        if event_code not in self.voron_codes_to_react:
            logger.debug(
                "event code (%s) not in event codes (%s)",
                event_code,
                self.voron_codes_to_react,
            )
            return

        if self.callback:
            alarm_messages = make_alarm_message(
                channel_obj.name, BaseUtils.ts_to_dt(event_ts), event_code, zone, boundary
            )
            self.callback(channel_full, event_ts, alarm_messages)
