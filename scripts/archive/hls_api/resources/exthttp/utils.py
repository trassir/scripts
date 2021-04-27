import os
import json
import codecs
from xml.etree import ElementTree
from datetime import datetime, date, time, timedelta

import host

from .constant import LANGUAGE_ID, SCRIPT_PATH
from helpers import get_logger


logger = get_logger()
__translation = dict()
__tr_file = os.path.join(SCRIPT_PATH, "{}.ts".format(LANGUAGE_ID))


if os.path.isfile(__tr_file):
    with codecs.open(__tr_file, "r", encoding="utf-8") as f:
        translation_xml = f.read().encode("utf-8")
        root = ElementTree.fromstring(translation_xml)
        context = root.find("context")
        for msg in context.iterfind("message"):
            try:
                src = msg.find("source")
                trn = msg.find("translation")

                src_text = src.text.encode("utf-8")
                for child in src:
                    src_text += ElementTree.tostring(child, encoding="utf-8")

                trn_text = trn.text
                if trn_text and ("type" not in trn.attrib or trn.attrib["type"] != "unfinished"):
                    trn_text = trn_text.encode("utf-8")
                    for child in trn:
                        trn_text += ElementTree.tostring(child, encoding="utf-8")
                    __translation[src_text] = trn_text
                else:
                    logger.debug("Translation not ready: %s", src_text)
            except:
                logger.exception("Unhandled exception while loading translate")


def tr(s):
    return __translation.get(s, s)


def _json_serializer(data):
    if isinstance(data, (datetime, date, time)):
        return data.isoformat()

    elif isinstance(data, timedelta):
        return str(data).split(".")[0]

    elif isinstance(data, host.ScriptHost.SE_Settings):
        return "settings('{}')".format(data.path)

    elif isinstance(data, host.ScriptHost.SE_Object):
        return "object('{}')".format(data.guid)

    return type(data).__name__


def to_json(data, **kwargs):
    return json.dumps(data, default=_json_serializer, **kwargs)
