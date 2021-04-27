# Show Module in Browser v0.0.1
#
# Press F1 to show module in minibrowser
"""
<parameters>
    <company>DSSL</company>
    <title>ShowModuleInBrowser</title>
    <version>0.0.1</version>

    <parameter>
        <id>SERVER_GUID</id>
        <type>server</type>
        <name>Server</name>
        <value></value>
    </parameter>
    <parameter>
        <id>MODULE_LINK</id>
        <type>string</type>
        <name>Module</name>
        <value>FaceWorkTime</value>
    </parameter>
</parameters>
"""

GLOBALS = globals()

SERVER_GUID = GLOBALS.get("SERVER_GUID", "")
MODULE_LINK = GLOBALS.get("MODULE_LINK", "FaceWorkTime")

assert SERVER_GUID, "Server not selected"

import host

gui = host.object('operatorgui_%s' % host.settings('').guid)

source = "%s_%s" % (host.stats().parent().guid, MODULE_LINK)
link = "http://exthttp/{server_guid}/{module_link}".format(
    server_guid=SERVER_GUID, module_link=MODULE_LINK
)

host.activate_on_shortcut("F1", lambda: gui.show_html(source, link))