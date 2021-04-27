import os
from shutil import copyfile

import host

from helpers import get_logger
from .module import create_module
from .handlers import BaseHandler, IndexHandler, PasswordChangeHandler, error_handler
from exthttp.http import (
    Request,
    HttpResponseRedirect,
    JsonResponse,
)
from exthttp.auth import LoginHandler, JsonLoginHandler
from exthttp.constant import SERVER_GUID

logger = get_logger()
BASE_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir))

__version__ = "1.2.0"
logger.debug("%s version: %s", __name__, __version__)

__available_rights = {
    "",
    "has_view_rights",
    "has_modify_rights",
    "has_setup_rights",
    "is_superuser",
}


def _check_rights_value(rights):
    if rights not in __available_rights:
        raise ValueError(
            "Bad rights value: %s. Must be one of: %s"
            % (rights, ", ".join('"%s"' % v for v in __available_rights))
        )


class ExtHttpApp(object):
    _BASE_FLAGS = (
        host.EXTHTTP_HANDLER_GET
        | host.EXTHTTP_HANDLER_POST
        | host.EXTHTTP_HANDLER_SESSION_OPTIONAL
        | host.EXTHTTP_HANDLER_SESSION_USER
    )
    jquery = None

    def __init__(self, basename):
        self.basename = basename
        self.routes = {}
        self.error_handler = error_handler
        self.need_auth = False
        self.debug = False
        self.allow_password_change = False
        self.menu = []

        self.mod = None
        self.route("login", basename=self.basename)(JsonLoginHandler)

    def _check_url(self, url):
        """Check if url not registered yet

        Args:
            url (str): Url

        Raises:
            ValueError: if url already registered
        """
        if url and url in self.routes:
            raise ValueError(
                "{} already registered for {}".format(url, self.routes[url])
            )

    @classmethod
    def copy_jqeury(cls, path="static/js", name="jquery-2.2.0.min.js"):
        copied_jquery = None
        jquery_path = os.path.join(os.getcwd(), "manual", "en", "jquery-2.2.0.min.js")
        if os.path.isfile(jquery_path):
            copied_jquery = os.path.join(path, name)
            new_jquery_path = os.path.join(BASE_PATH, copied_jquery)
            if not os.path.isfile(new_jquery_path):
                logger.info("jquery file successful copied to %s", new_jquery_path)
                copyfile(jquery_path, new_jquery_path)
            copied_jquery = copied_jquery
        else:
            logger.warning("jquery file not found: %s", jquery_path)

        cls.jquery = copied_jquery
        return copied_jquery

    def create_module(self, name=None, lang=None, icon_path=None, allow_change_password=False, allow_multiple=False):
        """Creating trassir cog module

        Args:
            name (str, optional): Trassir module name
            lang (str, optional): Current language
            icon_path (str, optional): Module image
            allow_change_password (bool, optional): Adding password change handler
            allow_multiple (bool, optional): Allow starting multiple scripts

        Returns:
            host.TrassirModule: Created module
        """
        self.mod = create_module(
            self.basename, name=name, lang=lang, icon_path=icon_path, allow_multiple=allow_multiple
        )
        self.basename = self.mod.guid

        self.route("", basename=self.basename)(IndexHandler)
        self.route("login", basename=self.basename)(LoginHandler)

        # static not working  with os.path.join ?
        self.static("static", BASE_PATH + "/static")

        if allow_change_password:
            self.allow_password_change = True
            self.route("changePassword", basename=self.basename)(PasswordChangeHandler)

        return self.mod

    def static(self, url, path):
        """Add static handler

        Args:
            url (str): Url
            path (str): Path
        """
        self._check_url(url)

        if not os.path.exists(path):
            os.makedirs(path)

        host.exthttp_add_static_handler(
            self.basename, url, path, host.EXTHTTP_HANDLER_GET
        )

    def auth_required(self, handle, method):
        if not isinstance(handle, LoginHandler) and SERVER_GUID:
            method_ = getattr(handle, method)
            need_auth = getattr(method_, "need_auth", self.need_auth)
            logger.debug("request.headers: %s", handle.request.headers)

            if method == "get":
                if handle.rights and not getattr(
                    handle.request.user, handle.rights, False
                ):
                    if (
                        self.mod
                        and handle.request.headers.get("Content-Type")
                        != "application/json"
                    ):
                        backref = handle.request.path or "index"
                        for key, value in handle.request.GET.iteritems():
                            backref += "&%s=%s" % (key, value)
                        return HttpResponseRedirect(
                            "/s/{self.basename}/login?backref={backref}".format(
                                self=self, backref=backref
                            )
                        )
                    else:
                        return JsonResponse(
                            {
                                "error": "Use '.../{self.basename}/login' method to get sid".format(
                                    self=self
                                )
                            },
                            status=403,
                        )

            if need_auth and not handle.request.user.guid:
                if SERVER_GUID == "client":
                    logger.warning("Authentication is not available for Trassir Client")
                else:
                    if (
                        self.mod
                        and handle.request.headers.get("Content-Type")
                        != "application/json"
                    ):
                        backref = handle.request.path or "index"
                        for key, value in handle.request.GET.iteritems():
                            backref += "&%s=%s" % (key, value)
                        return HttpResponseRedirect(
                            "/s/{self.basename}/login?backref={backref}".format(
                                self=self, backref=backref
                            )
                        )
                    else:
                        return JsonResponse(
                            {
                                "error": "Use '.../{self.basename}/login' method to get sid".format(
                                    self=self
                                )
                            },
                            status=403,
                        )

    def route(self, url, **handler_kwargs):
        """A decorator that is used to register a handler for cog app

        Args:
            url (str): Url for route
            **handler_kwargs: kwargs for decorated handler

        Returns:
            handler instance
        """
        self._check_url(url)

        def prepare_handler(handler):
            if not issubclass(handler, BaseHandler):
                raise TypeError("Handler must be subclass of BaseHttpHandler")

            handle = handler(**handler_kwargs)
            if self.mod:
                handle.lang = self.mod.lang
                handle.basename = self.basename
                handle.debug = self.debug
                handle.url = url
                handle.jquery = self.jquery

                if handle.title:
                    _check_rights_value(handle.rights)
                    self.menu.append(
                        {"title": handle.title, "link": url, "rights": handle.rights,}
                    )
                handle.menu = self.menu

            def wrapped_handler(request, session, *args, **kwargs):
                request = Request(
                    request, session, cog_guid=self.basename if self.mod else None
                )
                handle.request = request
                handle.allow_password_change = self.allow_password_change
                logger.debug("Request %s", request.url)
                try:
                    if request.method == "POST":
                        auth_response = self.auth_required(handle, "post")
                        logger.debug("auth_response: %s", auth_response)
                        return auth_response or handle.post(request, *args, **kwargs)
                    elif request.method == "GET":
                        auth_response = self.auth_required(handle, "get")
                        logger.debug("auth_response: %s", auth_response)
                        return auth_response or handle.get(request, *args, **kwargs)
                    else:
                        return NotImplemented(
                            "{} not implemented".format(request.method)
                        )
                except Exception as err:
                    return self.error_handler(request, err)

            host.exthttp_add_handler(
                self.basename, url, wrapped_handler, self._BASE_FLAGS
            )

            return handle

        return prepare_handler


def create_app(basename):
    """Crating app

    Args:
        basename (str): Module guid

    Returns:
        ExtHttpApp: ExtHttpApp instance
    """
    app = ExtHttpApp(basename)
    return app
