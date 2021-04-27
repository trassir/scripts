# -*- coding: utf-8 -*-
# IP Device info v1.0.1
"""
<parameters>
    <company>MNRudkovskyi</company>
    <title>IP Device info</title>
    <version>1.0.1</version>

    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Debug</name>
        <value>False</value>
    </parameter>

    <resources>
        <resource>export.py</resource>
        <resource>helpers.py</resource>
    </resources>
</parameters>
"""

import host
import helpers

GLOBALS = globals()
DEBUG = GLOBALS.get("DEBUG", False)

logger = helpers.init_logger("IP_Device_info", debug=DEBUG)

from export import save_data

screen_folder = host.settings("system_wide_options")["screenshots_folder"]


grabber_feedback_state = {
    1: "On Work",
    0: "No Work",
    3: "Exceed specification",
    4: "Invalid argument specified",
    9: "Wrong login or password",
    8: "Wrong login or password",
    1025: "On Work - No HDD",
    2051: "Exceed specification - HDD ok",
    1027: "Exceed specification - No HDD",
    2049: "On Work - HDD ok",
    8193: "On Work - HDD not format",
    1537: "On Work - No HDD",
}

type_motion_detector = {
    0: "Off or AutoTrassir",
    3: "Hardware",
    1: "Active",
    11: "Active HD",
    2: "Simt",
}


def get_data_from_ip_device(server_guid):
    device_info = {}
    for sett in host.settings("/{}/ip_cameras".format(server_guid)).ls():
        if sett.type == "Grabber":
            if sett["grabber_enabled"]:
                device_info["name"] = sett["name"]
                device_info["connection_ip"] = sett["connection_ip"]
                device_info["connection_port"] = sett["connection_port"]
                device_info["channel"] = get_data_from_channel(sett, server_guid)
                device_info["model"] = sett["model"]
                feedback = sett.cd("feedback")
                if feedback:
                    device_info["state"] = grabber_feedback_state.get(feedback["state"], "Unknown")
                logger.debug("device info: %s", device_info)

                yield device_info


def get_data_from_channel(sett, server_guid):
    channel_info = {}
    for ch_number in xrange(31):
        if sett["channel%02d_guid" % ch_number]:
            try:
                ch_object = host.object(sett["channel%02d_guid" % ch_number])
                channel_info["ch_name"] = ch_object.name
                channel_info["motion_detector"] = type_motion_detector.get(
                    host.settings(
                        "/{}/channels/{}".format(server_guid, ch_object.guid)
                    )["software_md_enable"],
                    "Unknown",
                )
            except EnvironmentError:
                logger.debug(
                    "Channel guid '%s' has no name, most likely the streams are disabled for the registrar channel",
                    sett["channel%02d_guid" % ch_number],
                )
                continue
            channel_info["codec"] = sett["channel%02d_codec" % ch_number]
            channel_info["audio_enabled"] = (
                "On" if sett["channel%02d_audio_enabled" % ch_number] else "Off"
            )
            channel_info["audio_codec"] = sett["channel%02d_audio_codec" % ch_number]
            channel_info["main"] = (
                "On" if sett["channel%02d_main_enabled" % ch_number] else "Off"
            )
            channel_info["main_fps"] = sett["channel%02d_fps" % ch_number]
            channel_info["main_gop"] = sett["channel%02d_gop" % ch_number]
            channel_info["main_resolution"] = sett["channel%02d_resolution" % ch_number]
            channel_info["sub"] = (
                "On" if sett["channel%02d_ext_gop" % ch_number] else "Off"
            )
            channel_info["sub_fps"] = sett["channel%02d_ext_fps" % ch_number]
            channel_info["sub_gop"] = sett["channel%02d_ext_gop" % ch_number]
            channel_info["sub_resolution"] = sett[
                "channel%02d_ext_resolution" % ch_number
            ]
            logger.debug("channel info: %s", channel_info)

            yield channel_info
        else:
            break


def get_data_from_server():
    data_from_server = {}
    for srv in host.settings("/").ls():
        if srv.type == "RemoteServer" or srv.type == "LocalServer":
            logger.debug("Server: name %s, guid %s", srv.name, srv.guid)
            data_from_server["server_name"] = srv.name
            data_from_server["ip_device_info"] = get_data_from_ip_device(srv.guid)
            host.stats()["run_count"] += 1

            yield data_from_server


if __name__ == host.stats().parent().guid:
    default_script_name = helpers.set_script_name()

    data = get_data_from_server()

    save_data(data, screen_folder)
