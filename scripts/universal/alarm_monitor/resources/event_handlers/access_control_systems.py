# -*- coding: utf-8 -*-

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

import time
from __builtin__ import object as py_object
import host
import localization as loc


# ---------------------------------------------------------------------
# Access control systems reactions
# ---------------------------------------------------------------------


class AccessControlOperations(py_object):
    def __init__(
        self,
        access_point_name,
        access_point_type,
        operation_type,
        delay_operations,
        show_message,
        show_message_delay,
    ):
        self.access_point_name = access_point_name
        self.access_point_obj = host.object(self.access_point_name)
        self.access_point_type = access_point_type
        self.operation_type = operation_type
        self.delay_operations = delay_operations
        self.show_message = show_message
        self.show_message_delay = show_message_delay
        self.ts_to_come_back = 0
        self.come_back_timer_is_working = False

    def _open_door(self):
        logger.debug(
            "ACS operation. Access point %s set open.", self.access_point_name
        )
        if self.access_point_type == "Sigur":
            try:
                self.access_point_obj.workmode_alwaysopen()  # pylint:disable=E1101
            except EnvironmentError as err:
                logger.error("error occurred when tried call Sigur method: %s", err)
        elif self.access_point_type == "Orion":
            try:
                self.access_point_obj.grant_access_once()  # pylint:disable=E1101
            except EnvironmentError as err:
                logger.error("error occurred when tried call Orion method: %s", err)

    def _close_door(self):
        logger.debug(
            "ACS operation. Access point %s set closed.", self.access_point_name
        )
        if self.access_point_type == "Sigur":
            try:
                self.access_point_obj.workmode_alwaysclose()  # pylint:disable=E1101
            except EnvironmentError as err:
                logger.error("error occurred when tried call Sigur method: %s", err)

        elif self.access_point_type == "Orion":
            try:
                self.access_point_obj.deny_any_access()  # pylint:disable=E1101
            except EnvironmentError as err:
                logger.error("error occurred when tried call Orion method: %s", err)

    def _normal(self):
        if self.access_point_type == "Sigur":
            try:
                self.access_point_obj.workmode_normal()  # sigur
            except EnvironmentError as err:
                logger.error("error occurred when tried call Sigur method: %s", err)
        elif self.access_point_type == "Orion":
            try:
                self.access_point_obj.allow_access_by_key()  # orion
            except EnvironmentError as err:
                logger.error("error occurred when tried call Orion method: %s", err)

    def _timer(self):
        if self.ts_to_come_back < time.time():
            self._normal()
            self.come_back_timer_is_working = False
        else:
            host.timeout(1000, self._timer)

    def acs_operation(self):
        try:
            self.ts_to_come_back = time.time() + self.delay_operations
            if self.come_back_timer_is_working:
                return
            else:
                self.come_back_timer_is_working = True

            if self.operation_type == loc.main.pacs_open_the_door:
                self._open_door()
            else:
                self._close_door()
            self._timer()
        except Exception as err:
            logger.exception("Error occurred in access control module: %s", err)