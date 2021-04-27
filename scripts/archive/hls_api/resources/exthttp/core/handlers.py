import os
import traceback

from mako.lookup import TemplateLookup
from mako.exceptions import html_error_template

from exthttp.http import (
    HttpResponse,
    HttpResponseNotAllowed,
    HttpResponseNotFound,
    HttpResponseUnknownError,
    HttpResponseServerError,
    JsonResponse,
)
from exthttp.constant import SCRIPT_NAME, SERVER_NAME
from exthttp.utils import tr
from helpers import get_logger

logger = get_logger()

BASE_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir))
directories = [BASE_PATH]

templates_path = os.path.join(BASE_PATH, "templates")
if os.path.exists(templates_path):
    directories.append(templates_path)

lookup = TemplateLookup(
    directories=directories,
    default_filters=["decode.utf8"],
    input_encoding="utf-8",
    output_encoding="utf-8",
    encoding_errors="replace",
)

is_dev = os.getenv("EXTHTTP_ENV", "prod") == "dev"


class BaseHandler(object):
    __template__ = None
    __mako_template__ = None

    title = None
    rights = ""

    def __init__(self):
        self.lang = "en"
        self.basename = ""
        self.url = ""
        self.menu = []
        self.debug = False
        self.__load_template()
        self.request = None
        self.allow_password_change = False
        self.jquery = None

    def __load_template(self):
        if self.__template__:
            self.__mako_template__ = lookup.get_template(self.__template__)
            # with open(os.path.join(BASE_PATH, self.__template__)) as tmpl:
            #     mako_template = tmpl.read().decode("utf8")
            #     self.__mako_template__ = Template(
            #         mako_template,
            #         default_filters=["decode.utf8"],
            #         input_encoding="utf-8",
            #         output_encoding="utf-8",
            #         encoding_errors="replace",
            #     )

    def get_sid(self):
        sid = ""
        if self.request:
            sid = self.request.GET.get("sid", "")
        return sid

    def _add_defaults_context(self, context):
        __default_context = {
            "title": SCRIPT_NAME,
            "author": "A.A.Trubilin",
            "description": "",
            "lang": self.lang,
            "basename": self.basename,
            "server_name": SERVER_NAME,
            "tr": tr,
            "request": self.request,
            "sid": self.get_sid(),
            "debug": self.debug,
            "allow_password_change": self.allow_password_change,
            "jquery": self.jquery,
        }

        __default_context.update(context)

        return __default_context

    def _add_menu(self, context):
        context["menu"] = []
        if self.request:
            sid = self.get_sid()
            for item in self.menu:
                item = dict(item)
                if item.get("rights"):
                    if getattr(self.request.user, item["rights"], False) is False:
                        continue
                is_active = ""
                if self.request.path == item["link"]:
                    is_active = "is-active"
                item["is_active"] = is_active
                if not getattr(self.request, "is_trassir", False) and sid:
                    item["link"] += "?sid=%s" % sid
                context["menu"].append(item)

    def render(self, **context):
        if is_dev:
            self.__load_template()

        if self.__mako_template__:
            context = self._add_defaults_context(context)
            self._add_menu(context)
            try:
                return HttpResponse(self.__mako_template__.render(**context))
            except:
                return HttpResponseServerError(html_error_template().render())

    def get(self, *args, **kwargs):
        return HttpResponseNotAllowed("GET")

    def post(self, *args, **kwargs):
        return HttpResponseNotAllowed("POST")


class PageNotFoundHandler(BaseHandler):
    __template__ = "404.mako"

    def get(self, context):
        response = self.render()
        if response.status_code == 200:
            response.status_code = HttpResponseNotFound.status_code
            response.status_message = HttpResponseNotFound.status_message
        return response


class IndexHandler(BaseHandler):
    __redirect_html = """<!DOCTYPE html>
    <html>
        <head>
            <script>
                // This script needs for right relative link to static folder
                String.prototype.endsWith = function (suffix) {{
                    return this.indexOf(suffix, this.length - suffix.length) !== -1;
                }};
                
                const href = window.location.href.split("?")[0];
                console.log({{href: href, basename: '{basename}'}});
                if (href.endsWith('{basename}')) {{
                    if (!href.endsWith('{basename}/{basename}')) {{
                        window.location.replace(href + "/index{sid}");
                    }}
                }} else if (href.endsWith('{basename}/')) {{
                    window.location.replace(href + "index{sid}");
                }}
            </script>
        </head>
        <body>
            <p>Redirecting...</p>
        </body>
    </html>"""

    def __init__(self, basename):
        super(IndexHandler, self).__init__()
        self.basename = basename
        self.page_not_found_handler = PageNotFoundHandler()

    def get(self, request, *args, **kwargs):
        sid = request.GET.get("sid", "")
        if sid:
            sid = "?sid=%s" % sid

        if not request.path or request.path == self.basename:
            location = "{}/index".format(self.basename)
            logger.info("Path: %s, redirecting to %s", request.path, location)
            return HttpResponse(self.__redirect_html.format(basename=self.basename, sid=sid))

        elif request.path.endswith("/"):
            location = "index"
            logger.info("Path: %s, redirecting to %s", request.path, location)
            return HttpResponse(self.__redirect_html.format(basename=self.basename, sid=sid))
        else:
            logger.info("Redirect to 404")

            try:
                context = self._add_defaults_context({})
                self._add_menu(context)
                response = HttpResponse(self.page_not_found_handler.__mako_template__.render(**context))
                response.status_code = HttpResponseNotFound.status_code
                response.status_message = HttpResponseNotFound.status_message
            except:
                response = HttpResponseServerError(html_error_template().render())

            return response


def error_handler(request, error, *args, **kwargs):
    return HttpResponseUnknownError("{}\n {}".format(request, traceback.format_exc()))


class PasswordChangeHandler(BaseHandler):

    def __init__(self, basename):
        self.basename = basename
        super(PasswordChangeHandler, self).__init__()

    def post(self, request, *args, **kwargs):
        user = request.user
        logger.info("%s try to change password", user)
        result = {
            "success": False,
            "error": ""
        }
        status_code = 403
        if user.guid:
            if user["can_change_password"]:
                password = request.POST.get("password") or ""
                if isinstance(password, list):
                    password = password[0]

                logger.info("%s changed password", user)
                user["password"] = password
                result["success"] = True
                status_code = 200
            else:
                result["error"] = "User %s has no rights to set new password" % user.name
                logger.info("%s can't change password", user)
        else:
            result["error"] = "Forbidden"

        return JsonResponse(result, status=status_code)
