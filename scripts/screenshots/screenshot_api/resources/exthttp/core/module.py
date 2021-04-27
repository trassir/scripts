import os

import host

from exthttp.auth import User
from exthttp.constant import SCRIPT_PATH


def _get_icon(icon_path):
    if icon_path:
        if not os.path.isfile(icon_path):
            icon_path = os.path.join(SCRIPT_PATH, icon_path)

        if os.path.isfile(icon_path):
            with open(icon_path, "rb") as f:
                return f.read()
    return ""


def create_module(guid, name=None, lang=None, icon_path=None, check_rights=None):
    name = name or guid.title()
    lang = lang or host.stats().parent()["language"] or host.settings("system_wide_options")["i18n_language"]

    tmod = host.TrassirModule(guid)
    tmod.set_name(name)
    tmod.set_lang(lang)

    tmod.set_icon_data(_get_icon(icon_path))

    def _mod_check_rights(userid, username):
        return User(userid, cog_guid=guid).has_view_rights

    tmod.set_check_rights(check_rights or _mod_check_rights)
    tmod.set_url(guid)

    host.trassir_module_add(tmod)
    host.cog_create_or_update(guid, name, None)

    tmod.name = name

    tmod.guid = guid
    tmod.name = name
    tmod.lang = lang

    return tmod
