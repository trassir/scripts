from .field import Field


class IntegerField(Field):
    default = 0

    def __init__(self, key, name, **kwargs):
        """__init__(key, name, default=None, min=None, max=None, description="")"""
        super(IntegerField, self).__init__(key, name, **kwargs)
        self.min, self.max = kwargs.get("min"), kwargs.get("max")
        if self.min is not None:
            self.min = int(self.min)
        if self.max is not None:
            self.max = int(self.max)
        if self.max is not None and self.min is not None:
            if self.max < self.min:
                raise ValueError("Min value is higher then max")

        self.value = kwargs.get("default")

    def __repr__(self):
        return "<{self.__class__.__name__}({self.value!r}, min={self.min!r}, max={self.max!r})>".format(self=self)

    def clear_value(self, value):
        if value is None:
            value = self.default
        value = int(value)
        if self.min is not None and value < self.min:
            value = self.min
        if self.max is not None and value > self.max:
            value = self.max
        return value

    def get_html(self):
        # https://getmdl.io/components/index.html#textfields-section

        html = (
            '<div class="mdl-textfield mdl-js-textfield" id="{s.key}">'
            '<input class="mdl-textfield__input" type="number" id="field-{s.key}" name="{s.key}" value={s.value} {max} {min}>'
            '<label class="mdl-textfield__label" for="field-{s.key}">{s.name}</label>'
            "</div>"
        ).format(
            s=self,
            max="" if self.max is None else 'max="%s"' % self.max,
            min="" if self.min is None else 'min="%s"' % self.min,
        )
        return html
