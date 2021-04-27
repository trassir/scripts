from .field import Field


class BooleanField(Field):
    default = False
    __id = 1

    def __init__(self, key, name, **kwargs):
        """__init(key, name, default=None, children=None, description="")"""
        self.__id += 1
        self.id = self.__id
        super(BooleanField, self).__init__(key, name, **kwargs)
        self.value = kwargs.get("default")

        self.children = list(kwargs.get("children", []))

    def clear_value(self, value):
        if value is None:
            value = self.default
        return bool(value)

    def get_html(self):
        # https://getmdl.io/components/index.html#toggles-section/switch

        html = (
            '<label class="mdl-switch mdl-js-switch mdl-js-ripple-effect bool-field" for="field-{s.key}">'
            '<input type="checkbox" id="field-{s.key}" name="{s.key}" onchange="changeChildren(this, {s.children})" class="mdl-switch__input" {checked}>'
            "</label>"
        ).format(s=self, checked="checked" if self.value else "")

        js = """
        <script type="text/javascript">
        document.addEventListener("DOMContentLoaded", function(){{
            addChildrenIcon({s.children});
        """
        if self.children and self.value is False:
            js += "changeChildren({{checked: false}}, {s.children});"
        js += "}});</script>"

        html += js.format(s=self)
        return html
