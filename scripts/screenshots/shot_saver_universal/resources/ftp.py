import os
import ftplib
import threading
from functools import wraps
from collections import deque, namedtuple

import host


try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

__version__ = "1.1.0"
logger.debug("%s version: %s", __name__, __version__)


Status = namedtuple("Status", ["sending", "error", "ftp_error", "success", "in_queue"])
status = Status("sending", "error", "ftp_error", "success", "in_queue")


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


class FTPError(Exception):
    pass


class CheckConnectionError(FTPError):
    pass


class FtpUploadTracker:
    """Upload progress class"""

    def __init__(self, task_guid, file_path, block_size_bytes):
        self.size_written = 0.0
        self.last_shown_percent = 0
        self.task_guid = task_guid
        self.block_size_bytes = block_size_bytes
        self.total_size = os.path.getsize(_win_encode_path(file_path))

    def __call__(self, *args, **kwargs):
        """Handler for storbinary

        See Also:
            https://docs.python.org/2/library/ftplib.html#ftplib.FTP.storbinary
        """
        self.size_written += self.block_size_bytes
        percent_complete = round((self.size_written / self.total_size) * 100)

        if self.last_shown_percent != percent_complete:
            self.last_shown_percent = percent_complete
            logger.debug("%s: %s", self.task_guid, percent_complete)


class FTPClient(object):
    TIMEOUT = 10
    SINGLETON = True
    BLOCK_SIZE_BYTES = 1024
    __INITED__ = False

    def __init__(
        self,
        host,
        port=21,
        user="anonymous",
        passwd="",
        work_dir=None,
        callback=None,
        queue_maxlen=1000,
        check_connection=True,
        passive_mode=True,
    ):
        """FTP client to send files

        Args:
            host (str): Ftp host
            port (int, optional): Ftp port, default: `21 `
            user (str, optional): Ftp username, default: `"anonymous"`
            passwd (str, optional): Ftp user password, default `""`
            work_dir (str, optional): Ftp working directory, default `None`
            callback (callable, optional): Sending process callback, default: `None`
            queue_maxlen (int, optional): Sending queue length, default: `1000`
            check_connection (bool, optional): Check connection on starting
            passive_mode (bool, optional): Enable 'passive' mode if val is true,
             otherwise disable passive mode, default: `True`

        Class attributes:
            TIMEOUT (int): Connection timeout in seconds, default: `10`
            SINGLETON (bool): Check if only one instance created, default: `True`
        """
        if self.SINGLETON and self.__INITED__:
            error_msg = (
                "You should init single instance of {cls_name}<br>"
                "or set {cls_name}.SINGLETON = False if you know what are you doing!!"
            ).format(cls_name=self.__class__.__name__)
            raise RuntimeError(error_msg)
        FTPClient.__INITED__ = True

        self._host = host
        self._port = port
        self._user = user
        self._passwd = passwd
        self._work_dir = work_dir
        self._passive_mode = passive_mode

        self.queue = deque(maxlen=queue_maxlen)

        self._ftp = None

        self.callback = callback or _do_nothing

        self._work_now = False
        logger.debug(self)

        if check_connection:
            self.check_connection()

    def __repr__(self):
        msg = (
            "<{self.__class__.__name__}("
            "{self._host!r}, "
            "port={self._port!r}, "
            "user={self._user!r}, "
            "passwd={hidden_passwd!r}, "
            "work_dir={self._work_dir!r}, "
            "callback={self.callback}, "
            "queue_maxlen={queue_maxlen!r}, "
            "passive_mode={self._passive_mode}"
            ")>"
        ).format(
            self=self,
            hidden_passwd="*" * len(self._passwd),
            queue_maxlen=self.queue.maxlen,
        )
        return msg

    def check_connection(self):
        """Check if it possible to connect"""
        try:
            ftp = ftplib.FTP()
            ftp.connect(self._host, self._port, timeout=self.TIMEOUT)
            ftp.login(self._user, self._passwd)
            ftp.set_pasv(self._passive_mode)
        except ftplib.all_errors as err:
            raise CheckConnectionError(err)
        if self._work_dir:
            try:
                ftp.cwd(self._work_dir)
            except ftplib.error_perm:
                ftp.mkd(self._work_dir)
                ftp.cwd(self._work_dir)

        ftp.quit()

    def _get_connection(self):
        """Connecting to ftp

        Returns:
            ftplib.FTP: Ftp object
        """
        logger.debug("Getting connection...")
        try:
            ftp = ftplib.FTP()
            ftp.connect(self._host, self._port, timeout=self.TIMEOUT)
            ftp.login(self._user, self._passwd)
            if self._work_dir:
                try:
                    ftp.cwd(self._work_dir)
                except ftplib.error_perm:
                    ftp.mkd(self._work_dir)
                    ftp.cwd(self._work_dir)
            ftp.encoding = "utf-8"
            ftp.set_pasv(self._passive_mode)
            logger.debug("Got connection success")
            return ftp
        except ftplib.all_errors:
            logger.warning("Can't get ftp connection", exc_info=True)
            pass

    def _close_connection(self):
        """Close ftp connection"""
        logger.debug("Closing connection...")
        try:
            if self._ftp is not None:
                try:
                    self._ftp.close()
                    logger.debug("Connection closed success")
                except:
                    logger.warning("Can't close connection", exc_info=True)
        finally:
            self._ftp = None

    def _send_file(self, task_guid, file_path, work_dir):
        """Storbinary file with self.ftp

        Args:
            task_guid (str): Task guid
            file_path (str): Full file path
            work_dir (str): Work dir on ftp
        """
        if work_dir is not None:
            work_dir = os.path.normpath(
                "/{}/{}".format(self._work_dir or "/", work_dir)
            )
            try:
                self._ftp.cwd(work_dir)
            except ftplib.error_perm:
                self._ftp.mkd(work_dir)
                self._ftp.cwd(work_dir)

        file_name = os.path.basename(file_path)
        upload_tracker = FtpUploadTracker(task_guid, file_path, self.BLOCK_SIZE_BYTES)
        with open(_win_encode_path(file_path), "rb") as opened_file:
            self._ftp.storbinary(
                "STOR %s" % file_name, opened_file, self.BLOCK_SIZE_BYTES, upload_tracker
            )

    @_run_as_thread
    def _sender(self):
        """Send files in queue"""
        try:
            if self.queue:
                if self._ftp is None:
                    self._ftp = self._get_connection()

                if self._ftp:
                    kwargs = self.queue.popleft()
                    # kwargs = {
                    #     "file_path": file_path,
                    #     "remote_dir": remote_dir,
                    #     "callback": callback,
                    #     "task_guid": task_guid,
                    # }

                    file_path, work_dir = kwargs["file_path"], kwargs["remote_dir"]
                    callback, task_guid = kwargs["callback"], kwargs["task_guid"]

                    logger.debug("%s sending file: %s", task_guid, kwargs)

                    if os.path.isfile(_win_encode_path(file_path)):
                        try:
                            host.timeout(100, lambda: callback(task_guid, status.sending))
                            self._send_file(task_guid, file_path, work_dir)
                            host.timeout(100, lambda: callback(task_guid, status.success))
                        except ftplib.all_errors:
                            logger.debug(
                                "Get exception while trying to send %r, append file to queue",
                                file_path,
                                exc_info=True,
                            )
                            self.queue.append(kwargs)
                            self._close_connection()
                            host.timeout(
                                100, lambda: callback(task_guid, status.ftp_error)
                            )
                            host.timeout(
                                100, lambda: callback(task_guid, status.in_queue)
                            )

                        except Exception as err:  # pylint: disable=W0703
                            logger.error(
                                "Got unhandled exception while sending %r",
                                file_path,
                                exc_info=True,
                            )
                            host.timeout(
                                100, lambda: callback(task_guid, status.error)
                            )

                    else:
                        logger.warning("File %r not found", file_path)
                        host.timeout(
                            100, lambda: callback(task_guid, status.error)
                        )

                host.timeout(500, self._sender)
            else:
                self._work_now = False
                self._close_connection()
        except:
            logger.exception("Unhandled exception in _sender ftp thread")
            host.timeout(
                100, lambda: callback(task_guid, status.error)
            )

    def send(self, file_path, remote_dir=None, callback=None, task_guid=None):
        """

        Args:
            file_path (str): File path
            remote_dir (str, optional): Remote ftp dir
            callback (callable, optional): Function that calling when sending finished
            task_guid (str, optional): Task guid, default: host.random_guid()

        Raises:
            IOError: if file not found
        """

        if not os.path.isfile(_win_encode_path(file_path)):
            raise IOError("File '%s' not found" % file_path)

        if task_guid is None:
            task_guid = host.random_guid()

        callback = callback or self.callback

        kwargs = {
            "file_path": file_path,
            "remote_dir": remote_dir,
            "callback": callback,
            "task_guid": task_guid,
        }

        self.queue.append(kwargs)

        if not self._work_now:
            logger.debug("Start sender")
            self._work_now = True
            self._sender()
        else:
            callback(task_guid, status.in_queue)
            logger.debug("Sender already working")

        return task_guid
