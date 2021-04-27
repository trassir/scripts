# -*- coding: utf-8 -*-

import abc
import time
from datetime import timedelta
from collections import OrderedDict
from __builtin__ import object as py_object
import host
from executor import Executor
from base_utils import BaseUtils

from helpers import get_logger

logger = get_logger()


# ------------------------------------------------------------------------------------------------------------
# Alarm monitor
# ------------------------------------------------------------------------------------------------------------


class AlarmMonitorManager(Executor):
    def __init__(
        self,
        alarm_template,
        am_type,
        max_channels,
        display_duration=30,
        base_template=None,
        no_motion_check=False,
    ):
        """
        Распределяет тревожные каналы по Тревожным мониторам.
        Максимальное количество мониторов 3.
        Сначала заполняется шаблон на одном мониторе, затем, по очереди заполняются
        шаблоны на других мониторах.
        Если на всех мониторах количество отображаемых каналов достигло максимального,
        то отправляем канал для отображения на следующий в очереди монитор.

        Задача класса распределять тревожные каналы равномерно по Тревожным мониторам.
        Args:
            alarm_template (str):
            am_type (int): 1 - show online, 2 - show archive
            max_channels (int):
            display_duration (int):
            base_template (str):
            no_motion_check (bool):
            am_type (str): host.tr("Отобразить канал") | host.tr("Открыть момент в архиве")
        """
        self.alarm_template = alarm_template
        self.am_type = am_type
        self._max_channels = 1
        self.max_channels = max_channels
        self.base_template = base_template
        self.no_motion_check = no_motion_check  # TODO: add
        self.display_duration = display_duration

        self.am_objects = None
        self._am_before = None
        self._count = 0
        self._gui = host.object("operatorgui_" + host.settings("").guid)

    @property
    def max_channels(self):
        return self._max_channels

    @max_channels.setter
    def max_channels(self, max_count):
        if self.am_type == 2:
            self._max_channels = 1
        else:
            self._max_channels = max_count
        logger.debug("max channels: %s", self._max_channels)

    def create_monitor(self, display_number):
        if self.am_type == 2:
            am = ShowArchive(alarm_template=self.alarm_template,
                             base_template=self.base_template,
                             display_number=display_number,
                             show_channel_duration=self.display_duration,
                             no_motion_check=self.no_motion_check,
                             )
        else:
            am = ShowOnline(alarm_template=self.alarm_template,
                            base_template=self.base_template,
                            display_number=display_number,
                            max_channels=self.max_channels,
                            show_channel_duration=self.display_duration,
                            no_motion_check=self.no_motion_check,
                            )
        if self.base_template:
            self._gui.show_template(self.base_template, display_number)

        if self.am_objects is None:
            self.am_objects = []
        self.am_objects.append(am)

    def drop_template(self, *args, **kwargs):
        for am_obj in self.am_objects:
            am_obj.drop_template()

    def execute(self, channel_obj, ts, *args, **kwargs):
        channel = getattr(channel_obj, 'guid')
        if not channel:
            logger.warning("Can't get guid to show in alarm monitor")
            return

        if "_" in channel:
            channel = channel.split("_")[0]
        for am_obj in self.am_objects:
            if am_obj.has_channel(channel):
                logger.debug("Am on display: %s has channel: %s",
                             am_obj.display_number,
                             channel)
                am_obj.execute(channel, ts)
                return
            if am_obj.channels_count() < self.max_channels:

                logger.debug("Am on display: %s has space for channel: %s, "
                             "channels_count: %s, max_channels: %s",
                             am_obj.display_number,
                             channel,
                             am_obj.channels_count(),
                             self.max_channels
                             )
                am_obj.execute(channel, ts)
                return

        # Если все мониторы отображают максимальное количество каналов
        # то принимаем решение о выборе монитора и удалении самого старого канала
        # для освобождения места для нового
        if self._am_before is None:
            self._am_before = len(self.am_objects)

        try:
            if self._am_before < len(self.am_objects):
                am_obj = self.am_objects[self._am_before]
                self._am_before += 1
            else:
                self._am_before = 1
                am_obj = self.am_objects[0]
            logger.debug("Decided to add channel (%s) on display: %s",
                         channel,
                         am_obj.display_number,
                         )
            am_obj.execute(channel, ts)
        except IndexError as err:
            logger.error("Can't get _obj: %s", err)
        except AttributeError as err:
            logger.error("_obj haven't attribute: %s", err)


class AlarmMonitor(py_object):
    __metaclass__ = abc.ABCMeta

    def __init__(
        self,
        alarm_template,
        base_template,
        display_number,
        max_channels,
        show_channel_duration,
        no_motion_check,

    ):
        self.alarm_template = alarm_template
        self.base_template = base_template
        self.display_number = display_number
        self.max_channels = max_channels
        self.show_channel_duration = show_channel_duration
        self.no_motion_check = no_motion_check
        self._gui = host.object("operatorgui_" + host.settings("").guid)
        self._CLEAN = "gui7(-1, '')"
        self._displaying_channels = OrderedDict()
        self.template_dropped = False
        self.show_timer_running = False
        logger.debug("Display number is: %s, max channels is: %s",
                     self.display_number,
                     self.max_channels,
                     )

    def has_channel(self, channel):
        if channel in self._displaying_channels:
            return True

    def channels_count(self):
        return len(self._displaying_channels)

    def clean_template(self, template_name):
        host.settings("templates/{template_name}".format(template_name=template_name))[
            "content"
        ] = self._CLEAN

    def show_base_template(self):
        if self.template_dropped:
            self.template_dropped = False
            return
        if self.base_template:
            # задан base_template
            self._gui.show_template(self.base_template, self.display_number)
            return
        else:
            # не задан base_template, чистим текущий
            self.clean_template(self.alarm_template)
            return

    def drop_template(self):
        if self._displaying_channels:
            logger.debug("Dropping template on display: %s", self.display_number)
            self.template_dropped = True
            self._displaying_channels = OrderedDict()

    @abc.abstractmethod
    def _show_channels_on_display(self, *args, **kwargs):
        pass


class ShowArchive(AlarmMonitor):
    def __init__(
        self,
        alarm_template,
        base_template=None,
        display_number=1,
        show_channel_duration=30,
        no_motion_check=False,
    ):
        """ Для отображения архивного канала

        Args:
            alarm_template (str):
            base_template (str| None):
            display_number (int):
            show_channel_duration (int):

        """
        max_channels = 1  # Only one channel
        super(ShowArchive, self).__init__(
            alarm_template,
            base_template,
            display_number,
            max_channels,
            show_channel_duration,
            no_motion_check,
        )

        self.queue_to_show = OrderedDict()
        self.archive_timer_running = False
        self.archive_start_show = 0
        self.start_show_delay = 5

    def show_timer(self):
        """Loop runner. Deletes channels which time to show expired"""
        count = 0
        now = int(time.time())
        try:
            channel, event_info = next(self._displaying_channels.iteritems())
        except StopIteration:
            logger.debug("no data in _displaying_channels, show timer stopping")
            self.show_timer_running = False
            return

        self.show_timer_running = True
        if event_info.get("start_to_show", 0) and (
            now - event_info.get("start_to_show", 0) > self.show_channel_duration
        ):
            logger.debug("deleting expired channel: %s", channel)
            count += 1
            try:
                del self._displaying_channels[channel]
            except KeyError:
                logger.debug("can't delete _displaying_channels[%s]", channel)

        if not self._displaying_channels:
            self.show_timer_running = False
            self._show_channels_on_display()
            return
        if count:
            self._show_channels_on_display()

        if not event_info.get("start_to_show", 0):
            self._show_channels_on_display()

        host.timeout(1000, self.show_timer)

    def show_archive(self, channel, ts):
        ts_start = BaseUtils.ts_to_dt(int(ts)) - timedelta(seconds=2)
        ts_end = BaseUtils.ts_to_dt(int(ts)) + timedelta(seconds=10)

        start_str = ts_start.strftime("%Y-%m-%d %H:%M:%S")
        end_str = ts_end.strftime("%Y-%m-%d %H:%M:%S")

        logger.debug(
            "open archive, for channel: %s, mon: %s, start: %s, end: %s"
            % (channel, self.display_number, start_str, end_str)
        )

        self._gui.show_archive(channel, self.display_number, start_str, end_str)

    def _show_channels_on_display(self):
        """
        Запускается при изменении в списке каналов для отображения,
        именно здесь происходит работа с методами Trassir
        Returns:
        """
        logger.debug("start show channels on display")
        try:
            channel, event_info = next(self._displaying_channels.iteritems())
        except StopIteration:
            logger.debug("No data in _displaying_channels, try to show base template")
            self.show_base_template()
            return

        now = int(time.time())
        logger.debug("diff: %s, show_delay: %s",
                     now - event_info.get("event_appended"),
                     self.start_show_delay)
        if now - event_info.get("event_appended") > self.start_show_delay:
            logger.debug("step 2")
            if not event_info.get("start_to_show"):
                event_info["start_to_show"] = now  # Если еще не приступили к отображению
                self.show_archive(channel, event_info.get("event_ts"))
            logger.debug("step 3")
        if not self.show_timer_running:
            logger.debug("step 4")
            self.show_timer()

    def _append_channel(self, channel, ts):
        if channel in self._displaying_channels:
            logger.debug("channel already showing on display, return")
            return
        self._displaying_channels[channel] = {
            "start_to_show": 0,
            "event_ts": ts,
            "event_appended": int(time.time())
        }
        self._show_channels_on_display()

    def execute(self, channel, ts, *args, **kwargs):
        """Entry point
        - len(self._displaying_channels) == 1 всегда,
        можем в архиве отображать только один канал.
        - Отображение начинается через 8 секунд после того, как событие произошло,
         чтобы архив записалься на диск. Это даёт 'плавное' проигрывание.
         Если идут два события с разных каналов, то отображаем сначала видео с того,
         кто пришел раньше и первее в очерерди
         риходит событие с другого канала, то
        -

        Args:
            channel (str):
            ts (Trassir 16 digit ts):
            *args:
            **kwargs:

        Returns:

        """
        self._append_channel(channel, ts)


class ShowOnline(AlarmMonitor):
    def __init__(
        self,
        alarm_template,
        base_template=None,
        display_number=1,
        max_channels=6,
        show_channel_duration=30,
        no_motion_check=False,
    ):
        """ Для отображения реал видео

        Args:
            alarm_template (str):
            base_template (str| None):
            display_number (int):
            max_channels (int):
            show_channel_duration (int):

        """
        super(ShowOnline, self).__init__(
            alarm_template,
            base_template,
            display_number,
            max_channels,
            show_channel_duration,
            no_motion_check,
        )

    def _replace_old(self):
        """Delete the oldest channel from the list before add new one
        """
        oldest_channel, event_info = next(self._displaying_channels.iteritems())
        min_time = event_info.get("start_to_show")

        for channel, event_info in self._displaying_channels.iteritems():
            if self.no_motion_check and host.object(channel).state("motion"):
                logger.debug("Motion detected on channel (%s), skip it", channel)
                continue
            if event_info.get("start_to_show") < min_time:
                min_time = event_info.get("start_to_show")
                oldest_channel = channel
        logger.debug("deleting old channel: %s", oldest_channel)
        try:
            del self._displaying_channels[oldest_channel]
        except KeyError:
            logger.debug("can't delete _displaying_channels[%s]", oldest_channel)

    def show_timer(self):
        """Loop runner. Deletes channels which time to show expired"""
        self.show_timer_running = True
        count = 0
        now = int(time.time())
        for channel, event_info in self._displaying_channels.items():
            if event_info.get("start_to_show", 0) and (
                now - event_info.get("start_to_show", 0) > self.show_channel_duration
            ):
                if self.no_motion_check and host.object(channel).state("motion"):
                    logger.debug("Motion detected on channel (%s), skip it", channel)
                    continue
                logger.debug("deleting expired channel: %s", channel)
                try:
                    del self._displaying_channels[channel]
                    count += 1
                except KeyError:
                    logger.debug("can't delete _displaying_channels[%s]", channel)

        if not self._displaying_channels:
            self.show_timer_running = False
            self._show_channels_on_display()
            return

        if count:
            self._show_channels_on_display()
        host.timeout(1000, self.show_timer)

    def _show_channels_on_display(self):
        """
        Запускается при изменении в списке каналов для отображения,
        именно здесь происходит работа с методами Trassir
        Returns:

        """
        if not self._displaying_channels:
            # Нет тревожных каналов для отображения
            self.show_base_template()
            return

        if not self.show_timer_running:
            # Первый тревожный канал для отображения
            # если используем len(self._displaying_channels) == 1, то в случае,
            # когда количество каналов меняется с 2 до 1 show_template() не нужно
            self._gui.show_template(self.alarm_template, self.display_number)
            self.clean_template(self.alarm_template)
        logger.debug("assign channels: %s", ",".join(self._displaying_channels))
        self._gui.assign_channels(
            ",".join(self._displaying_channels), self.display_number
        )
        if not self.show_timer_running:
            self.show_timer()

    def _append_channel(self, channel, ts):
        """
        Если канал уже отображается, то его счетчик запускается снова
        Если количество отображаемых каналов на монитеоре достигло максимального,
        то удаляем самый старый канал.

        Args:
            channel:
            ts:
        Returns:
        """
        if channel in self._displaying_channels:
            self._displaying_channels[channel] = {
                "start_to_show": int(time.time()),
                "event_ts": ts,
            }
            return
        if len(self._displaying_channels) >= self.max_channels:
            self._replace_old()
        self._displaying_channels[channel] = {
            "start_to_show": int(time.time()),
            "event_ts": ts,
        }
        self._show_channels_on_display()

    def execute(self, channel, ts, *args, **kwargs):
        """Entry point

        Args:
            channel (str):
            ts (Trassir 16 digit ts):
            *args:
            **kwargs:

        Returns:

        """
        self._append_channel(channel, ts)
