# -*- coding: utf-8 -*-

import os
import json
from collections import OrderedDict
import codecs
from xml.etree import ElementTree

import host

SCRIPT_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
LANGUAGE_ID = (
    host.stats().parent()["language"]
    or host.settings("system_wide_options")["i18n_language"]
)

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

save_originals = os.environ.get("SAVE_ORIGINALS") == "True"
__tr_file = os.path.join(SCRIPT_PATH, "{}.ts".format(LANGUAGE_ID))
_translation = OrderedDict()


def load_translation(tr_file):
    _translation.clear()
    if os.path.isfile(tr_file):
        with codecs.open(tr_file, "r", encoding="utf-8") as f:
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
                    if trn_text and (
                        "type" not in trn.attrib or trn.attrib["type"] != "unfinished"
                    ):
                        trn_text = trn_text.encode("utf-8")
                        for child in trn:
                            trn_text += ElementTree.tostring(child, encoding="utf-8")
                        _translation[src_text] = trn_text
                    else:
                        logger.debug("Translation not ready: %s", src_text)
                except:
                    logger.exception("Unhandled exception while loading translate")
    else:
        logger.debug("not a file: %s", tr_file)


load_translation(__tr_file)


def tr(s):
    return _translation.get(s, s)


class Translated(object):
    __instance = None
    __translations = None
    __json = None

    originals = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__translations = {}
            if save_originals:
                cls.originals = {}
            for attr, value in cls.__dict__.iteritems():
                if not attr.startswith("_") and isinstance(value, (str, unicode)):
                    if save_originals:
                        cls.originals[attr] = value
                    cls.__translations[attr] = tr(value)
                    setattr(cls, attr, cls.__translations[attr])
            cls.__instance = super(Translated, cls).__new__(cls, *args, **kwargs)
            logger.debug("__originals: %s", cls.originals)
        return cls.__instance

    @staticmethod
    def build_default_message(item):
        item = item.replace("_", " ")
        return item.capitalize()

    def __getattr__(self, item):
        logger.warning("Undefined translation %s" % item)
        return self.build_default_message(item)

    def to_dict(self):
        return self.__translations

    def to_json(self):
        if self.__json is None:
            self.__json = json.dumps(self.__translations)
        return self.__json


