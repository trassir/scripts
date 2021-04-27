import os
import sys
import argparse
from datetime import datetime
from difflib import get_close_matches

sys.path.append('resources')
sys.path.append('../../../../')
os.environ["SAVE_ORIGINALS"] = "True"

from localization.translation_base import load_translation


parser = argparse.ArgumentParser()
parser.add_argument("target", help="Target lang (ru,en,cn,...)")
parser.add_argument("-s", "--source", help="Source language, default: en", default="en")

args = parser.parse_args()

ts_path = r"resources\%s.ts" % args.target


try:
    load_translation(ts_path)
except Exception as err:
    print("Can't load translation %s" % ts_path)
    print("Got error: %s" % err)
    continue_ = raw_input("Would you like to continue? [y/N]: ").lower() or "n"
    if continue_ != "y":
        exit()

import localization as loc
from localization.translation_base import Translated

__xml_version__ = "1.0"
__encoding__ = "utf-8"
__ts_version__ = "2.1"
__version__ = "1.0.0"


with open("resources/%s.ts" % args.target, "w") as tf:
    tf.write(
        '<?xml version="{xml_ver}" encoding="{enc}"?>\n'
        "<!DOCTYPE TS>\n"
        "<!-- Automatically generated by ts_generator v{ver} at {today} -->\n"
        '<TS version="{ts_ver}" language="{a.target}" sourcelanguage="{a.source}">\n'
        "  <context>\n".format(
            ver=__version__,
            today=datetime.today().date(),
            a=args,
            xml_ver=__xml_version__,
            enc=__encoding__,
            ts_ver=__ts_version__,
        )
    )

    main = getattr(loc, "main", None)
    if main:
        script_name = main.script_name
        if script_name != Translated.build_default_message("script_name"):
            tf.write("    <name>%s</name>\n" % script_name)

    saved_data = {}
    _all_values = set(loc.translation_base._translation.keys())
    for key in sorted(loc.__dict__.keys()):
        item = loc.__dict__[key]
        if isinstance(item, Translated):
            tf.write("\n    <!-- %s -->\n" % item.__class__.__name__)

            # raise ValueError("for instance name: %s, originals: %s" % (item.__class__.__name__, item.originals))
            _originals = {value: key for key, value in item.originals.iteritems()}


            for value in sorted(_originals.keys()):
                key = _originals[value]
                translation = loc.translation_base._translation.get(value)
                if translation:
                    msg = (
                        "    <message>\n"
                        "      <source>{source}</source>\n"
                        "      <translation>{target}</translation>\n"
                        "    </message>\n".format(source=value, target=translation)
                    )
                    try:
                        _all_values.remove(value)
                    except KeyError:
                        pass
                else:
                    msg = (
                        "    <message>\n"
                        "      <source>{source}</source>\n"
                        "      <translation>[{lang}]{source}</translation>\n"
                        "    </message>\n".format(source=value, lang=args.target)
                    )

                if saved_data.get(value):
                    msg = ("    <!-- Translated in '%s' block\n%s    -->\n") % (
                        saved_data[value],
                        msg,
                    )
                else:
                    close_match = get_close_matches(
                        value, saved_data.keys(), n=1, cutoff=0.81
                    )
                    if close_match:
                        print(
                            "WARNING: '%s' is close match to '%s'"
                            % (value, close_match[0])
                        )

                    saved_data[value] = item.__class__.__name__

                tf.write(msg)

    _all_values = list(_all_values)
    if _all_values:
        _all_values.sort()
        msg = "Found %s not used translations in %s (%s" % (len(_all_values), ts_path, ", ".join(_all_values[:3]))
        if len(_all_values) > 3:
            msg += "..."
        print(msg + ")")
        continue_ = raw_input("Would you like to save them in new file? [Y/n]: ").lower() or "y"
        if continue_ == "y":
            tf.write("\n    <!-- Not used in current script -->\n")
            for value in _all_values:
                translation = loc.translation_base._translation.get(value)
                msg = (
                    "    <message>\n"
                    "      <source>{source}</source>\n"
                    "      <translation>{target}</translation>\n"
                    "    </message>\n".format(source=value, target=translation)
                )
                tf.write(msg)

    tf.write("  </context>\n" "</TS>")