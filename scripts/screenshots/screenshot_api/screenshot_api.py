# -*- coding: utf-8 -*-
"""
<parameters>
    <company>d.gavrilov</company>
    <title>screenshots_api</title>
    <version>1.0.1</version>
    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Debug mode</name>
        <value>False</value>
    </parameter>

    <resources>
        <resource>helpers.py</resource>
        <resource>shot_saver.py</resource>
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
DEBUG = GLOBALS.get("DEBUG", False)

import helpers

helpers.set_script_name()
logger = helpers.init_logger("Screenshots_API", debug=DEBUG)

import host
import time
import os
from datetime import datetime
from exthttp.core import create_app, BaseHandler
from exthttp.http import HttpResponse, HttpResponseNotFound
from shot_saver import ShotSaver, status

app = create_app("screenshots")

check_work_state = {}


def callback(task_guid, state):
    check_work_state[task_guid] = state


ss = ShotSaver(callback=callback)


# GET https://localhost:8080/s/screenshots/get?server_guid=server_guid&channel_guid=channel_guid&dt=dt&figures=1


@app.route("get")
class ScreenshotHandler(BaseHandler):
    def get(self, request, *args, **kwargs):
        request_dict = request.GET
        dt = None
        channel_full_guid = "{}_{}".format(
            request_dict["channel_guid"], request_dict["server_guid"]
        )
        if request_dict.get("dt") != None:
            dt = datetime.strptime(request_dict["dt"], "%Y%m%d_%H%M%S")
        figures = request_dict.get("figures")
        file_name = request_dict.get("file_name")
        file_path = request_dict.get("file_path")
        try:
            task_guid, shot_path = ss.save(
                channel_full_guid, dt, figures, file_name, file_path
            )
            check_work_state[task_guid] = None
            logger.debug("New task: <b>%s</b><br>File: %s" % (task_guid, shot_path))
        except (ValueError, EnvironmentError) as err:
            host.error(str(err))
            return HttpResponse(str(err))

        while check_work_state[task_guid] not in (status.success, status.error):
            time.sleep(0.1)

        state = check_work_state.pop(task_guid)
        if state == status.success:
            logger.debug("status.success")
            host.timeout(1000, lambda: self.delete_file(shot_path))
            with open(r"{}".format(shot_path), "rb") as img:
                response = HttpResponse(img.read())
                response.headers["Content-Type"] = "image/jpeg"
                # response.headers["Content-Disposition"] = "attachment; filename='%s'" % os.path.basename(shot_path)
                return response
        else:
            return HttpResponse("Can't get shot")

    def delete_file(self, shot_file):
        try:
            os.remove(shot_file)
            logger.debug("remove file")
        except:
            logger.warning("exception:", exc_info=True)
