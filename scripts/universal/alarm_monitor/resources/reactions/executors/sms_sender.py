# -*- coding: utf-8 -*-

import os
import re
import json
import urllib
import base64

from __builtin__ import object as py_object
from executor import Executor
from base_utils import BaseUtils
import host
from helpers import get_logger

logger = get_logger()


class ScriptError(Exception):
    """Base script exception"""

    def __init__(self, *args):
        super(ScriptError, self).__init__(*args)
        host.timeout(1, self.rise_from_thread)

    def rise_from_thread(self):
        raise self


class ParameterError(ScriptError):
    """Ошибка в параметрах скрипта"""

    pass


class PokaYoke(py_object):
    """Класс для защиты от дурака

    Позволяет блокировать запуск скрипта на ПО, где это
    не предусмотрено (например, на клиенте или TOS).
    А также производить некоторые другие проверки.
    """

    _EMAIL_REGEXP = re.compile(
        r"[^@]+@[^@]+\.[^@]+"
    )  # Default regex to check emails list
    _PHONE_REGEXP = re.compile(r"[^\d,;]")  # Default regex to check phone list

    def __init__(self):
        pass

    @classmethod
    def check_phones(cls, phones, regex=None):
        """Проверяет строку на валидность телефонных номеров с помощью regex.

        Args:
            phones (:obj:`str`): Список телефонов, разделенный запятыми или точкой с запятой
            regex (:obj:`SRE_Pattern`, optional): Новый regex шаблон для проверки.
                По умолчанию :obj:`None`

        Returns:
            :obj:`str`: Список номеров телефона

        Raises:
            ParameterError: Если найден невалидный номер телефона

        Examples:
            >>> PokaYoke.check_phones("79999999999,78888888888A")
            ParameterError: Bad chars in phone list: `A`
            >>>
            >>> PokaYoke.check_phones("a.trubilil@dssl.ru,support@dssl.ru")
            '79999999999,78888888888'
        """
        phones = phones.replace(" ", "")

        if not phones:
            raise ParameterError("No phones!")

        if regex is None:
            regex = cls._PHONE_REGEXP
        else:
            if not isinstance(regex, cls._PHONE_REGEXP.__class__):
                raise TypeError(
                    "Expected re.compile, got '{}'".format(type(regex).__name__)
                )
        bad_chars = regex.findall(phones)
        if bad_chars:
            raise ParameterError(
                "Bad chars in phone list: `{}`".format(", ".join(bad_chars))
            )

        return phones


class SenderError(Exception):
    """Base Sender Exception"""
    pass


class Sender(py_object):
    _HTML_IMG_TEMPLATE = """<img src="data:image/png;base64,{img}" {attr}>"""

    def __init__(self):
        pass

    @staticmethod
    def _get_base64(image_path):
        """Returns base64 image

        Args:
            image_path (str): Image full path
        """
        base64_image = ""
        image_path = BaseUtils.win_encode_path(image_path)
        if os.path.isfile(image_path):
            with open(image_path, "rb") as image_file:
                base64_image = base64.b64encode(image_file.read())

        return base64_image

    @staticmethod
    def _get_html_img(image_base64, **kwargs):
        """Returns html img

        Args:
            image_base64 (str): Base64 image
        """
        return BaseUtils.base64_to_html_img(image_base64, **kwargs)

    def text(self, text, **kwargs):
        """Send text

        Args:
            text (str): Text message
        """
        pass

    def image(self, image_path, text="", **kwargs):
        """Send image and optional text

        Args:
            image_path (str | List[str]): Image path or paths
            text (str, optional): Text message; default: ""
        """
        pass

    def files(self, file_paths, text="", **kwargs):
        """Send file or list of files

        Args:
            file_paths (str | List[str]): File path or list of paths
            text (str, optional): Text message; default: ""
        """
        pass


class SMSCSenderError(SenderError):
    """Raises with SMSCSender errors"""

    pass


class SMSCSender(Sender):
    """Класс для отправки сообщений с помощью сервиса smsc.ru

    See Also:
        `https://smsc.ru/api/http/ <https://smsc.ru/api/http/>`_

    Note:
        | Номера проверяются методом
          :meth:`PokaYoke.check_phones`
        | Также при первом запуске скрипт проверяет данные авторизации

    Warnings:
        | По умолчанию сервис smsc.ru отправляет сообщения от своего имени *SMSC.RU.*
          При этом отправка на номера Мегафон/Йота **недоступна** т.к. имя *SMSC.RU*
          заблокировано оператором.
        |
        | Мы настоятельно **НЕ** рекомендуем использовать стандартное имя *SMSC.RU.*
        |
        | Для отправки смс от вашего буквенного имени необходимо его
          создать в разделе - https://smsc.ru/senders/ и зарегистрировать для
          операторов в колонке Действия по кнопке Изменить (после заключения договора
          согласно инструкции - https://smsc.ru/contract/info/ ) а также приложить
          гарантийное письмо на МТС в личный кабинет http://smsc.ru/documents/ и
          отправить на почту inna@smsc.ru

    Args:
        login (:obj:`str`): SMSC Логин
        password (:obj:`str`): SMSC Пароль
        phones (:obj:`str`): Список номеров для отправки смс резделенный
            запятыми или точкой с запятой
        translit(:obj:`bool`, optional): Переводить сообщение в
            транслит. По умолчанию :obj:`True`

    Raises:
        SMSCSenderError: При любых ошибках с отправкой сообщения

    Examples:
        >>> sender = SMSCSender("login", "password", "79999999999")
        >>> sender.text("Hello World!")

            .. image:: images/smsc_sender.text.png
    """

    _BASE_URL = "https://smsc.ru/sys/send.php?{params}"
    _ERROR_CODES = {
        1: "URL Params error",
        2: "Invalid login or password",
        3: "Not enough money",
        4: "Your IP is temporary blocked. More info: https://smsc.ru/faq/99",
        5: "Bad date format",
        6: "Message is denied (by text or sender name)",
        7: "Bad phone format",
        8: "Can't send message to this number",
        9: "Too many requests",
    }

    def __init__(self, login, password, phones, translit=True):
        super(SMSCSender, self).__init__()
        if not login:
            raise SMSCSenderError("Empty login")
        if not password:
            raise SMSCSenderError("Empty password")

        self._params = {
            "login": urllib.quote(login),  # Login
            "psw": urllib.quote(password),  # Password or MD5 hash
            "phones": urllib.quote(
                PokaYoke.check_phones(phones)
            ),  # Comma or semicolon spaced phone list
            "fmt": 3,  # Response format: 0 - string; 1 - integers; 2 - xml; 3 - json
            "translit": 1 if translit else 0,  # If 1 - transliting message
            "charset": "utf-8",  # Message charset: "windows-1251"|"utf-8"|"koi8-r"
            "cost": 3,  # Message cost in response: 0 - msg; 1 - cost; 2 - msg+cost, 3 - msg+cost+balance
        }

        self._check_account()

    def _get_link(self, **kwargs):
        """Returns get link"""
        params = self._params.copy()
        params.update(kwargs)
        url = self._BASE_URL.format(params=urllib.urlencode(params))

        return url

    def _request_callback(self, code, result, error):
        """Callback for async_get"""
        if code != 200:
            raise SMSCSenderError("RequestError [{}]: {}".format(code, error))
        else:
            try:
                data = json.loads(result)
            except ValueError:
                data = {"error_code": 0, "error": "JSON loads error: {}".format(result)}

            error_code = data.get("error_code")
            if error_code is not None:
                error = self._ERROR_CODES.get(error_code)
                if not error:
                    error = data.get("error", "Unknown error")
                raise SMSCSenderError(
                    "ResponseError [{}]: {}".format(error_code, error)
                )

    def _check_account(self):
        """Send test request to smsc server"""
        url = self._get_link(cost=1, mes=urllib.quote("Hello world!"))
        host.async_get(url, self._request_callback)

    def text(self, text, **kwargs):
        """Отправка текстового сообщения

        Args:
            text (:obj:`str`): Текст сообщения.
        """

        url = self._get_link(mes=text)

        host.async_get(url, self._request_callback)


class SMSSendText(Executor):
    def __init__(self, smsc_sender):
        self.smsc_sender = smsc_sender

    def execute(self, channel, ts, alarm_messages, *args, **kwargs):
        if not isinstance(alarm_messages, dict):
            logger.error("alarm_messages is not dict: %s", alarm_messages)
            return
        alarm_message = alarm_messages.get("sms_message")
        if not alarm_message:
            logger.error("alarm_messages hasn't 'sms_message' key")
            return
        try:
            self.smsc_sender.text(alarm_message)
        except Exception as err:
            logger.exception(err)
