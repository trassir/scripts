from .field import Field


class StringField(Field):
    default = ""

    def __init__(self, key, name, **kwargs):
        """__init__(key, name, default=None, rows=None, description="")"""
        super(StringField, self).__init__(key, name, **kwargs)
        self.value = kwargs.get("default")
        self.rows = kwargs.get("rows")

    def clear_value(self, value):
        if value is None:
            value = self.default
        return str(value)

    def get_html(self):
        # https://getmdl.io/components/index.html#textfields-section

        if self.rows is None:
            input_textarea = '<input class="mdl-textfield__input" type="text" id="field-{s.key}" name="{s.key}" value={s.value}>'
        else:
            input_textarea = '<textarea class="mdl-textfield__input" type="text" id="field-{s.key}" name="{s.key}" rows="{s.rows}">{s.value}</textarea>'

        html = (
            '<div class="mdl-textfield mdl-js-textfield" id="{s.key}">'
            "{input_textarea}"
            '<label class="mdl-textfield__label" for="field-{s.key}">{s.name}</label>'
            "</div>"
        ).format(s=self, input_textarea=input_textarea.format(s=self))
        return html
