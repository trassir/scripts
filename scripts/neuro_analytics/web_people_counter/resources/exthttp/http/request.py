import json
from urlparse import parse_qs

import host

from exthttp.auth import User


class Request(object):
    def __init__(self, request, session, cog_guid=None):
        self._request = request

        try:
            post_data = json.loads(self._request.post_data)
        except ValueError:
            post_data = parse_qs(self._request.post_data)
        self._request.post_data = post_data
        for key in self._request.post_data:
            self._request.args.pop(key, None)

        self._session = session

        self.user = User(session.userid, cog_guid)
        self.headers = request.headers
        self.path = self.url = request.url

        if request.method == host.EXTHTTP_METHOD_POST:
            self.method = "POST"
        else:
            self.method = "GET"

        self.is_trassir = "Trassir" in request.headers.get("User-Agent", "")

    @property
    def GET(self):
        return self._request.args

    @property
    def POST(self):
        return self._request.post_data

    def __repr__(self):
        return "<Request({self.method!r}, path={self.path!r}, user={self.user})>".format(self=self)
