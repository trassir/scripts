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
        delay_before_assign=1500,
        channels_for_same_cell=None,
        all_displays=None,
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
            channels_for_same_cell(dict|None): Every time show a channel in the same cell
             for it if same_cell is not empty
            all_displays (List(int)| None): display numbers list

        """
        self.alarm_template = alarm_template
        self.am_type = am_type
        self._max_channels = 1
        self.max_channels = max_channels
        self.base_template = base_template
        self.no_motion_check = no_motion_check  # TODO: add
        self.display_duration = display_duration
        self.delay_before_assign = delay_before_assign
        self.channels_for_same_cell = channels_for_same_cell
        self.all_displays = all_displays

        self._monitor_by_channel = None
        self._associated_channels_by_monitor_number = None
        self.associated_channels_by_monitor_number = channels_for_same_cell

        self.am_objects = {}
        self._am_before = None
        self._count = 0
        self._gui = host.object("operatorgui_" + host.settings("").guid)

        self.prepare_before_creation()

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

    def create_monitor(self, display_number, channels_to_display=None):
        """

        Args:
            display_number (int):
            channels_to_display (List(srt)| None):

        Returns:

        """
        if self.am_type == 2:
            logger.debug("initializing show archive for display: %s", display_number)
            am = ShowArchive(
                alarm_template=self.alarm_template,
                base_template=self.base_template,
                display_number=display_number,
                show_channel_duration=self.display_duration,
                no_motion_check=self.no_motion_check,
            )
        else:
            logger.debug("initializing show online for display %s, am type: %s",
                         display_number, self.am_type
                         )
            am = ShowOnline(
                alarm_template=self.alarm_template,
                base_template=self.base_template,
                display_number=display_number,
                max_channels=self.max_channels,
                show_channel_duration=self.display_duration,
                no_motion_check=self.no_motion_check,
                delay_before_assign=self.delay_before_assign,
                channels_for_same_cell=channels_to_display,
            )
        if self.base_template:
            self._gui.show_template(self.base_template, display_number)

        return am

    @property
    def monitor_by_channel(self):
        return self._monitor_by_channel

    @monitor_by_channel.setter
    def monitor_by_channel(self, associated_channels_by_monitor_number):
        self._monitor_by_channel = {}
        for mon_index, channels in associated_channels_by_monitor_number.iteritems():
            for channel in channels:
                self._monitor_by_channel[channel] = mon_index

    @property
    def associated_channels_by_monitor_number(self):
        return self._associated_channels_by_monitor_number

    @associated_channels_by_monitor_number.setter
    def associated_channels_by_monitor_number(self, channels):
        if not channels:
            logger.debug("no channels found to show in fix template")
            return
        self._associated_channels_by_monitor_number = {}

        channels_guids = list(self.channels_for_same_cell)
        for indx, monitor_key in enumerate(self.all_displays):
            _start = indx * self.max_channels
            _end = (indx + 1) * self.max_channels
            self._associated_channels_by_monitor_number[monitor_key] = channels_guids[_start: _end]
        logger.debug("associated_channels_by_monitor_number: %s", self._associated_channels_by_monitor_number)

        self.monitor_by_channel = self._associated_channels_by_monitor_number

    def prepare_before_creation(self):
        if self.associated_channels_by_monitor_number:
            for monitor in self.all_displays:
                channels_to_display = self.associated_channels_by_monitor_number.get(monitor)
                self.am_objects[monitor] = self.create_monitor(monitor, channels_to_display)
        else:
            for monitor in self.all_displays:
                self.am_objects[monitor] = self.create_monitor(monitor)

    def drop_template(self, *args, **kwargs):
        for am_obj in self.am_objects:
            am_obj.drop_template()

    def execute(self, channel, ts, *args, **kwargs):
        if "_" in channel:
            channel = channel.split("_")[0]
        if self.monitor_by_channel:
            monitor = self.monitor_by_channel.get(channel)
            if not monitor:
                logger.debug("monitor not found for channel, return: %s", channel)
                return
            else:
                logger.debug("going to show channels %s on display: %s", channel, monitor)
            self.am_objects[monitor].execute(channel, ts)

        else:
            for am_obj in self.am_objects.itervalues():
                if am_obj.has_channel(channel):
                    logger.debug(
                        "Am on display: %s has channel: %s", am_obj.display_number, channel
                    )
                    am_obj.execute(channel, ts)
                    return
                if am_obj.channels_count() < self.max_channels:

                    logger.debug(
                        "Am on display: %s has space for channel: %s, "
                        "channels_count: %s, max_channels: %s",
                        am_obj.display_number,
                        channel,
                        am_obj.channels_count(),
                        self.max_channels,
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
                    am_object_key = self.all_displays[self._am_before]
                    am_obj = self.am_objects[am_object_key]
                    self._am_before += 1
                else:
                    am_object_key = self.all_displays[0]
                    self._am_before = 1
                    am_obj = self.am_objects[am_object_key]
                logger.debug(
                    "Decided to add channel (%s) on display: %s",
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
        logger.debug(
            "Display number is: %s, max channels is: %s",
            self.display_number,
            self.max_channels,
        )

    def has_channel(self, channel):
        if channel in self._displaying_channels:
            return True

    def channels_count(self):
        return len(self._displaying_channels)

    def clean_template(self):
        self._gui.show(self._CLEAN, self.display_number)

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
            self.clean_template()
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
        logger.debug(
            "diff: %s, show_delay: %s",
            now - event_info.get("event_appended"),
            self.start_show_delay,
        )
        if now - event_info.get("event_appended") > self.start_show_delay:
            logger.debug("step 2")
            if not event_info.get("start_to_show"):
                event_info[
                    "start_to_show"
                ] = now  # Если еще не приступили к отображению
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
            "event_appended": int(time.time()),
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
        delay_before_assign=1500,
        channels_for_same_cell=None,
    ):
        """ Для отображения реал видео

        Args:
            alarm_template (str):
            base_template (str| None):
            display_number (int):
            max_channels (int):
            show_channel_duration (int):
            channels_for_same_cell (List|None):

        """
        super(ShowOnline, self).__init__(
            alarm_template,
            base_template,
            display_number,
            max_channels,
            show_channel_duration,
            no_motion_check,
        )
        self.delay_before_assign = delay_before_assign
        self.channels_for_same_cell = channels_for_same_cell

    def _replace_old(self):
        """Delete the oldest channel from the list before add new one
        """
        oldest_channel, event_info = next(self._displaying_channels.iteritems())
        min_time = event_info.get("start_to_show")

        for channel, event_info in self._displaying_channels.iteritems():
            motion_state = host.object(channel).state("motion")
            if self.no_motion_check and motion_state == "Motion":
                logger.debug(
                    "Motion state is %s on channel (%s), skip it", motion_state, channel
                )
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
                try:
                    motion_state = host.object(channel).state("motion")
                except EnvironmentError as err:
                    logger.error("Can't get notion state for channel: %s, err: %s", channel, err)
                    motion_state = "No Motion"
                if self.no_motion_check and motion_state == "Motion":
                    logger.debug(
                        "Motion state is %s on channel (%s), skip it",
                        motion_state,
                        channel,
                    )
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

    def _show_channels_with_static_cells(self):   # TODO:
        channels_to_show = []
        for channel in self.channels_for_same_cell:
            if channel in self._displaying_channels:
                channels_to_show.append(channel)
            else:
                channels_to_show.append("")
        return channels_to_show

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

        if self.channels_for_same_cell:
            logger.debug("channels for same cell is True: %s", self.channels_for_same_cell)
            channels_to_show = ",".join(self._show_channels_with_static_cells())
        else:
            channels_to_show = ",".join(list(self._displaying_channels))
        logger.debug("assign channels: %s", channels_to_show)

        if self.show_timer_running:

            self._gui.assign_channels(
                channels_to_show, self.display_number
            )
        else:
            # Первый тревожный канал для отображения
            # если используем len(self._displaying_channels) == 1, то в случае,
            # когда количество каналов меняется с 2 до 1 show_template() не нужно
            self._gui.show_template(self.alarm_template, self.display_number)
            host.timeout(
                self.delay_before_assign,
                lambda: self._gui.assign_channels(
                    channels_to_show, self.display_number
                ),
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
        logger.debug("displaying channels: %s", self._displaying_channels)
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
