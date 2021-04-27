# -*- coding: utf-8 -*-
# Скрипт для клиентского доступа к модулям Trassir v1.0.0
# Порты модулей
# 9002 - Паркинг
# 9003 - Некоторые индивидуальные разработки
# 9006 - Аналитика
# 9009 - TFortis
# 9011 - Trassir Switches
"""
<parameters>
    <company>DSSL</company>
    <script>WebClient</script>
    <version>1.0.0</version>

    <parameter>
        <id>SERVER_GUID</id>
        <type>server</type>
        <name>Сервер</name>
        <value></value>
    </parameter>
    <parameter>
        <id>PORT</id>
        <type>integer</type>
        <name>Port</name>
        <value>9006</value>
        <min>9000</min>
        <max>10000</max>
    </parameter>
    <parameter>
        <type>integer</type>
        <id>MONITOR</id>
        <name>Монитор для вывода интерфейса</name>
        <value>1</value>
    </parameter>
    <parameter>
        <id>USER_FUNC</id>
        <name>Пользовательская функция для вызова интерфейса</name>
        <type>string_from_list</type>
        <value>U1</value>
        <string_list>U1,U2,U3,U4,U5,U6,U7,U8,U9,U10</string_list>
    </parameter>
</parameters>
"""

GLOBALS = globals()

SERVER_GUID = GLOBALS.get("SERVER_GUID", "")
PORT = GLOBALS.get("PORT", 9006)
MONITOR = GLOBALS.get("MONITOR", 1)
USER_FUNC = GLOBALS.get("USER_FUNC", "U1")

import host

assert SERVER_GUID, "Выберите сервер"
assert SERVER_GUID != "p2p", "Неправильно выбран сервер (p2p)"

try:
    server = host.settings("/%s" % SERVER_GUID)
except KeyError:
    raise RuntimeError("Сервер не доступен")

local_server = host.settings("")

if server.guid == local_server.guid:
    module_host = "localhost"
else:
    try:
        media_route = server["media_route"]
    except KeyError:
        raise RuntimeError(
            "Не доступны настройки севрера, проверьте настройки дсотупа пользователя Script"
        )

    for route in media_route.split(":"):
        if route.startswith("ip="):
            module_host = route[3:]
            break
    else:
        raise RuntimeError(
            "IP сервера %s не найден, возможно вы подключены к серверу через облако<br>"
            "media_route: %s" % (server.name, media_route)
        )


try:
    gui = host.object("operatorgui_%s" % local_server.guid)
    host.message("%s laoded success" % gui.name)
except EnvironmentError:
    raise EnvironmentError("OpertatorGUI is not available")


def show_minibrowser():
    gui.show(
        "minibrowser(0,htmltab(,http://{host}:{port}))".format(
            host=module_host, port=PORT
        ),
        MONITOR,
    )


host.activate_on_shortcut(USER_FUNC, show_minibrowser)
