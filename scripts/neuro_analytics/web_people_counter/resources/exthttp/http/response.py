import host
import copy
from collections import defaultdict

from exthttp.utils import to_json

server = "{srv.name} ({srv.guid})".format(srv=host.settings(""))
health = host.settings("health")

status_messages = defaultdict(lambda: "Unknown status")
status_messages.update({
    200: "Ok",
    400: "Bad Request",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error",
    520: "Unknown Error",
})


class HttpResponse(host.ExtHttpResponse, object):
    status_code = 200
    base_headers = {
        "Server": server,
        "Server-OS": health["os_version"],
        "Server-ServicePack": health["servicepack_level"],
        "Server-GrabberPack": health["grabberpack_level"],
        'Content-Type': 'text/html; charset=utf-8',
    }

    def __init__(self, data="", headers=None,):
        self.status_message = status_messages[self.status_code]
        self.headers = copy.copy(self.base_headers)
        if headers is None:
            headers = {}

        self.headers.update(headers)
        self.data = data


class HttpResponseRedirect(HttpResponse):
    status_code = 302

    def __init__(self, location, *args, **kwargs):
        super(HttpResponseRedirect, self).__init__(*args, **kwargs)
        self.headers["Location"] = location


class HttpResponseBadRequest(HttpResponse):
    status_code = 400


class HttpResponseForbidden(HttpResponse):
    status_code = 403


class HttpResponseNotFound(HttpResponse):
    status_code = 404


class HttpResponseNotAllowed(HttpResponse):
    status_code = 405

    def __init__(self, method, **kwargs):
        data = "Method %s not allowed" % method
        super(HttpResponseNotAllowed, self).__init__(data=data, **kwargs)


class HttpResponseServerError(HttpResponse):
    status_code = 500


class HttpResponseUnknownError(HttpResponse):
    status_code = 520


class JsonResponse(HttpResponse):
    def __init__(self, data, json_dumps_params=None, status=200):
        if json_dumps_params is None:
            json_dumps_params = {}
        data = to_json(data, **json_dumps_params)
        self.status_code = status
        self.status_message = status_messages[status]

        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*",
            "Cache-Control": "no-cache",
        }

        super(JsonResponse, self).__init__(data=data, headers=headers)
