# -*- coding: utf-8 -*-
# TRASSIR users_universals v1.0.5
"""
<parameters>
    <company>AAT</company>
    <title>usersUniversals</title>
    <version>1.0.5</version>
    <parameter>
        <type>caption</type>
        <name>Отчет по правам пользователей</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SAVE_BASE_REPORT</id>
        <name>Экспорт базового отчета</name>
        <value>0</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SAVE_ACL_REPORT</id>
        <name>Экспорт дополнительного отчета</name>
        <value>0</value>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>Изменение прав пользователей</name>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Список пользователей (Admin,Operator,User)</name>
        <id>USERS</id>
        <value></value>
    </parameter>
    <parameter>
        <id>WORK_MODE</id>
        <type>string_from_list</type>
        <name>Тип работы</name>
        <value>Расписание</value>
        <string_list>,Расписание,Тревожный вход</string_list>
    </parameter>
    <parameter>
        <id>INPUT_OBJECT</id>
        <name>Выбор объекта(расписание либо тревожный вход)</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>BTN</id>
        <type>string_from_list</type>
        <name>По горячей клавише</name>
        <value></value>
        <string_list>,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12</string_list>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>Эталонные пользователи</name>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Для зеленого цвета расписания или события "сигнал на входе появился"</name>
        <id>USER_GREEN</id>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Для красного цвета расписания или события "сигнал на входе пропал"</name>
        <id>USER_RED</id>
        <value></value>
    </parameter>
    <resources>
        <resource>schedule_object.py</resource>
    </resources>
</parameters>
"""

resources = {
    "schedule_object.py": """
        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
        kIw=
    """,
}
t1utils.resources_check(script_path, resources)
GLOBALS = globals()
SAVE_BASE_REPORT = GLOBALS.get("SAVE_BASE_REPORT", False)
SAVE_ACL_REPORT = GLOBALS.get("SAVE_ACL_REPORT", False)
USERS = GLOBALS.get("USERS", "")
WORK_MODE = GLOBALS.get("WORK_MODE", "Расписание")
INPUT_OBJECT = GLOBALS.get("INPUT_OBJECT", "")
BTN = GLOBALS.get("BTN", "")
USER_GREEN = GLOBALS.get("USER_GREEN", "")
USER_RED = GLOBALS.get("USER_RED", "")

""" Отчет по правам пользователей """

import os
import host
import pickle
import re
from datetime import datetime
from schedule_object import ScheduleObject


class Report:
    def __init__(self, filename=None):
        self.__report_dir = host.settings('system_wide_options')['screenshots_folder']  # os.getcwd()
        self.__filename = filename if filename else host.stats().parent()["name"]
        self.__table_header = "No name"
        self.__col_headers = []
        self.__rows = self.__load_data()
        self.__cur_date = datetime.today().strftime("%Y%m%d")
        self.__save_pkl = True

    def __clear_if_new_day(self):
        if self.__cur_date != datetime.today().strftime("%Y%m%d"):
            self.__cur_date = datetime.today().strftime("%Y%m%d")
            self.__clear_data()

    def __get_pkl_fname(self):
        return '%s_%s.pkl' % (
            datetime.today().strftime("%Y%m%d"), self.__filename)  # settings("scripts/%s"%__name__).name)

    def __get_report_fname(self):
        return '%s' % (self.__filename)  # settings("scripts/%s"%__name__).name)

    def __get_pkl_fpath(self):
        data_path = os.path.join(path_arbitrary_data(), self.__filename)
        if not os.path.exists(data_path):
            os.makedirs(data_path)
        return os.path.join(data_path, self.__get_pkl_fname())

    def __get_text(self, text_type):
        text = ""
        if text_type == "csv":
            text += self.__table_header + "\n"
            text += ';'.join(self.__col_headers) + "\n"
            for row in self.__rows:
                text += ';'.join(str(r) for r in row) + "\n"
        if text_type == "xml":
            text += '<?xml version="1.0" encoding="UTF-8"?>\n'
            text += '<export>\n'
            for idx_row, row in enumerate(self.__rows):
                text += '  <record id="%s">\n' % (idx_row + 1)
                for idx_col, col in enumerate(self.__col_headers):
                    text += '    <%s>%s</%s>\n' % (col, row[idx_col], col)
                text += '  </record>\n'
            text += '</export>\n'
        return text

    def __dump_data(self):
        if self.__save_pkl:
            with open(self.__get_pkl_fpath(), 'wb') as f:
                pickle.dump(self.__rows, f)

    def __load_data(self):
        if os.path.exists(self.__get_pkl_fpath()):
            with open(self.__get_pkl_fpath(), 'rb') as f:
                return pickle.load(f)
        else:
            return []

    def __clear_data(self):
        self.__rows = []

    def append(self, row):
        self.__clear_if_new_day()
        self.__rows.append(row)

    def save(self, text_type):
        text = self.__get_text(text_type)
        self.__dump_data()
        if text_type == "csv":
            text = text.decode("utf8").encode("utf-8-sig")
        try:
            path = os.path.join(self.__report_dir,
                                "%s.%s" % (self.__get_report_fname(),
                                           text_type))
            with open(path, "wb") as f:
                f.write(text)
        except IOError:
            pass

    def set_table_header(self, string):
        self.__table_header = string

    def set_col_headers(self, headers_list):
        self.__col_headers = headers_list

    def set_save_pkl(self, save_boolean):
        self.__save_pkl = save_boolean


class UserRights():
    def __init__(self):
        self.refresh_users()
        self.translate = {
            'channels': 'Каналы',
            'network': 'Сеть',
            'archive': 'Архив',
            'audit': 'Аудит',
            'cloud': 'Облако',
            'eskuel': 'База данных',
            'iscsi_setup': 'iSCSI',
            'map': 'Карты',
            'merger': 'Синхронизация архива',
            'netrec': 'Запись сетевых каналов',
            'network_interfaces': 'Сетевые интерфейсы',
            'persons': 'Персоны',
            'reports': 'Отчеты',
            'screenshots': 'Скриншоты',
            'templates': 'Шаблоны',
            'time_setup': 'Дата и время',
            'webserver': 'Веб-сервер',
            'pvr': 'PVR',
            'sip_phone': 'SIP Телефон',
            'scripts': 'Автоматизация',
            'ad': 'ActiveDome',
            'pos_folder2': 'ActivePOS',
            'asterisk': 'Asterisk',
            'auto_trassir': 'AutoTrassir',
            'gate-zba3UneR': 'Gate',
            'intellivision': 'IntelliVision',
            'sigur-tiTFDYvo': 'Sigur',
            'orion': 'Орион',
            'face_recognizer': 'Распознавание лиц',
            'ip_cameras': 'IP-Устройства',
            'boards': 'Платы',
        }

    def refresh_users(self):
        self.users = {obj.name: host.settings('users/%s' % obj.guid) for obj in host.settings("users/").ls() if
                      obj.type == "User"}

    def copy_user_rights(self, source, dest):
        copy_parametrs = [
            'acl',
            'analytics_rights',
            'archive_speed_limit',
            'base_rights',
            'can_change_password',
            'enable_analytics',
            'enable_local',
            'enable_remote',
            'ptz_priority',
            'settings_button',
            'shutdown_button',
            'templates_managing',
            'templates_sharing',
            'view_button'
        ]
        user_source = self.users.get(source, None)
        user_dest = self.users.get(dest, None)
        if user_source and user_dest:
            for parametr in copy_parametrs:
                try:
                    user_dest[parametr] = user_source[parametr]
                except KeyError:
                    continue

    def get_base_rights(self, users=None):
        result = {}
        users = users if users else self.users.keys()
        for user_name in users:
            user = self.users.get(user_name, None)
            if user:
                base_rights = bin(int(user['base_rights'])).lstrip('-0b').zfill(11)
                result.update({
                    user_name: {
                        'view': '+' if base_rights[10] == '1' else '-',
                        'view_archive': '+' if base_rights[9] == '1' else '-',
                        'hear_sound': '+' if base_rights[0] == '1' else '-',
                        'export_archive_and_screenshots': '+' if base_rights[2] == '1' else '-',
                        'edit_archive_bookmarks': '+' if base_rights[5] == '1' else '-',
                        'use_ptz': '+' if base_rights[1] == '1' else '-',
                        'modify': '+' if base_rights[8] == '1' else '-',
                        'setup': '+' if base_rights[7] == '1' else '-',
                        'manage_users_and_scripts': '+' if base_rights[4] == '1' else '-'
                    }
                })
        return result

    def decode_acl_rights(self, acl):
        acl_bin = bin(int(acl)).lstrip('-0b').zfill(65)
        acl_bin_list = [int(a) for a in acl_bin]
        acl_bin_list.reverse()
        grant = {
            0: 'Просмотр',
            1: 'Архив',
            2: 'Управление',
            3: 'Настройка',
            9: 'PTZ',
            10: 'Звук'
        }
        revoke = {
            32: 'Просмотр',
            33: 'Архив',
            34: 'Управление',
            35: 'Настройка',
            41: 'PTZ',
            42: 'Звук'
        }
        grant_text = ''
        for key in grant.keys():
            if acl_bin_list[key]:
                grant_text += grant[key] + '/'
        revoke_text = ''
        for key in revoke.keys():
            if acl_bin_list[key]:
                revoke_text += revoke[key] + '/'
        text = ''
        if grant_text: text += 'Разрешения: %s ' % grant_text[:-1]
        if revoke_text: text += 'Запреты: %s' % revoke_text[:-1]
        return text

    def get_name(self, obj):
        split_obj = obj.split('/')
        len_obj = len(split_obj)
        try:
            if len_obj == 2:
                return host.settings(obj)['name']
            elif len_obj == 3:
                return '%s/%s' % (
                    host.settings('/%s' % split_obj[1])['name'],
                    self.translate.get(split_obj[2], split_obj[2])
                )
            elif len_obj == 4:
                return '%s/%s/%s' % (
                    host.settings('/%s' % split_obj[1])['name'],
                    self.translate.get(split_obj[2], split_obj[2]),
                    host.settings(obj)['name']
                )
            else:
                return obj
        except KeyError:
            return obj

    def get_acl_rights(self, users=None):
        result = {}
        acl_objs = set()
        users = users if users else self.users.keys()
        for user_name in users:
            user = self.users.get(user_name, None)
            if user:
                user_acl = user['acl']
                if user_acl:
                    user_acl = user_acl.split(',')
                    it_1 = user_acl[::2]
                    it_2 = user_acl[1::2]
                    user_info = {
                        user_name: {it_1[i]: self.decode_acl_rights(it_2[i]) for i in xrange(len(it_1))}
                    }
                    for obj in user_info[user_name].keys():
                        acl_objs.add(obj)
                    result.update(user_info)

        result_obj_names = ['Пользователь']
        sub_result_obj = [obj for obj in acl_objs]
        sub_result_obj.sort()
        result_obj_names.extend([self.get_name(obj) for obj in sub_result_obj])

        return result, sub_result_obj, result_obj_names

    def user_setting(self, user, parametr):
        try:
            return user[parametr]
        except KeyError:
            return 'N/A'

    def get_other_rights(self, users=None):
        result = {}
        users = users if users else self.users.keys()
        for user_name in users:
            user = self.users.get(user_name, None)
            if user:
                result.update({
                    user_name: {
                        'enable_local': '+' if self.user_setting(user, 'enable_local') else '-',
                        'enable_remote': '+' if self.user_setting(user, 'enable_remote') else '-',
                        'enable_analytics': '+' if self.user_setting(user, 'enable_analytics') else '-',
                        'templates_managing': '+' if self.user_setting(user, 'templates_managing') else '-',
                        'templates_sharing': '+' if self.user_setting(user, 'templates_sharing') else '-',
                        'settings_button': '+' if self.user_setting(user, 'settings_button') else '-',
                        'shutdown_button': '+' if self.user_setting(user, 'shutdown_button') else '-',
                        'view_button': '+' if self.user_setting(user, 'view_button') else '-',
                        'can_change_password': '+' if self.user_setting(user, 'can_change_password') else '-',
                        'ptz_priority': self.user_setting(user, 'ptz_priority'),
                        'archive_speed_limit': self.user_setting(user, 'archive_speed_limit')
                    }
                })
        return result


def save_base_rights():
    ur = UserRights()

    r = Report('users_base_rights')
    r.set_save_pkl(False)
    r.set_table_header("Базовые права")
    r.set_col_headers([
        "Имя пользователя",
        "",
        "Локальный вход", "Вход через сеть", "Аналитика через сеть",
        "",
        "Просмотр", "Архив", "Макс. скорость воспроизведения архива",
        "Звук", "Экспорт", "Закладки архива", "PTZ", "Приоритет PTZ",
        "Управление", "Настройка", "Настройка пользователей и скриптов",
        "",
        "Управление шаблонами", "Публикация шаблонов в облако",
        "Кнопка 'Настройки'", "Выключение и перезагрузка",
        "Диалог 'Вид'", "Смена пароля",
    ]
    )

    base_rights = ur.get_base_rights()
    other_rights = ur.get_other_rights()
    users = base_rights.keys()
    users.sort()

    for user_name in users:
        user_other_rights = other_rights.get(user_name, None)
        user_base_rights = base_rights.get(user_name, None)
        if user_other_rights and user_base_rights:
            r.append([
                user_name,
                '',
                user_other_rights['enable_local'], user_other_rights['enable_remote'],
                user_other_rights['enable_analytics'],
                '',
                user_base_rights['view'], user_base_rights['view_archive'], user_other_rights['archive_speed_limit'],
                user_base_rights['hear_sound'], user_base_rights['export_archive_and_screenshots'],
                user_base_rights['edit_archive_bookmarks'], user_base_rights['use_ptz'],
                user_other_rights['ptz_priority'],
                user_base_rights['modify'], user_base_rights['setup'], user_base_rights['manage_users_and_scripts'],
                '',
                user_other_rights['templates_managing'], user_other_rights['templates_sharing'],
                user_other_rights['settings_button'], user_other_rights['shutdown_button'],
                user_other_rights['view_button'], user_other_rights['can_change_password']
            ]
            )
    r.save("csv")


def save_acl_rights():
    ur = UserRights()
    acl_rights, acl_objs, acl_bojs_names = ur.get_acl_rights()

    r = Report('users_acl_rights')
    r.set_save_pkl(False)
    r.set_table_header("Отдельные настройки прав")
    r.set_col_headers(acl_bojs_names)

    users = acl_rights.keys()
    users.sort()

    for user_name in users:
        result = [user_name]
        user_right = [acl_rights[user_name].get(obj, '') for obj in acl_objs]
        result.extend(user_right)
        r.append(result)
    r.save("csv")


""" Изменени прав по расписанию """


class PokaYoke():
    def __init__(self, raise_err=True):
        self.raise_err = raise_err
        self.objs = {
            'Channel': {obj[0]: {'guid': obj[1], 'parent': obj[3][:-1]} for obj in objects_list("Channel")},
            'IP Device': {obj[0]: {'guid': obj[1], 'parent': obj[3][:-1]} for obj in objects_list("IP Device")},
            'Template': {obj[0]: {'guid': obj[1], 'parent': obj[3][:-1]} for obj in objects_list("Template")},
            'Schedule': {obj.name: {'guid': obj.guid, 'parent': host.settings("").path[1:]} for obj in
                         host.settings("scripts/").ls() if obj.type == "Schedule"},
            'E-Mail': {obj.name: {'guid': obj.guid, 'parent': host.settings("").path[1:]} for obj in
                       host.settings("scripts/").ls() if obj.type == "EmailAccount"},
            'User': {obj.name: {'guid': obj.guid, 'parent': host.settings("").path[1:]} for obj in
                     host.settings("users/").ls() if
                     obj.type == "User"}
        }

    def check_fail(self, obj):
        if self.raise_err:
            raise ValueError("Can't find %s, recheck script settings." % obj)
        else:
            return False, obj

    def check_obj_type(self, obj_type):
        if obj_type not in self.objs.keys():
            raise ValueError('Unknown obj_type')

    def check(self, obj_type, obj):
        self.check_obj_type(obj_type)
        if not obj: self.check_fail(obj_type)
        if type(obj) is list:
            for sub_obj in obj:
                if sub_obj not in self.objs.get(obj_type, {}).keys():
                    return self.check_fail(sub_obj)
        if type(obj) is str:
            if obj not in self.objs.get(obj_type, {}).keys():
                return self.check_fail(obj)
        return True, ''

    def set_generate_motion_events(self, st, channels=[]):
        channels = channels if channels else self.objs['Channel'].keys()
        for channel in channels:
            parent = self.objs['Channel'][channel]['parent']
            guid = self.objs['Channel'][channel]['guid']
            host.settings('/%s/channels/%s' % (parent, guid))['generate_motion_events'] = st

    def get_info(self, obj_type, obj=None):
        self.check_obj_type(obj_type)
        if not obj:
            return self.objs.get(obj_type, {})
        if type(obj) is str:
            return self.objs.get(obj_type, {}).get(obj, None)
        else:
            raise ValueError('get_info(str, str)')


pk = PokaYoke()
ur = UserRights()


def check_params():
    pk.check('User', USERS.split(','))
    pk.check('User', USER_GREEN)
    pk.check('User', USER_RED)


def change_rights(sched):
    if not USERS:
        return
    if sched.color == "Red":
        source = USER_RED
    else:
        source = USER_GREEN
    for user in USERS.split(','):
        ur.copy_user_rights(source, user)


last_user = USER_RED


def change_rights_by_btn():
    global last_user
    if not USERS:
        return

    if last_user == USER_GREEN:
        source = USER_RED
    else:
        source = USER_GREEN
    for user in USERS.split(','):
        ur.copy_user_rights(source, user)

    last_user = source
    host.message(source)


def gpio_handler(ev):
    global last_user
    if not USERS:
        return
    if ev.origin_object.name == INPUT_OBJECT:
        if ev.type == "Input Low to High":
            source = USER_RED
        else:
            source = USER_GREEN
        for user in USERS.split(','):
            ur.copy_user_rights(source, user)


""" Activate """
if SAVE_BASE_REPORT:
    save_base_rights()
if SAVE_ACL_REPORT:
    save_acl_rights()
if USERS:
    check_params()
if WORK_MODE == "Расписание":
    schedule = ScheduleObject(INPUT_OBJECT, color_change_handler=change_rights)
    change_rights(schedule)
elif WORK_MODE == "Тревожный вход":
    if not INPUT_OBJECT:
        raise ValueError("GPIO input not selected")
    for event in ["Input Low to High", "Input High to Low"]:
        host.activate_on_events(event, "", gpio_handler)
if BTN:
    host.activate_on_shortcut(BTN, change_rights_by_btn)
