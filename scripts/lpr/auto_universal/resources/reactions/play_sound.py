# -*- coding: utf-8 -*-

import re
import os
import host
import subprocess
from executor import Executor

if os.name == "nt":
    import winsound

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger
logger = get_logger()


class PlaySound(Executor):
    def __init__(self, sound_name):
        self._path_to_sound_file = ''
        self.path_to_sound_file = sound_name
        self._default_sound_play_device = None
        self.default_sound_play_device = os.name

    @property
    def default_sound_play_device(self):
        return self._default_sound_play_device

    @default_sound_play_device.setter
    def default_sound_play_device(self, os_name):
        if os_name == "nt":
            return
        aplay_reg = r"(sysdefault:?.*)"
        p = subprocess.Popen(
            "aplay -L", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output = p.communicate()[0]
        match = re.findall(aplay_reg, output)
        self._default_sound_play_device = match[0]
        logger.debug("Sound device initialized: %s", self._default_sound_play_device)

    @property
    def path_to_sound_file(self):
        return self._path_to_sound_file

    @path_to_sound_file.setter
    def path_to_sound_file(self, file_name):
        self._path_to_sound_file = os.path.join(os.getcwd(), "sounds", file_name)
        if not os.path.exists(self._path_to_sound_file):
            raise ValueError(host.tr("Не найден файл для звуковых оповещений"))
        logger.debug("Sound file path: %s", self._path_to_sound_file)

    def play_sound(self):
        logger.debug("Start play sound")
        if os.name == "nt":
            winsound.PlaySound(
                self.path_to_sound_file,
                winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NOWAIT,
            )
        else:
            os.system(
                'aplay -D "{sound_device}" "{filename}" &'.format(
                    sound_device=self.default_sound_play_device,
                    filename=self.path_to_sound_file
                )
            )

    def execute(self, *args, **kwargs):
        self.play_sound()
