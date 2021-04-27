# -*- coding: utf-8 -*-
# lpr_events_pusher v1.0.0
"""
<parameters>
    <company>DSSL</company>
    <author>d.gavrilov</author>
    <title>lpr_events_pusher</title>
    <version>1.0.0</version>
    <parameter>
        <id>URL</id>
        <name>URL</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>DEBUG</id>
        <name>Debug</name>
        <value>False</value>
   </parameter>
    <resources>
        <resource>helpers.py</resource>
    </resources>
</parameters>
"""
GLOBALS = globals()
URL = GLOBALS.get("URL", "")
DEBUG = GLOBALS.get("DEBUG", False)

import helpers

helpers.set_script_name()
logger = helpers.init_logger("lpr_events_pusher", debug=DEBUG)

import host
import json
import requests
import threading
from functools import wraps
from __builtin__ import object

assert URL, "No address specified for POST request"


def _run_as_thread(fn):
    @wraps(fn)
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
        return t

    return run


session = requests.Session()
session.verify = False
session.headers.update(
    {"Content-type": "application/json; charset=utf-8", }
)


class LprEventsPusher(object):
    def __init__(self, url):
        self.url = url

    def __call__(self, ev):
        data = self.prepare_data(ev)
        self.send_request(data)

    def prepare_data(self, event):
        data = {
            "id": event.id,
            "plate": event.plate,
            "best_guess": getattr(event, "best_guess", ""),
            "radar_speed": getattr(event, "radar_speed", 0.0),
            "country": getattr(event, "country", ""),
            "lane": getattr(event, "lane", 0),
            "server": {
                "name": self.get_object_name(event.server),
                "guid": event.server,
            },
            "channel": {
                "name": self.get_object_name(event.channel),
                "guid": event.channel,
            },
            "direction": self.get_direction(event.flags),
            "vehicle_type": getattr(event, "vehicle_type", ""),
            "quality": event.quality,
            "time_enter": event.time_enter,
            "time_bestview": event.time_bestview,
            "time_leave": event.time_leave,
            "matched_embrecords_history": self.get_matched_embrecords_history(event),
            "matched_extlists_history": self.get_matched_extlists_history(event),
        }
        return data

    @staticmethod
    def get_matched_embrecords_history(ev):
        matched_embrecords = []
        if ev.matched_embrecords_history:
            for emblist_record, emblist in ev.matched_embrecords_history:
                matched_embrecords.append(
                    {"reaction": emblist.reaction, "comment": emblist_record.comment}
                )
        return matched_embrecords

    @staticmethod
    def get_matched_extlists_history(ev):
        matched_extlists = []
        if getattr(ev, "matched_extlists_history"):
            for element in ev.matched_extlists_history:
                matched_extlists.append(
                    {
                        "reaction": element.get("reaction"),
                        "comment": element.get("comment"),
                    }
                )
        return matched_extlists

    @staticmethod
    def get_object_name(guid):
        try:
            return host.object(guid).name
        except EnvironmentError:
            return guid

    @staticmethod
    def get_direction(lpr_flags):
        if lpr_flags & host.LPR_UP:
            return "UP"
        else:
            return "DOWN"

    @_run_as_thread
    def send_request(self, data):
        try:
            response = session.post(self.url, data=json.dumps(data, ensure_ascii=False))
            logger.debug(data)
            logger.debug("[%s] %s", response.status_code, response.text)
        except Exception as err:
            logger.warning(str(err))


lep = LprEventsPusher(URL)
host.activate_on_lpr_events(lep)
