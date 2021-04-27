# -*- coding: utf-8 -*-
"""
<parameters>
    <parameter>
        <type>objects</type>
        <name>Укажите IP устройства</name>
        <id>IP</id>
        <value></value>
    </parameter>
</parameters>
"""

import time
import threading
from functools import wraps


def _run_as_thread(fn):
    @wraps(fn)
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
        return t

    return run


@_run_as_thread
def reboot_ip():
    if not IP:
        raise ValueError('Выберите камеры')
    ip_list = IP.split(',')
    for x in objects_list("IP Device"):
        sett = settings("/%s/ip_cameras/%s" % (x[3][:-1], x[1]))
        if x[0] in ip_list:
            sett['model_missmatch_off'] = 1
            sett['grabber_enabled'] = 0
            time.sleep(4)
            sett['grabber_enabled'] = 1


reboot_ip()