# -*- coding: utf-8 -*-

import abc
import binascii
from __builtin__ import object as py_object
import host
import time
import json

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()


from base_utils import BaseUtils
import localization as loc


logger.debug("fr module is uploaded")
logger.debug("server guid: %s", host.settings("").guid)

ERR_FLAG = False
if host.settings("").guid != "client":
    try:
        from event_handlers.dbase import person_image
    except RuntimeError as err:
        logger.error(
            "Error occurred while trying from dbase import person_image %s", err
        )
        ERR_FLAG = True
    except Exception as err:
        logger.error(
            "Error occurred while trying from dbase import person_image %s", err
        )
        ERR_FLAG = True


def check_fr_master_guid(server_guid):
    """ Проверяем какой тип БД на указанном сервере
     с распознавателем лиц: локальная или другой сервер
    Для статистики.

    Args:
        server_guid (str): server guid with
    """
    this_server_guid = host.settings("").guid
    if this_server_guid == "client":
        msg = "This is Trassir Client."
    else:
        msg = "This is Trassir Server guid: {s_guid}.".format(s_guid=this_server_guid)

    try:
        master_guid = host.settings(
            "/{server_guid}/face_recognizer".format(server_guid=server_guid)
        )["master_guid"]
        if master_guid != this_server_guid:
            msg = "{} Fr master guid: {} is another server.".format(msg, master_guid)
        logger.debug(msg)
    except KeyError as err:
        if "face_recognizer" in err[0]:
            err_msg = "Face recognizer not found on: {}.".format(server_guid)
        else:
            err_msg = err[0]
        logger.error(err_msg)


def get_folders(server_guid, folders_names=None, depth_level=5):

    """Returns PersonsFolder data

    Args:
        server_guid (str, optional): Server guid. Default: None = current server
        folders_names (list):
        depth_level (int, optional): Maximum distance from root node to children nodes

    Returns:
        Dict[]: Persons folder data
    """

    try:
        root_setting = host.settings(
            "/{server_guid}/persons/".format(server_guid=server_guid)
        )
    except KeyError as err:
        raise KeyError("No access to server with guid: %s, error: %s", server_guid, err)

    all_folders = {}

    def _get_sub_folders(setting, current_depth_level):
        if setting and not (
            depth_level is not None and current_depth_level > depth_level
        ):
            for obj in setting.ls():
                if obj.type == "PersonsSubFolder":
                    all_folders[obj.guid] = unicode(obj.name)
                    _get_sub_folders(obj, current_depth_level + 1)

    _get_sub_folders(root_setting, 1)
    if folders_names:
        all_folders = {
            f_guid: f_name
            for f_guid, f_name in all_folders.iteritems()
            if f_name in folders_names
        }
    return all_folders


def make_alarm_message(channel_name, dt, person_name=None, folder_name=None, score=None):
    person_name = (
        loc.main.fr_unrecognized_person if person_name is None else person_name
    )
    dt = dt.strftime("%H:%M:%S %d-%m-%Y")
    logger.debug(
        "create alarm messages: chan. name: {}, dt: {}, person_name: {},"
        " folder_name: {}, score: {}".format(
            channel_name, dt, person_name, folder_name, score
        )
    )

    alarm_messages = {
        "alert_message": "{event_time}<br><b><font color='red'>{event_type}:</font></b>"
        "<br>{person_name}<br>{on_channel}: {chan_name}".format(
            event_time=dt,
            event_type=loc.fr.face_recognized,
            person_name=person_name,
            on_channel=loc.fr.on_channel,
            chan_name=channel_name,
        ),
        "sms_message": "{event_type}: {person_name}. {on_channel}: {chan_name}".format(
            event_type=loc.fr.face_recognized,
            person_name=person_name,
            on_channel=loc.fr.on_channel,
            chan_name=channel_name,
        ),
    }

    if score is not None:
        alarm_messages["mail_message"] = (
            "{dt}.{text_1}: '{event_type}': {person_name}. {text2}: {group_name}."
            " {text3}: {channel_name}. {text4}: {score}".format(
                dt=dt,
                text_1=loc.fr.alarm,
                event_type=loc.fr.face_recognized,
                person_name=person_name,
                text2=loc.fr.folder,
                group_name=folder_name,
                text3=loc.fr.on_channel,
                channel_name=channel_name,
                text4=loc.fr.percentage_of_similarity,
                score=score,
            )
        )
    else:
        alarm_messages[
            "mail_message"
        ] = "{dt}. {text_1}. {event_type}. {person_name}. {text3}: {channel_name}".format(
            dt=dt,
            text_1=loc.fr.alarm,
            event_type=loc.fr.face_recognized,
            person_name=person_name,
            text3=loc.fr.on_channel,
            channel_name=channel_name,
        )
    return alarm_messages


class SameEvent(py_object):
    def __init__(self):
        self.events = {}
        self.store_time = 60 * 60
        self.working = False

    def old_events_cleaner(self):
        if not self.events:
            self.working = False
            return
        self.working = True
        for channel, persons_info in self.events.items():
            for person, recognize_ts in persons_info.items():
                if time.time() - recognize_ts > self.store_time:
                    logger.debug("Deleting info about person: %s", person)
                    del persons_info[person]
            if not self.events[channel]:
                logger.debug("deleting info about channel: %s", channel)
                del self.events[channel]
        host.timeout(20000, self.old_events_cleaner)

    def is_same(self, channel, person, same_period):
        if not self.events.get(channel):
            self.events[channel] = {}
        channel_events = self.events[channel]
        if not channel_events.get(person):
            logger.debug("adding info about new person: %s", person)
            channel_events[person] = time.time()
            return

        if time.time() - channel_events[person] < same_period:
            # same person found, check time
            if not self.working:
                self.old_events_cleaner()
            logger.debug(
                "same event detected for person: %s, diff is: %s, same period: %s",
                person,
                time.time() - channel_events[person],
                same_period,
            )
            return True
        else:
            logger.debug("person %s was detected long time ago", person)
            channel_events[person] = time.time()


class FrFilter(py_object):
    def __init__(self, min_score):
        self.min_score = min_score

    @staticmethod
    def get_best_person(persons):
        """
        Args:
            persons (list): Cписок из словарей вида
            [{u'comment': u'', u'name': u'Mitrofanov' ...}, ...]
            каждый набор содержит информацию по персоне из БД,
            на которое похоже распознанное лицо

        Returns:
            dict: набор данных персоны с наибольшим person["score"]
        """
        if not isinstance(persons, list):
            return
        best_score = 0
        best_score_index = 0

        for i, person in enumerate(persons):
            score = int(person.get("score", 0))
            if score > best_score:
                best_score = score
                best_score_index = i
        best_person = persons[best_score_index]
        return best_person

    def best_person_data(self, event_data):
        """Ищет данные по распознанной персоне
        Обрабатывается случай, когда checkbox Режим для СКУД отключен

        Args:
            event_data (dict):

        Returns:

        """
        try:
            if not isinstance(event_data, dict):
                logger.debug("event data not dict, return")
                return
            if "name" not in event_data:
                return
            if event_data.get("score", 0) < self.min_score:
                logger.debug(
                    "event data score (%s) < min_score (%s)",
                    event_data.get("score", 0),
                    self.min_score,
                )
                return

            bp = {
                "person_guid": event_data.get("person_guid", "").split("_")[0],
                "name": event_data.get("name"),
                "folder_guid": event_data.get("folder_guid"),
                "score": int(event_data.get("score", 0) / 100),
            }
            return bp
        except Exception as err:
            logger.error(err)

    def best_person_data_acs(self, event_data):
        """
        Ищет данные по распознанной персоне
        Обрабатывается случай, когда checkbox Режим для СКУД включен

        Args:
            event_data:

        Returns:

        """
        try:
            if not isinstance(event_data, dict):
                return
            if "persons" not in event_data:
                return
            best_person = self.get_best_person(event_data.get("persons", []))
            if best_person.get("score", 0) < self.min_score:
                return

            bp = {
                "person_guid": best_person.get("person_guid", "").split("_")[0],
                "name": best_person.get("name", ""),
                "folder_guid": best_person.get("folder_guid", ""),
                "score": int(best_person.get("score", 0) / 100),
            }
            return bp
        except Exception as err:
            logger.error(err)

    @abc.abstractmethod
    def handle(self, event_data):
        pass


class Person(FrFilter):
    def __init__(self, alarm_persons, min_score):

        """ Фильтр для поиска персоны, чье имя в списке персон
        Args:
            alarm_persons (list): alarm persons names list
            min_score (int): minimal score
        """
        super(Person, self).__init__(min_score)
        self.alarm_persons = alarm_persons

    def handle(self, event_data):
        try:
            best_person = self.best_person_data(event_data)
            if (
                best_person
                and isinstance(best_person, dict)
                and best_person.get("name") in self.alarm_persons
            ):
                return best_person
        except Exception as err:
            logger.exception(err)

        # If Physical Access Control System mode enabled
        try:
            best_person_acs = self.best_person_data_acs(event_data)
            if (
                best_person_acs
                and isinstance(best_person_acs, dict)
                and best_person_acs.get("name") in self.alarm_persons
            ):
                return best_person_acs
            logger.debug("person not found in data")
        except Exception as err:
            logger.exception(err)


class Group(FrFilter):
    def __init__(self, fr_folders, min_score):
        """ Фильтр для поиска персоны, которая относится к одной из групп fr_folders

        Args:
            fr_folders (dict): {folder_guid: folder_name}
            min_score (int): minimal score
        """
        super(Group, self).__init__(min_score)
        self.fr_folders = fr_folders

        # if event_data["folder_guid"] in self.fr_folders:

    def handle(self, event_data):
        best_person = self.best_person_data(event_data)
        logger.debug("best person: %s", best_person)
        if (
            best_person
            and isinstance(best_person, dict)
            and best_person.get("folder_guid") in self.fr_folders
        ):
            return best_person
        best_person_acs = self.best_person_data_acs(event_data)
        logger.debug("best person_acs: %s", best_person_acs)
        if (
            best_person_acs
            and isinstance(best_person_acs, dict)
            and best_person_acs.get("folder_guid") in self.fr_folders
        ):
            return best_person_acs
        logger.debug("person doesn't belong to any fr db folder")


class Unrecognized(FrFilter):
    def __init__(self, min_score):
        """ Проверка действительно ли персона относится к нераспознанным

        Args:
            min_score:
        """
        super(Unrecognized, self).__init__(min_score)

    def handle(self, event_data):
        best_person = self.best_person_data(event_data)
        if best_person:
            return False
        best_person_acs = self.best_person_data_acs(event_data)
        if best_person_acs:
            return False
        return True


class AnyFace(FrFilter):
    """Фильтр на любое лицо"""

    def __init__(self, min_score):
        super(AnyFace, self).__init__(min_score)

    def handle(self, event_data):
        best_person = self.best_person_data(event_data)
        if best_person:
            return best_person
        best_person_acs = self.best_person_data_acs(event_data)
        if best_person_acs:
            return best_person_acs
        return True


class FaceRecognizerHandler(py_object):
    def __init__(self, fr_server, obj_storage, same_event_ignoring=0, callback=None):
        """

        Args:
            fr_server (str): fr server guid
            obj_storage (ObjectsStorage): ObjectsStorage instance
            same_event_ignoring (int): time period to ignore same event
            callback:
        """

        self.obj_storage = obj_storage
        self.fr_filter = None
        self.callback = callback
        self.same_event_ignoring = same_event_ignoring
        self._all_fr_folders = None
        self.all_fr_folders = fr_server

    def add_fr_filter(self, fr_filter):
        if not issubclass(fr_filter.__class__, FrFilter):
            raise TypeError(
                "{} is not subclass of FrFilter".format(fr_filter.__class__.__name__)
            )
        logger.info(
            "FaceRecognizerHandler.add executor: %s", fr_filter.__class__.__name__
        )
        self.fr_filter = fr_filter

    @property
    def all_fr_folders(self):
        if self._all_fr_folders:
            return self._all_fr_folders
        else:
            return {}

    @all_fr_folders.setter
    def all_fr_folders(self, server_guid):
        """ {'fpZCqGD0': u'department_1', ... }

        """
        if not isinstance(server_guid, str):
            logger.warning("Server guid not str")
        if not server_guid:
            logger.warning("Server guid is False, can't find fr folders info")
        fr_folders = get_folders(server_guid)
        if not fr_folders:
            logger.warning("No fr folders was found for server: %s", server_guid)
            return
        logger.debug("All fr folders known: %s", fr_folders)
        self._all_fr_folders = fr_folders

    @staticmethod
    def get_track_image(channel, person_guid):
        """

        Args:
            channel (str):
            person_guid (str):

        Returns: list[bytes]

        """

        track_image = host.service_fr_last_track_with_person_get(
            channel, person_guid, 0, 10
        )
        if isinstance(track_image, dict):
            return [binascii.a2b_base64(track_image["image"])]
        else:
            logger.debug(
                "Cant get track image for person %s, error: %s",
                person_guid,
                track_image,
            )

    def event_handler(self, event):
        """
        Args:
            event (obj):
        Returns:

        """
        if event.type != "Face Recognized":
            logger.debug("Event is not Face Recognized, break")
            return
        event_data = json.loads(event.data)
        channel = event_data["channel_guid"]
        server_guid = event_data["server_guid"]
        channel_full = "{channel}_{server_guid}".format(
            channel=channel, server_guid=server_guid
        )

        channel_obj = self.obj_storage.channels.get(channel)
        if not channel_obj:
            logger.info(
                "Channel %s not in channel list", channel,
            )
            return

        #  ts_best_view локальное время сервера, корректировать не нужно
        ts = event_data.get("ts_best_view", 0)

        if not self.fr_filter:
            logger.info("No event filter, break")
        # logger.debug("event data: %s", event_data)

        person_info = self.fr_filter.handle(event_data)
        logger.debug(
            "person info: %s, is isdict: %s", person_info, isinstance(person_info, dict)
        )
        if not person_info:
            logger.debug("Not suitable person")
            return

        if isinstance(person_info, dict):
            logger.debug("person_info: %s", person_info)
            if self.same_event_ignoring and se.is_same(
                channel, person_info.get("person_guid", ""), self.same_event_ignoring
            ):
                return

            if isinstance(self.all_fr_folders, dict):
                _folder_name = self.all_fr_folders.get(
                    person_info.get("folder_guid", ""),
                    person_info.get("folder_guid", ""),
                )
            else:
                _folder_name = person_info.get("folder_guid", "")

            alarm_messages = make_alarm_message(
                channel_name=channel_obj.name,
                dt=BaseUtils.ts_to_dt(ts),
                person_name=person_info.get("name", ""),
                folder_name=_folder_name,
                score=person_info.get("score", 0),
            )

            images = None
            if self.callback:
                if (
                    not ERR_FLAG
                    and host.settings("").guid != "client"
                    and person_info.get("person_guid")
                ):
                    pi = person_image(person_info.get("person_guid"))
                    # logger.debug("pi is: %s", pi)
                    images = {
                        "db_image": pi,
                        "track_image": self.get_track_image(
                            channel, person_info.get("person_guid")
                        ),
                    }
                # from datetime import datetime
                # import time
                #
                # logger.debug(
                #     "chann: %s, trassir ts: %s, trassir dt (%s),"
                #     " time now: %s, dt now: %s, after correction trassir dt is: %s\n",
                #     channel,
                #     event_data["ts_best_view"],
                #     datetime.fromtimestamp(int(event_data["ts_best_view"]) / 1e6),
                #     time.time(),
                #     datetime.now(),
                #     BaseUtils.ts_to_dt(ts),
                # )
                self.callback(channel_full, ts, alarm_messages, images=images)
        else:
            logger.debug("Unknown face.")
            if self.fr_filter.__class__.__name__ in ["AnyFace", "Unrecognized"]:
                alarm_messages = make_alarm_message(
                    channel_name=channel_obj.name,
                    dt=BaseUtils.ts_to_dt(ts),
                    person_name=loc.fr.unrecognized_person,
                )
                if self.callback:
                    self.callback(channel_full, ts, alarm_messages)


se = SameEvent()
