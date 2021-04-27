from collections import OrderedDict, Iterable

import host

from helpers import get_logger

from .field import Field

logger = get_logger()


# choices = ((key, value), (key2, value2), (key3, value3), ...)


class StringListField(Field):
    def __init__( self, key, name, **kwargs):
        """__init__(key, name, default=None, choices=None, multiple=False, description="", nullable=False)"""
        choices = kwargs.get("choices")
        if choices is None:
            raise ValueError("Keyword argument 'choices' required")

        super(StringListField, self).__init__(key, name, **kwargs)
        self.nullable = kwargs.get("nullable", False)

        if callable(choices):
            logger.debug("Choices is callable: %s", choices)
            self.__choices = choices
        else:
            logger.debug("Choices is not callable: %s", choices)
            # noinspection PyTypeChecker
            self.__choices = self._prepare_choices(choices)

        self.value = kwargs.get("default")
        self.multiple_size = 3

    def _prepare_choices(self, choices_list):
        logger.debug("Prepare choices ordered dict from: %s", choices_list)
        choices = OrderedDict()
        if self.nullable:
            choices[None] = ""
        for key, item in choices_list:
            choices[key] = item
        logger.debug("Result choices dict: %s", choices)
        return choices

    def clear_value(self, value):
        if value is not None:
            if isinstance(value, (str, unicode)):
                choice_found = self.choices.get(value)
                if choice_found is None:
                    logger.warning("Value %s not found in choices", value)
                    value = None
                else:
                    if self.multiple:
                        value = [value]
            elif isinstance(value, Iterable):
                if self.multiple is False:
                    raise ValueError("Multiple select is disabled")
                choices = self.choices
                values = []
                for val in value:
                    if choices.get(val):
                        values.append(val)
                value = values or None
            else:
                raise ValueError("Value must me str or List[str]")
        return value

    @property
    def choices(self):
        if callable(self.__choices):
            return self._prepare_choices(self.__choices())
        return self.__choices

    def get_html(self):
        choices = self.choices

        if choices:
            options = ""
            cur_values = self.value
            if not isinstance(cur_values, list):
                cur_values = [cur_values]
            for key, item in choices.iteritems():
                options += '<option value="{key}" {selected}>{item}</option>'.format(
                    key=key or "",
                    item=item,
                    selected="selected" if key in cur_values else "",
                )

            html = (
                '<div class="mdl-textfield mdl-js-textfield">'
                '<select class="mdl-textfield__input" name="{s.key}" id="field-{s.key}" {multiple}>'
                "{options}"
                "</select>"
                "</div>"
            ).format(
                s=self,
                options=options,
                multiple='multiple size="%s" style="border: 1px solid #e3e3e3;"' % self.multiple_size if self.multiple else "",
            )
        else:
            html = "Nothing to select"

        return html
