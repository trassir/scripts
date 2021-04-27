import os
import time
import datetime
from collections import deque, namedtuple

import host


try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

__version__ = "1.0.6"
logger.debug("%s version: %s", __name__, __version__)


Status = namedtuple("Status", ["canceled", "exporting", "error", "success", "in_queue"])
status = Status("canceled", "exporting", "error", "success", "in_queue")


def _do_nothing(*args, **kwargs):
    pass


class VideoExporterError(Exception):
    """Base ShotSaver Exception"""

    pass


class VideoExporter(object):
    """"""

    def __init__(
        self,
        file_name_tmpl="{name} ({dt_start} - {dt_end}){sub}.avi",
        export_folder=None,
        callback=None,
        queue_maxlen=1000
    ):
        """

        Args:
            file_name_tmpl (str, optional): Default filename template,
                default: "{name} ({dt_start} - {dt_end}){sub}.avi"
            export_folder (str, optional): Default export path, default: screenshots_folder
            callback (callable, optional): Default callback function, default: None
            queue_maxlen (int, optional): Max queue length, default: 1000
        """
        self._export_folder = ""
        self.export_folder = (
            export_folder or host.settings("system_wide_options")["screenshots_folder"]
        )
        self._now_exporting = False
        self._queue = deque(maxlen=queue_maxlen)
        self.file_name_tmpl = file_name_tmpl
        self._default_prebuffer = host.settings("archive")["prebuffer"] + 2
        self.callback = callback or _do_nothing
        self.__exporting_task = None

    @property
    def export_folder(self):
        """"""
        return self._export_folder

    @export_folder.setter
    def export_folder(self, folder):
        if not os.path.isdir(folder):
            try:
                os.makedirs(folder)
            except OSError as err:
                raise OSError("Can't make dir '{}': {}".format(folder, err))

        self._export_folder = folder

    def _get_prebuffer(self, server_guid, dt_end):
        """Get prebuffer delay

        Args:
            server_guid (str): Server guid, to get prebuffer setting

        Returns:
            int: Prebuffer delay
        """
        setting_path = "/{}/archive".format(server_guid)

        try:
            prebuffer = host.settings(setting_path)["prebuffer"] + 2
        except KeyError:
            prebuffer = self._default_prebuffer

        wait_dt_end = (int(time.mktime(dt_end.timetuple())) + prebuffer) * 1000000

        return "%.0f" % wait_dt_end

    @staticmethod
    def clear_complete_tasks():
        """Cleaning complete tasks"""
        try:
            for task in host.archive_export_tasks_get():
                if (
                    task["state"] > 1
                ):  # 0 - in queue; 1 - exporting; 2 - success; 3 - failed
                    logger.debug("Clear task: %s", task)
                    host.archive_export_task_cancel(
                        task["id"],  # task id from archive_export_tasks_get
                        -1,  # -1 - do not wait for result, 0 - wait forever, > 0 - wait timeout_sec seconds
                        _do_nothing,  # callback_success
                        _do_nothing,  # callback_error
                    )
        except:
            logger.warning(
                "Unhandled exception while clearing complete tasks", exc_info=True
            )

    def _check_queue(self):
        host.timeout(10, self.clear_complete_tasks)
        if self._queue:
            kwargs = self._queue.popleft()
            self._export(**kwargs)

    def _export_checker(self, state, **kwargs):
        callback, task_guid = kwargs["callback"], kwargs["task_guid"]
        logger.debug("Task %s: %s", task_guid, status[state])
        if state == 1:
            if task_guid == self.__exporting_task:
                return
            else:
                self.__exporting_task = task_guid

        callback(task_guid, status[state])
        if state != 1:
            self.__exporting_task = None
            self._now_exporting = False
            self._check_queue()

    def _export(self, **kwargs):
        """"""
        self._now_exporting = True

        def checker(status_):
            self._export_checker(status_, **kwargs)

        host.archive_export(
            kwargs["server_guid"],
            kwargs["channel_guid"],
            kwargs["exporting_path"],
            kwargs["ts_start"],
            kwargs["ts_end"],
            kwargs["options"],
            checker,
        )

    def _create_task(self, **kwargs):
        if self._now_exporting:
            self._queue.append(kwargs)
            state = status.in_queue
        else:
            state = status.exporting
            self.__exporting_task = kwargs["task_guid"]
            self._export(**kwargs)
        kwargs["callback"](kwargs["task_guid"], state)

    def export(
        self,
        channel_full_guid,
        dt_start,
        dt_end=None,
        duration=60,
        prefer_substream=False,
        file_name=None,
        file_path=None,
        options=None,
        callback=None,
        task_guid=None,
    ):
        """Exporting file

        Call callback(success: bool, file_path: str, channel_full_guid: str)
        when export finished, and clear tasks in trassir main control panel

        Note:
            Export task adding only when previous task finished
            You can set dt_start, dt_end, or dt_start, duration for export
            if dt_end is None: dt_end = dt_start + timedelta(seconds=duration)

        Args:
            channel_full_guid (str): Full channel guid; example: "CFsuNBzt_pV4ggECb"
            dt_start (datetime.datetime): datetime instance for export start
            dt_end (datetime.datetime, optional): datetime instance for export end; default: None
            duration (int, optional): Export duration (dt_start + duration seconds) if dt_end is None; default: 10
            prefer_substream (bool, optional): If True - export substream; default: False
            file_name (str, optional): File name with extension; default: _EXPORTED_VIDEO_NAME_TEMPLATE
            file_path (str, optional): Path to save shot; default: screenshots_folder
            options (Dict[str: str], optional): Options dict; default: None
            callback (function, optional): Function that calling when export finished
            task_guid (str, optional): Task guid; default: host.random_guid()

        Raises:
            ValueError: if bad channel guid
            EnvironmentError: if channel not found
            TypeError: if got unexpected datetime object
        """

        task_guid = task_guid or host.random_guid()
        callback = callback or self.callback

        try:
            channel_guid, server_guid = channel_full_guid.split("_")
        except ValueError:
            raise ValueError(
                "Expected full channel guid, got {}".format(channel_full_guid)
            )

        try:
            channel_name = host.settings(
                "/{}/channels/{}".format(server_guid, channel_guid)
            ).name
        except KeyError:
            raise EnvironmentError("Channel %s not found" % channel_full_guid)

        if not isinstance(dt_start, datetime.datetime):
            raise TypeError("Expected datetime, got {}".format(type(dt_start).__name__))

        if dt_end:
            if not isinstance(dt_end, datetime.datetime):
                raise TypeError(
                    "Expected datetime, got {}".format(type(dt_end).__name__)
                )
        else:
            dt_end = dt_start + datetime.timedelta(seconds=duration)

        if options is None:
            options = {}

        ts_start = "%.0f" % (time.mktime(dt_start.timetuple()) * 1000000)
        ts_end = "%.0f" % (time.mktime(dt_end.timetuple()) * 1000000)

        if file_name is None:
            file_name = self.file_name_tmpl.format(
                name=channel_name,
                dt_start=dt_start.strftime("%Y.%m.%d %H-%M-%S"),
                dt_end=dt_end.strftime("%Y.%m.%d %H-%M-%S"),
                sub="_sub" if prefer_substream else "",
            )

        if file_path is None:
            file_path = self.export_folder

        exporting_path = os.path.join(file_path, file_name)

        options_ = {
            "prefer_substream": prefer_substream,
            "postponed_until_ts": self._get_prebuffer(server_guid, dt_end),
        }
        options_.update(options)

        kwargs = {
            "server_guid": server_guid,
            "channel_guid": channel_guid,
            "exporting_path": exporting_path,
            "ts_start": ts_start,
            "ts_end": ts_end,
            "options": options_,
            "callback": callback,
            "task_guid": task_guid,
        }

        host.timeout(100, lambda: self._create_task(**kwargs))

        return task_guid, exporting_path
