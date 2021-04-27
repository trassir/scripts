import os
import shutil

from __builtin__ import object
import host

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

import datetime

logger = get_logger()


class Worker(object):
    SLEEP_TIMEOUT_SEC = 60

    def __init__(self, base_path, days_store):
        self.working = False
        self.base_path = base_path
        self.today = datetime.datetime.now().date()
        self.timedelta = datetime.timedelta(days=days_store)
        self._report_delta = self.SLEEP_TIMEOUT_SEC + self.SLEEP_TIMEOUT_SEC / 2

    @staticmethod
    def _time_to_sec(time_):
        return (time_.hour * 60 + time_.minute) * 60 + time_.second

    @property
    def __day_changed(self):
        today = datetime.datetime.now().date()
        changed = today != self.today
        self.today = today
        return changed

    def remove_shots(self):
        if self.timedelta:
            remove_before_date = (
                self.today
                - self.timedelta
            ).isoformat()
            logger.debug("%s remove folders before %s", self.today, remove_before_date)
            for name in os.listdir(self.base_path):
                fp = os.path.join(self.base_path, name)
                if os.path.isdir(fp):
                    if name < remove_before_date:
                        logger.debug("Remove %s", fp)
                        try:
                            shutil.rmtree(fp)
                        except OSError as err:
                            logger.error("Can't delete file: %s", err)

    def _work_iteration(self):
        changed = self.__day_changed
        if changed:
            self.remove_shots()

        if self.working:
            host.timeout(1000 * self.SLEEP_TIMEOUT_SEC, self._work_iteration)

    def run(self):
        self.working = True
        self._work_iteration()


# Example to use
# BASE_SCREENSHOT_FOLDER = os.path.join(
#         host.settings("system_wide_options")["screenshots_folder"], "AlarmMonitor"
#     )
# DAYS_TO_STORE = 5
# worker = Worker(BASE_SCREENSHOT_FOLDER, DAYS_TO_STORE)
# worker.run()
