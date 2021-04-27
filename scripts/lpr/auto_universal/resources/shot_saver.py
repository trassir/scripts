import os
import sys
import time
import datetime
import threading

from functools import wraps
from Queue import Queue, Empty
from collections import namedtuple


import host

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

__version__ = "1.0.2"
logger.debug("%s version: %s", __name__, __version__)


Status = namedtuple("Status", ["saving", "error", "success", "in_queue"])
status = Status("saving", "error", "success", "in_queue")


def _do_nothing(*args, **kwargs):
    pass


def _win_encode_path(path):
    if os.name == "nt":
        try:
            path = path.decode("utf8")
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
    return path


def _run_as_thread(fn):
    """Run function as thread"""

    @wraps(fn)
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
        return t

    return run


def ts_to_dt(ts):
    ts = int(ts)
    if ts > 1e10:
        ts_sec = ts / 1e6
        ts_ms = ts - ts_sec * 1e6
    else:
        ts_sec = ts
        ts_ms = 0

    return datetime.datetime.fromtimestamp(ts_sec) + datetime.timedelta(
        microseconds=ts_ms
    )


def dt_to_ts(dt):
    return int(int(time.mktime(dt.timetuple())) * 1e6 + dt.microsecond)


class Worker(threading.Thread):
    """Thread executing tasks from a given tasks queue"""

    def __init__(self, tasks):
        super(Worker, self).__init__()
        self.tasks = tasks
        self.daemon = True
        self.start()

        self.task_working = False

    def run(self):
        while __name__ in sys.modules.keys():
            try:
                func, args, kwargs = self.tasks.get_nowait()
                self.task_working = True
            except Empty:
                self.task_working = False
                continue

            try:
                func(*args, **kwargs)
            except:
                logger.exception("ThreadPool Worker error")
            finally:
                self.tasks.task_done()


class ThreadPool:
    """Pool of threads consuming tasks from a queue"""

    def __init__(self, num_threads):
        self.tasks = Queue()
        self.workers = [Worker(self.tasks) for _ in xrange(num_threads)]

    @property
    def working(self):
        for worker in self.workers:
            if worker.task_working:
                return True
        return False

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()


class ShotSaverError(Exception):
    """Base ShotSaver Exception"""

    pass


class ShotSaver(object):
    def __init__(
        self,
        pool_size=10,
        callback=None,
        screenshots_folder=host.settings("system_wide_options")["screenshots_folder"],
    ):
        self.timeout_sec = 10
        self.max_tries = 2
        self.file_name_tmpl = "{channel.name} (%Y.%m.%d %H-%M-%S.%f).jpg"

        self.callback = callback or _do_nothing

        self.__thread_pool = None

        self._pool_size = 10
        self.pool_size = pool_size

        self._screenshots_folder = ""
        self.screenshots_folder = screenshots_folder

    @property
    def pool_size(self):
        return self._pool_size

    @pool_size.setter
    def pool_size(self, value):
        self._pool_size = value
        self.__thread_pool = ThreadPool(self._pool_size)

    @property
    def pool_queue_size(self):
        if self.__thread_pool is None:
            return -1
        return self.__thread_pool.tasks.qsize()

    @property
    def pool_working(self):
        if self.__thread_pool is None:
            return None
        return self.__thread_pool.working

    @property
    def screenshots_folder(self):
        return self._screenshots_folder

    @staticmethod
    def __check_path(path):
        path = _win_encode_path(path)
        if not os.path.isdir(path):
            try:
                os.makedirs(path)
            except OSError as err:
                raise OSError("Can't make dir '{}': {}".format(path, err))
        return path

    @screenshots_folder.setter
    def screenshots_folder(self, folder):
        folder = _win_encode_path(folder)
        if not os.path.isdir(folder):
            try:
                os.makedirs(folder)
            except OSError as err:
                raise OSError("Can't make dir '{}': {}".format(folder, err))

        self._screenshots_folder = folder

    @staticmethod
    def __is_file_exists(file_path, timeout=1):
        file_path_encoded = _win_encode_path(file_path)
        if os.path.isfile(file_path_encoded):
            return True
        for _ in xrange(timeout - 1):
            time.sleep(1)
            if os.path.isfile(file_path_encoded):
                return True
        return False

    def __async_shot(
        self, channel_full_guid, file_name, file_path, ts, figures, callback, task_guid
    ):
        method = host.screenshot_v2_figures if figures else host.screenshot_v2

        for _ in xrange(self.max_tries):
            host.timeout(10, lambda: callback(task_guid, status.saving))
            method(channel_full_guid, file_name, file_path, ts)
            logger.debug("Path to check: %s, is exists: %s", os.path.join(file_path, file_name),
                         os.path.exists(os.path.join(file_path, file_name)))
            if self.__is_file_exists(
                os.path.join(file_path, file_name), timeout=self.timeout_sec
            ):
                host.timeout(10, lambda: callback(task_guid, status.success))
                break
        else:
            host.timeout(10, lambda: callback(task_guid, status.error))

    @_run_as_thread
    def _pool_awaiting(self):
        self.__thread_pool.wait_completion()

    def save(
        self,
        channel_full_guid,
        dt=None,
        figures=False,
        file_name=None,
        file_path=None,
        callback=None,
        task_guid=None,
    ):
        task_guid = task_guid or host.random_guid()
        callback = callback or self.callback
        logger.debug(
            "ShotSaver.save(%r, dt=%r, figures=%r, file_name=%r, file_path=%r, callback=%r, task_guid=%r)",
            channel_full_guid,
            dt,
            figures,
            file_name,
            file_path,
            callback,
            task_guid,
        )
        if "_" not in channel_full_guid:
            raise ValueError(
                "Expected full channel guid, got {}".format(channel_full_guid)
            )

        channel_guid, server_guid = channel_full_guid.split("_")

        try:
            server = host.settings("/{server_guid}".format(server_guid=server_guid))
        except KeyError:
            raise EnvironmentError(host.tr("Server %s not found") % server_guid)
        try:
            channel = host.settings(
                "/{server_guid}/channels/{channel_guid}".format(
                    server_guid=server_guid, channel_guid=channel_guid
                )
            )
        except KeyError:
            raise EnvironmentError(
                host.tr("Channel %s not found on server %s")
                % (channel_guid, server.name)
            )

        if dt is None:
            ts = 0
            dt = datetime.datetime.now()
        else:
            if not isinstance(dt, datetime.datetime):
                ts = dt
                try:
                    dt = ts_to_dt(dt)
                except ValueError:
                    raise ValueError(
                        "Can't parse datetime from %s, try to use datetime.datetime instance"
                        % dt
                    )
            else:
                ts = dt_to_ts(dt)

        ts = str(ts)
        file_name = (file_name or self.file_name_tmpl).format(
            channel=channel, server=server
        )
        file_name = dt.strftime(file_name)
        file_path = file_path or self.screenshots_folder
        self.__check_path(file_path)

        self.__thread_pool.add_task(
            self.__async_shot,
            channel_full_guid,
            file_name,
            file_path,
            ts,
            figures,
            callback,
            task_guid,
        )
        host.timeout(10, lambda: callback(task_guid, status.in_queue))
        return task_guid, _win_encode_path(os.path.join(file_path, file_name))
