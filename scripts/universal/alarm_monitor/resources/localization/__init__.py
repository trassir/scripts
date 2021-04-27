from .main import Main
from .fr_loc import FaceRecognizerLoc
from .simt_loc import SimtLoc
from .gate_loc import GateLoc
from .gpio_loc import GpioLoc
from .neuro_loc import NeuroLoc
from .popup_loc import PopupLoc
from .events_loc import EventsLoc

main = Main()

fr = FaceRecognizerLoc()
gate = GateLoc()
gpio = GpioLoc()
simt = SimtLoc()
neuro = NeuroLoc()
popup = PopupLoc()
events_loc = EventsLoc()







