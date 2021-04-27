# coding: utf-8

import time
import host
from executor import Executor

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger
logger = get_logger()


# ---------------------------------------------------------------------
# Access control systems reactions
# ---------------------------------------------------------------------


class AccessControlOperations(Executor):

    def __init__(
        self,
        access_point_name,
        access_point_type,
        operation_type,
        delay_operations,
    ):
        """
        Args:
            access_point_name (str):
            access_point_type (str): "Sigur" or "Orion"
            operation_type (str): host.tr("открыть дверь") or host.tr("закрыть дверь")
            delay_operations (int):
        """
        self.access_point_name = access_point_name
        self.access_point_obj = host.object(self.access_point_name)
        self.access_point_type = access_point_type
        self.operation_type = operation_type
        self.delay_operations = delay_operations

        self.ts_to_come_back = 0
        self.come_back_timer_is_working = False

    def _open_door(self):
        logger.debug(
            "ACS operation. Access point %s set open.", self.access_point_name
        )
        if self.access_point_type == "Sigur":
            self.access_point_obj.workmode_alwaysopen()  # pylint:disable=E1101
        elif self.access_point_type == "Orion":
            self.access_point_obj.grant_access_once()  # pylint:disable=E1101

    def _close_door(self):
        logger.debug(
            "ACS operation. Access point %s set closed.", self.access_point_name
        )
        if self.access_point_type == "Sigur":
            self.access_point_obj.workmode_alwaysclose()  # pylint:disable=E1101
        elif self.access_point_type == "Orion":
            self.access_point_obj.deny_any_access()  # pylint:disable=E1101

    def _normal(self):
        if self.access_point_type == "Sigur":
            self.access_point_obj.workmode_normal()  # sigur
        elif self.access_point_type == "Orion":
            self.access_point_obj.allow_access_by_key()  # orion

    def _timer(self):
        if self.ts_to_come_back < time.time():
            self._normal()
            self.come_back_timer_is_working = False
        else:
            host.timeout(1000, self._timer)

    def manual_activation(self):
        logger.debug("Manual activation of access point starting.")
        host.stats()['run_count'] += 1
        self.execute()

    def acs_operation(self):
        try:
            self.ts_to_come_back = time.time() + self.delay_operations
            if self.come_back_timer_is_working:
                return
            else:
                self.come_back_timer_is_working = True

            if self.operation_type == host.tr("открыть дверь"):
                self._open_door()
            else:
                self._close_door()
            self._timer()
        except Exception as err:
            logger.exception("Error occur in access control module: %s", err)

    def execute(self, *args, **kwargs):
        self.acs_operation()
