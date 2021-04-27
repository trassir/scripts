# -*- coding: utf-8 -*-

from executor import Executor
from sound_player import SoundPlayer

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()


class PlaySound(Executor):
    sound_player = SoundPlayer()

    def __init__(self, sound_file):
        self.sound_file = self.sound_player.clear_sound(sound_file)

    def execute(self, *args, **kwargs):
        self.sound_player.play(self.sound_file)
