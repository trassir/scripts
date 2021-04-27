# -*- coding: utf-8 -*-
# Trassir SNMP v2.0.6
"""
<parameters>
    <company>AATrubilin</company>
    <title>TRASSIR_SNMP</title>
    <version>2.0.6</version>
    <parameter>
        <type>caption</type>
        <name>Main settings</name>
    </parameter>
    <parameter>
        <id>PORT</id>
        <type>integer</type>
        <name>Connection port (UDP)</name>
        <value>161</value>
        <min>1</min>
        <max>65535</max>
    </parameter>
    <parameter>
        <id>IP_CIDR</id>
        <type>string</type>
        <name>IPv4 CIDR</name>
        <value>0.0.0.0/0</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Other settings</name>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>New changes push timeout(min)</name>
        <id>TIMEOUT</id>
        <value>0</value>
        <min>0</min>
        <max>10000</max>
    </parameter>
</parameters>
"""

import os

if os.name == "nt":
    raise OSError("SNMP service is not available on Windows")

import re
import subprocess
from functools import wraps

from pysnmp.hlapi import *
from pysnmp.proto import api

import host

GLOBALS = globals()

PORT = GLOBALS.get("PORT", 161)
IP_CIDR = GLOBALS.get("IP_CIDR", "0.0.0.0/0")
TIMEOUT = GLOBALS.get("TIMEOUT", 0)

CONFIG = "/etc/snmp/snmpd.conf"
CUSTOM_INDICATORS_REGEXP = re.compile(r"([^|]+:0:)([^|]+)")  # value must be in group(2)
p_mod = api.protoModules[api.protoVersion2c]

__health = host.settings("health")
__system_wide_options = host.settings("system_wide_options")
__state = {1: "OK", 0: "ERROR", -1: "N/A"}


def _as_state(fn):
    """Run function as thread"""

    @wraps(fn)
    def run(*args, **kwargs):
        res = fn(*args, **kwargs)
        return __state.get(res, res)

    return run


@_as_state
def db_ok():
    """Returns DataBase state"""
    return __health["db_connected"]


def archive_days():
    """Returns archive days"""
    days = str(int(__health["disks_stat_main_days"]))

    priv = int(__health["disks_stat_priv_days"])
    if priv:
        days += " / %s" % priv

    subs = int(__health["disks_stat_subs_days"])
    if subs:
        days += " / %s" % subs

    return days


@_as_state
def disks_ok():
    """Returns disks state"""
    return not (__health["disks_error_count"] > 0 or __health["disks_is_slow"])


@_as_state
def network_ok():
    """Returns network state"""
    if __health["network_really_connected"] == -1:
        state = -1
    elif (
            __health["network_really_connected"] == __health["network_should_be_connected"]
    ):
        state = 1
    else:
        state = "{h[network_really_connected]} / {h[network_should_be_connected]}".format(
            h=__health
        )
    return state


def channels():
    """Returns channels state"""
    online = __health["channels_board_online"] + __health["channels_network_online"]
    total = __health["channels_board_total"] + __health["channels_network_total"]
    return "%i / %i" % (online, total)


@_as_state
def scripts_ok():
    """Returns scripts state"""
    return __health["scripts_total"] == __health["scripts_ok"]


@_as_state
def cloud_ok():
    """Returns cloud state"""
    return 1 - __health["cloud_have_error"]


def cpu_usage():
    """Returns cpu usage"""
    return "%.1f" % __health["cpu_usage"]


indicators = [
    db_ok,
    archive_days,
    disks_ok,
    network_ok,
    channels,
    scripts_ok,
    cloud_ok,
    cpu_usage,
]


def on_health_changes():
    if host.stats()["run_count"] > 1000:
        host.stats()["run_count"] = 0
    else:
        host.stats()["run_count"] += 1

    state = "\n".join(str(ind()) for ind in indicators) + "\n"

    if __health["custom_indicators"]:
        state += "\n%s" % ";".join(
            res.group(2)
            for res in CUSTOM_INDICATORS_REGEXP.finditer(__health["custom_indicators"])
        )

    next(
        setCmd(
            SnmpEngine(),
            CommunityData("private"),
            UdpTransportTarget(("localhost", PORT)),
            ContextData(),
            ObjectType(ObjectIdentity(".1.3.6.1.4.1.3333.0"), p_mod.OctetString(state)),
        )
    )


def touch_service():
    if not re.findall(
            r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/([0-9]|[1-2][0-9]|3[0-2]))$",
            IP_CIDR,
    ):
        raise ValueError('value "%s" must be match to IPv4 CIDR' % IP_CIDR)

    if subprocess.call(
            'sudo sed -i "s/^agentAddress.*/agentAddress udp:%s/g" %s' % (PORT, CONFIG),
            shell=True,
    ):
        raise ValueError("FAIL setup PORT to config file")

    if subprocess.call(
            'sudo sed -i "s/^com2sec world.*/com2sec world %s dssl/g" %s'
            % (IP_CIDR.replace("/", r"\/"), CONFIG),
            shell=True,
    ):
        raise ValueError("FAIL to setup IPv4 CIDR value to config file")

    if subprocess.call("sudo /etc/init.d/snmpd restart", shell=True):
        raise ValueError("Failed to start snmpd service")


touch_service()


def _timeout_loop():
    on_health_changes()
    host.timeout(TIMEOUT * 6e4, _timeout_loop)


if TIMEOUT == 0:
    on_health_changes()
    __health.activate_on_changes(on_health_changes)
else:
    _timeout_loop()
