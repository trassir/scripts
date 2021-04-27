import re
import os
import threading
from functools import wraps
from collections import deque
import host

if os.name == "nt":
    import winsound

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger


logger = get_logger()

__version__ = "1.0.0"
logger.debug("%s version: %s", __name__, __version__)


def run_as_thread(fn):
    """Run function as thread"""

    @wraps(fn)
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()
        return t

    return run


class SoundPlayer(object):
    _regex_device = r"(\w*:\w*=\w*.*)(\W*)(\w*.*)"
    _regex_card = r"(CARD=)(\w*)"
    _regex_sys_default = r"(sysdefault:CARD=\w*\b)"
    _regex_select_card = r"(.*\S)(\s\S)(\b.*\d+)"
    __aplay_device = None

    def __init__(self):
        """Sound player for WinOS and TOS"""
        if os.name == "nt":
            self.play_now = self._play_win
            self.sounds_dir = ["sounds"]
            self.decode_filename = lambda filename: filename
        else:
            self.play_now = self._play_tos
            self.sounds_dir = ["/opt/trassir/tech1/sounds"]
            self.decode_filename = self._win_decode

    @property
    def aplay_device(self):
        if self.__aplay_device is None:
            regexp_selected_device = re.compile(r"([\w\s,]+)\s\(CARD=(\w+),DEV=\d\)")
            regexp_device = re.compile(r"((\w+):CARD=([\w]+)[\w,=]*)\n*\s*([^\n]+)")

            self.__aplay_device = regexp_selected_device.search(
                host.settings("system_wide_options")["audio_playback_device"])

            for res in regexp_device.finditer(os.popen("aplay -L").read()):
                if not self.__aplay_device:
                    if res.group(2) == "sysdefault":
                        self.__aplay_device = res.group(1)
                        break
                else:
                    if res.group(4) == self.__aplay_device.group(1) and res.group(3) == self.__aplay_device.group(
                            2):
                        self.__aplay_device = res.group(1)
                        break

        return self.__aplay_device

    @staticmethod
    def _win_decode(path):
        try:
            path = path.decode("utf8").encode("cp1251")
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass
        return path

    def clear_sound(self, filename):
        if filename[-4:].lower() != ".wav":
            raise TypeError("Sound file must be in *.wav format")

        filename_ = self.decode_filename(filename)
        if os.path.isfile(filename_):
            return filename_
        basename = os.path.basename(filename_)
        for base_dir in self.sounds_dir:
            filename_ = os.path.join(base_dir, basename)
            if os.path.isfile(filename_):
                return filename_

        raise ValueError("Sound not found %s" % filename)

    def _play_win(self, sound_file, flags=None):
        """Play sound command on WinOS"""
        logger.debug("Play sound: %s", sound_file)
        if flags is None:
            flags = winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NOWAIT

        winsound.PlaySound(sound_file, flags)

    def _play_tos(self, sound_file, flags="&"):
        """Play sound command on TOS"""
        logger.debug("Play sound: %s", sound_file)
        os.system(
            'aplay -D "{device}" "{sound_file}" {flags}'.format(
                device=self.aplay_device, sound_file=sound_file, flags=flags
            )
        )

    def play(self, sound):
        """Play sound

        Args:
            sound (str): Sound file path

        Raises:
            TypeError: if sound ext is not *.wav
            ValueError: if sound not found
        """
        self.play_now(self.clear_sound(sound))


class SoundQueuePlayer(SoundPlayer):
    """Sound queue player

    This class play sound in queue. It means that the next
    sound will be played only when previous finished.

    Args:
        maxlen (int, optional): Max queue len. Default 10
    """

    def __init__(self, maxlen=10):
        super(SoundQueuePlayer, self).__init__()

        self._queue = deque(maxlen=maxlen)
        self._now_playing = False

    def _play_win(self, sound_file, flags=None):
        if flags is None:
            flags = winsound.SND_FILENAME
        super(SoundQueuePlayer, self)._play_win(sound_file, flags=flags)

    def _play_tos(self, sound_file, flags=""):
        super(SoundQueuePlayer, self)._play_tos(sound_file, flags=flags)

    @run_as_thread
    def _play_queue(self):
        try:
            self._now_playing = True
            while self._queue:
                self.play_now(self._queue.popleft())
        except:
            logger.exception("Unhandled exception in queue player")
        finally:
            self._now_playing = False

    def play(self, sound):
        """Append sound file to queue, and run play queue loop

        Args:
            sound (str): Sound file path

        Raises:
            TypeError: if sound ext is not *.wav
            ValueError: if sound not found
        """
        self._queue.append(self.clear_sound(sound))

        if not self._now_playing:
            self._play_queue()
