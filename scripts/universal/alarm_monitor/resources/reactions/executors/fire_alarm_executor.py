# -*- coding: utf-8 -*-

import host
from executor import Executor
from base_alarm import BaseAlarm

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()


class FireAlarmExecutor(BaseAlarm, Executor):

    def __init__(self, token, add_video, obj_storage):
        super(FireAlarmExecutor, self).__init__()
        self.token = token
        self.add_video = add_video
        self.obj_storage = obj_storage

    def execute(self, full_channel, ts, alarm_messages, *args, **kwargs):
        alarm_message = alarm_messages.get("mail_message")
        self.contents = []
        if self.add_video:
            try:
                channel, server = full_channel.split("_")
                channel_obj = self.obj_storage.channels.get(channel)
                if not channel_obj:
                    logger.debug("channel object not found: %s, return", channel)

                channel_name = channel_obj.name

                self.contents.append({
                    "type": "trassir_channel",
                    "channel_guid": channel,
                    "name": channel_name,
                    "server_guid": server,
                })
            except IndexError:
                logger.debug("Can't get server name to make video content for alarm")

        if alarm_message:
            self.contents.append({
                "type": "html",
                "html": (
                    "<!doctype html><head><meta charset='utf-8'></head><body>"
                    ""
                    "{message}"
                    ""
                    "</body></html>"
                ).format(message=alarm_messages.get('mail_message', 'No text')),
            })
        if not self.contents:
            logger.debug("nothing in contents")
            return
        super(FireAlarmExecutor, self).fire()


