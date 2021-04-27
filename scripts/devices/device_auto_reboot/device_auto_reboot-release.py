# DeviceAutoReboot v0.0.6
"""
<parameters>
    <company>DSSL</company>
    <author>AATrubilin</author>
    <title>DeviceAutoReboot</title>
    <version>0.0.6</version>
    
    <parameter>
        <id>DEVICES</id>
        <type>objects</type>
        <name>Devices, optional</name>
        <value></value>
    </parameter>
    <parameter>
        <id>MIN_TIMEOUT_BETWEEN_REBOOTS</id>
        <type>integer</type>
        <name>Min timeout between reboots, min</name>
        <value>15</value>
        <min>1</min>
        <max>3600</max>
    </parameter>
    
    <parameter>
        <type>caption</type>
        <name>Reboot on Signal Lost event</name>
    </parameter>
    <parameter>
        <id>SIGNAL_LOST_ENABLE</id>
        <type>boolean</type>
        <name>Enable</name>
        <value>True</value>
    </parameter>
    <parameter>
        <id>SIGNAL_LOST_TIMEOUT</id>
        <type>integer</type>
        <name>Signal Lost timeout, sec</name>
        <value>5</value>
        <min>1</min>
        <max>3600</max>
    </parameter>
    
    <parameter>
        <type>caption</type>
        <name>Reboot by Schedule</name>
    </parameter>
    <parameter>
        <id>SCHEDULE_REBOOT_ENABLE</id>
        <type>boolean</type>
        <name>Enable</name>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SCHEDULE_NAME</id>
        <type>objects</type>
        <name>Schedule (reboot on change to Red zone)</name>
        <value></value>
    </parameter>
    
    <parameter>
        <type>caption</type>
        <name>Other settings</name>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Debug mode</name>
        <value>False</value>
    </parameter>

    <resources>
        <resource>helpers.py</resource>
        <resource>long_event_handler.py</resource>
        <resource>schedule.py</resource>
    </resources>
</parameters>
"""

resources = {
    "helpers.py": """
        eNqtWN1q3EYUvjf4HQaVBanZVWxSSlh2t7jxOjH4J9hrQnCNkKXZtRr9ZWZkxxhD2+1dKaRQ
        ShuS0jZ3pZS0V22h7U0fYN032IuEPkbPjEbSSNp1fJENxJo5/9+cOedIb6HW2y3kRK4Xjtoo
        YcPWTb6zuOAFcUQYoqc0fyY4f4yKXT8ajUB4cWFIogA0+T52mBeFFEkGFz9MQDIXOIoo48vd
        WzvrdwfW1spmH3XFrkmZzahumLFNcMjgIbQDEF3tr63sbQwsRWIXRM4WFxD8tPs49BB9QLyY
        aU25txdyURftOqXt6fj5dPz9dPx4Ov55Ov5yOn4yHT9DYuub6fi76fjr6fjb6fgHeMhlJl9N
        Xvz7fPICXXw8+ePio8lvk78vPsmpqQEURkkh8Gzy1+TXi88mv88WUfxFbkRPbfrPLxVhkJgj
        /Orpjy+/+PPl48//+/TJq6c/8f3zxYXA9kIriNzExwAMHJqZLqg5wkyfje0o8dymwN3gx7G4
        4OIhOgE9OIR8wFZssyOd/2e0U9veEM5dHAnqdpEWMk0S+I+RU2XFf1wUnOF/TBdzlboGCXZT
        Mwo+/MjBgIK+F3qcYVWw9QmJSBPJvX6Y7xk1C5SmOwSzhITCVhqL4wMNrSax7zk2w2uezzDR
        Za6a6TJTp2nabhLHBFMKRBQkPvNiADKADXuEKYACkVAetxOFDNAzuQkuOiC284ALgbn0KkDO
        EYiCuMgOXTQUhlCUMFieZr7GGFxykU69wPNtYkgJmqvtP7ID8EAJt9VqocERTu1IxwpNNxDz
        YDMPJ9PDT9SyvNBjlqVT7A9VBGkSAyQViJpIsJm5lHJYnGJa3AMLIoWj3YpCPI9sOVESMmBa
        Vp1J8RCuNGXUqkvpjulmPlGQ59FkdCchPHmleV2yp6me6TN9fIz9MMrXAR0pQUASl7R0K35X
        UmxmUNdEVCqbzL8126cKIhhWFX1gfqbKHlqucM7DQ6+zZT/t8ixp0DRNPgg11JjpRl21cRkc
        4I2C5RWAm4fbgKQdIru3d6AobUSjO3CFfOXaynWWMTyhcOCxuekk6h63LqEQjOYwIoHNZPIY
        hmr3bhQn8WuswvWCWw+lgqCYs6OjlK5cO0sQaNGihBw0r8H6rZUNrZ06hkWZUxjWVgaXUPs7
        O9s7c6n3Vna2MqIN3rAqcX3r9lz6+tbadkaUUKnk1f77e7cvoW9tD3b7g9kM5+rtv/Sw4Joi
        eRnLJ1StMCm4+6XbDrX5QE8venGam6dQ0/BrjvMenErfGqxv9rf3BtYmnyuWl5aW5lbQJq9h
        mBus19KSwddXUotrsmSbrDbe8j2Bviv66IeRF84oAGmDx4xBgFTXoP8zHFgnHiiLYjGMaca+
        Rh2CcUiPIkatYeS7kLMHRThlrYqzdb9PiAdV3DqJiOh93Wrdk2xwHhaMfgkfScQQqAf2IzDW
        5QAbZYRTlbUeJTpvFONQr0LWRJqtGcimvOuK7Ur9PDmCvZorM4psJm8KH3StUSqQhagJiefj
        IYxOV0fkirlfM2XHELM7p15lUtBLwojNdmFmG6u7mRbeWirxNgEzS2q/ekOaZW3K8CgSXQxB
        ROcp1YTID5NRV4ABi6yNWekYkO5nOKRzJdLO+MM50s/4fHpuaFn8fLubauWU7vyhVkKUOgIq
        s5sPo/BG4VyegKA/q+EWhCDlTLlF99sHakuRjKbjRxSrd1qKERxEx3nRydhzY5IL7uoGL1y6
        LK45nUdlSSlwvdIIjTpToSoLU2jkySHAF0NIDgGv9KqSFFtWgmkt21MKjdZIMaNov6HnJddo
        3aQHCDa8EIeR0XqHok5DHyahsyWYe6gFVNkQDCoHuTlBFGbLnpVO07RdN8dWUZDjJ5qDAmCp
        oxszeOr4cYzmwCcbaUnPVSEcBqyrdQ57JQDpQef6YQ9tAIDtAkjaOSS9jtcrsDPfvbFEO9e9
        XhnDWiSF4Ypzc1EsqchhzMJvl/zn17Oh29Th9eGN5IJQzEt6cWLlrg3VmE9wvB7LSztLbM4l
        qHJfflQQINQoKE/ipBr3W42g1YCp+U67sdlu7GrlylstZpWCm6NVzO4QNLrGCRXON+pZDRk4
        avnyW30ZNi4BU7Fdcq9e75RUUpXkmSQn/JS7aBVQi7NOkTUAyQkUMEV05ZMG9PqUV2uKd04D
        QcmuV3WlE0EIFhVfZiyeNrkNN3IA4dkmLAuolqXayN49mcfEhxWCARybOEc60Tpis6eb14zO
        9fQZREGFxOgYegdMXqXXZMgbwakkS8FWUi63pfpsVTIAcdqJX4pT9E9h4Rwdn0mp87yFKl9r
        OE9X/G+OSJTE+rLRzHzpyr85hfud+SnqofaeCf/KtQh41C960Ehnfbarvp1VG/i+xuPQDsTI
        WIuvlCgz6f8DOZtdDw==
    """,
    "long_event_handler.py": """
        eNqdVluL4zYUfg/kP5w1DNitazID+zKQwtBm6cJuX3YolCEYxT521HEkI8mZGdr97z3yLZLt
        MLB+SCzrnO/cP4mfaqkMGH7C9Wq94t3yKLWxS6Pe7tcroKdQ8gRHrGpUGnqpEk1aybJEtV7h
        a4a1gc/tzk4pqVxFK8VF6Sh+afWAaQ9lvereYOt8DiO7kaZnMs2lSFPaDW6TTbIJBvkkx0NT
        hsGNhl7qHm50EEOaCnbCNLVvo36Lt15lFdMavkhR7s4ozB9M5BVZk4d/MDNR736OBalywU2a
        hhqrIga00ql5q1HHkLGqOrDsefhc8Mqg2v4pBcaQN4oZMrn9GMNJ5ri9G2DtEwSBdWNYPqhS
        O7v2cSxB+NjUFT5po2Kgn310D63bGozdSOCTVICv7EQLCIOv0hqGb4YpQ3m4rGUdRL6VIQQI
        7Rs7VBjiOSL834aNohFZq/7CzbHzylaOqbI50fuS010efMgYZG1hWNWD240erpcfLFG+Gm1A
        oWmUgIOUlW9kyCyEXBgP9ysXSY85CFHCMJMi1wn8jgVrKgMfh08+rC3SHHLMQwfLRY6vEG7g
        P7iNEvhc9F+4BtkYkAUoJkqEXy6Zpf9OWSeT+g8LTiiaC22YyGyynBYLK67JobbMUTRpEduS
        SZq6nbLtRF2QScXJWIUinOtG8GELdxMT9lGMa4S/WNVgO9xhsHutaUwwh7s+Lb23pTR29ODm
        mgnHF6w0Tox1hh5J0rMDNgdAHd6GBoXtdTdHF6v2gxd6MnCAY/jCa5M8DhXrPLa5XAjhybbJ
        PnYD6dnP9oFLfu+iz8EvioNSo5TdHXX+/T6TeZHqmfg1FfKFBD4xyqtLLa3UODLbcTAmEmO7
        bsfOnUh4s731Rn2w1xFm52yaHTF7Jk61ym7nUgMKqthihMupW4zQa5yWKtyoyX4nbQ+3xP6E
        TslsC5UNz2l4l/1InvFNh9N5I8973F+X1Z4s6H7MZToLaKEfwmUHalmHFi2K3LDs2dxGQ2QT
        +pX9CW43m9hrqrEGkV8gz7Q9vCblwXNi29HNjt+8S2UaQQnONceI08/MYEqnb6c96wgiw4c8
        HyVBtnY7huk7/9gd0B5ttsm4Aj8Z2s2ejsGgy070Qwi3PsI0nc4FYRLZzgvALebfsqFZE9AQ
        6V3xBIzsNSGjM5FuU7OT5GE8XsAcmWlni08T2BE08FJIhXny7tUDwtahb7u0dZ/OwUdFFybe
        M+/1c2zeOk4S5+NknR1vCTOWiSzpz76GfoqHhwamxrwzdyHXhakiF6XidCWNwd7UojkUOeah
        0eFuJReMdtlyB96nHPjZ599lhGUuGf3ct2zr1mzi7AJNksstT17x+Sq5PqoG31WZEDxl8H8T
        5rQ2
    """,
    "schedule.py": """
        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
    """,
}
t1utils.resources_check(script_path, resources)

GLOBALS = globals()

DEVICES = GLOBALS.get("DEVICES", "")
MIN_TIMEOUT_BETWEEN_REBOOTS = GLOBALS.get("MIN_TIMEOUT_BETWEEN_REBOOTS", 15) * 60

SIGNAL_LOST_ENABLE = GLOBALS.get("SIGNAL_LOST_ENABLE", True)
SIGNAL_LOST_TIMEOUT = GLOBALS.get("SIGNAL_LOST_TIMEOUT", 5)

SCHEDULE_REBOOT_ENABLE = GLOBALS.get("SCHEDULE_REBOOT_ENABLE", False)
SCHEDULE_NAME = GLOBALS.get("SCHEDULE_NAME", "")

DEBUG = GLOBALS.get("DEBUG", False)

APP_NAME = "DeviceAutoReboot"

import time
import host
import helpers

default_script_name = helpers.set_script_name()
logger = helpers.init_logger(APP_NAME, debug=DEBUG)

from schedule import ScheduleObject
from long_event_handler import LongEventHandler


logger.info("Starting script %s (%s)", default_script_name, __name__)
logger.debug("DEVICES='%s'", DEVICES)
logger.debug("SIGNAL_LOST_ENABLE=%s", SIGNAL_LOST_ENABLE)
logger.debug("SIGNAL_LOST_TIMEOUT=%s", SIGNAL_LOST_TIMEOUT)
logger.debug("SCHEDULE_REBOOT_ENABLE=%s", SCHEDULE_REBOOT_ENABLE)
logger.debug("SCHEDULE_NAME='%s'", SCHEDULE_NAME)


_ip_cameras = host.settings("ip_cameras")
_channels = host.settings("channels")


def get_ip_cameras(names):
    if names:
        names = set(names.split(","))
    else:
        names = None

    ip_cameras = []
    for sett in _ip_cameras.ls():
        if sett.type == "Grabber" and sett["grabber_enabled"]:
            if names is None or sett.name in names:
                sett.prev_reboot_ts = 0
                ip_cameras.append(sett)
                if names:
                    names.remove(sett.name)
                    if not names:
                        break
    if names:
        raise RuntimeError("Not found ip cameras: %s" % ", ".join(names))

    return ip_cameras


devices = {dev.guid: dev for dev in get_ip_cameras(DEVICES)}


def reboot_device(dev):
    if time.time() - dev.prev_reboot_ts > MIN_TIMEOUT_BETWEEN_REBOOTS:
        logger.info("Reboot device %s", dev.name)
        dev["reboot"] = 1
        dev.prev_reboot_ts = time.time()
    else:
        logger.debug("Device %s not rebooted, timeout", dev.name)


def reboot_channel_device(ev):
    channel = _channels.cd(ev.origin)
    if channel:
        info = channel.cd("info")
        if info:
            reboot_device(info["grabber_path"].rsplit('/', 1)[-1])
        else:
            logger.warning("Channel %s (%s) has no info", channel.name, channel.guid)
    else:
        logger.debug("Channel %s not found", ev.origin)


if SIGNAL_LOST_ENABLE:
    leh = LongEventHandler(
        (
            "Signal Lost",
            "Signal Restored",
        ),
        reboot_channel_device,
        duration=SIGNAL_LOST_TIMEOUT,
        mode=0
    )


if SCHEDULE_REBOOT_ENABLE:
    assert SCHEDULE_NAME, "Please, select schedule..."

    def reboot_all_devices(sched):
        logger.info("Reboot all devices")
        if sched.color == "Red":
            for dev in devices.itervalues():
                reboot_device(dev)

    schedule = ScheduleObject(SCHEDULE_NAME, color_change_handler=reboot_all_devices)
