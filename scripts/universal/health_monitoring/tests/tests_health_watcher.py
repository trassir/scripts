# pylint: skip-file
import time
import logging
import threading
from datetime import datetime

from unittest import TestCase

import health_monitoring


_MIN_DURATION = 5
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
health_monitoring.logger = logger


def notify(**kwargs):
    print(health_monitoring.BaseUtils.to_json(kwargs, indent=4, sort_keys=True, ensure_ascii=False))


class TestHealthWatcher(TestCase):
    _alarmed = [False, False]

    def _notify(self, idx, kwargs=None):
        self._alarmed[idx] = True
        print("NOTIFY: %s" % kwargs)

    def test_watcher_notify(self):
        min_duration = 2
        hw = health_monitoring.HealthWatcher(min_duration)
        hw.state_change_callback = lambda **kwargs: self._notify(0, kwargs)

        self.assertRaises(health_monitoring.ParameterError, hw.run)

        hw.add_indicator(health_monitoring.CloudIndicator)

        for idx in xrange(min_duration * 4):
            logger.debug("Check health # %s" % idx)
            time.sleep(.5)
            hw.check_health()

        self.assertEqual(True, self._alarmed[0])
