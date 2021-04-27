# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

import host

from . import pkl, fields
from .fields.field import Field
from exthttp import constant
from helpers import get_logger, main_module

logger = get_logger()

__version__ = "0.0.1"
logger.debug("%s version: %s", __name__, __version__)


def deserialize(instance, data):
    type_ = data.pop("type", None)
    logger.debug("deserialize %s", type_)
    if type_:
        cls = getattr(fields, type_, None) or getattr(main_module, type_, None)
        if cls:
            return cls.deserialize(instance, data)
        else:
            logger.warning("cls %s not found", type_)


class ConfigManager(object):
    def __init__(self, *config, **kwargs):
        """Subclass of dict with save method

        Upload data from config file,
        and save current when call save method

        Args:
            config_file (str): Path to config file
        """
        logger.info("Init %s config params", len(config))
        path = kwargs.pop("path", None)
        if path is None:
            path = constant.SCRIPT_PATH
            app = getattr(main_module, "app", None)
            if app:
                mod = getattr(app, "mod", None)
                if mod:
                    if mod.allow_multiple is True:
                        logger.warning("App is multiple, but use default config path!")
        else:
            if not os.path.exists(path):
                os.makedirs(path)

        self.__config = OrderedDict()
        for item in config:
            self.__config[item.key] = item

        self._config_path = os.path.join(path, "config.pkl")
        self.load_data()

        self._is_clear_requested()

    def __getattr__(self, item):
        try:
            return self.__config[item]
        except KeyError:
            try:
                return getattr(self.__config, item)
            except AttributeError:
                raise AttributeError("Config %s not found. Available settings: %s" % (item, self.__config.keys()))

    def _is_clear_requested(self):
        script_name = host.stats().parent()["name"]
        if "clear_config" in script_name:
            self.clear()
            host.stats().parent()["name"] = script_name.replace("clear_config", "")

    def save_form_data(self, data):
        logger.debug("Save form data: %s", data)
        errors = {}
        for key, item in self.__config.iteritems():
            if isinstance(item, fields.Field):
                try:
                    if item.multiple:
                        item.value = data.get(key, [])
                    else:
                        item.value = data.get(key, [None])[0]
                except ValueError as err:
                    errors[key] = str(err)
                    logger.warning("Cant save field %s=%r", key, item, exc_info=True)
        self.save()

        return not errors, errors

    def clear(self):
        if os.path.isfile(self._config_path):
            os.remove(self._config_path)
            logger.info("Config cleaned: %s", self._config_path)
            host.message("Config cleaned")
        else:
            host.alert("Config not found")

    def load_data(self):
        data = pkl.load(self._config_path, default_type=dict)
        version = data.get("version")
        if version and version != __version__:
            logger.warning("Config version is not same: %s -> %s", version, __version__)

        logger.debug("Loaded data: %s", data)

        for cfg in data.get("config", []):
            if cfg["key"] in self.__config:
                try:
                    self.__config[cfg["key"]] = deserialize(
                        self.__config[cfg["key"]], cfg
                    )
                except:
                    logger.exception("Can't deserialize %s", cfg["key"])

    def save(self):
        """Save self to file"""
        data = {
            "version": __version__,
            "config": []
        }
        for item in self.__config.values():
            if isinstance(item, Field):
                data["config"].append(item.serialize())

        pkl.save(self._config_path, data)
        logger.debug("Config saved to: %s", self._config_path)
        logger.debug("%s", data)
