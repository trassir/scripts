# -*- coding: utf-8 -*-
# Включает дублирование POS_Dump в папку скриншотов.
# Запускается сразу после активации скрипта.
# Switching settings("pos_folder2/terminals")["dump_incoming_data"] = 1/0

terminals = settings("pos_folder2/terminals")
terminals["dump_incoming_data"] = 0 if terminals["dump_incoming_data"] else 1
stats()["run_count"] = terminals["dump_incoming_data"]  # Show state in run_counter
stats().parent()["enable"] = 0  # Turn off script
