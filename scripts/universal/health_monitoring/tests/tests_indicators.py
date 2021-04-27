# pylint: skip-file
from unittest import TestCase

import health_monitoring

_MIN_DURATION = 5


class TestIndicators(TestCase):
    def test_cpu_indicator(self):
        indicator = health_monitoring.CPUIndicator(_MIN_DURATION)
        indicator._health["cpu_usage"] = 70

        self.assertEqual(True, indicator.state_ok())

        indicator._health["cpu_usage"] = 91

        self.assertEqual(False, indicator.state_ok())
        self.assertEqual("\nCPU overloaded (91%)", indicator.error)

    def test_cloud_indicator(self):
        indicator = health_monitoring.CloudIndicator(_MIN_DURATION)
        indicator._health["cloud_have_error"] = 1

        self.assertEqual(False, indicator.state_ok())
        self.assertEqual("\nimport_accounts empty or invalid", indicator.error)

        indicator._health["cloud_have_error"] = 0
        self.assertEqual(True, indicator.state_ok())

    def test_hdd_indicator(self):
        indicator = health_monitoring.HDDIndicator(_MIN_DURATION)
        indicator._health["disks_error_count"] = 0

        self.assertEqual(True, indicator.state_ok())

        indicator._health["disks_error_count"] = 1
        self.assertEqual(False, indicator.state_ok())
        self.assertEqual("\nUnknown error", indicator.error)

    def test_sql_indicator(self):
        indicator = health_monitoring.SQLIndicator(_MIN_DURATION)
        indicator._health["db_connected"] = 0

        self.assertEqual(False, indicator.state_ok())
        self.assertEqual("\nFailed to start connection", indicator.error)

        indicator._health["db_connected"] = 1
        self.assertEqual(True, indicator.state_ok())

    def test_device_indicator(self):
        indicator = health_monitoring.DevicesIndicator(_MIN_DURATION)
        indicator._health["ip_devices_connected"] = 1  # ip_devices_total = 2

        self.assertEqual(False, indicator.state_ok())
        self.assertEqual("\nUnknown error", indicator.error)

        indicator._health["ip_devices_connected"] = 2
        self.assertEqual(True, indicator.state_ok())

    def test_channels_indicator(self):
        indicator = health_monitoring.ChannelsIndicator(_MIN_DURATION)
        indicator._health["channels_network_online"] = 1  # channels_network_total = 2

        self.assertEqual(False, indicator.state_ok())
        self.assertEqual("\nUnknown error", indicator.error)

        indicator._health["channels_network_online"] = 2
        self.assertEqual(True, indicator.state_ok())

    def test_network_indicator(self):
        indicator = health_monitoring.NetworkIndicator(_MIN_DURATION)
        indicator._health[
            "network_really_connected"
        ] = 1  # network_should_be_connected = 2

        self.assertEqual(False, indicator.state_ok())
        self.assertEqual("\nUnknown error", indicator.error)

        indicator._health["network_really_connected"] = 2
        self.assertEqual(True, indicator.state_ok())

    def test_scripts_indicator(self):
        indicator = health_monitoring.ScriptsIndicator(_MIN_DURATION)
        indicator._health["scripts_ok"] = 1  # scripts_total = 2

        self.assertEqual(False, indicator.state_ok())
        self.assertEqual("\nUnknown error", indicator.error)

        indicator._health["scripts_ok"] = 2
        self.assertEqual(True, indicator.state_ok())
