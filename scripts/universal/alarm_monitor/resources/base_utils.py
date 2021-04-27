# -*- coding: utf-8 -*-

import os
import ssl
import time
import json
import pickle
import base64
import urllib2
import httplib
import threading
from functools import wraps
from datetime import datetime, date, timedelta
import host


class BaseUtils:  # pylint: disable=R0904,C1001
    """Base utils for your scripts"""

    _FOLDERS = {obj[1]: obj[3] for obj in host.objects_list("Folder")}
    _TEXT_FILE_EXTENSIONS = [".txt", ".csv", ".log"]


    _IMAGE_EXT = [".png", ".jpg", ".jpeg", ".bmp"]
    _HTML_IMG_TEMPLATE = """<img src="data:image/png;base64,{img}" {attr}>"""

    _SCR_DEFAULT_NAMES = [
        "Yeni skript",
        "Unnamed Script",
        "უსახელო სკრიპტი",
        "Жаңа скрипт",
        "Script nou",
        "Новый скрипт",
        "Yeni skript dosyası",
        "Новий скрипт",
        "未命名脚本",
    ]

    def __init__(self):
        pass

    # noinspection PyUnusedLocal
    @staticmethod
    def do_nothing(*args, **kwargs):  # # pylint: disable=W0613
        """Ничего не делает.

        Returns:
            :obj:`bool`: ``True``
        """
        return True

    @staticmethod
    def run_as_thread(func):
        """Декоратор для запуска функций в отдельном потоке.

        Returns:
            :obj:`threading.Thread`: Функция в отдельном потоке

        Examples:
            >>> import time
            >>>
            >>>
            >>> @BaseUtils.run_as_thread
            >>> def run_count_timer():
            ...     time.sleep(1)
            ...     host.stats()["run_count"] += 1
            >>>
            >>>
            >>> run_count_timer()
        """

        @wraps(func)
        def run(*args, **kwargs):
            thread = threading.Thread(target=func, args=args, kwargs=kwargs)
            thread.daemon = True
            thread.start()
            return thread

        return run

    @staticmethod
    def catch_request_exceptions(func):
        """Catch request errors"""

        @wraps(func)
        def wrapped(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except urllib2.HTTPError as err:
                return err.code, "HTTPError: {}".format(err.code)
            except urllib2.URLError as err:
                return err.reason, "URLError: {}".format(err.reason)
            except httplib.HTTPException as err:
                return err, "HTTPException: {}".format(err)
            except ssl.SSLError as err:
                return err.errno, "SSLError: {}".format(err)

        return wrapped

    @staticmethod
    def win_encode_path(path):
        """Изменяет кодировку на ``"cp1251"`` для WinOS.

        Args:
            path (:obj:`str`): Путь до файла или папки

        Returns:
            :obj:`str`: Декодированый путь до файла или папки

        Examples:
            >>> path = r"D:/Shots/Скриншот.jpeg"
            >>> os.path.isfile(path)
            False
            >>> os.path.isfile(BaseUtils.win_encode_path(path))
            True
        """
        if os.name == "nt":
            try:
                path = path.decode("utf8")
            except (UnicodeDecodeError, UnicodeEncodeError):
                pass

        return path

    @staticmethod
    def is_file_exists(file_path, tries=1):
        """Проверяет, существует ли файл.

        Проверка происходит в течении ``tries`` секунд.

        Warning:
            | Запускайте функцию только в отдельном потоке если ``tries > 1``
            | Вторая и последующие проверки производятся с ``time.sleep(1)``

        Args:
            file_path (:obj:`str`): Полный путь до файла
            tries (:obj:`int`, optional): Количество проверок. По умолчанию ``tries=1``

        Returns:
            :obj:`bool`: ``True`` if file exists, ``False`` otherwise

        Examples:
            >>> BaseUtils.is_file_exists("_t1server.settings")
            True
        """
        file_path_encoded = BaseUtils.win_encode_path(file_path)
        if os.path.isfile(file_path) or os.path.isfile(file_path_encoded):
            return True
        for _ in xrange(tries - 1):
            time.sleep(1)
            if os.path.isfile(file_path) or os.path.isfile(file_path_encoded):
                return True
        return False

    @staticmethod
    def is_folder_exists(folder):
        """Проверяет существование папки и доступ на запись.

        Args:
            folder (:obj:`str`): Путь к папке.

        Raises:
            IOError: Если папка не существует

        Examples:
            >>> BaseUtils.is_folder_exists("/test_path")
            IOError: Folder '/test_path' is not exists
        """

        if not os.path.isdir(folder):
            raise IOError("Folder '{}' is not exists".format(folder))

        readme_file = os.path.join(folder, "readme.txt")
        with open(readme_file, "w") as opened_file:
            opened_file.write(
                "If you see this file - Trassir script have no access to remove it!"
            )
        os.remove(readme_file)

    @classmethod
    def is_template_exists(cls, template_name):
        """Проверяет существование шаблона

        Args:
            template_name (:obj:`str`): Имя шаблона

        Returns:
            :obj:`bool`: :obj:`True` если шаблон существует, иначе :obj:`False`
        """
        for tmpl_ in host.settings("templates").ls():
            if tmpl_.name == template_name:
                return True
        return False

    @classmethod
    def _json_serializer(cls, data):
        """JSON serializer for objects not serializable by default"""
        if isinstance(data, (datetime, date)):
            return data.isoformat()

        elif isinstance(data, host.ScriptHost.SE_Settings):
            return "settings('{}')".format(data.path)

        elif isinstance(data, host.ScriptHost.SE_Object):
            return "object('{}')".format(data.guid)

        return type(data).__name__

    @classmethod
    def to_json(cls, data, **kwargs):
        """Сериализация объекта в JSON стрку

        Note:
            Не вызывает ошибку при сериализации объектов :obj:`datetime`,
            :obj:`date`, :obj:`SE_Settings`, :obj:`SE_Object`

        Args:
            data (:obj:`obj`): Объект для сериализации

        Returns:
            :obj:`str`: JSON строка

        Examples:
            >>> obj = {"now": datetime.now()}
            >>> json.dumps(obj)
            TypeError: datetime.datetime(2019, 4, 2, 18, 01, 33, 881000) is not JSON serializable
            >>> BaseUtils.to_json(obj, indent=None)
            '{"now": "2019-04-02T18:01:33.881000"}'
        """

        return json.dumps(data, default=cls._json_serializer, **kwargs)

    @staticmethod
    def ts_to_dt(ts):  # pylint: disable=C0103
        """Конвертирует timestamp в :obj:`datetime` объект

        Args:
            ts (:obj:`int`): Timestamp

        Returns:
            :obj:`datetime`: Datetime объект

        Examples:
            >>> BaseUtils.ts_to_dt(1564109694242000)
            datetime.datetime(2019, 7, 26, 9, 54, 54, 242000)
        """
        if ts > 1e10:
            ts_sec = int(ts / 1e6)
            ts_ms = int(ts - ts_sec * 1e6)
        else:
            ts_sec = int(ts)
            ts_ms = 0

        return datetime.fromtimestamp(ts_sec) + timedelta(microseconds=ts_ms)

    @staticmethod
    def dt_to_ts(dt):  # pylint: disable=C0103
        """Конвертирует :obj:`datetime` объект в trassir timestamp

        Args:
            dt (:obj:`datetime`): Datetime

        Returns:
            :obj:`int`: Trassir timestamp

        Examples:
            >>> BaseUtils.ts_to_dt(datetime(2019, 7, 26, 9, 54, 54, 242000))
            1564109694242000
        """
        return int(int(time.mktime(dt.timetuple())) * 1e6 + dt.microsecond)

    @classmethod
    def lpr_flags_decode(cls, flags):
        """Преобразует флаги события AutoTrassir

        Приводит флаги события человекочитаемый список

        Note:
            Список доступных флагов:

            - ``LPR_UP`` - Направление движения вверх
            - ``LPR_DOWN`` - Направление движения вниз

            - ``LPR_BLACKLIST`` - Номер в черном списке
            - ``LPR_WHITELIST`` - Номер в черном списке
            - ``LPR_INFO`` - Номер в информационном списке

            - ``LPR_FIRST_LANE`` - Автомобиль двигается по первой полосе
            - ``LPR_SECOND_LANE`` - Автомобиль двигается по второй полосе
            - ``LPR_THIRD_LANE`` - Автомобиль двигается по третей полосе

            - ``LPR_EXT_DB_ERROR`` - Ошибка во внешнем списке
            - ``LPR_CORRECTED`` - Номер исправлен оператором

        Args:
            flags (:obj:`int`): Биты LPR события. Как правило аргумент :obj:`ev.flags`
                события :obj:`SE_LprEvent` AutoTrassir. Например :obj:`536870917`

        Returns:
            List[:obj:`str`]: Список флагов

        Examples:
            >>> BaseUtils.lpr_flags_decode(536870917)
            ['LPR_UP', 'LPR_BLACKLIST']
        """
        return [bit for bit, code in cls._LPR_FLAG_BITS.iteritems() if flags & code]

    @classmethod
    def image_to_base64(cls, image):
        """Создает base64 из изображения

        Args:
            image (:obj:`str`): Путь к изображению или изображение

        Returns:
            :obj:`str`: Base64 image

        Examples:
            >>> BaseUtils.image_to_base64(r"manual/en/cloud-devices-16.png")
            'iVBORw0KGgoAAAANSUhEUgAAB1MAAAH0CAYAAABo5wRhAAAACXBIWXMAAC4jA...'
            >>> BaseUtils.image_to_base64(open(r"manual/en/cloud-devices-16.png", "rb").read())
            'iVBORw0KGgoAAAANSUhEUgAAB1MAAAH0CAYAAABo5wRhAAAACXBIWXMAAC4jA...'
        """
        _, ext = os.path.splitext(image)

        if ext.lower() in cls._IMAGE_EXT:
            image = cls.win_encode_path(image)
            if not BaseUtils.is_file_exists(image):
                return ""

            with open(image, "rb") as image_file:
                image = image_file.read()

        return base64.b64encode(image)

    @classmethod
    def base64_to_html_img(cls, image_base64, **kwargs):
        """Возвращает base64 изображение в `<img>` html теге

        Args:
            image_base64 (:obj:`str`): Base64 image
            **kwargs: HTML `<img>` tag attributes. Подробнее на `html.com
                <https://html.com/tags/img/#Attributes_of_img>`_

        Returns:
            :obj:`str`: html image

        Examples:
            >>> base64_image = BaseUtils.image_to_base64(r"manual/en/cloud-devices-16.png")
            >>> html_image = BaseUtils.base64_to_html_img(base64_image, width=280, height=75)
            >>> html_image
            '<img src="data:image/png;base64,iVBORw0KGgoAA...Jggg==" width="280" height="75">'
            >>> host.message(html_image)

                .. image:: images/popup_sender.image.png
        """
        html_img = cls._HTML_IMG_TEMPLATE.format(
            img=image_base64,
            attr=" ".join(
                '%s="%s"' % (key, value) for key, value in kwargs.iteritems()
            ),
        )
        return html_img

    @staticmethod
    def save_pkl(file_path, data):
        """Сохраняет данные в `.pkl` файл

        Args:
            file_path (:obj:`str`): Путь до файла
            data: Данные для сохранения

        Returns:
            :obj:`str`: Абсолютный путь до файла

        Examples:
            >>> data = {"key": "value"}
            >>> BaseUtils.save_pkl("saved_data.pkl", data)
            'D:\\DSSL\\Trassir-4.1-Client\\saved_data.pkl'

        """
        if not file_path.endswith(".pkl"):
            file_path = file_path + ".pkl"

        with open(file_path, "wb") as opened_file:
            pickle.dump(data, opened_file)

        return os.path.abspath(file_path)

    @staticmethod
    def load_pkl(file_path, default_type=dict):
        """Загружает данные из `.pkl` файла

        Args:
            file_path (:obj:`str`): Путь до файла
            default_type (optional):
                Тип данных, возвращаемый при неудачной загрузке данных из файла.
                По умолчанию :obj:`dict`

        Returns:
            Данные из файла или :obj:`default_type()`

        Examples:
            >>> BaseUtils.load_pkl("fake_saved_data.pkl")
            {}
            >>> BaseUtils.load_pkl("fake_saved_data.pkl", default_type=list)
            []
            >>> BaseUtils.load_pkl("fake_saved_data.pkl", default_type=int)
            0
            >>> BaseUtils.load_pkl("fake_saved_data.pkl", default_type=str)
            ''
            >>> BaseUtils.load_pkl("saved_data.pkl")
            {'key': 'value'}
        """

        if not file_path.endswith(".pkl"):
            file_path = file_path + ".pkl"

        data = default_type()

        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as opened_file:
                    data = pickle.load(opened_file)
            except (EOFError, IndexError, ValueError, TypeError):
                # dump file is empty or broken
                pass

        return data

    @classmethod
    def get_object(cls, obj_id):
        """Возвращает объект Trassir, если он доступен, иначе ``None``

        Args:
            obj_id (:obj:`str`): Guid объекта или его имя

        Returns:
            :obj:`ScriptHost.SE_Object`: Объект Trassir или ``None``

        Examples:
            >>> obj = BaseUtils.get_object("EZJ4QnbC")
            >>> if obj is None:
            ...     host.error("Object not found")
            ... else:
            ...     host.message("Object name is {0.name}".format(obj))
        """
        if not isinstance(obj_id, (str, unicode)):
            raise TypeError(
                "Expected str or unicode, got '{}'".format(type(obj_id).__name__)
            )
        obj = host.object(obj_id)
        try:
            obj.name
        except EnvironmentError:
            # Object not found
            obj = None
        return obj

    @classmethod
    def get_object_name_by_guid(cls, guid):
        """Возвращает имя объекта Trassir по его guid

        Tip:
            Можно использовать:

            - guid объекта ``"CFsuNBzt"``
            - guid объекта + guid сервера ``"CFsuNBzt_pV4ggECb"``

        Args:
            guid (:obj:`str`): Guid объекта Trassir

        Returns:
            :obj:`str`: Имя объекта, если объект найден, иначе ``guid``

        Examples:
            >>> BaseUtils.get_object_name_by_guid("EZJ4QnbC")
            'AC-D2141IR3'
            >>> BaseUtils.get_object_name_by_guid("EZJ4QnbC-")
            'EZJ4QnbC-'
        """
        guid = guid.split("_", 1)[0]
        obj = cls.get_object(guid)
        if obj is None:
            name = guid
        else:
            name = obj.name
        return name

    @classmethod
    def get_full_guid(cls, obj_id):
        """Возвращает полный guid объекта

        Args:
            obj_id (:obj:`str`): Guid объекта или его имя

        Returns:
            :obj:`str`: Полный guid объекта
        """

        tr_obj = cls.get_object(obj_id)
        full_guid = None
        if tr_obj is not None:
            for obj in host.objects_list(""):
                if tr_obj.guid == obj[1]:
                    full_guid = "{}_{}".format(obj[1], cls._FOLDERS.get(obj[3], obj[3]))
                    break
        return full_guid

    @classmethod
    def get_server_guid(cls):
        """Возвращает guid текущего сервра

        Returns:
            :obj:`str`: Guid сервера

        Examples:
            >>> BaseUtils.get_server_guid()
            'client'
        """
        return host.settings("").guid

    @classmethod
    def get_script_name(cls):
        """Возвращает имя текущего скрипта

        Returns:
            :obj:`str`: Имя скрипта

        Examples:
            >>> BaseUtils.get_script_name()
            'Новый скрипт'
        """
        return host.stats().parent()["name"] or __name__

    @classmethod
    def get_screenshot_folder(cls):
        """Возвращает путь до папки скриншотов

        При этом производит проверку папки методом
        :meth:`BaseUtils.is_folder_exists`

        Returns:

            :obj:`str`: Полный путь к папке скриншотов

        Examples:
            >>> BaseUtils.get_screenshot_folder()
            '/home/trassir/shots'
        """
        folder = host.settings("system_wide_options")["screenshots_folder"]
        cls.is_folder_exists(folder)
        return folder

