# -*- coding: utf-8 -*-

from .translation_base import Translated


class GpioLoc(Translated):
    input_name = "Input name"  # Имя тревожного входа
    associated_channel = "Associated channel"  # Ассоциированный канал
