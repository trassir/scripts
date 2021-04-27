import os

import host

from helpers import get_logger
from .module import create_module
from .handlers import BaseHandler, IndexHandler, error_handler
from exthttp.http import Request, HttpResponseRedirect, HttpResponseForbidden
from exthttp.auth import LoginHandler, JsonLoginHandler
from exthttp.constant import SERVER_GUID

logger = get_logger()
BASE_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir))

__version__ = "1.1.0"
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
        raise ValueError("Bad rights value: %s. Must be one of: %s" % (rights, ", ".join('"%s"' % v for v in __available_rights)))


class ExtHttpApp(object):
    _BASE_FLAGS = (
        host.EXTHTTP_HANDLER_GET
        | host.EXTHTTP_HANDLER_POST
        | host.EXTHTTP_HANDLER_SESSION_OPTIONAL
        | host.EXTHTTP_HANDLER_SESSION_USER
    )

    def __init__(self, basename):
        self.basename = basename
        self.routes = {}
        self.error_handler = error_handler
        self.need_auth = False
        self.debug = False
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

    def create_module(self, name=None, lang=None, icon_path=None):
        """Creating trassir cog module

        Args:
            name (str, optional): Trassir module name
            lang (str, optional): Current language
            icon_path (str, optional): Module image

        Returns:
            host.TrassirModule: Created module
        """
        self.mod = create_module(
            self.basename, name=name, lang=lang, icon_path=icon_path
        )

        self.route("", basename=self.basename)(IndexHandler)
        self.route("login", basename=self.basename)(LoginHandler)

        # static not working  with os.path.join ?
        self.static("static", BASE_PATH + "/static")

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

            if method == "get":
                if handle.rights and not getattr(handle.request.user, handle.rights, False):
                    if self.mod:
                        return HttpResponseRedirect(
                            "/s/{self.basename}/login?backref={backref}".format(
                                self=self, backref=handle.request.path
                            )
                        )

            if need_auth and not handle.request.user.guid:
                if SERVER_GUID == 'client':
                    logger.warning("Authentication is not available for Trassir Client")
                else:
                    if self.mod:
                        return HttpResponseRedirect(
                            "/s/{self.basename}/login?backref={backref}".format(
                                self=self, backref=handle.request.path
                            )
                        )
                    else:
                        return HttpResponseForbidden("Use '{self.basename}/login' method to get sid".format(self=self))

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

                if handle.title:
                    _check_rights_value(handle.rights)
                    self.menu.append({
                        "title": handle.title,
                        "link": url,
                        "rights": handle.rights,
                    })
                handle.menu = self.menu

            def wrapped_handler(request, session, *args, **kwargs):
                request = Request(
                    request, session, cog_guid=self.basename if self.mod else None
                )
                handle.request = request

                try:
                    if request.method == "POST":
                        return self.auth_required(handle, "post") or handle.post(request, *args, **kwargs)
                    elif request.method == "GET":
                        return self.auth_required(handle, "get") or handle.get(request, *args, **kwargs)
                    else:
                        return NotImplemented("{} not implemented".format(request.method))
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
