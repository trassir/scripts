"""Default script object"""

from base_object import BaseObject, State


class ScriptObject(BaseObject):
    classname = "Script"
    states = (
        State("health", (State.Value("OK"), State.Value("Error"))),
        State("check_me", (State.Value("1"), State.Value("0"))),
    )

    def fire_event_v2(self, message, channel="", data=""):
        """Generate trassir script event

        Args:
            message (str): Event message (p1)
            channel (str, optional): Event associated channel (p2)
            data (str, optional): Event data (p3)
        """
        self.fire_event_("Script: %1", message, channel, data)
