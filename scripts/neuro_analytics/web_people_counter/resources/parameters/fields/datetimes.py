import datetime

from .field import Field


class DateField(Field):
    default = datetime.date(1970, 1, 1)
    __splitter = "-"

    def __init__(self, key, name, **kwargs):
        """__init(key, name, default=None, description="")"""
        super(DateField, self).__init__(key, name, **kwargs)
        self.value = kwargs.get("default")

    def clear_value(self, value):
        if value is None:
            value = self.default
        elif isinstance(value, (str, unicode)):
            args = [int(v) for v in value.split(self.__splitter)]
            try:
                value = datetime.date(*args)
            except TypeError as err:
                raise ValueError(str(err))
        elif isinstance(value, datetime.date):
            value = value
        else:
            raise ValueError(
                "Value must be datetime.date or str: YYYY{s}MM{s}DD".format(
                    s=self.__splitter
                )
            )
        return value

    def serialize(self):
        data = {
            "key": self.key,
            "type": self.__class__.__name__,
            "value": self.value.isoformat(),
        }
        return data

    def get_html(self):
        html = (
            '<div class="mdl-textfield mdl-js-textfield datepicker" id="{s.key}">'
            '<a class="input-button" title="toggle" data-toggle style="float: right;">'
            '<img class="material-icons" src="static/img/icons/calendar_today-24px.svg">'
            '</a>'
            '<input class="mdl-textfield__input flatpickr flatpickr-input active" style="width: 275px;" type="text" id="field-{s.key}" name="{s.key}" value={value} data-input>'
            '<label class="mdl-textfield__label" for="field-{s.key}">{s.name}</label>'
            "</div>"
        )
        return html.format(s=self, value=self.value.isoformat())


class TimeField(Field):
    default = datetime.time()
    __splitter = ":"

    def __init__(self, key, name, **kwargs):
        super(TimeField, self).__init__(key, name, **kwargs)
        self.value = kwargs.get("default")

    def clear_value(self, value):
        if value is None:
            value = self.default
        elif isinstance(value, (str, unicode)):
            args = [int(v) for v in value.split(self.__splitter)]
            value = datetime.time(*args)
        elif isinstance(value, datetime.time):
            value = value
        else:
            raise ValueError(
                "Value must be datetime.time or str: YYYY{s}MM{s}DD".format(
                    s=self.__splitter
                )
            )
        return value

    def serialize(self):
        data = {
            "key": self.key,
            "type": self.__class__.__name__,
            "value": self.value.isoformat(),
        }
        return data

    def get_html(self):
        html = (
            '<div class="mdl-textfield mdl-js-textfield timepicker" id="{s.key}">'
            '<a class="input-button" title="toggle" data-toggle style="float: right;">'
            '<img class="material-icons" src="static/img/icons/access_time-24px.svg">'
            '</a>'
            '<input class="mdl-textfield__input flatpickr flatpickr-input active" style="width: 275px;" type="text" id="field-{s.key}" name="{s.key}" value={value} data-input>'
            '<label class="mdl-textfield__label" for="field-{s.key}">{s.name}</label>'
            "</div>"
        )
        return html.format(s=self, value=self.value.isoformat())


class DateTimeField(Field):
    default = datetime.datetime(1970, 1, 1)
    __formats = ("%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M",)

    def __init__(self, key, name, **kwargs):
        super(DateTimeField, self).__init__(key, name, **kwargs)
        self.value = kwargs.get("default")

    def clear_value(self, value):
        if value is None:
            value = self.default
        elif isinstance(value, (str, unicode)):
            for format_ in self.__formats:
                try:
                    value = datetime.datetime.strptime(value, format_)
                    break
                except ValueError:
                    continue
            else:
                raise ValueError("Bad str format {}".format(self.__formats))
        elif isinstance(value, datetime.datetime):
            value = value
        else:
            raise ValueError(
                "Value must be datetime.datetime or str: {f}".format(f=self.__formats)
            )
        return value

    def serialize(self):
        data = {
            "key": self.key,
            "type": self.__class__.__name__,
            "value": self.value.isoformat(),
        }
        return data

    def get_html(self):
        html = (
            '<div class="mdl-textfield mdl-js-textfield datetimepicker" id="{s.key}">'
            '<a class="input-button" title="toggle" data-toggle style="float: right;">'
            '<img class="material-icons" src="static/img/icons/calendar_today_access_time-24px.svg">'
            '</a>'
            '<input class="mdl-textfield__input flatpickr flatpickr-input active" style="width: 275px;" type="text" id="field-{s.key}" name="{s.key}" value={value} data-input>'
            '<label class="mdl-textfield__label" for="field-{s.key}">{s.name}</label>'
            "</div>"
        )
        return html.format(s=self, value=self.value.isoformat())
