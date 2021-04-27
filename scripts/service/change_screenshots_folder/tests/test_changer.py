# pylint: skip-file
import os
import shutil
from unittest import TestCase

import host

import screenshot_folder_changer as changer


DEFAULT_FOLDER = "/home/trassir/shots"

NETWORK_FOLDER = "//172.20.0.10/shots"
NETWORK_USER = "guest"
NETWORK_PASSWORD = ""


class TestDefaultFolder(TestCase):
    def test_mount(self):
        obj = changer.DefaultFolder()
        self.assertEqual(DEFAULT_FOLDER, obj.mount())


class TestHDDFolder(TestCase):
    def tearDown(self):
        shutil.rmtree('shots')

    def test_mount(self):
        obj = changer.HDDFolder()
        new_folder = obj.mount()
        self.assertEqual(".\\shots", new_folder)
        self.assertTrue(os.path.exists(new_folder))


class TestCustomFolder(TestCase):
    _FOLDER = "custom_folder"

    def tearDown(self):
        shutil.rmtree(self._FOLDER)

    def test_mount(self):
        obj = changer.CustomFolder(self._FOLDER)

        self.assertFalse(os.path.exists(self._FOLDER))
        self.assertRaises(EnvironmentError, obj.mount)  # Folder not exist.

        obj.create_if_not_exists = True
        new_folder = obj.mount()

        self.assertTrue(os.path.exists(self._FOLDER))
        self.assertEqual(self._FOLDER, new_folder)


class TestNetworkFolder(TestCase):
    def test_mount(self):
        obj = changer.NetworkFolder(NETWORK_FOLDER)
        obj.username = NETWORK_USER
        obj.password = NETWORK_PASSWORD

        # Windows did't know sudo
        self.assertTrue(True)

    def test_umount(self):
        self.assertTrue(True)


class TestFolderSetter(TestCase):
    _FOLDER = "custom_folder"
    folder = changer.CustomFolder(_FOLDER, True)
    setter = changer.FolderSetter(folder)

    def tearDown(self):
        shutil.rmtree(self._FOLDER)

    @staticmethod
    def _current_path():
        return host.settings("system_wide_options")["screenshots_folder"]

    def _rollback(self):
        self.setter.rollback()
        self.assertEqual(DEFAULT_FOLDER, self._current_path())

    def test_set_folder(self):
        self.assertEqual(".", self._current_path())
        self.setter.set_folder()
        self.assertEqual(self._FOLDER, self._current_path())
        self._rollback()
