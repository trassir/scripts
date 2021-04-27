# -*- coding: utf-8 -*-
# WebPeopleCounter v0.0.4
"""
<parameters>
    <company>AATrubilin</company>
    <title>WebPeopleCounter</title>
    <version>0.0.4</version>
    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Debug mode</name>
        <value>False</value>
    </parameter>

    <resources>
        <resource>en.ts</resource>
        <resource>helpers.py</resource>
        <resource>exthttp/constant.py</resource>
        <resource>exthttp/utils.py</resource>
        <resource>exthttp/__init__.py</resource>
        <resource>exthttp/auth/login.py</resource>
        <resource>exthttp/auth/user.py</resource>
        <resource>exthttp/auth/__init__.py</resource>
        <resource>exthttp/core/app.py</resource>
        <resource>exthttp/core/handlers.py</resource>
        <resource>exthttp/core/module.py</resource>
        <resource>exthttp/core/__init__.py</resource>
        <resource>exthttp/http/request.py</resource>
        <resource>exthttp/http/response.py</resource>
        <resource>exthttp/http/__init__.py</resource>
        <resource>parameters/config.py</resource>
        <resource>parameters/pkl.py</resource>
        <resource>parameters/__init__.py</resource>
        <resource>parameters/fields/boolean.py</resource>
        <resource>parameters/fields/caption.py</resource>
        <resource>parameters/fields/datetimes.py</resource>
        <resource>parameters/fields/field.py</resource>
        <resource>parameters/fields/integer.py</resource>
        <resource>parameters/fields/string.py</resource>
        <resource>parameters/fields/string_list.py</resource>
        <resource>parameters/fields/__init__.py</resource>
        <resource>static/css/flatpickr.min.css</resource>
        <resource>static/css/material.trassir.min.css</resource>
        <resource>static/css/style.css</resource>
        <resource>static/css/template.css</resource>
        <resource>static/img/favicon.png</resource>
        <resource>static/img/trassir.png</resource>
        <resource>static/img/icons/access_time-24px.svg</resource>
        <resource>static/img/icons/calendar_today-24px.svg</resource>
        <resource>static/img/icons/calendar_today_access_time-24px.svg</resource>
        <resource>static/img/icons/keyboard_arrow_right-24px.svg</resource>
        <resource>static/img/icons/more_vert-24px.svg</resource>
        <resource>static/img/icons/play_circle_filled-24px.svg</resource>
        <resource>static/js/flatpickr.js</resource>
        <resource>static/js/material.min.js</resource>
        <resource>static/js/script.js</resource>
        <resource>templates/404.mako</resource>
        <resource>templates/footer.mako</resource>
        <resource>templates/header.mako</resource>
        <resource>templates/index.mako</resource>
        <resource>templates/login.mako</resource>
        <resource>templates/settings.mako</resource>
    </resources>
</parameters>
"""

GLOBALS = globals()
DEBUG = GLOBALS.get("DEBUG", False)

APP_NAME = "WebPeopleCounter"

EVENTS_INCREASE = (
    "Border Crossed A -> B",
    "Border %1 Unique Object A-B Crossing"
)
EVENTS_DECREASE = (
    "Border Crossed B -> A",
    "Border %1 Unique Object B-A Crossing"
)

import datetime
import threading
from __builtin__ import object

import host

import helpers

default_script_name = helpers.set_script_name()
logger = helpers.init_logger(APP_NAME, debug=DEBUG)

from exthttp.utils import tr
from exthttp.core import create_app, BaseHandler
from exthttp.http import HttpResponseForbidden, JsonResponse
from parameters import ConfigManager, fields

app = create_app(APP_NAME)
app.debug = DEBUG
app.create_module(
    name=APP_NAME,
    icon_path="static/img/favicon.png",
    allow_change_password=False,  # Allow users to change password
    allow_multiple=False,  # If False - raise RuntimeError when creating another script copy
)
app.copy_jqeury()

lock = threading.Lock()


def get_channels():
    channels = []
    for name, guid, _, parent in sorted(
        host.objects_list("Channel"), key=lambda x: (x[3], x[0])
    ):
        srv = host.object(parent[:-1])
        try:
            name = "%s@%s" % (name, srv.name)
        except EnvironmentError:
            name = "%s@%s" % (name, parent[:-1])
        channels.append((guid, name))
    return channels


class BorderListField(fields.StringListField):
    def __init__(self, *args, **kwargs):
        kwargs["choices"] = kwargs.get("choices", self.get_choices)
        kwargs["nullable"] = kwargs.get("nullable", True)
        super(BorderListField, self).__init__(*args, **kwargs)
        self.__selected_objects = None
        self.onchange = self.__onchange
        self.onchange()

    def __onchange(self, *args, **kwargs):
        if self.value:
            self.__selected_objects = set(self.value)
        else:
            self.__selected_objects = None

    @staticmethod
    def get_choices():
        objects = host.objects_list("SIMT Border")
        objects.extend(host.objects_list("PeopleBorder"))
        objects.extend(host.objects_list("HeadBorder"))

        def deep_people_border_filter(object_from_list):
            """ filtering border from deep_people """
            border_guid = object_from_list[1]
            border = host.object(border_guid)
            try:
                channel_guid, server_guid = border.associated_channel.split("_")
                zones_dir = host.settings("/%s/channels/%s/deep_people" % (server_guid, channel_guid))
                for i in xrange(16):
                    if zones_dir["zone%02d_guid" % i] == border_guid:
                        return zones_dir["zone%02d_type" % i] == "border"
                return False
            except (ValueError, KeyError):
                return False

        deep_people_borders = filter(deep_people_border_filter, host.objects_list("PeopleZone"))
        objects.extend(deep_people_borders)
        objects.sort()

        return [(obj[1], obj[0]) for obj in objects]

    def is_working_border(self, guid):
        return self.__selected_objects is None or guid in self.__selected_objects


config_fields = [
    fields.CaptionField(
        '<span style="font-size: 24px;">%s</span>' % default_script_name
    ),
    fields.CaptionField("<hr>", is_html=True),

    BorderListField(
        "borders",
        tr("Линии для подсчета"),
        description=tr("Если не выбраны - скрипт работает со всеми линиями"),
        multiple=True,
    ),

    fields.IntegerField(
        "peoples_current",
        tr("Текущее кол-во людей"),
        description=tr("Вы можете изменить текущее кол-во людей в любое вермя"),
        min=0,
    ),
    fields.IntegerField(
        "peoples_total",
        tr("Максимальное кол-во людей"),
        description=tr("Укажите максимальное кол-во людей в магазине"),
        min=0,
        default=50,
    ),

    fields.BooleanField(
        "reset_enable",
        tr("Сбрасывать счетчик автоматически"),
        description=tr("Если активно - сбрасывает счетчик до 0 автоматически"),
        default=False,
        children=("reset_time",)
    ),
    fields.TimeField(
        "reset_time",
        tr("Время сброса счетчика"),
        description=tr("Укажите время, когда сбрасывать счетчик"),
    )
]


config = ConfigManager(*config_fields)


def event_handler(ev):
    if config.borders.is_working_border(ev.origin):
        with lock:
            if ev.type in EVENTS_INCREASE:
                config.peoples_current.value += 1
            else:
                config.peoples_current.value -= 1
            host.stats()["run_count"] = config.peoples_current.value


for event in EVENTS_INCREASE:
    host.activate_on_events(event, "", event_handler)

for event in EVENTS_DECREASE:
    host.activate_on_events(event, "", event_handler)


@app.route("index")
class IndexHandler(BaseHandler):
    __template__ = "index.mako"

    title = host.tr("Главная")

    def get(self, request, *args, **kwargs):
        return self.render()

    def post(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "current": config.peoples_current.value,
                "total": config.peoples_total.value,
                "available": config.peoples_total.value - config.peoples_current.value,
            }
        )


@app.route("settings")
class SettingsHandler(BaseHandler):
    __template__ = "settings.mako"

    title = host.tr("Настройки")
    rights = "has_setup_rights"

    def get(self, request, *args, **kwargs):
        if not request.user.has_setup_rights:
            return HttpResponseForbidden(
                "Sorry %s, you have no setup rights" % request.user.name
            )

        return self.render(config=config, saved=kwargs.get("saved"), errors=kwargs.get("errors", {}))

    get.need_auth = True

    def post(self, request, *args, **kwargs):
        if not request.user.has_setup_rights:
            return HttpResponseForbidden(
                "Sorry %s, you have no setup rights" % request.user.name
            )
        with lock:
            success, errors = config.save_form_data(request.POST)
        kwargs["saved"] = success
        kwargs["errors"] = errors
        return self.get(request, *args, **kwargs)

    post.need_auth = True


class Worker(object):
    def __init__(self, cfg):
        self.config = cfg
        self.working = False

    @staticmethod
    def time_now(dt_now=None):
        dt_now = dt_now or datetime.datetime.now()
        return dt_now.time().replace(second=0, microsecond=0)

    def _is_time_to_reset_counter(self, time_now):
        if self.config.reset_enable.value is True:
            return time_now == self.config.reset_time.value
        return False

    def _work_iteration(self):
        logger.debug("Work iteration")
        now = datetime.datetime.now()
        time_now = self.time_now(now)

        delay = 30

        with lock:
            if self._is_time_to_reset_counter(time_now):
                logger.info("Reset peoples current value to 0")
                self.config.peoples_current.value = 0
                delay *= 3

            config.save()

        if self.working:
            host.timeout(1000 * delay, self._work_iteration)

    def run(self):
        self.working = True
        self._work_iteration()


worker = Worker(config)
worker.run()
