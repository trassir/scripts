# -*- coding:utf-8 -*-

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

import time
from datetime import datetime
from base_utils import BaseUtils
import localization as loc


# ---------------------------------------------------------------------------
# GPIO operations
# ---------------------------------------------------------------------------


class InputStateChangeHandler:
    """Класс для обработки событий от тревожных входов
    Args:
        events_translation (dict): словарь соответствия английских названий русским
        input_high_to_low_enable (bool): включить тревогу при размыкании тревожного входа
        input_low_to_high_enable (bool): включить тревогу при замыкании тревожного входа

    """

    def __init__(
        self,
        events_translation,
        input_high_to_low_enable,
        input_low_to_high_enable,
        callback=None,
    ):
        self.events_translation = events_translation
        self.input_high_to_low_enable = input_high_to_low_enable
        self.input_low_to_high_enable = input_low_to_high_enable
        self.callback = callback

    def make_alarm_message(self, channel_name, input_guid, event_type, tmstmp):

        input_name = BaseUtils.get_object_name_by_guid(input_guid)

        alarm_messages = {}
        event_time = datetime.fromtimestamp(tmstmp/1e6)
        ev_translation = self.events_translation.get(event_type, "Unknown")

        alarm_messages["alert_message"] = (
            "<br><b><font color='red'>{event_type}</font></b><br>{event_time}"
            "<br>{input_name_text}:<br>{input_name}. <br>{on_channel}: {chan_name}"
        ).format(
            event_time=event_time,
            event_type=ev_translation,
            input_name_text=loc.gpio.input_name,
            input_name=input_name,
            on_channel=loc.gpio.associated_channel,
            chan_name=channel_name,
        )

        alarm_messages["sms_message"] = (
            "{event_type}: {input_name}. {on_channel}: {chan_name}"
        ).format(
            event_type=ev_translation,
            input_name=input_name,
            on_channel=loc.gpio.associated_channel,
            chan_name=channel_name,
        )

        alarm_messages["mail_message"] = (
            "{event_time}. {event_type}: {input_name}."
            " {on_channel}: {channel_name}.".format(
                event_time=event_time,
                input_name=input_name,
                event_type=ev_translation,
                on_channel=loc.gpio.associated_channel,
                channel_name=channel_name,
            )
        )
        return alarm_messages

    def event_handler(self, obj_input, associated_channels, event_type, origin):
        """Function creates alarm message and pass data to callback function
        Args:
            obj_input (:class: 'InputObj'): InputObj instance
            associated_channels (list): channels objects list
            event_type (str): "Input High to Low" or "Input Low to High"
        """
        try:
            tmstmp = int(time.time()) * 1e6
            input_guid = obj_input.guid
            if input_guid != origin:
                logger.warning("Origin: (%s) != obj_input.guid (%s)", origin, input_guid)

            if (
                event_type == "Input Low to High" and self.input_low_to_high_enable
            ) or (event_type == "Input High to Low" and self.input_high_to_low_enable):

                alarm_messages_for_each_channel = {
                    channel: self.make_alarm_message(
                        channel.name, obj_input.name, event_type, tmstmp
                    )
                    for channel in associated_channels
                }

                if self.callback:
                    for (
                        channel,
                        alarm_messages,
                    ) in alarm_messages_for_each_channel.iteritems():
                        self.callback(channel.full_guid, tmstmp, alarm_messages)
        except Exception as err:
            logger.exception("Error occurred in gpios handler: %s", err)
