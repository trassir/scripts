import host


class CaptionField(object):
    def __init__(self, name, is_html=False):
        self.name = name
        self.is_html = is_html

    @property
    def key(self):
        return host.random_guid()
