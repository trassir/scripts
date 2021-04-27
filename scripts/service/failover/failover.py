# -*- coding: utf-8 -*-
# <h3><font color='green'>Failover</font></h3>
# <code>
# <br><br>При потере соединения с сервером (камеры которого резервируются) скрипт включает соответствующие камеры
# на локальном сервере.<br>
# При восстановлении связи камеры выключаются.
# При запуске скрипт сопоставляет камеры на локальном и подключенных серверах по <br>
# сетевым настройкам (порт, ip)
# </code>
"""
<parameters>
    <company>DSSL Mitrofanov</company>
    <title>Failover</title>
    <version>0.0.2</version>
    <parameter>
        <type>caption</type>
        <name>Общие настройки</name>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Время включения, после того как пропало соединение с резервируемым сервером, сек</name>
        <id>DELAY_BEFORE_ENABLE_BACKUP_DEVICES</id>
        <value>5000</value>
        <min>1</min>
        <max>100000</max>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <name>log</name>
        <type>boolean</type>
        <value>True</value>
    </parameter>
    <resources>
        <resource>helpers.py</resource>
    </resources>
</parameters>
"""

import time
from __builtin__ import object
from helpers import init_logger, set_script_name
import host

GLOBALS = globals()
DEBUG = GLOBALS.get("DEBUG", False)
DELAY_BEFORE_ENABLE_BACKUP_DEVICES = GLOBALS.get(
    "DELAY_BEFORE_ENABLE_BACKUP_DEVICES", 10
)
logger = init_logger(name=host.stats().parent().name, debug=DEBUG)

logger.info(
    "SCRIPT START. Script info: %s, pc id %s, pc name: %s",
    set_script_name(),
    host.settings("").guid,
    host.settings("").name,
)


class TRObject(object):
    def __init__(self, sett):
        self.sett = sett

    def __getattr__(self, name):
        return getattr(self.sett, name)


class ServerObj(TRObject):
    def __init__(self, sett):
        super(ServerObj, self).__init__(sett)

    def __repr__(self):
        return "<server: {}-{}>".format(self.name, self.guid)


class CameraObj(TRObject):
    def __init__(self, sett, server):
        super(CameraObj, self).__init__(sett)
        self.server = server
        self._is_enabled_initially = False
        self.is_enabled_initially = sett["grabber_enabled"]

    def __repr__(self):
        return "<grabber: {}-{}>".format(self.name, self.guid)

    @property
    def is_enabled_initially(self):
        return self._is_enabled_initially

    @is_enabled_initially.setter
    def is_enabled_initially(self, current_state):
        self._is_enabled_initially = current_state


def servers_generator(names=None):
    """

    Args:
        names (set):

    Returns: Server

    """

    for server_name, server_guid, _, _ in host.objects_list("Server"):
        if names and server_name not in names:
            logger.debug("object name: %s not in %s, continue", server_name, names)
            continue
        try:
            _srv_obj = host.settings("/{}".format(server_guid))
        except EnvironmentError as err:
            logger.error(
                "Can't get settings object for server: %s (%s), err: %s",
                server_name,
                server_guid,
                err,
            )
            raise EnvironmentError(
                "Can't get settings object for server: %s (%s)"
                % (server_name, server_guid)
            )
        else:
            yield ServerObj(_srv_obj)


def get_cameras(server_guid):
    """
    Args:
        server_guid (str):
    Returns: Dict()

    """
    is_local = host.settings("").guid == server_guid

    for sett in host.settings("/%s/ip_cameras" % server_guid).ls():
        if sett.type != "Grabber":
            continue

        if is_local:
            yield sett
        else:
            if not sett["grabber_enabled"]:
                logger.debug(
                    "for server %s device %s (%s) is disabled, skipping it",
                    server_guid,
                    sett.name,
                    sett.guid,
                )
                continue
            yield sett


def network_nodes():
    for sett in host.settings("network").ls():
        if not sett.type == "NetworkNode":
            continue
        yield sett


class ObjectsStorage(object):
    def __init__(self):
        self.this_server = ServerObj(host.settings(""))

        self._servers = {}
        self.servers = []

        self._associations_network_nodes_with_servers = {}
        self.associate_network_nodes_with_servers()

        self._local_grabbers_by_network_settings_tuple = {}
        self.local_grabbers_by_network_tuple = self.this_server

        self._association_local_grabbers_with_remote_servers = {}
        self.associate_local_grabbers_with_remote_servers()

    @property
    def servers(self):
        return self._servers

    @servers.setter
    def servers(self, servers_names):
        duplicate_server_count = 0
        servers_count = 0

        for server in servers_generator(servers_names):
            if server.guid == self.this_server.guid:
                continue
            self._servers[server.guid] = server
            servers_count += 1
            logger.debug("add server: %s (%s)", server.name, server.guid)

        logger.debug(
            "found %s server(-s), also found duplicate server(-s): %s",
            servers_count,
            duplicate_server_count,
        )

    @property
    def associations_network_nodes_with_servers(self):
        return self._associations_network_nodes_with_servers

    def associate_network_nodes_with_servers(self):
        for sett in network_nodes():
            for server in self.servers.itervalues():
                if server.guid in sett["reachable_via_this_node"]:
                    self._associations_network_nodes_with_servers[
                        sett.name
                    ] = server.guid
                    break

        if len(self._associations_network_nodes_with_servers) != len(self.servers):
            logger.warning(
                "not all associations found for all servers. servers: %s, associations_network_nodes_with_servers: %s",
                self.servers,
                self._associations_network_nodes_with_servers,
            )
        logger.debug("found network associations: %s", self._associations_network_nodes_with_servers)

    @property
    def local_grabbers_by_network_tuple(self):
        return self._local_grabbers_by_network_settings_tuple

    @local_grabbers_by_network_tuple.setter
    def local_grabbers_by_network_tuple(self, server):
        for sett in get_cameras(server.guid):
            self._local_grabbers_by_network_settings_tuple[
                (sett["connection_ip"], sett["connection_port"])
            ] = CameraObj(sett, server)

    @property
    def association_local_grabbers_with_remote_servers(self):
        return self._association_local_grabbers_with_remote_servers

    def associate_local_grabbers_with_remote_servers(self):
        count = 0
        for server_guid, server_obj in self.servers.iteritems():
            self._association_local_grabbers_with_remote_servers[server_guid] = []
            for sett in get_cameras(server_guid):
                res = self.local_grabbers_by_network_tuple.get(
                    (sett["connection_ip"], sett["connection_port"])
                )
                if not res:
                    logger.debug(
                        "for server %s associated grabber not found with name %s, connection ip %s and port %s",
                        server_obj.name,
                        sett.name,
                        sett["connection_ip"],
                        sett["connection_port"],
                    )
                    continue
                self._association_local_grabbers_with_remote_servers[
                    server_guid
                ].append((sett["connection_ip"], sett["connection_port"]))
                count += 1
        logger.debug(
            "found %s associations: %s",
            count,
            self._association_local_grabbers_with_remote_servers,
        )


class FailoverManager(object):
    def __init__(self, delay_before_start):
        self.delay_before_start = delay_before_start
        self.disconnected_servers = {}
        self._launch_running = False

    def _loop_timer(self):
        now = time.time()
        for server_guid, down_time in self.disconnected_servers.items():
            if now - down_time >= self.delay_before_start:
                logger.debug(
                    "time to enable reversed devices for server %s",
                    obj_storage.servers.get(server_guid),
                )
                del self.disconnected_servers[server_guid]
                self._enable_reserved_devices(server_guid)
                host.stats()["run_count"] += 1
        if self.disconnected_servers:
            host.timeout(1000, self._loop_timer)
        else:
            self._launch_running = False

    def _enable_reserved_devices(self, server_guid):
        device_ids = obj_storage.association_local_grabbers_with_remote_servers.get(
            server_guid
        )
        for device_id in device_ids:
            device_obj = obj_storage.local_grabbers_by_network_tuple.get(device_id)
            logger.debug("enabling device: %s", device_obj.name)
            device_obj.sett["grabber_enabled"] = 1

    def _disable_reserved_devices(self, server_guid):
        device_ids = obj_storage.association_local_grabbers_with_remote_servers.get(
            server_guid
        )
        if not device_ids:
            logger.debug("device ids not found for server_guid: %s", server_guid)
        for device_id in device_ids:
            device_obj = obj_storage.local_grabbers_by_network_tuple.get(device_id)
            logger.debug("disabling device: %s", device_obj.name)
            device_obj.sett["grabber_enabled"] = 0

    def handler(self, ev):
        logger.debug(
            "type: %s, ts: %s, origin: %s, p1: %s, p2: %s, p3: %s, server_address: %s",
            ev.type,
            ev.ts,
            ev.origin,
            ev.p1,
            ev.p2,
            ev.p3,
            ev.server_address,
        )

        if ev.type == "Connected To %1 under %2":
            server_guid = obj_storage.associations_network_nodes_with_servers.get(ev.p1)


            res = obj_storage.association_local_grabbers_with_remote_servers.get(
                server_guid
            )
            if not res:
                logger.debug("No grabbers found for connected server: %s. server guid: %s", ev.p1, server_guid)
                return

            if self.disconnected_servers.get(server_guid):
                del self.disconnected_servers[server_guid]
            else:
                logger.debug(
                    "Connection detected, going to disable reversed devices for server: %s, server guid: %s",
                    ev.p1, server_guid
                )
                self._disable_reserved_devices(server_guid)

        if ev.type == "Disconnected From %1":
            server_guid = obj_storage.associations_network_nodes_with_servers.get(ev.p1)
            if not server_guid:
                logger.debug("No server guid found for disconnected server: %s", ev.p1)
                return

            res = obj_storage.association_local_grabbers_with_remote_servers.get(
                server_guid
            )
            if not res:
                logger.debug("No grabbers found for disconnected server: %s", ev.p1)
                return

            logger.debug("Disconnection of %s detected", ev.p1)
            self.disconnected_servers[server_guid] = time.time()
            if not self._launch_running:
                self._loop_timer()


if __name__ == host.stats().parent().guid:
    assert host.settings("").guid != "client", "Script starts on Trassir server only, not client"

    obj_storage = ObjectsStorage()
    fm = FailoverManager(DELAY_BEFORE_ENABLE_BACKUP_DEVICES)
    host.activate_on_events("Connected To %1 under %2", "", fm.handler)
    host.activate_on_events("Disconnected From %1", "", fm.handler)
