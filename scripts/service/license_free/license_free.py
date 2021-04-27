# -*- coding: utf-8 -*-
# license counting v1.0.2
"""
<parameters>
    <company>EGUvarov, MNRudkovskyi</company>
    <title>license counting</title>
    <version>1.0.2</version>
    <parameter>
        <id>DEBUG</id>
        <type>boolean</type>
        <name>Debug mode</name>
        <value>False</value>
    </parameter>
    <resources>
        <resource>helpers.py</resource>
    </resources>
</parameters>
"""

import os
import time
import host
from functools import wraps
import threading
import helpers

GLOBALS = globals()
DEBUG = GLOBALS.get("DEBUG", False)

helpers.set_script_name()
logger = helpers.init_logger("LicenseFree", debug=DEBUG)


def run_as_thread(func):
    """Run function as thread"""

    @wraps(func)
    def run(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread

    return run


class RunUp:
    """parce license file and reconnect ip-dev according to license"""

    def __init__(self):
        self.all_device_dict = {
            x.guid: x["family"].upper().replace("-", "_")
            for x in host.settings("ip_cameras").ls()
            if x.type == "Grabber" and x["grabber_enabled"]
        }
        self.license_dict = {}
        self.license_list = [
            "DVS1_FULL",
            "DVS1_HIGH",
            "DVS1_MIDDLE",
            "DVS1_SILEN",
            "DVS1_WIDE",
            "DVS1_WIDE_OPTIMA",
            "DVS1_WIDE_SILEN",
            "DVS2_FULL",
            "DVS2_HIGH",
            "DVS2_MIDDLE",
            "DVS2_SILEN",
            "HYBRID",
            "TECHWELL",
            "V4L",
            "XVR",
            "DAHUA_RECORDER",
            "HIKDVR_RECORDER",
            "HIWATCH_RECORDER",
            "LTV_RECORDER",
            "NVR_RECORDER",
            "RVI_RECORDER",
            "HIKVISIONDVR",
            "TRASSIR_RECORDER",
            "VIVOTEK_RECORDER",
            "3S",
            "ACTI",
            "ACTIVECAM",
            "AKSILIUM",
            "AKTECHNOLOGY",
            "ALTERON",
            "AMATEK",
            "ANYFREE",
            "ANYIP",
            "APPRO",
            "ARECONT",
            "ASTROHN",
            "AVER",
            "AVTECH",
            "AXIS",
            "BERGER",
            "BESTDVR",
            "BESTIP",
            "BEWARD",
            "BOLID_IP",
            "BOSCH",
            "BRICKCOM",
            "BSP_SECURITY",
            "CONTOURHD",
            "DAHUA",
            "DALLMEIER",
            "DLINK",
            "DLINKPRO",
            "ETROVISION",
            "EVERFOCUS",
            "EVIDENCE",
            "FALCONEYE",
            "FLIR",
            "FSAN",
            "GEOVISION",
            "GRANDSTREAM",
            "GRUNDIG",
            "GTVS",
            "HIKVISION",
            "HIKVISIONDVR",
            "HIWATCH",
            "HIWATCH_REC",
            "HONEYWELL",
            "HUAWEI",
            "HUNT",
            "ICAM",
            "ICSM",
            "IDIS",
            "INFINITY",
            "IPTRONIC",
            "J2000",
            "JASSUN",
            "KAREL",
            "KEDACOM",
            "KENO",
            "LEVELONE",
            "LONGSE",
            "LTV",
            "MICRODIGITAL",
            "MILESIGHT",
            "MOBILECAM",
            "MOBOTIX",
            "NETPING",
            "NEUTRON",
            "NOVICAM",
            "NOVUS",
            "NVR",
            "OMNY",
            "ONVIF",
            "OPTIMUS",
            "PANASONIC",
            "PELCO",
            "USB",
            "POLYVISION",
            "PROGMATIC",
            "PROVIDEO",
            "QIHAN",
            "RTSP_MJPEG",
            "RTSP",
            "RVI",
            "SATVISION",
            "SIMPLEIP",
            "SMARTEC",
            "RTSP",
            "MJPEG" "SNR",
            "SONY",
            "SPACETECHNOLOGY",
            "SPEZVISION",
            "SUNELL",
            "SUNVISION",
            "SURVEON",
            "TANTOS",
            "TEB",
            "TECSAR",
            "TECSARLEAD",
            "TPTECHNOLOGY",
            "TRASSIR",
            "UNIVIEW",
            "USB_CAM",
            "VESTA",
            "VGUARD",
            "VISIONHITECH",
            "VIVOTEK",
            "WISENET_SAMSUNG",
            "YOKO",
            "ZAVIO",
        ]

        self.parce_file()

    def parce_file(self):
        with open(
            os.path.join(host.path_working(), " Trassir 3 License.txt"), "r"
        ) as f:
            for line in f.readlines():
                line_ = line.replace("\n", "")
                if "LICENSE" in line_:
                    first_split = line_.split(" ")
                    family = first_split[0].split("LICENSE_")[1]
                    if "RTSP" in family:
                        family = "RTSP"

                    num = int(first_split[-1:][0])
                    if family in self.license_list:
                        self.license_dict.update({family: num})

    @run_as_thread
    def reconnect(self):
        logger.debug("All device: %s", self.all_device_dict)
        dev_for_reboot_after = []
        for guid in self.all_device_dict:
            host.settings("ip_cameras/%s" % guid)["grabber_enabled"] = 0
            logger.debug(
                "GUID: %s off device. Setting: %s",
                guid,
                host.settings("ip_cameras/%s" % guid)["grabber_enabled"],
            )
        time.sleep(5)
        logger.debug("License dict: %s", self.license_dict)
        for guid, family in self.all_device_dict.iteritems():
            if family not in self.license_dict:
                host.settings("ip_cameras/%s" % guid)["grabber_enabled"] = 1
                logger.debug(
                    "GUID: %s, FAMILY: %s on device. Setting: %s",
                    guid,
                    family,
                    host.settings("ip_cameras/%s" % guid)["grabber_enabled"],
                )
            else:
                dev_for_reboot_after.append(guid)
                logger.debug(
                    "Add GUID: %s, FAMILY: %s to list after reboot", guid, family
                )
        time.sleep(5)
        for guid in dev_for_reboot_after:
            host.settings("ip_cameras/%s" % guid)["grabber_enabled"] = 1
            logger.debug(
                "After reboot. GUID: %s, on device. Setting: %s",
                guid,
                host.settings("ip_cameras/%s" % guid)["grabber_enabled"],
            )
        MatchLicense()


class MatchLicense:
    """license counting"""

    def __init__(self):
        self.all_device_dict = rp.all_device_dict
        self.license_dict = rp.license_dict
        self.error_dict = {}
        self.start = True
        self.counting()

    def counting(self):
        logger.debug("Start: %s" % self.start)
        self.write()
        self.start = False
        logger.debug("Start: %s" % self.start)
        for guid_ip_dev, family in self.all_device_dict.copy().iteritems():
            logger.debug("guid_ip_dev: %s, family: %s" % (guid_ip_dev, family))
            if family not in self.license_dict:
                if self.license_dict.get("ANYFREE"):
                    self.license_dict["ANYFREE"] -= 1
                    self.all_device_dict.pop(guid_ip_dev)
                    continue
                if self.license_dict.get("HYBRID"):
                    self.license_dict["HYBRID"] -= 1
                    self.all_device_dict.pop(guid_ip_dev)
                    continue
                if self.license_dict.get("ANYIP"):
                    self.license_dict["ANYIP"] -= 1
                    self.all_device_dict.pop(guid_ip_dev)
                    continue
        for guid_ip_dev, family in self.all_device_dict.iteritems():
            if family in self.license_dict:
                if self.license_dict[family] == 0:
                    continue
                self.license_dict[family] -= 1
            else:
                self.error_dict[guid_ip_dev] = family
        logger.debug("Start: %s" % self.start)
        self.write()
        host.message("Done!")

    def write(self):
        try:
            with open(
                host.settings("system_wide_options")["screenshots_folder"]
                + "/"
                + "License_Free.txt",
                "a",
            ) as f:
                if self.start:
                    f.write("В файле лицензии: \n")
                    logger.debug("В файле лицензии:")
                else:
                    f.write("Свободных лицензий: \n")
                    logger.debug("Свободных лицензий:")

                for name, count in self.license_dict.iteritems():
                    f.write("%s - %s \n" % (name, count))
                    logger.debug("%s - %s" % (name, count))
                if self.error_dict:
                    f.write("Не возможно лицензировать: \n")
                    logger.debug("Не возможно лицензировать:")
                    for name, family in self.error_dict.iteritems():
                        f.write("%s - %s \n" % (name, family))
                        logger.debug("%s - %s" % (name, family))
            f.close()
        except Exception as err:
            host.error("Error: %s" % err)
            logger.debug("Error: %s" % err)


old = os.path.join(
    host.settings("system_wide_options")["screenshots_folder"], "License_free.txt"
)
if os.path.isfile(old):
    os.remove(old)


rp = RunUp()
rp.reconnect()
