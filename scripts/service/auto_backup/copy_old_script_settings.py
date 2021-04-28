import os
from shutil import copyfile
import host

VERSION = "0.2.9"

config_path = os.path.join(
    script_path,
    "AATrubilin__MNRudkovskyi_AutoParking_%s" % VERSION.replace(".", "_"),
    "config.json",
)
config_in_shots = os.path.join(
    host.settings("system_wide_options")["screenshots_folder"],
    "AutoParking config v%s.json" % VERSION
)

if not os.path.exists(config_path):
    raise RuntimeError("Config not found at %s" % config_path)


copyfile(config_path, config_in_shots)
