# -*- coding: utf-8 -*-
import os
import shutil
import time
from datetime import datetime, timedelta
import tempfile
import host
from base_utils import BaseUtils
import re
from __builtin__ import object as py_object

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()


try:
    from shot_saver import status as STATUS
except ImportError as err:
    logger.exception("Can't import status codes from shot_saver, err: %s", err)
    raise ImportError("Can't import status codes from shot_saver, err: %s", err)

from reactions.executors.executor import Executor


def bytes_to_file(bytes_image, base_folder, prefix=None):
    """Save bytes to temp file
    Args:
        bytes_image (str): Image in bytes
    Returns:
        str: temp file path
    """

    tmp_track_image = tempfile.NamedTemporaryFile(
        suffix=".jpeg", prefix=prefix, dir=base_folder, delete=False
    )
    tmp_track_image.write(bytes_image)
    tmp_track_image.close()
    return tmp_track_image.name


class TempShotsRemover:
    """ Удаление временных шотов через заданный промежуток времени """

    def __init__(self):
        self._working = False
        self.delay_to_del = 180
        self.create_last_time = 0
        self.paths_to_check = []

    def remover(self):
        if not self.paths_to_check:
            self._working = False
            return
        self._working = True
        if time.time() - self.create_last_time < self.delay_to_del:
            #  Если псоледнее создание файла произошло неадвно
            host.timeout(120000, self.remover)
            return
        for path in self.paths_to_check:
            if not os.path.exists(path):
                continue
            if not os.path.isdir(path):
                path = os.path.dirname(path)
            tree_iter = os.walk(path)
            try:
                tree_info = next(tree_iter)
            except StopIteration:
                continue

            for folder in tree_info[1]:
                print(folder)
                to_del_path = os.path.join(path, folder)
                try:
                    shutil.rmtree(os.path.join(to_del_path))
                except OSError:
                    logger.exception("Can't delete folder: %s", to_del_path)

            for _file in tree_info[2]:
                to_del_path = os.path.join(path, _file)
                try:
                    os.remove(to_del_path)
                except OSError:
                    logger.exception("Can't delete file: %s", to_del_path)
        host.timeout(120000, self.remover)

    def add(self, path):
        """
        Args:
            path (str): папка для сохранения временных файлов
        Returns:
        """
        if path not in self.paths_to_check:
            self.paths_to_check.append(path)
        self.create_last_time = time.time()
        if not self._working:
            self.remover()


temp_remover = TempShotsRemover()


def check_path(path):
    """Проверка существования папки для временных изображений"""
    path = BaseUtils.win_encode_path(path)
    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except OSError as err:
            logger.error("Can't make dir '%s': %s", path, err)
            raise OSError("Can't make dir '{}': {}".format(path, err))
    return path


def save_images(imgs, base_folder):
    """
    Сохраняет изображение, возвращает путь до файла.
    При распознавании лица на сервере фото из БД и фото распознанного
    лица из трека лежат в kwargs.get("images") в виде
    kwargs.get("images") = {
                            "db_image": [bytes_1, bytes_2],
                            "track_image": [bytes_3]
                            }
    Args:
        imgs (dict):
        base_folder (str)

    Returns: (str): path to file
    """
    check_path(base_folder)
    img_paths = []
    try:
        for img_source, imgs_list in imgs.iteritems():
            if not imgs_list:
                continue
            for _image in imgs_list:
                if not _image:
                    continue
                path = bytes_to_file(_image, base_folder, prefix="{}_".format(img_source))
                if path:
                    img_paths.append(path)
                    temp_remover.add(base_folder)
        return img_paths
    except TypeError as err:
        logger.error(err)


class ShotSpamFilter(py_object):
    """
    Remembers the timestamp of creating a screenshot on the channel and
    if the time elapsed since the previous screenshot was created
    less than 'same_period', then returns True
    """
    def __init__(self, shot_spam_period):
        """

        Args:
            shot_spam_period (int): period in seconds
        """
        self.shot_spam_period = shot_spam_period
        self.handled_channels = {}

    def is_same(self, channel):
        now = time.time()
        if self.handled_channels.get(channel) is None:
            self.handled_channels[channel] = now
            return
        if now - self.handled_channels.get(channel) > self.shot_spam_period:
            self.handled_channels[channel] = now
            return

        return True


class ReactionsWithScreenshots(Executor):
    """
    Класс для создания и рассылки снимков
    Для работы со скриншотами используется класс ReactionsWithScreenshots,
    этот класс являет потомком Executor с обязательным методом

    ```Executor.execute(channel, tmstmp, alarm_messages, shot_name, *args, **kwargs)```
    Через данный класс выполняется работа по созданию и отправлению скриншотов
     посредством различных объектов Senders.

    Отличительная особенность ReactionsWithScreenshots: класс обладает
     методом add_sender, через который добавляются классы различных
     AdoptedSender (mail, Telegram, ftp)

     All info about the tasks stored in
        self._working[task_guid] = {
            "channel": channel_full_guid,
            "export_path": export_path,
            "ts_start": ts_start,
            "ts_end": ts_end,
            "task_status": "just created",
            "ftp_status": "not started",
            "save_on_disk_status": "not started",
            "created_ts": int(time.time()),
        }
    """

    def __init__(self, delta, base_folder, online_shot=False, save_screen=False, figures=False):
        super(ReactionsWithScreenshots, self).__init__()
        self.delta = delta
        self.base_folder = base_folder
        self.online_shot = online_shot
        self.save_screen = save_screen
        self.figures = figures
        self.temp_folder = os.path.join(self.base_folder, "temp")
        self.shot_saver_obj = None
        self.senders = {}
        self._working = {}
        self.spec_symbols = re.compile(r'[|\\/:*?"<>]')
        self.save_substream = False
        self.shot_spam_filter = None
        logger.debug("DELTA for screenshot: %s", self.delta)

    def add_sender(self, sender):
        if not self.shot_saver_obj:
            raise RuntimeError("shot_saver_obj couldn't be None")
        # if not issubclass(executor.__class__, Executor):
        #     raise TypeError("{} is not subclass of Executor".format(executor.__class__.__name__))
        logger.info("Add sender: %s", sender.__class__.__name__)
        self.senders[sender.__class__.__name__] = sender

    def send_shots(self, task_guid, state):
        """
        shot_saver callback
        Args:
            task_guid (str):
            state (str): "saving", "error", "success", "in_queue"

        Returns:

        """
        try:
            task = self._working[task_guid]
            if state != task["state"]:
                logger.debug("status changed: %s --> %s", task["state"], state)
                task["state"] = state
            if state not in (STATUS.success, STATUS.error):
                return
            if state == STATUS.success:
                images_paths = [task["file_path"]]
                if not self.save_screen:
                    temp_remover.add(task["file_path"])
            else:
                images_paths = []
            alarm_messages = task["alarm_messages"]
            if images_paths and task.get("images") and isinstance(task.get("images"), dict):
                images_paths_list = save_images(task.get("images"), self.temp_folder)
                if images_paths_list:
                    logger.debug("appending db and track images paths")
                    images_paths.extend(images_paths_list)

            for s_name, sender in self.senders.iteritems():
                sender.send(state, images_paths, alarm_messages, channel=task.get("channel"))

        except KeyError as err:
            logger.error("Key error for task_guid: %s, err: %s", task_guid, err)

    def execute(self, channel, ts, alarm_messages, *args, **kwargs):
        """
        При распознавании лица на сервере фото из БД и фото распознанного
        лица из трека лежат в kwargs.get("images") в виде
        kwargs.get("images") = {
                                 "db_image": [bytes_1, bytes_2],
                                 "track_image": [bytes_3]
                                 }

        Args:
            channel (str): channel full guid
            ts (int): (Trassir 16 digit timestamp)
            alarm_messages (dict):
            *args:
            **kwargs:
        Returns:
        """
        if self.shot_spam_filter and self.shot_spam_filter.is_same(channel):
            logger.debug("shot spam filter enabled, break for channel: %s", channel)
            return

        ts = int(ts) + int(self.delta * 1e3)

        if self.online_shot:
            ts = None

        if self.save_substream:
            ts = datetime.now() + timedelta(days=7)

        channel_name = re.sub(self.spec_symbols,
                              "_",
                              BaseUtils.get_object_name_by_guid(channel),
                              )
        zone_name = kwargs.get("zone_name")
        if zone_name:
            file_name = "{channel_name}({zone_name}) (%Y.%m.%d %H-%M-%S.%f).jpg".format(channel_name=channel_name, zone_name=zone_name)
        else:
            file_name = "{channel_name} (%Y.%m.%d %H-%M-%S.%f).jpg".format(channel_name=channel_name)
        if self.save_screen:
            file_path = os.path.join(datetime.now().date().isoformat(), channel_name)
            full_path = os.path.normpath(os.path.join(self.base_folder, file_path))
        else:
            full_path = self.temp_folder
        logger.debug("file path for screen: %s", full_path)

        #  shot_saver.ShotSaver
        task_guid, file_path = self.shot_saver_obj.save(
            channel, ts, figures=self.figures, file_path=full_path, file_name=file_name, callback=self.send_shots
        )
        self._working[task_guid] = {
            "alarm_messages": alarm_messages,
            "state": "just_created",
            "created_ts": int(time.time()),
            "file_path": file_path,
            "images": kwargs.get("images"),
            "channel": channel,
        }
        # logger.debug("all tasks: %s", self._working)
