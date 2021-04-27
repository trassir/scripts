import host

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

__version__ = "1.0.1"
logger.debug("%s version: %s", __name__, __version__)


class BaseAlarm(object):
    token = ""

    priority = None
    status = None
    description = None
    comment = None
    type_action = None
    contents = None
    processing = None
    device_guid = None
    created_ts = None
    parent_id = None
    reviewer = None
    primary_account = None
    live_mode = None

    __optional_parameters = (
        ("priority", (str, unicode)),
        ("status", (str, unicode)),
        ("description", (str, unicode)),
        ("comment", (str, unicode)),
        ("type_action", (str, unicode)),
        ("contents", (list, tuple, dict)),
        ("processing", (str, unicode)),
        ("device_guid", (str, unicode)),
        ("created_ts", (int, float, long)),
        ("parent_id", int),
        ("reviewer", (str, unicode)),
        ("primary_account", (str, unicode)),
        ("live_mode", bool),
    )

    def __init__(self,):
        """Base alarm class"""
        logger.info("[%s] alarm inited", self.token)

    def __repr__(self):
        return "<{self.__class__.__name__}({self.description!r})>".format(self=self)

    def fire(self, *args, **kwargs):
        """Generates new alarm event"""
        logger.debug("[%s] firing alarm", self.token)

        if not self.token:
            raise RuntimeError("%s.token is empty" % self.__class__.__name__)

        alarm = {"token": self.token}

        for parameter, instance_type in self.__optional_parameters:
            value = getattr(self, parameter, None)
            if value is not None:
                if isinstance(value, instance_type):
                    alarm[parameter] = value
                else:
                    logger.error(
                        "For %s expected %s got %s",
                        parameter,
                        instance_type,
                        type(value).__name__,
                    )
        try:
            res = host.fire_alarm(alarm)
        except EnvironmentError as err:
            logger.error("Error occurred while tried to fire alarm: %s", err)

        if isinstance(alarm.get("contents"), list):
            alarm["contents"] = [cont.get("type") for cont in alarm["contents"]]
        logger.debug("[%s] prepared alarm: %s", self.token, alarm)

        if res:
            logger.debug("[%s] fired alarm success", self.token)
        else:
            logger.debug("[%s] can't fire alarm", self.token)

        return res
