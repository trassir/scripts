# -*- coding: utf-8 -*-
# hls_api v1.0.1
"""
<parameters>
    <company>DSSL</company>
    <author>d.gavrilov</author>
    <title>hls_api</title>
    <version>1.0.1</version>
    <parameter>
        <name>User settings</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <type>string</type>
        <id>USER</id>
        <name>User</name>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>PASSWORD</id>
        <name>Password</name>
        <value></value>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Debug mode</name>
        <value>False</value>
    </parameter>

    <resources>
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
    </resources>
</parameters>
"""

GLOBALS = globals()
USER = GLOBALS.get("USER", "")
PASSWORD = GLOBALS.get("PASSWORD", "")
DEBUG = GLOBALS.get("DEBUG", False)

APP_NAME = "hls_api"

import host

import helpers

helpers.set_script_name()
logger = helpers.init_logger(APP_NAME, debug=DEBUG)

import re
import json
import datetime
import requests
from __builtin__ import object
from exthttp.core import create_app, BaseHandler
from exthttp import http

app = create_app(APP_NAME)

assert USER, "User is requirement parameter"
assert PASSWORD, "Password is requirement parameter"

login_res_regexp = re.compile(r"\/\*.*\*\/", flags=re.S)

http_port = host.settings("webserver")["http_port"]
BASE_URL = "https://127.0.0.1:{port}".format(port=http_port)

session = requests.Session()
session.verify = False


def check_user(user_name):
    for sett in host.settings("users").ls():
        if sett.type == "User" and sett.name == user_name:
            logger.debug("Found user with name %s", user_name)
            return True


user = check_user(USER)
if not user:
    raise ValueError("Not found user -> %s" % USER)


def get_error_message(required_parameter):
    return (
        "Not found requirements parameters {param}! Example request "
        "https://server_ip:port/s/hls_api/get_video?&channel=channel&stream=main".format(
            param=required_parameter
        )
    )


def push_request(request_url, get_token=False):
    response = session.get(request_url)
    try:
        if get_token:
            data = json.loads(response.text)
        else:
            data = json.loads(login_res_regexp.sub("", response.text))
    except ValueError:
        data = {"success": 0, "error_code": response.text}

    if data.get("success"):
        if get_token:
            return data.get("token")
        else:
            return data.get("sid")
    else:
        raise ValueError("Connections ERROR %s" % data.get("error_code"))


class Sid(object):
    start = datetime.datetime(year=2000, month=1, day=1)

    def __init__(self, login, password, base_url):
        self.time_out = self.start
        self.url = base_url + "/login?username=%s&password=%s" % (login, password,)
        self.live_sid = datetime.timedelta(minutes=4)
        self.sid = None

    def __call__(self, *args, **kwargs):
        if datetime.datetime.now() - self.time_out > self.live_sid:
            self.sid = push_request(self.url)
            self.time_out = datetime.datetime.now()
            return self.sid
        else:
            self.time_out = datetime.datetime.now()
            return self.sid

    def __str__(self):
        return self.__call__()


sid = Sid(USER, PASSWORD, BASE_URL)


@app.route("get_video")
class HlsVideoHandler(BaseHandler):
    def get(self, request, *args, **kwargs):
        _host = request.headers.get("Host")
        hw = request.GET.get("hw", "")
        channel = request.GET.get("channel")
        if not channel:
            return http.HttpResponseBadRequest(get_error_message("channel"))
        stream = request.GET.get("stream")
        if not stream:
            return http.HttpResponseBadRequest(get_error_message("stream"))
        if hw:
            hw = "&hw=" + hw
        token_url = "{host}/get_video?channel={channel}&container=hls&stream={stream}{hw}&sid={sid}".format(
            host=BASE_URL, channel=channel, stream=stream, hw=hw, sid=sid
        )
        logger.debug(token_url)
        token = push_request(token_url, get_token=True)
        hls = "https://{host}/hls/{token}/master.m3u8".format(host=_host, token=token)
        data = {"hls": hls, "sid": str(sid), "token": token}
        logger.debug(data)
        return http.JsonResponse(data)
