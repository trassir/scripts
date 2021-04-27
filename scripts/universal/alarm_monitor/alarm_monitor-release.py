# -*- coding: utf-8 -*-
# TRASSIR Alarm Monitor v2.12.5

'''<parameters>
<company>DSSL Mitrofanov Egor</company>
<title>TRASSIR Alarm Monitor</title>
<version>2.12.5</version>
    <parameter>
        <name>""" Alarm types """</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>MOTION_ALARM</id>
        <name>Motion detection alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>CROSSLINE_ALARM</id>
        <name>Crossing of line detection alarm (SMART event from camera)</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>INTRUSION_ALARM</id>
        <name>Intrusion detection alarm (SMART event from camera)</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>

    <parameter>
        <id>PEOPLE_DETECTED</id>
        <name>People detected (SMART event from camera)</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>

    <parameter>
        <id>SOUND_ALARM</id>
        <name>Sound detection alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>FIRE_ALARM</id>
        <name>Fire or smoke appears</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>FIRE_STOPPED_ALARM</id>
        <name>Fire or smoke went out</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>LEFT_OBJ_ALARM</id>
        <name>Item abandoned alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SABOTAGE_ALARM</id>
        <name>Sabotage alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>ORION_ENABLE</id>
        <name>Orion events alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SIGUR_ENABLE</id>
        <name>Sigur events alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>FR_ENABLE</id>
        <name>Face recognition alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>FACE_DETECTOR_ENABLE</id>
        <name>Face detection alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SIMT_ALARM_ENABLE</id>
        <name>SIMT detector alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>INPUT_HIGH</id>
        <name>Input low to high alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>INPUT_LOW</id>
        <name>Input high to low alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>DD_OBJECT_IN_ZONE</id>
        <name>The appearance of an object in the neuro zone</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>DD_CROSS_BORDER</id>
        <name>Neuro border crossing</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SCRIPT_NO_HELMET</id>
        <name>Person without helmet</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SCRIPT_NO_UNIFORM</id>
        <name>Person without uniform</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>WARNING_TERMAL_SIGNAL</id>
        <name>Person with fever</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SCRIPT_AU</id>
        <name>Auto universal events</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>GATE_PACS_EVENT</id>
        <name>Gate PACS events</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>ARUCO_ENTERED</id>
        <name>Aruco appeared</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>ARUCO_LEFT</id>
        <name>Aruco disappeared</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>VORON</id>
        <name>Voron events</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>NO_MASK_DETECTION</id>
        <name>Person without a mask</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>DISTANCE_VIOLATION</id>
        <name>Distance violation</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SIGNAL_LOST</id>
        <name>Signal Lost</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SIGNAL_RESTORED</id>
        <name>Signal Restored</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SUSPICIOUS_POSE</id>
        <name>Suspicious pose</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>

    <parameter>
        <name>""" Reactions for events """</name>
        <type>caption</type>
    </parameter>

    <parameter>
        <id>SHOW_CHAN</id>
        <name>Show channel with alarm</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SAVE_SCREEN</id>
        <name>Save screenshot in screenshot folder</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_FTP</id>
        <name>Send screen to FTP</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_SCREEN_EMAIL</id>
        <name>Send screen to e-mail</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_SCREEN_TELEGRAM</id>
        <name>Send screen to Telegram (only on server)</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_EMAIL</id>
        <name>Send notification to e-mail</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_SMS</id>
        <name>Send SMS notification</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SHOW_MESSAGE</id>
        <name>Show text message</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SHOW_MESSAGE_DELAY</id>
        <name>Text message showing duration(sec)</name>
        <type>integer</type>
        <value>5</value>
        <min>1</min>
        <max>60</max>
    </parameter>
    <parameter>
        <id>PLAY_SOUND</id>
        <name>Sound notification</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SOUND_NAME</id>
        <name>Sound file name</name>
        <type>string_from_list</type>
        <string_list>alarm.wav,bell.wav,boxing-bell-1.wav,boxing-bell-3.wav,cardlock-open.wav,chime.wav,chip001.wav,chip019.wav,chip069.wav,cordless-phone-ring.wav,countdown.wav,dialtone.wav,ding.wav,horn-beep.wav,phone-beep.wav,police2.wav,ship-on-fog.wav,ships-bell.wav,SNES-startup.wav,spin-up.wav,tada1.wav,tape-slow9.wav</string_list>
        <value>bell.wav</value>
    </parameter>
    <parameter>
        <id>CUSTOM_SOUND_PATH</id>
        <name>Custom sound path (.wav)</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <id>SHOW_POPUP</id>
        <name>Show pop-up</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Display number to show pop-up</name>
        <id>MON_POPUP</id>
        <value>1</value>
        <min>1</min>
        <max>15</max>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Popup duration</name>
        <id>POPUP_DURATION</id>
        <value>10</value>
        <min>1</min>
        <max>3600</max>
    </parameter>
    <parameter>
        <id>OUTPUT_ON</id>
        <name>Make operations with outputs</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>ACS_ENBL</id>
        <name>Make operations with PACS</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_SIP_CODE_ENBL</id>
        <name>Send code to SIP (server only)</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SIP_NUMBER</id>
        <name>SIP number</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <id>SIP_CODE</id>
        <name>SIP code</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <id>TOKEN</id>
        <name>Send cloud alarm by token</name>
        <type>string</type>
        <value></value>
    </parameter>
    <parameter>
        <id>ADD_SCREEN_TO_ALARM</id>
        <name>Add an image to the alarm content</name>
        <type>boolean</type>
        <value>True</value>
    </parameter>
    <parameter>
        <id>ADD_VIDEO_TO_ALARM</id>
        <name>Add a video to the alarm content</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>

    <parameter>
        <name>""" Optional settings """</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>SERVER_CHECK_LIST</id>
        <name>Working servers</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>CHANS_CHECK_LIST</id>
        <name>Working channels</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>FOLDER_NAME</id>
        <name>Folder name for saving shots</name>
        <type>string</type>
        <value>default</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Shot time correction ('-' - before, '+' - after)(ms)</name>
        <id>SAVE_SCREEN_DELTA</id>
        <value>0</value>
        <min>-7000</min>
        <max>7000</max>
    </parameter>
    <parameter>
        <type>float</type>
        <name>Buffering time before saving a shot (sec)</name>
        <id>SAVE_BUFFER_DELAY</id>
        <value>0</value>
        <min>0</min>
        <max>7</max>
    </parameter>

    <parameter>
        <id>ONLINE_SHOT</id>
        <name>Online shot</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>FIGURES</id>
        <name>Shots with figures</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SUBSTREAM_SHOT</id>
        <name>Screenshot of the sub-stream (experimental)</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Only one screenshot per period (sec)</name>
        <id>SHOT_SPAM_PERIOD</id>
        <value>0</value>
        <min>0</min>
        <max>999</max>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Shot storage time (days)</name>
        <id>DAYS_TO_STORE</id>
        <value>5</value>
        <min>0</min>
        <max>999</max>
    </parameter>
    <parameter>
        <id>AM_SCHEDULE</id>
        <name>Schedule for running the script</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>INPUT_FILTER_REACTIONS</id>
        <name>Alarm input for running the script (optional)</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>INPUT_STATE_TO_MAKE_REACTION</id>
        <name>Input state to make reaction</name>
        <type>string_from_list</type>
        <string_list>closed,opened</string_list>
        <value>closed</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Delay the start of the script</name>
        <id>STARTUP_DELAY</id>
        <value>10</value>
        <min>0</min>
        <max>10000</max>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" E-mail settings """</name>
    </parameter>
    <parameter>
        <id>EMAIL_ACCOUNT</id>
        <name>E-mail account, created in Trassir</name>
        <type>string</type>
    </parameter>
    <parameter>
        <id>EMAIL_ADDRESSES</id>
        <name>Mail recipient list separated by comma</name>
        <type>string</type>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" Telegram """</name>
    </parameter>
    <parameter>
        <type>string</type>
        <name>User Telegram id</name>
        <id>TG_IDS</id>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Proxy (optional) (http://{login}:{password}@{host}:{port})</name>
        <id>TG_PROXY</id>
        <value></value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" FTP settings """</name>
    </parameter>
    <parameter>
        <type>string</type>
        <name>FTP host</name>
        <id>FTP_HOST</id>
        <value>172.16.12.69</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>FTP port</name>
        <id>FTP_PORT</id>
        <value>21</value>
        <min>1</min>
        <max>999999</max>
    </parameter>
    <parameter>
        <type>string</type>
        <name>FTP user</name>
        <id>FTP_USER</id>
        <value>trassir</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>FTP password</name>
        <id>FTP_PASSWD</id>
        <value>123456</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>FTP folder on server</name>
        <id>FTP_PATH</id>
        <value></value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>FTP_PASSIVE_MODE</id>
        <name>FTP passive mode</name>
        <value>1</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" SMS settings """</name>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Numbers to send SMS messages(79999999999)</name>
        <id>PHONE_NUMB</id>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>SMS service login</name>
        <id>SMSC_LOGIN</id>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Password or MD-5 hash in lowercase</name>
        <id>SMSC_PASSWORD</id>
        <value></value>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" Face recognizer """</name>
    </parameter>
    <parameter>
        <id>FR_SERV</id>
        <name>Server with the necessary folders of persons database</name>
        <type>server</type>
    </parameter>
    <parameter>
        <id>FR_MIN_SCORE</id>
        <name>Minimal compliance percentage in recognition</name>
        <type>integer</type>
        <min>0</min>
        <max>100</max>
        <value>75</value>
    </parameter>
    <parameter>
        <id>FR_ALARM_TYPE</id>
        <name>Activation by</name>
        <type>string_from_list</type>
        <string_list>Person,Group,Any person,Unrecognized person</string_list>
        <value>Group</value>
    </parameter>
    <parameter>
        <id>FR_ALARM_NAME</id>
        <name>Alarm person name</name>
        <type>string</type>
    </parameter>
    <parameter>
        <id>FR_ALARM_GROUP</id>
        <name>Alarm group name</name>
        <type>string</type>
    </parameter>
    <parameter>
        <id>FR_SAME_EVENT_IGNORING</id>
        <name>Ignoring identical events for a period, (sec)</name>
        <type>integer</type>
        <min>0</min>
        <max>9999</max>
        <value>0</value>
    </parameter>

    <parameter>
        <name>"""Alarm monitor"""</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <name>Alarm Monitor base settings</name>
        <type>caption</type>
    </parameter>

    <parameter>
        <id>AM_DISPLAY_DURATION</id>
        <name>The display duration of the channel in alarm template (sec)</name>
        <type>integer</type>
        <min>1</min>
        <max>9999</max>
        <value>30</value>
    </parameter>
    <parameter>
        <id>AM_ALARM_TEMPLATE</id>
        <name>Alarm template</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>AM_BASE_TEMPLATE</id>
        <name>Basic template (after alarm)</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>AM_MON_1</id>
        <name>Display number for alarm template 1</name>
        <type>integer</type>
        <value>1</value>
    </parameter>
    <parameter>
        <id>AM_MON_2</id>
        <name>Display number for alarm template 2</name>
        <type>integer</type>
        <value>0</value>
    </parameter>
    <parameter>
        <id>AM_MON_3</id>
        <name>Display number for alarm template 3</name>
        <type>integer</type>
        <value>0</value>
    </parameter>
    <parameter>
        <id>AM_TYPE</id>
        <name>Action type</name>
        <type>string_from_list</type>
        <string_list>Show channel,Playback in archive</string_list>
        <value>Show channel</value>
    </parameter>
    <parameter>
        <name>Alarm Monitor optional settings</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>AM_NO_MOTION_CHECK</id>
        <name>Alarm reset if no motion</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>AM_CHANGE_TEMPLATE_CHECK</id>
        <name>Alarm reset if another template choosing by user</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>

    <parameter>
        <id>AM_MAX_CHANS</id>
        <name>Alarm channels displaying at once limit</name>
        <type>integer</type>
        <value>24</value>
        <min>1</min>
    </parameter>

    <parameter>
        <id>SAME_CELL</id>
        <name>Every time show a channel in the same cell</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" SIMT / Neurodetector settings """</name>
    </parameter>
    <parameter>
        <id>SIMT_ENTER_ALARM</id>
        <name>Entrance in zones alarm (*simt, neuro)</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>SIMT_LEAVE_ALARM</id>
        <name>Escaping from zones alarm (*simt, neuro)</name>
        <type>objects</type>
        <value></value>
    </parameter>

     <parameter>
        <type>caption</type>
        <name>Crossing SIMT border</name>
    </parameter>
    <parameter>
        <id>SIMT_BORDER_ALARM</id>
        <name>Crossing border alarm (*simt)</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>SIMT_BORDER_ALARM_DIR</id>
        <name>Crossing border direction (*simt)</name>
        <type>string_from_list</type>
        <string_list>A -> B,B -> A,any</string_list>
        <value>A -> B</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>SIMT events in the selected zones</name>
    </parameter>
    <parameter>
        <id>SIMT_CHECK_ZONES</id>
        <name>Zone names to check (for events in zone)</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>SIMT_PRESENCE_CHECK</id>
        <name>Continuous presence in zones alarm (*simt)</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SIMT_PRESENCE_DELAY</id>
        <name>Time, spent by object in zone, before alarm(sec)</name>
        <type>integer</type>
        <value>10</value>
        <min>1</min>
        <max>60</max>
    </parameter>
    <parameter>
        <id>SIMT_SIZE_ALARM</id>
        <name>Object size alarm (*simt)</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SIMT_SPEED_ALARM</id>
        <name>Object speed alarm (*simt)</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SIMT_LENGTH_ALARM</id>
        <name>Object track length alarm (*simt)</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Spam filter</name>
    </parameter>
    <parameter>
        <id>SIMT_SIMILAR_EVENTS_DELAY</id>
        <name>Ignore same events by period (sec)</name>
        <type>integer</type>
        <value>5</value>
        <min>1</min>
        <max>600</max>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" Operations with PACS """</name>
    </parameter>
    <parameter>
        <id>ACS_TYPE</id>
        <name>PACS type</name>
        <type>string_from_list</type>
        <string_list>Sigur,Orion,Hikvision</string_list>
        <value>Sigur</value>
    </parameter>
    <parameter>
        <id>ACS_DOOR</id>
        <name>PACS name</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>ACS_LOGIC</id>
        <name>Operation type</name>
        <type>string_from_list</type>
        <string_list>open the door,close thе door</string_list>
        <value>open the door</value>
    </parameter>
    <parameter>
        <id>ACS_DELAY</id>
        <name>Door open / close state duration, (sec)</name>
        <type>integer</type>
        <value>5</value>
        <min>1</min>
        <max>3600</max>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <name>Hotkey for manual activation of operations</name>
        <id>ACS_MAN_ACTIV</id>
        <string_list>no,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,F18,F19,F20,F21,F22,F23,F24,F25,F26,F27,F28,F29,F30,F31,F32,F33,F34,F35,F36,F37,F38,F39,F40,F41,F42,F43,F44,F45,F46,F47,F48,F49,Ctrl+F1,Ctrl+F2,Ctrl+F3,Ctrl+F4,Ctrl+F5,Ctrl+F6,Ctrl+F7,Ctrl+F8,Ctrl+F9,Ctrl+F10,Ctrl+F11,Ctrl+F12,Ctrl+F13,Ctrl+F14,Ctrl+F15,Ctrl+F16,Ctrl+F17,Ctrl+F18,Ctrl+F19,Ctrl+F20,Ctrl+F21,Ctrl+F22,Ctrl+F23,Ctrl+F24,Ctrl+F25,Ctrl+F26,Ctrl+F27,Ctrl+F28,Ctrl+F29,Ctrl+F30,Ctrl+F31,Ctrl+F32,Ctrl+F33,Ctrl+F34,Ctrl+F35,Ctrl+F36,Ctrl+F37,Ctrl+F38,Ctrl+F39,Ctrl+F40,Ctrl+F41,Ctrl+F42,Ctrl+F43,Ctrl+F44,Ctrl+F45,Ctrl+F46,Ctrl+F47,Ctrl+F48,Ctrl+F49</string_list>
        <value>Ctrl+F17</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" Operations with alarm outputs """</name>
    </parameter>
    <parameter>
        <id>OUTPUTS</id>
        <name>Alarm outputs</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>OUTPUT_ACTION_TYPE</id>
        <name>Operation type</name>
        <type>string_from_list</type>
        <string_list>1.close,2.open,3.close-open,4.open-close,5.close-close,6.open-open</string_list>
        <value>3.close-open</value>
    </parameter>
    <parameter>
        <id>OUTPUT_DELAY</id>
        <name>Delay before next operation with alarm otput(sec)</name>
        <type>integer</type>
        <value>5</value>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <name>Hotkey for manual activation of operations</name>
        <id>OUTPUT_MAN_ACTIV</id>
        <string_list>no,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,F18,F19,F20,F21,F22,F23,F24,F25,F26,F27,F28,F29,F30,F31,F32,F33,F34,F35,F36,F37,F38,F39,F40,F41,F42,F43,F44,F45,F46,F47,F48,F49,Ctrl+F1,Ctrl+F2,Ctrl+F3,Ctrl+F4,Ctrl+F5,Ctrl+F6,Ctrl+F7,Ctrl+F8,Ctrl+F9,Ctrl+F10,Ctrl+F11,Ctrl+F12,Ctrl+F13,Ctrl+F14,Ctrl+F15,Ctrl+F16,Ctrl+F17,Ctrl+F18,Ctrl+F19,Ctrl+F20,Ctrl+F21,Ctrl+F22,Ctrl+F23,Ctrl+F24,Ctrl+F25,Ctrl+F26,Ctrl+F27,Ctrl+F28,Ctrl+F29,Ctrl+F30,Ctrl+F31,Ctrl+F32,Ctrl+F33,Ctrl+F34,Ctrl+F35,Ctrl+F36,Ctrl+F37,Ctrl+F38,Ctrl+F39,Ctrl+F40,Ctrl+F41,Ctrl+F42,Ctrl+F43,Ctrl+F44,Ctrl+F45,Ctrl+F46,Ctrl+F47,Ctrl+F48,Ctrl+F49</string_list>
        <value>Ctrl+F41</value>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" Operations with alarm inputs """</name>
    </parameter>
    <parameter>
        <type>objects</type>
        <name>Alarm input for activation of operations</name>
        <id>INP_ACTIV_1</id>
        <value></value>
    </parameter>
    <parameter>
        <type>objects</type>
        <name>Associated channel(s)</name>
        <id>INP_ACTIV_1_CHAN</id>
        <value></value>
    </parameter>
    <parameter>
        <type>objects</type>
        <name>Alarm input for activation of operations</name>
        <id>INP_ACTIV_2</id>
        <value></value>
    </parameter>
    <parameter>
        <type>objects</type>
        <name>Associated channel(s)</name>
        <id>INP_ACTIV_2_CHAN</id>
        <value></value>
    </parameter>
    <parameter>
        <type>objects</type>
        <name>Alarm input for activation of operations</name>
        <id>INP_ACTIV_3</id>
        <value></value>
    </parameter>
    <parameter>
        <type>objects</type>
        <name>Associated channel(s)</name>
        <id>INP_ACTIV_3_CHAN</id>
        <value></value>
    </parameter>
    <parameter>
        <type>objects</type>
        <name>Alarm input for activation of operations</name>
        <id>INP_ACTIV_4</id>
        <value></value>
    </parameter>
    <parameter>
        <type>objects</type>
        <name>Associated channel(s)</name>
        <id>INP_ACTIV_4_CHAN</id>
        <value></value>
    </parameter>
    <parameter>
        <type>objects</type>
        <name>Alarm input for activation of operations</name>
        <id>INP_ACTIV_5</id>
        <value></value>
    </parameter>
    <parameter>
        <type>objects</type>
        <name>Associated channel(s)</name>
        <id>INP_ACTIV_5_CHAN</id>
        <value></value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" Orion alarm """</name>
    </parameter>
    <parameter>
        <id>ORION_ALARM_NODES</id>
        <name>Only sensors alarm</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>ORION_EVENT_REACTION_ALL</id>
        <name>Make reactions for all events</name>
        <type>boolean</type>
        <value>True</value>
    </parameter>
    <parameter>
        <id>ORION_EVENT_REACTION_1</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,Intrusion Alert,Fire Detected,Allowed Access By Key,Allowed Access By Key,Door Restored,Door Broken,Door Blocked,No Access To All,No Access %1,Access Granted %1,No Access %1,Reader Contact Lost,Walk Detected,Free Walk Allowed,Armed,Orion Disconnectedd</string_list>
        <value>no</value>
    </parameter>
    <parameter>
        <id>ORION_EVENT_REACTION_2</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,Intrusion Alert,Fire Detected,Allowed Access By Key,Door Restored,Door Broken,Door Blocked,No Access To All,No Access %1,Access Granted %1,No Access %1,Reader Contact Lost,Walk Detected,Free Walk Allowed,Armed,Orion Disconnectedd</string_list>
        <value>no</value>
    </parameter>
    <parameter>
        <id>ORION_EVENT_REACTION_3</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,Intrusion Alert,Fire Detected,Allowed Access By Key,Door Restored,Door Broken,Door Blocked,No Access To All,No Access %1,Access Granted %1,No Access %1,Reader Contact Lost,Walk Detected,Free Walk Allowed,Armed,Orion Disconnectedd</string_list>
        <value>no</value>
    </parameter>
    <parameter>
        <id>ORION_EVENT_REACTION_4</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,Intrusion Alert,Fire Detected,Allowed Access By Key,Door Restored,Door Broken,Door Blocked,No Access To All,No Access %1,Access Granted %1,No Access %1,Reader Contact Lost,Walk Detected,Free Walk Allowed,Armed,Orion Disconnectedd</string_list>
        <value>no</value>
    </parameter>
    <parameter>
        <id>ORION_EVENT_REACTION_5</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,Intrusion Alert,Fire Detected,Allowed Access By Key,Door Restored,Door Broken,Door Blocked,No Access To All,No Access %1,Access Granted %1,No Access %1,Reader Contact Lost,Walk Detected,Free Walk Allowed,Armed,Orion Disconnectedd</string_list>
        <value>no</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" Sigur settings """</name>
    </parameter>
    <parameter>
        <id>SIGUR_ALARM_NODES</id>
        <name>Only sensors alarm</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>SIGUR_EVENT_REACTION_ALL</id>
        <name>Make reactions for all events</name>
        <type>boolean</type>
        <value>True</value>
    </parameter>
    <parameter>
        <id>SIGUR_EVENT_REACTION_1</id>
        <name>Make reactions for all events</name>
        <type>string_from_list</type>
        <string_list>no,Deny: %1 (%2),Allow: %1 (%2),Pass: %1 (%2),Access Point Disconnected,Access Point Connected,Access Point Once Opened,Access Point: %1,Alarm: %1 (%2),Access Point Closed To All,Access Point Opened To All,Access Point Allows By Key</string_list>
        <value>no</value>
    </parameter>
    <parameter>
        <id>SIGUR_EVENT_REACTION_2</id>
        <name>Make reactions for all events</name>
        <type>string_from_list</type>
        <string_list>no,Deny: %1 (%2),Allow: %1 (%2),Pass: %1 (%2),Access Point Disconnected,Access Point Connected,Access Point Once Opened,Access Point: %1,Alarm: %1 (%2),Access Point Closed To All,Access Point Opened To All,Access Point Allows By Key</string_list>
        <value>no</value>
    </parameter>
    <parameter>
        <id>SIGUR_EVENT_REACTION_3</id>
        <name>Make reactions for all events</name>
        <type>string_from_list</type>
        <string_list>no,Deny: %1 (%2),Allow: %1 (%2),Pass: %1 (%2),Access Point Disconnected,Access Point Connected,Access Point Once Opened,Access Point: %1,Alarm: %1 (%2),Access Point Closed To All,Access Point Opened To All,Access Point Allows By Key"</string_list>
        <value>no</value>
    </parameter>
    <parameter>
        <id>SIGUR_EVENT_REACTION_4</id>
        <name>Make reactions for all events</name>
        <type>string_from_list</type>
        <string_list>no,Deny: %1 (%2),Allow: %1 (%2),Pass: %1 (%2),Access Point Disconnected,Access Point Connected,Access Point Once Opened,Access Point: %1,Alarm: %1 (%2),Access Point Closed To All,Access Point Opened To All,Access Point Allows By Key"</string_list>
        <value>no</value>
    </parameter>
    <parameter>
        <id>SIGUR_EVENT_REACTION_5</id>
        <name>Make reactions for all events</name>
        <type>string_from_list</type>
        <string_list>no,Deny: %1 (%2),Allow: %1 (%2),Pass: %1 (%2),Access Point Disconnected,Access Point Connected,Access Point Once Opened,Access Point: %1,Alarm: %1 (%2),Access Point Closed To All,Access Point Opened To All,Access Point Allows By Key"</string_list>
        <value>no</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" GATE settings """</name>
    </parameter>
    <parameter>
        <id>GATE_EVENT_REACTION_ALL</id>
        <name>Make reactions for all events</name>
        <type>boolean</type>
        <value>True</value>
    </parameter>
    <parameter>
        <id>GATE_EVENT_REACTION_1</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,Legal card authentication passed: %1,Controller Disconnected,Controller Connected,Controller: %1,Invalid card: %1,Controller Alarm: %1</string_list>
        <value>no</value>
    </parameter>
    <parameter>
        <id>GATE_EVENT_REACTION_2</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,Legal card authentication passed: %1,Controller Disconnected,Controller Connected,Controller: %1,Invalid card: %1,Controller Alarm: %1</string_list>
        <value>no</value>
    </parameter>
    <parameter>
        <id>GATE_EVENT_REACTION_3</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,Legal card authentication passed: %1,Controller Disconnected,Controller Connected,Controller: %1,Invalid card: %1,Controller Alarm: %1</string_list>
        <value>no</value>
    </parameter>
    <parameter>
        <id>GATE_SUB_EVENT</id>
        <name>Event subtype 'Controller: %1'</name>
        <type>string_from_list</type>
        <string_list>Key found,Pass happened,any</string_list>
        <value>any</value>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" Settings BOPOH """</name>
    </parameter>
    <parameter>
        <id>VORON_EVENT_REACTION_1</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,alert in a zone,zone failure,the zone is unguarded,zone guarded,manual alarm confirmation,automatic alarm confirmation</string_list>
        <value>alert in a zone</value>
    </parameter>
    <parameter>
        <id>VORON_EVENT_REACTION_2</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,alert in a zone,zone failure,the zone is unguarded,zone guarded,manual alarm confirmation,automatic alarm confirmation</string_list>
        <value>zone failure</value>
    </parameter>
    <parameter>
        <id>VORON_EVENT_REACTION_3</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,alert in a zone,zone failure,the zone is unguarded,zone guarded,manual alarm confirmation,automatic alarm confirmation</string_list>
        <value>the zone is unguarded</value>
    </parameter>
    <parameter>
        <id>VORON_EVENT_REACTION_4</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,alert in a zone,zone failure,the zone is unguarded,zone guarded,manual alarm confirmation,automatic alarm confirmation</string_list>
        <value>zone guarded</value>
    </parameter>
    <parameter>
        <id>VORON_EVENT_REACTION_5</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,alert in a zone,zone failure,the zone is unguarded,zone guarded,manual alarm confirmation,automatic alarm confirmation</string_list>
        <value>manual alarm confirmation</value>
    </parameter>
    <parameter>
        <id>VORON_EVENT_REACTION_6</id>
        <name>Make reactions for event</name>
        <type>string_from_list</type>
        <string_list>no,alert in a zone,zone failure,the zone is unguarded,zone guarded,manual alarm confirmation,automatic alarm confirmation</string_list>
        <value>automatic alarm confirmation</value>
    </parameter>


    <parameter>
        <type>caption</type>
        <name>""" Neuro detector settings """</name>
    </parameter>
    <parameter>
        <id>DD_SAME_EVENT_IGNORING</id>
        <name>Ignore same events by period (sec)</name>
        <type>integer</type>
        <value>10</value>
        <min>1</min>
        <max>3600</max>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>Reactions on objects presence in neuro zones</name>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>DD_DETECTOR_TYPE</id>
        <name>The type of work for detection in zone</name>
        <value>immediate</value>
        <string_list>immediate,long-lasting</string_list>
    </parameter>
    <parameter>
        <id>DEEP_DETECTIONS_ZONES</id>
        <name>Zones names for detections (for all channels)</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Detector confidence coefficient (1-100 percent)</name>
        <id>DEEP_DETECTIONS_CONFIDENCE</id>
        <value>95</value>
        <min>1</min>
        <max>100</max>
    </parameter>
    <parameter>
        <id>DEEP_DETECTIONS_MAX_PERSONS</id>
        <name>Number of people for alarm</name>
        <type>integer</type>
        <min>0</min>
        <value>1</value>
    </parameter>
    <parameter>
        <id>DEEP_DETECTIONS_MAX_VEHICLE</id>
        <name>Number of vehicle for alarm</name>
        <type>integer</type>
        <min>0</min>
        <value>0</value>
    </parameter>
     <parameter>
        <id>DEEP_DETECTIONS_MAX_BICYCLE</id>
        <name>Number of bicycle for alarm</name>
        <type>integer</type>
         <min>0</min>
        <value>0</value>
    </parameter>
     <parameter>
        <type>integer</type>
        <name>Time of observation before the alarm (*long-lasting), sec</name>
        <id>DD_OBSERVATION_TIME</id>
        <value>10</value>
        <min>1</min>
        <max>999</max>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Successful detections, % (*long-lasting)</name>
        <id>DD_MATCH_DETECTIONS</id>
        <value>60</value>
        <min>40</min>
        <max>100</max>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>Borders for reaction</name>
    </parameter>
    <parameter>
        <id>AB_DD_BORDERS</id>
        <name>Border Crossed A -> B</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>BA_DD_BORDERS</id>
        <name>Border Crossed B -> A</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>CROSS_PERSON</id>
        <name>React for people</name>
        <value>1</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>CROSS_VEHICLE</id>
        <name>React for vehicle</name>
        <value>0</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>CROSS_BICYCLE</id>
        <name>React for bicycles</name>
        <value>0</value>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" Aruco settings """</name>
    </parameter>
    <parameter>
        <id>ARUCO_CODES</id>
        <name>Aruco codes</name>
        <type>string</type>
    </parameter>
    <parameter>
        <id>ARUCO_IGNORING_MODE</id>
        <name>Aruco ignoring codes</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>Other</name>
    </parameter>

    <parameter>
        <id>DEBUG</id>
        <name>log</name>
        <type>boolean</type>
        <value>True</value>
    </parameter>

    <resources>
        <resource>base_alarm.py</resource>
        <resource>base_utils.py</resource>
        <resource>cn.ts</resource>
        <resource>constants.py</resource>
        <resource>delete_old_shots.py</resource>
        <resource>email_sender.py</resource>
        <resource>ftp.py</resource>
        <resource>helpers.py</resource>
        <resource>ru.ts</resource>
        <resource>schedule.py</resource>
        <resource>shot_saver.py</resource>
        <resource>sound_player.py</resource>
        <resource>tbot.py</resource>
        <resource>event_handlers/access_control_systems.py</resource>
        <resource>event_handlers/aruco_handler.py</resource>
        <resource>event_handlers/dbase.py</resource>
        <resource>event_handlers/face_recognizer.py</resource>
        <resource>event_handlers/gate_pacs.py</resource>
        <resource>event_handlers/gpio_events.py</resource>
        <resource>event_handlers/orion.py</resource>
        <resource>event_handlers/sigur.py</resource>
        <resource>event_handlers/simple_events.py</resource>
        <resource>event_handlers/simt.py</resource>
        <resource>event_handlers/voron_events_handler.py</resource>
        <resource>event_handlers/__init__.py</resource>
        <resource>event_handlers/neuro_detections/crossline_detector.py</resource>
        <resource>event_handlers/neuro_detections/deep_detections.py</resource>
        <resource>event_handlers/neuro_detections/long_presence.py</resource>
        <resource>event_handlers/neuro_detections/same_event_filter.py</resource>
        <resource>event_handlers/neuro_detections/zone_detections.py</resource>
        <resource>event_handlers/neuro_detections/__init__.py</resource>
        <resource>localization/events_loc.py</resource>
        <resource>localization/fr_loc.py</resource>
        <resource>localization/gate_loc.py</resource>
        <resource>localization/gpio_loc.py</resource>
        <resource>localization/main.py</resource>
        <resource>localization/neuro_loc.py</resource>
        <resource>localization/popup_loc.py</resource>
        <resource>localization/simt_loc.py</resource>
        <resource>localization/translation_base.py</resource>
        <resource>localization/__init__.py</resource>
        <resource>reactions/reactions.py</resource>
        <resource>reactions/__init__.py</resource>
        <resource>reactions/executors/access_control.py</resource>
        <resource>reactions/executors/alarm_mon.py</resource>
        <resource>reactions/executors/executor.py</resource>
        <resource>reactions/executors/fire_alarm_executor.py</resource>
        <resource>reactions/executors/mail_text_sender.py</resource>
        <resource>reactions/executors/output_reaction.py</resource>
        <resource>reactions/executors/output_reaction_v2.py</resource>
        <resource>reactions/executors/play_sound.py</resource>
        <resource>reactions/executors/reactions_with_screenshots.py</resource>
        <resource>reactions/executors/show_message.py</resource>
        <resource>reactions/executors/show_popup.py</resource>
        <resource>reactions/executors/sms_sender.py</resource>
        <resource>reactions/executors/telegram_text_sender.py</resource>
        <resource>reactions/executors/__init__.py</resource>
        <resource>reactions/screenshot_senders_adopters/screenshot_senders_adopters.py</resource>
        <resource>reactions/screenshot_senders_adopters/__init__.py</resource>
    </resources>
    </parameters>
'''

resources = {
    "base_alarm.py": """
        eNqFVltr2zAUfg/kP2iCMruEsL2WZbBBNwZjD3stRaj2iavVlowkJw2l/33nSLYju0njh0SW
        vnP7zkVWTWusZ4/G+eViufD2cLNcMHy21jTsEeoWrGMqoirwojZVBXa5gOcCWs9+hZNba41N
        BQmldJUI/g5yTLqJluUirtgm2c5yOhBih6aV0ULgKf+8/rT+zAf8uoSHrsr4lWM96oZdOb5i
        QmjZgBC0GuWDvuWiqKVz7Lt08K2WtsnMwz8ofN777c0TaLLECUs7rVXGKn/AzT9GQ9x0XvrO
        TbZKcIVVrUdbk/3CNA1oP9nzhxaELE5gtUfsVHFrTQHOEZFTeztVgKg6VU51WJAeSjHXIi1q
        FjOwRSWwD8ynBlUj7QEdLEw387xWOxCNKWHcjftCmBC6rAVaQvI9VcyGZfGYnowPVGKGMuft
        inVaFagrz1cpLJJ7AZTQfQHZJ+ACKknJRX0xSQSrlfMr5ru2hhUrFdbRFHvM3cVwxmxeMj/m
        l4BKo/1tbST+1UZXc/tD1hGL0OnhkPwLBmflcAE9FgjiHoyph9N8qJQStlgtSisvROag3q6G
        3qOHc06tyST1Jgu9yqkXh/O+8ZXemozfXbn7Hkn6gKIkjevQxTOLFlrbW0wNWvCd1Yx/eQmS
        QgSbQqyHGfKaxZOk4D7Y1/wrX2+NbaQPGjdBbWpwqyzE8Ni1tJXDv+unPa1m4f4EDRYz6piG
        fR8N7KhgT8TdD7wQOFqgmRAkTgdOj9oybXxymlgP8UuFdP/FxKoGwgSneRqhTDkGTYsNy67Y
        GXomxqL3G/bCgzy/Sey+pkCkjo1zgkoTe15j/VMX4ttg7MRMmbm/k3UH8d6Q3tue8UQ1Dal8
        KoOURDEMj7ghyExtD1Nu8CwLEjNP8xNSIw13oxP36F8Qf4uG2sEZJX3GIaTkNCRU0A+kEi9A
        eG7xGoOS1hUGRffgeakjQecxk1DfwdFxpCcfq+IMPEnE8Rvj2Il0YdA3yJqaRwQWs/CbyPVf
        HLd6p6zRNNhD0dInBVI1UznhkEegKYrOWiRq/6hqQD8Urr0JDRsz139EoNS8k5J6CMg1ll1y
        IeQ4g/FCmJdFLIcjjOrhjt6iOPHH89AStEnl/0bi/t1J0OJskxRS6v6x81ZsIHESDPJ9mq7Z
        kBn0MtcVdJnNZ807tXxCYSH1R5+QfX5y9ZMZ3Vwu/gPFjP91
    """,
    "base_utils.py": """
        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
    """,
    "cn.ts": """
        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
        DC9xj4KFO8cOgdJk/hCQ62OHWlu+/H+YQ9OZ
    """,
    "constants.py": """
        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
        zL660g==
    """,
    "delete_old_shots.py": """
        eNqVVm1v0zAQ/p5fYTJNJFBCQYIPE5UYWxCTNjo1RQghZKXNpfFI4sh26PrvOTtpa6fdBvnS
        xHfPPffiuyurGi4U4dJj3ZssWsVKz8sFrwili5aVitWUkl7OF3ewVFvtgkvleUpszjyCjwEV
        UDYg5BawAkVLvlqB8OB+CY0iV0YQC8GFBdM6rF5ZsGuDIqm0bWyZs1SBYhV4XicgE0srCD3P
        W5aplOQ7F7/xoHM77PiS6zi+pfOrm3j6bU6T+ALB78eekWWQY9isZorSQEKZj8gilUCbVBUj
        ZN1IKhUX0JvSj9aK1sij3Z+Qz2kpwRXuLKB49+6qKI62UbyNK9q91HwdhOYTw3IxKM6gVKmN
        2x0G2tmJ5bELpgJ0IunWgDk8zMzLhwSvydsuYx+lShVbVqAKnu1zqP2gilMJy8C8WxkToFpR
        k+48KngryAusAJJ1JxWrWwWhe4iGeJ31nI3geMnUxqoZRkqXRVqvIDOFs/j+M7m9FQR0wGcT
        q0bHy+aK+vh6O/uLJaDif4DKgis59JHlg6LuRZ1JA11AjqWk2mFkDRwV16kD0auBfUchjJjk
        aLpKlZUI/XQdFWWwaFeBfyp7T0jOy0y3eecROZX+yGIfHXHYtYvxchnpRkDqjInA7ZTw7CAA
        NETqtALCag0tmVT/hDPYBtO15bvjrB7ARsZyeBR74GnePMDSaxsnPxzJwMOow0zPujSbvCLh
        o8jdAH7s6SZ7JColAIKnTPazepqYOa2HMAjxNEkfA2hQ4F+k9XMc1VACXteclXDWxYNilx1w
        ZB4adxNyiwXQeFJzhXehrbPtjdsX35rheiBTpkDgcOL1sNv2Ld4NQ3t62C3ZH7m+GYjTyz1x
        D7IXgovU+9J0IG9V8GY8HuOIOz5f+9AGYVgBivYgqMEimot2sIeGSdFr8oTE92nVlIAzjLS4
        uU7Ip/MkpsnFLI6/Jl+mc/p5en0Zz4YNhIpOWBIU/lNYycCXG6mgomuWAeWNZpJ++NOXS7x4
        tUkY7aaH/2tE/PMyFdUNx43Lhd8bDfH38vxHQudTmsynsxjJ3+HZ2mxz/OjX+nFPRy423AEj
        nbTQ+wunu5k+
    """,
    "email_sender.py": """
        eNqVV1tr5DYUfg/kPwhDQNOdmmRpoQydJaHNQmHZl9C+pKnw2JoZtbZkJHk32aX/vedIsi3b
        mkl3ArFH5/6di86IplXaEs0vL4R/VWZ4PSpjLy8uL6x+2VxeEPjstWrIkdct14YErgO3rFaH
        A9eXF/y55K0lvznKvdZKx4LIJeQhEvzg5EhhJlrwz7+TbUSgKyQw9gmMCyUZA2p2k1/nN1nP
        n1d81x1odmVI4NqQK5OtCWOyaDhj+DbIe328KUTNPhW1qJjmB/7cgl7N81I1rag51dnjX7dP
        b27d/z9z98hW3suyLowh96jBRUvvHQCgfRUCb4FhwXtXlqqT9qOy7+FZ0VHBWTHg/wPdPMtf
        8T1hn4VkXJaq4qwt7JHiv55V7CHHOcJBtgCgtFkg4GdMdf9BUQAEH4AuqqRZZ/c/IQQ9T0g7
        /V0KZPjVsTn/1iSc3cvhbLWwgL7jm+a209LZWgT/wGUFNaB2f/PS9iog2KKrLTOdO8aC+Gq4
        hgy7fP9Lvn9HvppSi9b6gyzfK90Ulo4uRPxbrPjccGuhTA3NspXHSWmS/VILDlitI8FRbxC0
        hTV0lbeFBlbqhYOAK5jgMtSgkMIyRg2v92tS+HKIcUFCzligQFzuAHvBl2sg0F50JtkUz6yw
        tiiPDXhi2O7FcgNa3v5IviM3129/CI/eqVt0XZQNt0dVjX6ethe5CvUkle2DmOVWF8JwAlXb
        +dzT7L5p7UvPnQ2wuCEBOCP4REgyy4TH2kBCakB4ZgQ8QM7cvrS+puMmy0ghK0IdQ1/0PazB
        Xn7oRBWdz/VHpYnsscs+vmRTj6k5i7HHVxg/gaj7GjsQDO+UqmliVkGqbXkMYqMt1zhzU1CX
        hjPkNLSszdrbNolkesL/zKVnnsyD2vBFk4PtygeAlfj4tMihMEICRrLkPhxwkBoLI6TzI2SV
        ysug0L/kpq2Fpdl6Wll9dTkmLK9kgMEPgCZ/LSsnQ8uLtoVJFSQS/i6hSdTSMOlTaoYpGZmd
        TJeDVl3L9nB5YeczHAZGfOFh2uC5uxUmic+y7AGhc2RDrCJOi8nJA4gSBYUK08QfQqYIMAHX
        kUvSq4/xvtOHObijWUJrYaDJyAd4oGZncuLKoiBH6U0SDCynkeC9nBZZ2WnnJhxfT0eOqJ4j
        VFx1yK7hurCcpsFyiXQXWsVGwe3y3h2Iq0W1Y1RwD7t7VRhkpAuVqYoLi87nQksYjTR7D8we
        Ipw6Yd05ZdcBoSQM1Y4n0hPwAbdwViX8gfOQ64RLYfe6qyoy3j3gT+wTCp92T+wjP95tz9xl
        rwOT7jHcDJ12eO46S5LKt+hvWn7w/BzdBZmmn44oIZAumqGQoXTp8OXNaHpFfv425EYl21HL
        ks11VT/fTqXwxHzbaV78c/aC6BvZWZl085QCkfrl6NSUG1v2ETp78zTZvAz67udguGIsf7bb
        DOozQmr7UUko07BVum9xK07qfRpFhmsq/sbxN82VDgbwJTaA33v1V3pebd616RmqmR1FCmeU
        oDo6XU1Gar8vwyDH4DZJ6X7rnC3ZcWpAVeTEZnnhuiTBCIm4cMCez2DEnJqAYTWUlVtlGP60
        HPbTM103bNNu3TvXn/Ge5DekU9wLmF/J2KSVprCc7/9Ew3wbDCkITkY7BOZjWCxr4Nh/udOX
        +Q==
    """,
    "ftp.py": """
        eNrVWv9v27gV/z1A/gdWh6By5ylJt2GH4DTsrpfegnXt0KQ43A6FKlt0rIss+iiqvszI/773
        SIoiKcp22hXYjKC1xfceyfceP+8LVa7WjAvCmuOjUn1diHVVzsxPseQ0L8r69vhowdmKLNp6
        LhirGqIJNjxfN3pwzqqKzkXJajNc0F9bOiV1vqKFaNcVPT4yspesEfjz+Ejw+4vjIwIfKWdJ
        qzXlRsYtFVnFbm8pPz6iv83pWpArOXLJOeM2I1LBWi3GV5KP5I0j5fhIfSOp9Tie4ECWfYSp
        YQtZBqPReXKenEUdfVLQWXsbRycN0VQX5KSJpiTLcIdZht8M/0Rt7lrkom1AWK+EOFIPgfPn
        qKE1Khi+RxQ3hF/ACpn50bTzOW2QOCrrDPTZ0ug9CG86wUpY/GmS9CoLuiBZwbKaiSXIiJ/l
        /LaZkmfP7jb4baLVvM6bxmLYgBhaz1lBs3UuljH+05GWC/CrBDdNUtBkLSI9gJ/e4t0HWWEv
        +B+oGUXGUSsWX+MCOxpt/fhdXSLB95JMesGU6GeXtXk2GcyAa8dvnIqW13IuazO8rbO8yZTL
        x4u644+i6G1bK9cHw6IzKRoYQGak+as8B8ikfqNAkDemRqkC2K05XsmNmlUAFRXpop4SpE8V
        u2JOtQxLRFLkdAVLSskNb6k9AM7BRWzR6j2LbsX6NyxSqWBegXrIy5t/St3Fl1LVsN2h5RXl
        iyWd371gda1OvOLq2MeYXor1u3XF8uKG5/M7ynsNq8dkzdktBxclkt5SsLRQVtalyLK4odVi
        SkTe3GW3bVlMyaKslAdOyaxi87usKf9Ns9m9oI7KkS+RQxteCkFRcWfJmUcAM4usWbJNnQEM
        zWmNlvKJzORoxe67R+MvBUj9R75UJvJKDgMtnB55GsAh8Ek8OG1m15OJq6Z5XlVGTTtcEPT7
        t7wuKkDCBeOkEYzPyjrn9504/FxTSr6tGuadpqUQ6+bi9LRgc1jnvViyOmH89vT5KcQPDjJO
        VShJlmJVfaW/g38k9izWQnZZ6XdpWKE9jzZUNmcrwFeB6uOsrYs4Hko79XU9Ic/I+dnZxN41
        oNeYMzxJB9N5uhl3I5/R5fOjjI4ursNNB0Im3gl+UZUwHLPZL3A2O3vfXP3j8s27G1jDufbl
        66vXP7y6vHnz2oGP7169efH37PrqX5fZdz/dXF5Lhud/VINZdvX66ubyexkcX+ZVQ4Pn07Xl
        tP+JId/6iVE6fX5uPWkbytMor1l9v2IYIC1i2N2mSCP72Ybxu6woefqa1dR6jgdgBgjjP5ch
        L1vlv1W0TsHkZzYPAhrotEO0FHXizV9+BG44f/aYd6BA/wBeaAAiGMGQLNGpsZ3rWziH/nEC
        zZC4EQCdiJI6OXLCF6Y0cVmLKWESmfNK0+LIFC2Qt5W4IB+en5MPLi+qVUof8OIIxmib39L/
        h2EI3RTjkhQB44URB9J8IZ3RwmJwFHM4IAA7MH5viUJresI6S5MYv+WzijoSr1VKhHFlLsOK
        Jre3G5Bq+8lQ551QSUWA5BYDTy8QHctfpudcJJ5BFu1IlQGVWCTwJ6O4zL59K3SeGBB0WaMa
        yFNN9pRIOgC0j3lFSkheXL+WH8j6KN+UDQW9N5Jdc0tme3Po+R9sZ34hYScXgpezFkDZc+wO
        d1CLuMt+f6JcUdYKUsI+IZOri8ZVoqfCHq7klo3GMM+sq3v4BzZZg8bqOSVzyKYELQILD4ac
        Du37OSAsqkc95Hkbk1l1tmpuAQpjT50o/yfWEoD/tioIwiJpwI6VtUS2INt51cjK4eGbGf9L
        FBCCUZkKizCxUVsiMC7+Hua6q9mGbJa5gMyRyicFgymfPPHkThKI9atcxJ3MVO9Txo8sS7pi
        ZuLy8RzdAzJhtJtK94wKLFITfxInWKgA4wX5TKJe6oGdGpJwl0ps84ck0qQScAZcCqBSjVT+
        sIGe1KBQSII5XKlz1gbrVwCQqio31mHFxo7JcMuQCQEHYs5gzGBZ2sMaOIBVlg3FyW2g5U08
        7sadZAKJ/fzGx6RQEuPTxF6myema60zTjoPBUxF9sx3xtIfY89Fo2/vHE/4A9ao3LjOHbe8p
        QSKZTGx7nwlLUmnFdlkWBa21AwUpTbKxdZ0pSGwykK1j2gClk5Ns7V+j6zVpyHbosw8+w8QG
        FnP4h7ZOvVwNP45S0uhZBJkyLCy2D9tkOh470/6YJOqJRTwsTsFtbPcaOJ/vZoDhJgYAwq4Z
        qAFjFyRemstB+WHTQR3GvjiJJ4PxREuKe4+cWhA17cKY2qqOdgExcBzLTnHojFMHsQIMgPs4
        +DEe2njYEtFbwLpPgnKDXQr4dhHC8GDpDsSTYUA0Tu4JGqrSqGtTxC6rtzd3xSqEQEWzGpG3
        utsjb+fEPSmS/NqWwkMw7P/t8TA9Cgkf+BWIsaW+lY7bDN1KO5TKaVUlNpJ7uEXfD1TIqfo1
        JUli98D+f5x4nw+N+9HBvvRIf3qUTx28CCSSbRm0W0qwa/n7r6NPPdABl2DCLgu6Jq6fnikI
        lf4ZVk0PDhfB6TY5r7H1G73I66eyey5dq586mqJEKPIXTBbA3gq6Zp85W/OKNXTf6UIaf57x
        44Hkjzwexg1xEih/IJWS6dejvNFISOSm4hF/8RbbG01yFWO26211sVOuZyEp9DD7LEqoDav7
        UIoXyEil9bB1kWHrYme71ZwJ16zXpsknicmmFEs1nQeggVZI31rV/ZAbeEDc/qrak16F6Zu0
        VaWmU519m9hpOgDtj/AbewxYZTtnxq8LDeO461hVRdezrSHLkj3aQE13un2Av6jLxLzKBBL+
        6DSyFOtVb4fEYctbAbw+Pw738hA5d2Dm6MS2J4LV1K2Q0dYsB2eDR1ZH22oJypuBTKgbA6xz
        vEuEOOyZci1+N9OSK12SrSGb3dFYh/ybz6IJZlNIStWJGDtGVm87ZPjrmzdvsaNLTnotTG25
        I4ueejoYeIS+g3JvsLyjDHoKwO+16U9iG0bdCO5OmTs4lbQBX/HhdgRqHb0R3d/3szHHcUIT
        jAhWNx2dVFV+rNm6ogsxhtxf9UzbMQqpM+Mb0YXlbTtZOF0xQfEkAE//YzdTVzECi2la7mQw
        pwA4+hMxxvIQUi1+AtgOOlHK+dna/fupeWjt731YaN92te/NOn6zVUtmv5v3Yysd3Mnr+2+5
        BX11YkGDuT0NS1PX1RKOykaGvV33bSOOh5/xJKL7YPqd6Iw7Pj87m5IqX82KvLe0DWnqmj/R
        m5tMdstWR6OP3Xui9pdYqMpxdi30wLx0p8F3k+IHayk9FaZgmyVmBmAdXcnJq5kTKGHy9bpD
        QXyuQHC6X/6+0+/tuM/L9tAfYmGFaWrl8eC9gHHHGKTkj/GA/ds81EfMWymTz1LFF1pd927M
        /sXtdXHzGkXXj0HsXd9XZS0uuquW9MezP5/94SDXlzo7yPUhU23rpbzcLwaHoAPKE/4/7Odf
        yLgHul2YgFYN3QFSfpn2EpV9wmXdsMDXESILhXes4RFb/29tO7hlZx1/wpn68EIH9URYN/uu
        KVy6XfgUrJC7g9F5eBy9C7g95LZ60bLVoF/f8jawR+ufo2mn54gL0TW1FZL7JEq9tOC9w9Bn
        MvK3l8bvqaiHlXK4SO7XMLybfyvHpPqcWzP87LmEf9m9OSfwdhJJEHw2S1pbKVtdNkvqVfhu
        J8CRaXoC1hWvNCAH47OV5HLrh7fY+/Y1c/VGvUSK6Z9MAMxRHdUvUCLRpyeLqgmvZ9Yg8fSk
        eWrBRFchapxwJu+VEq6u7Ax7t0ZG7hudCyubfqxCOqgmOrAKOqDu2VvpPIQvagfp0sCmLlaF
        kUaXG9f4ZgZRmOIDyQDy3JczexJdl9sYNwTRxycq3koV7uUVYt59935N5Oy/ezm0f5HxPydS
        l0U=
    """,
    "helpers.py": """
        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
    """,
    "ru.ts": """
        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
    """,
    "schedule.py": """
        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
    """,
    "shot_saver.py": """
        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
    """,
    "sound_player.py": """
        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
    """,
    "tbot.py": """
        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
        /izzVw34MQA/+vPL3+nZ94fxUvr/Ruuq7h/p3M9vfx2jtbxUIBp/DPWf//CHP33NWTfs2Z/5
        qF3+oUL+LPffoYmfuv9/pYmfPv07lPGnFP89qqgNa/Z37feHuflZ99Xics6i9IeQoiOq1q8l
        mbOsX8rhMqDrl/W67G/LPqKfRS+nv85XG75+qssv/ygq/PNXtmfz64evH/r0f7x1/FVvvw2E
        39r26+cXV38/6vn7Et+j9ePyH1Hox4eo/REjPj98jOp34/KXSPGHP/xdnPjNPL7+GA9D+zeV
        Wb/9kFeX7kf5mv11rK9h74f1d5X+tK1//e824V+jNt66f8OQl79Y8vIzyv4/NOafZvqz7v80
        6/806/9ws/6u9UdNV+kf77+G/Cv/vZVnUVL+G6b++yr+xki/K0v+avl/rerfBoj/MYZ/QdGt
        u1Toj3/bmL/3Addln1D+oxl91GUfB/B/Fdl/q+4fuYTvO/6QzbeF/Kdf+Hf6hW+h/o9zDT/V
        8f/rTuFbrf9hpP+W6d8W+db/fxDtt2Udur9c8PfW/sv/e9Dw19H9PW745T/Ef/yf8hzBtw==
    """,
    "event_handlers/access_control_systems.py": """
        eNrNV02P2jAQvSPxHyxWlUK7RHCrUDmsVlSqVGkP27tlkiG4ODayndL013fsJOCEBCF1uyKr
        BTJfnnnzPHEeyOzjjCQq5TJbksJuZ5+dZDwaj6wul+MRwWurVU52IA6gDeH5QWlLMrBUqCwD
        PR7B7wQOlnzzmrXWSoeOzgqjB47fvR9hphVlPKp+kVUgjqZOUbtansN45INSuim4sFxS2gRW
        m5+QWBf1UNLq5uS5U+Z8I1TCBP/DLFfSmeO9W2Q8eiCzt7hcoKckAWMQWGm1EsSUxkJuiAaW
        uGXNGy7m/hLBcLVq0edqzRfsli/RRCc8pnVfUtgiglxyS2lUidxlQGwfz7fMh6MHxaWlkuUw
        pLPlIdSpZuWuIgXBMJVTYoHK7NSR5hiSZTAgpt69VjaVNGnHF8kijS5k13wQIXRxRIkrsKL+
        uNNrQVzB3YWdrOPTRggd2oKOdRc2tO+KOh4hbGgd3l6xrADu2FfCjpc11CqaqBzohiV7dJl3
        LE466jatptzQo9J7NwdW5CsTBhxtT1zESiRNldIe9LC51RhADDZFFlDVXZOn59czcnGz5zzq
        5IPBRKxTy3jyOMCRc7ygq3w72NgVmbzyrNCTZTuT86gMr16OxQ6GXKVAmTiy0rgEoykhDzi1
        BNosU27YRsBqvVjMF+2g9Zxdy19cK5mDrIatm2GgdU8GNXjgrKKJ/yIqSQqtISXHHUjMnONP
        nIeC+MpIDnan0iXih6ihRwAMiOvQvGhsw79Ak2mGv2qxkgncBzC+rj5gAgInQhn4Lwz2kdO7
        5rBP8T56NUjid6RxCrKkzP17zX0AcwuJpdI5ExcEfi8y1ct7uIyLehfEeTfaYBb42K3Fm5Lu
        oaywUC7yvXHFP9YHqdI9IHzxZ/fYfUTTTnre4dT8Ht0tZ4lzlwx04vsjnfNUhY0W8/m8nqRV
        tFZVLDHnQ9VFcZfNHDgMBbWST/1nuHacBrbhSntaqsEWusuLy/Jvg/GHLiAckmFW3dPqyr0x
        xTnjMj7UiKFqVz3+hlYPjnjT23MOn6t91KhpGG7Temf4r/oF73JLNNuhsYom6/aW4LI+xJ9e
        4XBEFQKC7fAXDFV5tQ==
    """,
    "event_handlers/aruco_handler.py": """
        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
        9sXO2XEq8HudU9B1DDb/AyLKmvA=
    """,
    "event_handlers/dbase.py": """
        eNqFVMFq20AQvRv8D4tDQS6KzsFgaFLaYgihJLmUUsRaGstLVrvO7irE0ENb2lP7MUmhJE2b
        9BfkP+qMVrIVOyEyWNLOe29n5s1qi20/32aJToXKBqxwk+0dWul2uh1n5oNuh+E1MTpnU5Az
        MJaJfKaNYxm4WOosA9PtwHkCM8dGVeSVMdq0iYRC9RZxv+Ixbu+pdDv+iQ1by0GfAt1OpWRP
        JZfJFPJ5I/ZSyyJXITtyBrcI2T43GewJxc08ZHsiGykHqILPo4Pdw3d0fzM6ON7Qi+DcRSkk
        khvuxBk0+q2leMwtbBK1yRuwBWuFVjk/oXLqxam2blUb7jEusqCXkhjLdVpI3MuyYiY1TyHt
        VeWCwoYB9oHIETUj5Y4TJU60UpA43IY6c+R3RGR772AsVDr0IgiyS1ANJ+Ye7T/cqK9pN65a
        y96i31qNcp5BQIR+bWscYzYSFM8hjlGlN6uANhYEtbHreZxfjrNCpIjyXgXeqmCn3/egivMY
        JmQzgwAzj09gPjw2BYRMFVLS9sPXXFp8L5Q4LaAKtiVXat77OuamRT5WXMhH4gZy7SC2YM7A
        PJE6+icmIuFkR9wG+imrUSlIcJDGzj4A8JAXVb9zcFOdNqQJnYIgkbbpus/OFUY1bkdYt5lX
        mCeVvDeEDdu+tMV7vV4jQ9euyWwrum5oYJ0h9gpxWCW3zgmksI59ZAcap3FQV2BZtaonbDx3
        YNsqVRbNyxZ6mWHbMG06B0E/mgjpcMRp4d54De9V1RZEjUklg+dMaVclMmiHlyNDBr0XkR+f
        iTZMMKGI+mEdXvvgWf7I0AGJsPGczmqUGOA4RlzKYHkQ6Udu1Il6Qx7wYtmBNQce737Ted9s
        7PLic/mvvMb/u/KGldflFVt8Le8WX8o7hoFfi09V6Hbx3QfLy/KivKK3n/75N0IvFt/CFu1v
        VF5GrLxF9ufyBtl/Fj/o3uSwzPr+l84CN8nUf/+rFlNffSWMKhmwZ7YXrpnnW0x2tD5B0WqK
        N9FoMRI2T4rx9vwHXZ4/MA==
    """,
    "event_handlers/face_recognizer.py": """
        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
        5vItvP03KgDUZg==
    """,
    "event_handlers/gate_pacs.py": """
        eNq9VluP4yYUfo+U/4C8isauHM/OPlVWMg+teln1okpVH6rtChEbJ3SwsQDvThrlv/dgcIDE
        o05f1qNRuBw+vnP4zoE3aP3VGlWiZt2+RINu1l+bkeViuWikaBHGu4FxzTqMEWt7ITUSu79p
        pZcL1z0I5TuatdSs1fJYLhcIvhHlQHlPpZoQ9lRjLvZ7KpcL+lzRXqP348x3UgoZLjRWwCxY
        +PO4DhEVoSwXtoW2wXCaXdzYEUXxoBm/cPgGRv4wAxfuXFSEs3+IZqIz+NA365eLmjYQmQqL
        plFUp4rKT1Ti/cDqzHHFfhoYvLWDPga3JiZoBTQhsHuVeivzJfenYIvzvToqTVv8mdUUi96w
        U0nRCNmSiMs25OURsw+J3xm3rBs0VclHb2BjVdR0N+xTY4usbYlWKslD3g7VnVj6vqvp83hi
        OfqJHsdWZgJHpSxv8KmZTpOKdHfjOSK/U4HsudsNwdBtJKkeZBcysOdBOJXgClWK7CkE08Uv
        OdFPtNPYaPC82cnHze5x04hOg7y5kNs7Seu7x5Omzxo/nBO3aHNvTB4392AMa5IYqyMO6zJu
        lr87l+hUHUjXUW5NYBpIq1YFtCI+xbRvGSIXE9wNWksY/0+sv7oQDHovkjNB49iKRgHeybkT
        hTIpUdTPnVHgFpgEvckgJAsWYRdMzj6LWvJEMeFEttN8GjLNkW6VbnsQgfX22FOTYk53F1fH
        gJwvSRAYh5YmVmB5SfRCK6wFrnVqd3HGtclHv6JQWjamkSarer1q16s/0erHcvVLufo9ySYu
        kQ9BQM1nGJYIN7LVE8M4wf1m21rn8Zw92S3UnmJPNC16UilsWnhclc8hmQ23vjmD+M4Dunhf
        GYWnsI2OJKgkvgluIXtgo5uIQcH0+iqYphL+W5W6NecooePgWXW8Qesv95ntfoBgoLQ/HBWD
        so9IVQEfqBSdloIjW3NtfFWGICA1ZAZqRT1w+sXZmr+KE+BnWP8GkkjtJTzdPya3MGYd0xjD
        ncCb3NzSWGkhTQ4i8JDvSPW0/VV0NAuKs7EtAlNQctC7sptQwGhqTvlgCFQHWj1hJx7HwvXC
        LeWYL98TrgJ81qBO6Bs6hVGVw1DgH/4s5FMZS9fiOSOjxBuQCSDkMArxVdsh0Lq0Mp08tbnm
        ROE8Hcey8oV79eqGH42RqVjm0svHHLWt/sH+Csng4eNmlftlLbWX5EwVKAza/ASAz070D7PD
        dut5KHVdXEzFHKtlFlcK35mqSTNwbp9nRGuZhnthq+Yc7iOlRMVA5PV0DvAiGEV7o5UQ90oS
        8ZPm28uTw6Nf9NLYd0eOdpKSpySPYpBdK82oZsY3r7+RTaF6znSa4CT78PbjvMjjZJlJk1s/
        ps1WaoQBpU9SRZwpiJ7ll/iseyV9E35w4cW8KSB26S3m1TnAylfRt2c9Lm3E0NU2/P+be/Ag
        DxgU9hEcCXB88Ez69cP+1eCnIVPClTe3/Mz7Zf4eNVTci0aFr5nZ2xQCGdXXqzBGc2koNIse
        swTcfwHEpBke
    """,
    "event_handlers/gpio_events.py": """
        eNrNWF9v2zYQfzfg78CpKCIVjoO9DIMQBdiGbg1QLAOGPg2DQMu0rUYSDZJemgUGkhTFHjps
        7/sUadpuWdNkX0H6Rruj/suSk3R9mAI75PH+/O6O5J18j2w+2CQeH/vR1F6oyebnSOj3+j0l
        Du1+j8AzETwkMxbMmZDED+dcKDJlyg34dMpEv8eeeWyuyK5eeSgEF1VB5ALlFcHHWo5QWdPS
        76Uj4lTIpoULmajyQ9bvaaVjqhhOc635PFseUcnchfKDAu+XQHmChEJbwD0a+D9T5fMIscAc
        bfV798jmx3tQ3Tff7e4RDtHTtuRHt4B/XkClJLvRfKG+VxCMr2Y0mrJHNBoHLE+HYRjxH/Fl
        fJacJCckfhNfJr+T+Dp+lRzHZ/Gr+Do5jd/FFyQ50cSXML2I/yZIJ8kpML2Nz2Hlz/gK1l6Q
        +Dx5AdM38DlPDXwhpjKzhQ/7iUVKukrQSAZpnM2x7ynLRhOXKAdYjpNfU4to/jx+C5ZO9OgC
        0Z3FV/Fr4AUgwATo0PAVkP9CYRghQtDxHH3C9fh9CcDHcLgzfzpzFYcddeCyiI4CRswR5wHA
        AB3vIAq/Jb+A4lMEUrr5OnlO4n9gCgE51gbfJy+BPTV60YgICsTXZUzOmijQOoDQYD4MBSA4
        uyuGIvH5cMwmxHX9yFeua5YYJQsmg3WZG9wc1cHNLldY4PAFI+rtO9/yKKdbdh3RsGUHOS3g
        GlKdaXc6sbdqaEmZ0+laQ0PuHkjkw2oKQrrPXBpQEbohk5JOmalTQDw4txEL3IiGbJAZmy78
        8SB121WHc6CrUKpwjuFqxhzlwGZx3Q3xLuWjp8xL19zRodZnlqqtqpYaJgmajpaNbeHqe9cp
        rtwh3rg4kIqGczOFtvUp+8yqCjZy2JFdRGtWHTWeRPsRP4iMNSB/MCjccSqfGz+C/srW1gdg
        eyR2tkc72xMeKah2ARfOhmDjjZ2j0tpyewuXd7a3gBH4j0p3l0aLvqMy4q5iz9TSblCXQ6Ip
        PHKztC5tcoTDdLmi1BpOuAipauAuETjlcNDKAw449TA3+BpoHah3w+nc58NyoVPC6eQpfSsV
        QiXing/bY5yvNYSKEDi17V4Jx7psy1CuzXU1pRDvWj7+ey7uEOf/VdRC6ge3CpufBqo7iM2z
        0BbUHB1wt0fztrv7thG9S4Y+OAN5FnLvuhKRJaNlKJhaiKiRnGphSH2YpX1bVhPg+na14wOy
        ClHWKwMXPnTb1UIKxf/rReTpi9cTDGRlap9k9gkYI3NsH+FKp0TxomKRSSZYamu0eDqUOTxi
        2roNtcmGbkT3Rk83oL3Jx5BHKBGRx+riLS4RM/AltokFIa1g0KQDvetYElMqAUKGNkgeQW1G
        Zx7zAwPCkpNhilRcNWpBKiflm09B0UVNV39l6qKHX6ZlkQcEKl3bBYCVFQSK4AyR0GCcVHk/
        cbLk2aubLn0ZGh5QEcGrlGnspYzEvC8tLVizoslGvheqXUTthsggmOsOEnGctsDpLbO2U2oc
        BkyA2aq2lqaG2tU+rd7yFFuodpxcuHBcRr1Zvp+wi1kVqhxmOzXa0pS1i1VEh2mjViYgna82
        a+2arHYyeJAbgOy1HZFVuWVbZCC/tXbU7rZ3s6+Dbo56BjoYLe3L+lwNfcUEfEJpWna3vZpT
        Zi47WQRB1i2nQR80zFVb0vRHi4f6X/YTABOiYTM7eCznMg39+wbhnrcQ0ECiR1g7JMmubJvc
        l3D0QBPY+hf6BKEm
    """,
    "event_handlers/orion.py": """
        eNrtV1uL2zgUfg/kPwiXErsknmkfSgmTge6SZYctU9hO96UUodhyxhtZCpIylw3573t0sS3b
        mZC+9GXXgSBL5/Kdcz4dya/Q7M0MZSIv+Xq+08Xsg5kYj8YjLZ/n4xGCp5CiQveUbalUqKy2
        Qmq0phozsV5TOR7Rp4xuNbqxK0sphQwVjRQYDxQ/WT1EVMfKeORGaBFMx4lZGI+88r1Qejyy
        ZldEUbzTJWsg/QIzX82El8gEV5pw3Qgs/1re3n3Bd39+vP3y6ePdzefbxjATGWHlP0SXghtg
        8O4cv0Kzn/cYd5+lgUAfqAF+T3jOICWVyHeM/nQ05pfTAu10hkVRKKpjReUDlXi9K/PEVxm3
        y1C7SzfZsmcoYqqYwlADLVTcSpknutgHLg4X6llpWuHHMqdYbE15VJQWQlakg2UR4motJt+i
        1jOuSr7TVEXfWwHHsjSnq906NrLIyc7RaxVNQ9zequd6fMNz+mS5PkV/0Gc7SgxzqJTzgX1q
        luMoI3xidwBqPaXI7RjnEAS9I0n1TvIQQVuPimwoJozICldUKbKmcQZU4ZRhTio6dfTB+nkL
        Y10pXW3rYtEHrCXhijmqL45sihQAxqGF6CvfcPHIozoHbq2sKOg3uy7VCmuBcx17jwatEe8A
        VaCyb/MTEaC3rhejOYquVtdXheAati8TcjGRNJ9c7zV90vjtYY4m+24Eh8nVhRG/vroAxZV0
        ou9Ach+m5NCQpku3NpRFO5x2ZZzvBbSEtCIlT208076dENSi+3rE3rvWnIfZEwrBLzrFDdgd
        jCNVqTCN+zacQ3oqfSn6r2YMbLH/U3Zuyg71dvaNqburXW/KGFHKnWBLe4D97s4v33tM68K4
        5KXGGJo3K6ZIrP7GSgsJNuDFKPq+xkVO1RTBqcxWJNssbgWnSdBYjXoaaENbCd76cn3DRro/
        19OpPYNoPawzYOLI7mm2wT5nPhj/FsKU1tdvhKkAU1kgLvQgBKg5qy0qSBN+FHIz71bM2fNC
        qORDI7WBEIMt2FnuIC3GRxipo6y/ifhI7Vwyf+kctcvIHB7mWLOFhSugG2tVH3VGKHUnjBs7
        sWZFBQd59zphHlMzy1XIR6iOIUSa6dQsdTW6GI0+MkIeTmMv8OoP+yV/KKXgFTixZ/XwmD8F
        6BSIX5sLgVUUhaOlteUg+dyh+LVK4PJ3jRrc9uLQB1/fIDpke2EPQEUD0IaRDZ/6svMTQXSX
        bGdtMDrY3rS1h5xvVio9xH7ceddB0t8QhtxhwHUfK3aMuW8JorWMj3AEbjbQr0RWEk3zeisA
        IttrBts1tHs8H49EcrjSvpQRXLMNrvXK1J2YT43af21/ilaSkk2YmLMScJxgQ/uoVC7vYTzJ
        kQS2fcaKpGrLSh1HOEq+XX4/3sy6TfFIOxwCrJ1BVjxN6pZkOTL18bV4z64/1BhCeLE/2lvu
        0Gav2KB5FnxHKKtaiB3PXa/7YexaNc0DhrPwwytAlLqPnQS9Qe8v4e8tfX9sx9fHVi+AwXX8
        xNeEcRZ8Ufhu3enM5um4i0PWGOFpzyUo/wsoXOtO
    """,
    "event_handlers/sigur.py": """
        eNrtV0tv3DYQvi+w/4FQYFgKZNnJISgWXgNp4aJGAxeonV6CgOBK1JpdiVyQlB9Z7H/v8CGJ
        WsmOe8mlXQMGJc7jm5mPM9QbdPL2BOWiYHy9aHR58pN5MZ/NZ1o+LeYzBL9Sihrd0WpLpUKs
        3gqp0ZpqXIn1msr5jD7mdKvRld25lFLIUNFIgfFA8ZPVQ0QNrMxnboWWwes4MRte9U4oPZ9Z
        oyuiKG40qzpAP8Obz+aFl8gFV5pw3Qlc/nV5fXuDb//8eH3z6ePt1R/XneFK5KRi34hmghtY
        8GzcvkEnP+5n3N2wdSMRvacG9h3hRQXpqEXRVPSHozF/BS1Ro3MsylJRHSsq76nE64YVia8w
        7rehbmfuZc+csYipYQZLDZRQcS9lftHpLnCxP1VPStMaP7CCYrE1xVFRVgpZkwGWZYirt5h8
        iXrPuGa80VRFX3sBx7CsoKtmHRtZ5GQX6EhFaYjbW/U8j694QR8tz1P0O32yq8Twhkq5GNmn
        ZjuOcsKPLftR7ylD7rQ4hyDoHUmqG8lDBH09arKhmFRE1rimSpE1jXOgCqcV5qSmqaMP1k9b
        WOta6XrbFoveYy0JV5Uj+nLiSGQAMA4tRJ/5hosHHrU5cHuspqDfnblMK6wFLnTsPTrhAUwF
        Crs+OxEBcut2M1qg6Hx1cV4KruHoVkIujyUtji92mj5q/G6/QMe7If798fmpEb84PwXFlXSi
        70FyFyZk31FmSLY+kGW/TIcyzvcS2kFWE8YzG096aCcEtRw+Tth735vzMA+EQvDLQWkDbgfr
        SNUqTOOuD2efvZS+DP1XMwa2qv9T9tqU7QdNaXimXV/KK6KUm16Xdnj95maX7zumbWHMONMY
        Q+OuyhSJ1d9YaSHBRoqUUfQ9jYuCqhTBPK5WJN8srwWnSdBUjXoWaENTCZ4O5EaGQXr07kCn
        9Qyi7dKE2MaR39F8g33GfDD+KYQpra9fSaUCTKxEXOhRCFDxqrWoIE34QcjNYlgvZ88LIcbH
        RloDIQZbsFe5Q0IaH2GkjrD+FuIjte+SxXMz1G4jMzjMSIMqSwZXP7fWqh1zRihz08WtnVi3
        o4IhPrxKmJ+pmWUq5CNUxxAizXVmtoYaQ4xGHxkhD6ezF3j1g/6S3zMpeA1O7Jwej/iXAL0E
        4pfuMmAVReloaW05SD53KD5SCVz8LlCH214aDsG3t4cB2abPwAF8S8o2AkPPllzfUxxFNd62
        zbYD7mLxLqxd5A5lxZS/dE2b6KOc3p+GOyGcjF+5QxImru2GZVNV7luEaC3jCa7B7Qj6nsgZ
        0bRojxRUxfas0bEP7S5eIMcYY0CX3l/XDGDwoAGpU7SSlGyykB/fzUWbh2m+TrhlylEwDCuZ
        yGPftqxIprYV03GEo+TL2dfp3jjssRPddQywdXakWoK1Hc6yK/Xx9XifCX9MAyi1mRrPtVt7
        YR7bPKg5aL4KvuOVVS1FwwtXzn+NXauuF8HyJPyGCxBl7rspQW/RhzP4945+mGog7RQ8CGB0
        t3/hw8Q4Cz5OfPMfNPruHLfu4pA1Rjg9cAnK/wAbn/Q0
    """,
    "event_handlers/simple_events.py": """
        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
    """,
    "event_handlers/simt.py": """
        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
        jWQ43E4xQqOXxr8hIQ+lxh8t+C/ryakp
    """,
    "event_handlers/voron_events_handler.py": """
        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
        57hZfAqU9nohBFDxH15Wm+U=
    """,
    "event_handlers/__init__.py": """
        eNqNkU1ug0AMhfeRcgcOEPUOVehPpEiJitRFNqPp8BimBRt5hixy+g4kQEsj0aWfv/ds2YVw
        nTwU2kAJDFtyF0ji6oYlJM9RfhvVV015BdkkpoT5UoWoWvsAUbZ1+SaxCKrgKof49Wq9Kvpg
        2zhWOIOCH0J31LQhCzpgW2qyuMUODh+xCjNP1otPvfaXDz+wMLYnwLYyEbG4m8PimAbs0BV3
        MRv3Vo0242ovUTjGehpIaIVVjgATYsxIboW93ztC2rdYlgyHj8+o+B2d+P+mPZM9CjzIYHmn
        FGjSUV2iM11fnzAFa2kNq/J6pIF77MTZ+QbDmYXp9t65773r/fJ9A7Z69rk=
    """,
    "event_handlers/neuro_detections/crossline_detector.py": """
        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
        P0dY+LE8bOzu/BeOREDX
    """,
    "event_handlers/neuro_detections/deep_detections.py": """
        eNqNVE1r3DAQvRv8H4YNBW/I+lwMeyjdFAKBHHrrRXjlsVeNIhlJbpL++urDCpLtLNXJGr15
        895o5Bs43B6Ayo6JoZlMf/jqAmVRFr2SL0DIeWLcMEEIsJdRKgPy/BupgVbD+E7CxsGNem/K
        AuzyiRfkIyodkwY0hMthQFUW+EZxNPDgT+6VkipNdCirJUl89HmuYMpSFuELjkm42ruDsqC8
        1RpOiOMJjRXIpNDVh9z9XK/D3hpkghlCqhCKSyPv7/KQzSXaSNUOuDj5KwWSzheSanFGldSa
        cLZGRBVu7XY7Jztuv6lBN59Wh+rJ29A/w37fQB4AJrRpBcUrMqHqbHfmrW1PPVM8iF8Wdoqo
        vGFXTC3pvjvII7tK5V2nHa9Tl8fU8wKXWznm1hbYDbE2YyMab8CNBb0gfSb00gqBvPLTAPMu
        daBQW64fLdeJQtaDkGZlqG45j4zaTh15lep50djAN4PsNa5JIkGqwUxK/F85sN5tjdQp/kFh
        iMV13L6f4NTHUp9R0TEcRRVkmFi3bTxv4Ebr3AqPtu7wPA2LB+jnI5b9oj2x7Uc0BJxpczd7
        333cTc6xXzbXgTO562Fq1v+BHFDnDQutWpNuzNcW9QbskwL/ABuutzc=
    """,
    "event_handlers/neuro_detections/long_presence.py": """
        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
    """,
    "event_handlers/neuro_detections/same_event_filter.py": """
        eNrNVU2L2zAQvRv8HwaXglOSwG4vxTSHUrZQ6KntLSzCsceOGls2ktw0XfLfq5EVr/AmWffj
        0IGEsWbem5kn2XoBi1eLrMm5KBPodLF4QwthEAa8bhupQfMaw6CQTQ2MbTpeaS4YAxdtNt8w
        05AqaA+sfyCslockDMCYBW6xalGqE6hEzaqmLFGGAf7IsNXw0UbupGykD6Qs05kH/GRxVNBn
        CYPeg5W3HM8oEAZZlSoFX9Ia776j0PHQ6cyViqKod95vMdsBV4CUCMpAln3ELiiIc04weMi2
        qRBYGe9nI5Dx3HhMH1pMrGBKp3V7PB49/t7NsTAycsE1Y7HCqpjbKszysxyr9HDqiowylq72
        Ch6Oo8gYanLGSyPEvpE7EnQFH9JKod8WV4zArqs81anfyaAR2TtZKi9mGUz+JHmyphN6kIbs
        M+pOCiIclXt8FM3etEzKLumPdvYUKhoJrtwcWH4DXNhmllyjNL9axbNRr7wwhNoXd2lOTexY
        xtmnIm4SKnJLRUytKzV8pJ3c4HrU7QTUaO/XrrV7OgRnD5yTxZf1ZP3LsMxx05VxZAc325zA
        jdLR7Gm6tLvhi//nAjwVepjEKu4Y/1/tLusHtyI/J58v4b+Z54qIazdPr6al/l1VBoq1hd9f
        es0mqvJaXlTlmjLDnHtYTGvz7fkvYDKx48tpZBFdFu4SyFGbqwLNsd9ITHcJvFTm68iLgrxo
        fp1oyijPUEzX5ArRs1sCX2WH55PQ3BN/f6jMGL8Ap8lKkw==
    """,
    "event_handlers/neuro_detections/zone_detections.py": """
        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
    """,
    "event_handlers/neuro_detections/__init__.py": """
        eNptjjEKAjEQRfuF3CEn8BLGQlhQsLMJmv2RSDITMsHC05uVTRpt33t/GF846Z0rLBIDwS6o
        cJWLDilzqXq/mrkZswk1+e/kzaMOTNL70/3ZiBzpyr+byPSwuUBADn0xN3jemJp6ugD5z3nT
        sBm0x3JLsHiBqvUhVozvL00cVq6mD/PVVlM=
    """,
    "localization/events_loc.py": """
        eNp9V01v4zYQvS+w/2GQYoHdQwtsjwFawHaS7aL5QmxsgV4EmqZt1hQpkJK9zq/vzJCSRUlJ
        chHfvEcOyfmgt96V8FvthQ1G1NrZYi2CAl1WztewSrjafPxA/9KIEOD2qGwd7p38fLF/uf74
        AfBP29o3geYRRuEMf8DV9xaCGUFXkSiMcSe1KYSUKoRifS4O6kz0WTTAjA0wP8Pf6pxEG+d8
        4VWonUcGkm8QgJcE9Elr7w7KdpQ5DzOCcfLQm2Qex4liXetYjV/GEO3RtT6t8MuYdiORt1FW
        x+kS6SYCn77mvB0eWZ0RvyWkY3aL56t2dq/ERvlCOlsLWRfGBT7nF4ZhEWG4RzgJTsIc0MFa
        ybTyPwiggxFIpK1XqmBmuhoi3iEIzE7X0m7Gl2kP9JFAo7Z14db/4azZaveIwxPjw0V1rcpC
        rIXdOBvJ3xGBWYv0aaUOQdtdR3qI40QJ6F6xcSebLb1EFG4QHS5ci7LCM+yCdMXjLEL7FJx0
        62QThtRrnJcNUxrpjirFaa5ZRMOUZosZtk+7zEV3ZDF6t5/0D0XbeixaEpz4peP8DrWIW37g
        MSxp3B6ia+wmP0BChocXSsymnEbIKKK0z1l3CEySMH+rqsdZxnGP0ppaSEiFhUC6ndWvSYgQ
        loIWuhBD8ZXts8Xy+pJEbNjogFlkLw4iB256YJ88Zi4GtEsp4EqGFeBMK8LnT79/ySmcYl21
        G5IqQYVn712z2xPpGcdvTFQ5rLijfaSK8UzGqf1k4reVi/dkzuIVuErZCeET2uCJbRPSIX14
        K8JgeYmHgx/vblxi8cMmcinSuf9snSzXaQ/s4lvyuIF35HyLWe/qy/lqew0s5Y7eWWG6or3k
        Yb9YJ0K/yyVSr8+1zbZqeBOeW3eI3RYxcj1haVbpXQhG2zwhF4TeIzqqy10b79MvnXyYxJSO
        WaZTMvZIkbZ2nhsXrUqtv1gTd84oLCIKM/j1T5hfTSrWhZhQzEkxS4rUf/BFIw+FUXZX7y8B
        lZrQioxwz0bgIMvFAQvISLREcJJcKdrLkE3oFB2fTlT7Mb1V8Yotrqe5jSZAE/yLplzI3XVC
        xd11WlJhEClK06F3rQFEz8FS/MRa0GBcV8pVhtd4ED+BMYjYiHpUey2NCjm5RUf0tZbnMb1F
        r/phvcdWR5lJfV3Ri/MS3X+hCWqHWXPKJERFBSsHEqSSgpTtGXkO70HlfPIc3uOSiQkVkH/S
        9d6Rd8qUKn/mPDMDEgMiAzZ5pgymaazeOl++N0+iDCc6CW/xnUAR4UusF7FsxMcdW65hFU0Q
        y0frAD3X8/UIGftJ193xCqsa76J3HBuDAiB8I91kbM/IAqoX2q+XOI2yUWRHjWkDOwmi5Bf4
        Nlvdwu2P28fVsn137vAApPCYhg0KbK1l/C1DjbR9gyIHiAM5ByKn14PoXe2dwQfUKDoWnWkq
        RHrCt1SLtyWVdzK+VC78nlfaHoXRG95mDGse85amnefcnpwWusbaHevReTyvLml+PL08PQIP
        pwO3FOFQbPlxOA5ZMgIbu3el1HhFeJy1oHp01C792szfmsSClgUdaxicoQmVlto11IgDh8yy
        g4AgJP4PdYvLNg==
    """,
    "localization/fr_loc.py": """
        eNpNkMFqAzEMRO+B/IPIKb30Awo5lEBOPZSSnoXqlbcCr7XIbkP69bV3nTi7FzHzxhrkTSd4
        zkYxBcqiEb8oMcg0q2U4N52H7ab+LlBKcCLHH+x0jPLH9qZu37mnl+0GyucLg3aDBjjArsag
        S7sVLBvdN8XIoTLHdWweBbKpyq91aOLM5jhmGhnVY5JJiin5Wrn3uwfqoXst6jUMbEuXZWry
        T+ytsDyfNFbm80GGVX7shfk6M3o19Ibksvyu95OEF9M43ntDBctuWw4H/XLQUyAJllTZ8A+d
        x4c6
    """,
    "localization/gate_loc.py": """
        eNpTVtDV0lVIzk/JzEu3UigtSdO1AInwcvFypRXl5yrolRQl5hXnJJZk5ufFJyUWpypk5hbk
        F5UohEDFU1NAanm5knMSi4sV3IECPvnJGghZTSteLgUgKEhMLo5PB4rEp5al5pUo2CooBQCF
        FNwdQ1wVwEJKCgrKChcWXth3YePF7otNF3Zc2Arizrqw+MIUsMEQg5IzEvPyUnNABjhDmEq8
        XAB8e0VI
    """,
    "localization/gpio_loc.py": """
        eNpFjbFuwjAQhndLfodfYWmRwlwhdehUVWJkj1wTqKXEjhKzN5Vg6QAjjxFRQEBLnuH8RtgF
        wQ2n+787fddB3I0hzUjpSR9TO46fAuGMs3FpcvRsKXSVCauMTt5FlULlhSkthleejsItZzIT
        VYXXQpmBkQ/37WOfM/hSupjaRIs8xTOit5AQUgR0QCv6cwu4L/dJW1pTSzs6+f5DLWjtZn7c
        UHMR+TdGqqBO5IfQOs2C8OVGcaUX8dLVrqbWzWlPe29vvb3x7pP7pgPo+B8a+uXsDCOFcjw=
    """,
    "localization/main.py": """
        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
        3/8Dan/HPA==
    """,
    "localization/neuro_loc.py": """
        eNpFj7EOwiAQhvcmfYdLJ118ABMXE7fGOBgHF0LpGUkop8e1SX16gVKF5f+/7wjwYBpgJ6x9
        cFosedXpgGCHF7HAtXDs6ypt43QIcMaRqSWz+evtvq4grhdyIA8HaC45NQue8GmNw8RvSyyi
        s2Yu4rjEVRD3yJnnVDBO6EWJHfKRU2qQWtEf8qi8Xuw9FkilyPh2UT0KmvzP96i9WJnTaBsV
        /BSsaj0Yb3VKSDFqI3k+ERCCTOLYF+3mZp0=
    """,
    "localization/popup_loc.py": """
        eNpFi7EKwkAQRPtA/mFIpY0fIFjZWgjaH+u6koXL7nF3xt/3EgPONMO8mVf2CYeayUqkqm7h
        QUWgU/Jccd96efbdYo5UCq6e3univPvj/bHv0MRkLBEnDOc1Db+6jP4JMovVoBYo86izLKtb
        A1gB1LCBdvoCNm4x6w==
    """,
    "localization/simt_loc.py": """
        eNpljrFOAzEQRHtL/odR0gDSUaNIFFDTQZXm5PgcsHRnI58pQpU0aZBISj4jgBCBkHzD+o9i
        3x2hYJvVjHeep4/sJIO0hTa3Azz4cXaWHM44Gztb4dQ7YepSeG1NPhK1gq7urfO46XxVpFvO
        ZCnqGte68ldWHv29Hg84Q5xHa1RuRKVwjt4wCiTRA/qgF/oJC9An7Wgbntr7kXWFcofEZSP/
        Z97DlFa0pXWY/yZjDyt1+juXd8IYVSbAxcFF57acZZiFGe3CnNYRMo0V3hpgLEJfoO9GrGjT
        sc0kweJq05vwTK8x88HZHli8hdw=
    """,
    "localization/translation_base.py": """
        eNqVV21r4zgQ/h7If9D5WJB7qeG+LYXCldvSK5Tusu3el1KEak8S9RwpSHJfbtn/fjOS7ciO
        E/Zcim15nplnXqX8yk5PTllpKqVXZ6zxy9OPtDKfzWdqszXWM+P6x2dn9Hy2tGaDiLqG0iuj
        HWu/frYVWKg+qdL3CFQMpWsxb5u6AG8BOsRlDRvQ/h6XEoNr4zy93v359frLvfhycf8XO0ca
        xVb6dSGfHN159/5slOZCLFUNQiyimK2UTR7zfD67ubi9+nZxdSmuP6EyPp8xvMhS4bz0juck
        i1x4/pDVUq8auYLsMYoZ20qC9xgmxzP37jxsxKuqQJhtiEKGQPX7Ry1SdE5+ePt+FhWFKKyh
        3oLto7YCL2qzWoGdz+CthK1n1+HLpbXGpkCSQvMJ8CbgmHQDLfNZfEI/d8s8UHHyBQlbhXpk
        7WJUQb8oa3SBsjy7u/j7Unz+en11fXtxc5fl7PycZfe2gWw+E8LbEOckGyH6SaIWLPv+o/Au
        K5bGbqTnSdwpDahCaldLChmqSUomEpzPKliip7JKJXlrOG/DkX4ryhpkcI++qGVPTTmCjKF0
        vSq/biuzMFvo1SN5my0Y6NgO51loBwwCBniZ4OlKGAisa/RlWViQFRZSwAPv0EOcNcajcFL5
        BSXXeYsW+UjrCFsa7eGN4KSlWCpd8axdHNvB8LONw2LRHaxQHmzEbMA5qtB85FR07H1ilS5n
        SzSNSlvLzjS2hLHhnR49kE5cy0KqD5gQrYv4WATaR8OZuluuVV2Rwwg94MLAxm/DNHjTJiHo
        mSiDQ6TR0440PgbS04JYnL2s1FU3haauzL9vIWMaiwUdIrXSI7snmkW7t4co9sh+wS5tNAZa
        uTVU2bTe/EhQhj6Inw/8XvARfsTOwNb/T8AhlelAeOgS/Jg4Mw2F2sERsnFyFhU8NSuOU3A3
        uSgv1O3vZ+yDw5HRmZygGGf6ASuthShDgy77ptdYGjVUrF9kr2saujQUafx3rvadN/JiyJqY
        SkbTraXazcM4bfcmbT/kk3HsLXdd8VjwDXb2YALTzuEwCC2krKVzrAsXVNw8PeNRoR/eQmnc
        c3VJ+8it0dAtJyrd6BMdPPqlblPe7WLpOhEWQsOrELyskdaJtCu6nfzzSk9pF2BDokiRMFIu
        KBulKwqN+H3/MRRCZcPtdSLnpCglPtZBnUStvWAvsm4gTO9gu8IdUogwwvF/g+eVCe3IIKQb
        FdCpxnpHOx3PBG1hOG+U6/zkQf2CcUe2Gq2o0/NDA+JnPJv08IGoUBsGc9Og/dj2KKy7ADzQ
        +HgcI8mY5Ri1Q8ryqXwmZegaPJLxXckGTXlxtI6GKoddJ5JYxbYbxCXBtv00ZNTV8h90NlXl
        BvzaVLvyfmpwPgp8kk3tRbuZc6qLQXHjO7pGNzyZbGuJacdSwEMOy/YJBLFSbpWXtfoXeD7s
        p1WMNcbCQb1csLGx1n2MjKYJjmMMcUrjGEsPfBgJ9iFi9wiQ3uKIZykfb0JDBC4pi1TVsAxG
        aJone2gq84gM42Z6FKQS5+EHUVE1m63jE0bzQ8zi7yj6+w8Te+HK
    """,
    "localization/__init__.py": """
        eNplkDEOwjAMRfdKvUNHWLhBR2ABhOAAKIqcKhKJozTtwOmx3Ua4Ql3q9/7wf1zG0B2C8bHz
        IWEu3ZX+28YJd/n1RlvNyVh4gMUh+g/kC9oaG30oOvikW+nBFND6TLfWyeNG0610hClv/I2B
        CiRMU9KBOwMVgBliGXXiKEQibSPje9m92zNwmc6/sex4Cbl1gBAqy2TpzIQfg8j6BkxkAaFa
        nJmUJla7MlM9+1/FpZP+vnFvjbI=
    """,
    "reactions/reactions.py": """
        eNqVVltr40YUfjf4P5yqLJFSx7AvSzE4UEIopWVTnIU+LMugSGNHjaQxo1E2Ybtgp80u3fTy
        3of+BjeNWTcX718Y/aOeGV0sKXK6FdiSzplz+86ZT/MpbG1ugcNcLxz1IBbDrc+VpN1qt7xg
        zLiAQxaJdmvIWQCEHMSeL7yQEMi07OB76giwIxifkvRF2erlh9QfUx7lS0dUEJ+NRpSrFekT
        9Eti08oM6Ql1YsFWpruZQBm2W45vRxEMqO0Ij4WRWUS2eu0W4GUYhvxD3shZMk2mIK/kIpnK
        D3KenCVv8X+iRDfJ7yAvkwv5Xi7lpZyplykqz2EDRbNkIufyb3yfotEEHUxw0VLO5J28Sy6S
        8400krwElMzlLWiDmbxO3siF/Ker8lQLdk/sYOzTKMtMXdvb28Dz5BGAVSHWmkVd23VJDor5
        rW+f7rM4dM1I/ZPQDqi11jSwjygpXk3n0A5D6ndABJEIxh2wfZsHJKBRZI9o1EHE1b3/lIXU
        yovQlf4p/0reYY3XyRk0pqCQQMQR97m8Sn7UcE8Vyku0kNd5PxDqvJ0gFyl8S/R9jv/YKXkr
        l51V2ORtcqbVF+hH3oFeMJc3oG5adZWNC/1/tZViYJ+v5BwyczAjwS3YQjEWsUD/mLvq+0xV
        kDtH/TOOY+hxEB5GENjmkstqZDBdD6cTbTQ8et6SSfILqOlEYJLfcC5nWNECDNunXOSWRskl
        GFEQrRRgBLbnNy3E8VWNwEnH+wILS35VQGGw5CfsxUTFwX+dhRpnfJqrxJYa558LM5ztVIrW
        l1k3z1CzUGnrpw+ove2Wp+QLPiqPuroi55C6sU/B3M+e9vRm/UG3oQc66js9VpUhQf/vVZeX
        epjUds09FZs8j/zd3uDrr55+SXb2vtkb4I4yBtQtlC4dInF5oScIMSPqDzuFI5yIcBwLMkRS
        o1yRSC7BfgpKBEt3jlUqSXnoFjX1a0kVK+qOcWVd1GhRDVxYVcU1yxVd9uHV63LdFd5Ia89f
        yzV5QwiZAC+K4gNNrma+qkuIFhDSKXatVWswt72IwrPTMd3lHONUtbpVr16jcx0jjwBsWDg0
        ukPGA1s0RMUnxS2EWFWvpdf024HwDZlpDMqUWdTag0eRsSr9YfdVSJ8/YPQC8aalL1OOeo1y
        U9z/k5w2bdw7eNs8eqmeyiiXRn3NJqtwV02XEZbps3CE+y2nrcdPwPVGnljxV9WskcJ65TzU
        pbOuBcxLqCweUBHzsCrTdZWGsLq3solRNAF26Fa1XYf5+AH5pJ+KKwxQSycbEJcexKOm4dw9
        pqEAl4UbAhzb94uPZ2/FXWm0R9gfwVI9BHEk4ICms3XfbUO261ZVku+sHXS91zSKZQxz2Ors
        Uh8Cftq7H96JOcfiU3qBfrOnrtaaxmjsMZIqfXpMfcO677CaTY3MNMeE1aANSX1Ez4re7aS+
        IC0AOUUHxtHpNTZrTa8a4Xhg3doSm02sZnHey7KMnjh0jOfd8NjjLAwwGc2pDShlCOFGC/Ho
        bho7tppfPExnWCClZmAgCGkzi8GGl4wfGZXjnTrl60bjKfS5weOQOHiyE8YL+KwPj1frlFuq
        +W/Fp6qpVdbsehgOfwF6e2g3GvvCxuO9IszSrkvJOj1U1uHJyPijj3x1Vm23/gVnGXMi
    """,
    "reactions/__init__.py": """
        eNqdkdFqwzAMRd8D+Yd8wH6ilAb6YBrmQB+LcNTWYFtGtln397OzLmUDZ1vfZOlcXa51ZrId
        I6ioyYVOW08cu9evRtucC4A3VCkSL8Du3nh2vlEKQ9iSi0zm4JFh1W5jgK0gp3NTgIMLVjcf
        UvQp/hrgB7bf18DBwLuk5Ka2qSHLlqOOV6kY0YUrxaq3zEPpwfbaxBJkhXsT+Zty3DVkIJ98
        FRByK9FNyC+lLuWIt1jDBWhT5p+SGtVrxvkkjzPf0bCkP4V5RTjBRD7HfNxyfk87m62+2fxd
        O6LBC4N9Ut6Pw3+VS+K2+QCOuTL0
    """,
    "reactions/executors/access_control.py": """
        eNrNV1tr2zAUfg/kPwiXUbuXkLyNMj+U0rGX0cH2NoZQ7JPUiywFSW7m/fodyXLia5qVjtXQ
        xvK56Fw+nXN0RhKZZmJ9Qwqzun4/nUwnWb6VyhCT5bBfPEptppOVkjmBX5AURiriSfd+7cmP
        wLegdE1dg6Fcrteg9rq4TBjPfjOTSUGYtmu7bcVF4oZIGFnCdHJGrl/jsYpukwS0RqeFUZIT
        XWoDuSYKWGLt0a+42XSScIZ7VVveVTs+YHCc5zqsAxfdWF6CTworQmkmMkNpWH2yjwa+ujos
        mdNHtzIThgqWwxjNlNsmTdZbdwkpcFbSPVl7krWrZgmC4LC4VWvdoA3aREJtVHSMyxrhuYKv
        2bpQAUFQBQ8KTQjacm3LvRAJ8LMg5hFIKqWXTrjUQM0jdZ/aWrpukhDNGHXSBn3Wdyvuu3pM
        Ri5/oog9PTN8hcSEw3qjY0qc03E/eh2ZTpTiTtg63L1oxL0A1bDcyxhNjaSJzIEuWbJBkXmH
        Y0+jtnwommm6k2qDBQaZPzKuoYV1m0GXKheWZi6qAoBWLot12M5jcHv39eDbrD7SLi7knUZD
        jCWLWXA1ksWDvkbcjSo7cM1Wo8mIicdsR2QUBTMbhlymQBnfsVJbA8OIkDOyLTny3KSZZksO
        8f1iMV+0lQI/bkl1ZE62ZK0YvvnPUiTwWnZ8yjZPmf4rWzCLORMgDC8bYGhkBX4lsMUmI54y
        JUWOnPdK4UnHvgFKdfbxoAHLEQZ3TJy7BuRPjkdI+E5HxMi6BVw5PYibUbQ4jqiF26rM/Avg
        Os3pm4auM/E/YTcFUVJm/xzljSC3AYc3D10h0W7eg+0LAPMMWPxGLkPayjci8xJQDG/HOJe7
        upgtS7qBstpSWh2nbzmKgFqs211jO7fOcpaJ2ZYluqpeOIw4GJyMIn+WumjVcLKGqpE0He0J
        e2ztmBLYiMOghSnnTSE2Qu7EKJYsUxtGrr2Poqg7KHxwt4mZ/RdGQ3ndo2WAdspMccR7N3xZ
        SVmYcDGfz72DlbaWVz6PVZ57zvWr7MhQhBELG/5G5HJ45BoG2ri7A5hQYAolTofP0Vh+UwU0
        Z75Xh/9wi3/O5pHyeqBXWByovO7H3zLHS27NFQZVfZZJUigFKeaxLr/1dRELW8HBH5NuacV2
        UDBOq/sxHB8Mgs+Omdhb51N1E5Yr8sUOCNowZewI0HDIYRgJBjve93NVCMRbIcz5D3IZk0Vn
        Bm+juGVi07YrcsHwIoc/F5udfWsaO6zoDx2awF4=
    """,
    "reactions/executors/alarm_mon.py": """
        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
    """,
    "reactions/executors/executor.py": """
        eNpdUE1PhDAUvJPwH17wUgiYeDGGZBNX49GL8d6UUqBaWtK+Rv33vi67izinvpl5H9MbaKoG
        pOu1HVuIODQPicmzPNPz4jyC6GSeDd7NwHkXtUFtOYez6LoPJckTYPnha5Fa80waEQK8fCsZ
        0Xl2Vcs2z4DA+axQnFw07ZC23B6fnl+JTO3J8pg40QX0QiK5J9evQq8GUKfJigVlhhrkJKxV
        pgYMNQgj/EzjQxCjojpMDrkVs6qhEn4kpqo+v9LrckxCURRbsdpW08YeqfrTkXBeDGyIxsAY
        dV/+c2AAZpwdyxbePaXVHu7um16PGgE1XYliXvYt+wDAer392wXXUMDog5K66W8Ko7dhx+3i
        LXTHLwvojHY=
    """,
    "reactions/executors/fire_alarm_executor.py": """
        eNqVVduOmzAQfY+Uf3CpKiBi2dcKJZHaaitVqvoDVYUcPBAasJFttolW++8dm0sMBWnrF7Dn
        zMw5M768Jw+7B5IJVvIiIa3OHz6ale1muynrRkhNzkLp7SaXoiZwhazVQpLe9NTPe/OJKkhp
        RWU9AD7jyiezYOJpeUu2G4LDos9QNSDVAC1Ap5UoCsBocM2g0eSbtTxJKaTraFDI1nH8bv0I
        VZMo2033Rw7OchAaw3aTVVQp8rWUHb9BSTAyjkZ1YWIcTHoGOUnTkpc6TQMFVR4RLS7AI0IZ
        S59LBiIi4vQ7VehGCwh72maoFtUG/ySMiIkTxmPY0HFBS2wToAT7ndnGrGgf/2cYhw6inJkr
        qmss9JrytqrS7Ew5hwoVKpRnKKc1KIWOON9RWZjP7vLH/Lk6J1DDa+IaYycCr6ZlNSx5c8GZ
        4Bq4Vuj789fdVuYzzU5OM+67yx2jCgXy2W4FV1ysmqpEPqlLYuaaYsnQbV7LuDd3ivrJQhSk
        zYV2gy2wNKPbnjGDU1sEXo83/YJM2xC5aDlLyAesuwTdSu5F5J53nT+ntemDwyA2S0suk/rH
        tGmAs+Blma+nbw14CX4lnqRSDjX1ohX8QKBoS4Z+Q2dW0IbiHWVFrEG71g5xu9kC9nXWneGS
        4Qyu7h2z3pQvlPv2vhl2ky2tFqSmFyDdQeyrh92S3db3Js3B7TA5ELOcb23AWPyzrhcr3hkS
        EqzUbP+OicwEIQZ43J+BsuO+Bk1NyaUCffDtY+Af94+d8STY7eitxFtbf+l1vv6v4/7R5sPk
        ht8CKoyxxDXVQZ/hsHDR+O5F40fE/yGIhqv2w3BWM3dz9Ed20otZn6b7AtFn+yDxof1qfqF0
        J/bNr0GOhuGl+gtgNR7O
    """,
    "reactions/executors/mail_text_sender.py": """
        eNp9UsFuwyAMvUfKP1jdoWmV5jxV6jGHSdtpuyOUOikqgQio1v79bJIopNrmA2Dznv0wfoHD
        /gCNPSvTHeEW2sMrR/Isz1pne8A7NrdgHah+sC5APfkMCO5xzDMgi9AL6gGdn5EdBqFt1yFh
        8d7gEOAt3tTOWZcSGUXlE+J75IH0qyx5Np7glISLHV/kWaOl9/Ahlf7Ce/hEc6a7We1uKnfG
        FoRQRgUhCo+6LaEnhvARXgJGz2GjBoUm+JnHxvAqQZOKxHvCPSci8HOIRc+axi7jJKm5SGNQ
        lxB8CVJL14sevZcdkr+XruNtf/3mU6pwBaWKa2pFPSs2UcQU2uwWrmrB2LCmJKnZxn5XyN9X
        bNbJ4SK92QbYpvm3cMVHWoTNYbg5s8SWIfqr0RVvBQf86dfmUqPoy08rRUnVafjquClreKzo
        Ef+9jlZK8APgufrJ
    """,
    "reactions/executors/output_reaction.py": """
        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
    """,
    "reactions/executors/output_reaction_v2.py": """
        eNqlVcFu2zAMvQfIPxAeitmpY6Q7DUFzHdDTgK13QbFpR4giGZK8tH8/yXYcWXbTBdPBUCTx
        8ZF8ZL7AerWGXBZMVFtoTLn+7k6Wi+WCnWqpDBh2wuWiVPIEmWxM3RiikOaGSQH9k5/t8a/+
        VA+mB6mNQ2qND8hrVPpiU6EhXFYVKvei28HOO44Td7Fc5JxqHbp4eYmDk2S7XIBdBZZACBPM
        EBJr5GUKVc2kTu0Np+8pXMgT817jxcot3Vh+8cRRCg4lyQbQW3AemjXKDNVHkstGGBvaJrjM
        D1QI5PYmilygA3uXcdVy9+mxssfUxEgLekKyp/kRntsKZe4T++/d6jKZFbhvqnh85VbkjMBI
        yLnUdnNAqKjBDB60hX3QUTrrMvU9jlGDn621rZ8hJzQHWcRz97JGQUpOK5uJH5RrnHnjJXK9
        g6f7onQxgUOADqHA3FZNY5H6p0xv/ZAHhzcDHIpy5fcMm+2URM/xTJWwnRZHr1fH9ssL8dXA
        HkGgJcv+IETJFOOmpObZzDBxTdnWzjZz/G2z2fQRC3wzhBlU1MnZc4+2JAHOCOPpitFJN/HV
        PIYdVB30gq+BV9Vg2EeB5nfAhIk9FSbw2L1suzKwLpmaVaBHOR5x7secJRWw/qgSjyNNjvQ4
        UR8T96gvmQ6AIVdBURSaRombdfu/ZP5Lr/22JOp2PqgUXOfDkEU4M86dyGlp5dDNTxe09ZVL
        UdjgP5B8N2k/HzSfiOhuGeAb5o3B/l+kH9cprKiq7PxfrY5nt5vo4jrX+12o9VBd1ulfotIl
        xA==
    """,
    "reactions/executors/play_sound.py": """
        eNp1UU9rwyAUvwf8Dg92sWHpeRR67KHQw2AfQMQ8ndTGoIa1334+YzY7WC7q7+975AWGfgDl
        RzuZAyxJD2+EsI51Ovgb4B3VknwAe5t9SHCq70pHv0yjmJ184I/kg7D3AlFMCo8D6yB/xfGJ
        bsYQN7HBJJw3hrR4VzgnOBfmFIIPrZFUecjGeCk+kPEphXXrDY4NzHdEsE45GSPQcGVKvq2z
        q01P+xzbVdYE0oyoQQg72SQEj+j0a7Vp63ALKmGZ2/9SOa9B1o69ciiDKBBvUtqu9Rdgrepl
        MDEf/fWLbv/01XQ6+J8xcvY36JSjaw==
    """,
    "reactions/executors/reactions_with_screenshots.py": """
        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
    """,
    "reactions/executors/show_message.py": """
        eNqVUstqxCAU3QfyD5eUkgdJmO5KoMsuu+qyFLHJjZExOqhhOn9fbZROMpRSN8bDeXnNHTRV
        A70auGQdLHZsHj2SJmkyajUDfmK/WKWBzyelLTyHc5oEYFLGBu6E4oTaRCpDS4RiDB153eHp
        CizKCLcDfiysyM2kzjCjMZQhBMXqhUNe+kpp0gtqDLw65stKLGKjsksTcGvAEQjhkltCCoNi
        rMEbk2BMBhT0Esl+eU57S3Flb0FfIYaso8GQ0U9UShQ1WFMDFVTPUenOFdXMb9Xx7L+u0/kI
        Ulnghktjqeyx2IsH3ttrhV9hcKi10kW2VTivb0uv6+DeZPs+5dZLo120/ME2ZDeFrbh1L+gT
        UduIZeXNdTaa/3SfqJG5hXwTAEe85Nkftf2P2AbBboZvu77v9a+PXsHD4XBwUV9GQ/3I
    """,
    "reactions/executors/show_popup.py": """
        eNqdVUuL2zAQvgfyH4SXEGebmO6hUAKB0rLQS6Gw9NCTUKSJra4tuZK82fTXdyTbseXNPtpc
        Io1mvpn55uErsrneEK6FVPmWNO6w+egl89l8djC6IoI5cLICIqtaG0f8WUDpWPdugHEntbIZ
        PAJvnDbDqbe57e6dyZ5ZoI2Tpe0VPqPkhxfMZ52k0NZ16gWUNZizbg6OljrPwZyVS81ZKf8w
        Hwdh1t99/K0W2Y1M0pV/mM94yawld4U+ftd1U6d9hKvtfEbwJ+BAKJVKOkpTC+VhTSqNN22o
        09SiHWWGF/IBqI+R1h5lTYS0dclOVDQmBNPD+Z9HyV4HwXBfV5qgTt0ixlQ0saB5I1HLs5zp
        /S/gLk00sszQLz7RhLxrHy04h51h0+VyleGLCAT2FKGJ6sPraOIFUwrKNXGVdVU9ZqAtQSZg
        3+RpcucYls4nSDqEszGRdksWtsfw5+Qp8gDsLLUBbTd0UoZCJFC4tFPfnDsXI+VaCbv7EGOA
        Ei8i9JkHFr0/9Orbq3ef4fXgvaTJ4ueiWgi6+Lr4trhLRm7Qx2CFl7fYRLwNYv9Lugp4+sgm
        UNQyhz3UHkJk7RHdtVTGGD2vsfSN7Tq16mmZyLu0B+GYeXPaXvDtWzQbe00JuSL1qZTKbbG9
        2b6E3e3Nzfub2Pj5lP4/rZdSu5jeJEV45FDjHlQP0mhVgXK3xuB+xF0Fxkyyj8fkC1PLeEwy
        0hprzhvTzQainNvzE0bqJK/AFVoMs8qZ4lDSQ6PCvk7Hk1njNhzPdWAlEHF5qteElaailc3f
        NN/tYjtKJfQxicYo7JjfDdgQUsxD72I9pYdnATBrM7rUt5Ncn0UIecID1gN3fd8GU21W7QXb
        tsDRwpsupEuRTPfwOhqBgfH2k/l0iVpPNfNEgLUsB7xfM5P7v+v7oz+NKyAPRGmH61MqbALk
        IJ0aC8nd6nLDge+qNIktECtAeruu12KFVYxlwDVm9LWJlHHrxcYZfpm9R8DJ6mTjxdelE9n8
        S+wFs354lpEDcg+nZfJK2KF2oyl4viChin8B5QrPLQ==
    """,
    "reactions/executors/sms_sender.py": """
        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
        iMhvX/E2DjicwLqGwtAESP4DI1Mf+g==
    """,
    "reactions/executors/telegram_text_sender.py": """
        eNqVUk1rwzAMvQfyH0TGqFOankdhx/2C9W6Mo7imjl0sl7X/fvKSbEm2MaaLrI/3nmT7AZpt
        Azq01psDXFPXPOVMWZRFF0MPeEN9TSGC7S8hJngZ47F8QnfBSFPVYJIuGINcHzw8z5Kizrxl
        oZ0igiM6NFH1r+jbI96SmLjrQ1kAW4sdSGm9TVIKQtftII0YSQzCz85suWG/qrP6KpPlJ+5h
        Nxyp9Ul5j441aAfKqdjLHomUQY63Kprstue3fJrr2g58SGDJekrKaxRrcGt1miOyDReyxxhD
        FNUSwVwflBl3gEeq1vPUS66I6Rr9V27RzFewBO/5PUTVK+umVFV/22YB+c/oJ0V+k2Az59/A
        Ge/VH0OneF/p/PSgHPNHWWjOePGm8ZL/aHY2eFAEPOYv809dgluY5B1YP/Cv
    """,
    "reactions/executors/__init__.py": """
        eNqNksFqwzAMhu+FvkMeoKe9wSgr9BBa5sGOwrjKaogtYylL+/azEzsNZYPdrE/fL7DlLpJr
        8IZmEIqNdYGiNG+l3m663NbGIDMY8hKpr9LrRPczPAWMWix5rpleRweO/KJn0JK3aW6rvf7C
        Op4GCYNARG3yhBo4Tfi9UP5dhu+XP/zjsSRCr+/ANPhLNc+JqAy2m+LUcQyjlSuwiYieryRc
        M8vczySoR//fA1QqVNDuYHvJVy/B5Izg0kOmB1mpYzujtRUoDGHtnDOohmNg9BdclqhatVcT
        2eVzPn7gTYrvtO1BUv2UahPP2pwscmcjwrzR569ySK1ptY8/8wNgE9/q
    """,
    "reactions/screenshot_senders_adopters/screenshot_senders_adopters.py": """
        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
    """,
    "reactions/screenshot_senders_adopters/__init__.py": """
        eNqdj01Ow0AMhfeRcgdLXcMduqBrJLqvhmSASJmm8swBSjcgFYkl14giokZp2lzh+UY4UzhA
        2Xj88z173ozmebUJNn+w69wy3ZB59IFNFigrjfdpMiN8ocY3anlDTRhxlh3OGNBrbEhe9TlM
        czTK7OSDLjhG5VrZyp7Qk2y1c8ARna45yR7DtFrFLU5Kt3E+kKZH+aR4Y4y9Ru90E9hr2an0
        /fcDzW2apMkTV458xtau/UsVVj768CsTbbGnwm0qDn8275wpyovXq7VLW9pnNu6f8sXy/lrl
        omA7Lw27yWma/ABCPM3P
    """,
}
t1utils.resources_check(script_path, resources)

import os
import re
import json
import time
from collections import OrderedDict
from __builtin__ import object as py_object

from helpers import init_logger, set_script_name
import host


GLOBALS = globals()
DEBUG = GLOBALS.get("DEBUG", True)

logger = init_logger(name=host.stats().parent().name, debug=DEBUG)

logger.info(
    "SCRIPT START. Script info: %s, pc id %s, pc name: %s",
    set_script_name(),
    host.settings("").guid,
    host.settings("").name,
)

import localization as loc


# """ Типы тревоги """
MOTION_ALARM = GLOBALS.get("MOTION_ALARM", False)
CROSSLINE_ALARM = GLOBALS.get("CROSSLINE_ALARM", False)
INTRUSION_ALARM = GLOBALS.get("INTRUSION_ALARM", False)
PEOPLE_DETECTED = GLOBALS.get("PEOPLE_DETECTED", False)
SOUND_ALARM = GLOBALS.get("SOUND_ALARM", False)
FIRE_ALARM = GLOBALS.get("FIRE_ALARM", False)
FIRE_STOPPED_ALARM = GLOBALS.get("FIRE_STOPPED_ALARM", False)
LEFT_OBJ_ALARM = GLOBALS.get("LEFT_OBJ_ALARM", False)
SABOTAGE_ALARM = GLOBALS.get("SABOTAGE_ALARM", False)
ORION_ENABLE = GLOBALS.get("ORION_ENABLE", False)
SIGUR_ENABLE = GLOBALS.get("SIGUR_ENABLE", False)
FR_ENABLE = GLOBALS.get("FR_ENABLE", False)
FACE_DETECTOR_ENABLE = GLOBALS.get("FACE_DETECTOR_ENABLE", False)
SIMT_ALARM_ENABLE = GLOBALS.get("SIMT_ALARM_ENABLE", False)
INPUT_HIGH = GLOBALS.get("INPUT_HIGH", False)
INPUT_LOW = GLOBALS.get("INPUT_LOW", False)
DD_OBJECT_IN_ZONE = GLOBALS.get("DD_OBJECT_IN_ZONE", False)
DD_CROSS_BORDER = GLOBALS.get("DD_CROSS_BORDER", False)
SCRIPT_NO_HELMET = GLOBALS.get("SCRIPT_NO_HELMET", False)
SCRIPT_NO_UNIFORM = GLOBALS.get("SCRIPT_NO_UNIFORM", False)
WARNING_TERMAL_SIGNAL = GLOBALS.get("WARNING_TERMAL_SIGNAL", False)
SCRIPT_AU = GLOBALS.get("SCRIPT_AU", False)
GATE_PACS_EVENT = GLOBALS.get("GATE_PACS_EVENT", False)
ARUCO_ENTERED = GLOBALS.get("ARUCO_ENTERED", False)
ARUCO_LEFT = GLOBALS.get("ARUCO_LEFT", False)
VORON = GLOBALS.get("VORON", False)
NO_MASK_DETECTION = GLOBALS.get("NO_MASK_DETECTION", False)
DISTANCE_VIOLATION = GLOBALS.get("DISTANCE_VIOLATION", False)
SIGNAL_LOST = GLOBALS.get("SIGNAL_LOST", False)
SIGNAL_RESTORED = GLOBALS.get("SIGNAL_RESTORED", False)
SUSPICIOUS_POSE = GLOBALS.get("SUSPICIOUS_POSE", False)

# """ Реакции по событиям """
SHOW_CHAN = GLOBALS.get("SHOW_CHAN", False)
SAVE_SCREEN = GLOBALS.get("SAVE_SCREEN", False)
SEND_FTP = GLOBALS.get("SEND_FTP", False)
SEND_SCREEN_EMAIL = GLOBALS.get("SEND_SCREEN_EMAIL", False)
SEND_SCREEN_TELEGRAM = GLOBALS.get("SEND_SCREEN_TELEGRAM", False)
SEND_EMAIL = GLOBALS.get("SEND_EMAIL", False)
SEND_SMS = GLOBALS.get("SEND_SMS", False)
SHOW_MESSAGE = GLOBALS.get("SHOW_MESSAGE", False)
SHOW_MESSAGE_DELAY = GLOBALS.get("SHOW_MESSAGE_DELAY", 5)
PLAY_SOUND = GLOBALS.get("PLAY_SOUND", False)
SOUND_NAME = GLOBALS.get("SOUND_NAME", "bell.wav")
CUSTOM_SOUND_PATH = GLOBALS.get("CUSTOM_SOUND_PATH", "")
SHOW_POPUP = GLOBALS.get("SHOW_POPUP", False)
MON_POPUP = GLOBALS.get("MON_POPUP", 1)
POPUP_DURATION = GLOBALS.get("POPUP_DURATION", 40)
OUTPUT_ON = GLOBALS.get("OUTPUT_ON", False)
OUTPUT_ALGORITHM = GLOBALS.get("OUTPUT_ALGORITHM", "type_1")
ACS_ENBL = GLOBALS.get("ACS_ENBL", False)
SEND_SIP_CODE_ENBL = GLOBALS.get("SEND_SIP_CODE_ENBL", False)
SIP_NUMBER = GLOBALS.get("SIP_NUMBER", "")
SIP_CODE = GLOBALS.get("SIP_CODE", "")
TOKEN = GLOBALS.get("TOKEN", "")
ADD_SCREEN_TO_ALARM = GLOBALS.get("ADD_SCREEN_TO_ALARM", False)
ADD_VIDEO_TO_ALARM = GLOBALS.get("ADD_VIDEO_TO_ALARM", False)


# """ Дополнительно """
SERVER_CHECK_LIST = GLOBALS.get("SERVER_CHECK_LIST", "")
CHANS_CHECK_LIST = GLOBALS.get("CHANS_CHECK_LIST", "")
FOLDER_NAME = GLOBALS.get("FOLDER_NAME", "default")
SAVE_SCREEN_DELTA = GLOBALS.get("SAVE_SCREEN_DELTA", 0)
SAVE_BUFFER_DELAY = GLOBALS.get("SAVE_BUFFER_DELAY", 0)
ONLINE_SHOT = GLOBALS.get("ONLINE_SHOT", False)
FIGURES = GLOBALS.get("FIGURES", False)
SUBSTREAM_SHOT = GLOBALS.get("SUBSTREAM_SHOT", False)
SHOT_SPAM_PERIOD = GLOBALS.get("SHOT_SPAM_PERIOD", 0)
DAYS_TO_STORE = GLOBALS.get("DAYS_TO_STORE", 5)
AM_SCHEDULE = GLOBALS.get("AM_SCHEDULE", "")
INPUT_FILTER_REACTIONS = GLOBALS.get("INPUT_FILTER_REACTIONS", "")
INPUT_STATE_TO_MAKE_REACTION = GLOBALS.get("INPUT_STATE_TO_MAKE_REACTION", "closed")

# """ Настройка e-mail """
EMAIL_ACCOUNT = GLOBALS.get("EMAIL_ACCOUNT", "")
EMAIL_ADDRESSES = GLOBALS.get("EMAIL_ADDRESSES", "")

# """ Telegram """
TG_IDS = GLOBALS.get("TG_IDS", "")
TG_PROXY = GLOBALS.get("TG_PROXY", "")

# """ Настройки ftp """
FTP_HOST = GLOBALS.get("FTP_HOST", "172.16.12.69")
FTP_PORT = GLOBALS.get("FTP_PORT", 21)
FTP_USER = GLOBALS.get("FTP_USER", "trassir")
FTP_PASSWD = GLOBALS.get("FTP_PASSWD", "123456")
FTP_PATH = GLOBALS.get("FTP_PATH", "")
FTP_PASSIVE_MODE = GLOBALS.get("FTP_PASSIVE_MODE", True)

# """ Настройки SMS """
PHONE_NUMB = GLOBALS.get("PHONE_NUMB", "")
SMSC_LOGIN = GLOBALS.get("SMSC_LOGIN", "")
SMSC_PASSWORD = GLOBALS.get("SMSC_PASSWORD", "")

# """ Распознаватель лиц """
FR_SERV = GLOBALS.get("FR_SERV", "")
FR_MIN_SCORE = GLOBALS.get("FR_MIN_SCORE", 75)
FR_ALARM_TYPE = GLOBALS.get("FR_ALARM_TYPE", "Any person")
FR_ALARM_NAME = GLOBALS.get("FR_ALARM_NAME", "")
FR_ALARM_GROUP = GLOBALS.get("FR_ALARM_GROUP", "")
FR_SAME_EVENT_IGNORING = GLOBALS.get("FR_SAME_EVENT_IGNORING", 0)

# """Тревожный монитор"""

# Базовые настройки ТМ
AM_DISPLAY_DURATION = GLOBALS.get("AM_DISPLAY_DURATION", 30)
AM_ALARM_TEMPLATE = GLOBALS.get("AM_ALARM_TEMPLATE", "")
AM_BASE_TEMPLATE = GLOBALS.get("AM_BASE_TEMPLATE", "")
AM_MON_1 = GLOBALS.get("AM_MON_1", 1)
AM_MON_2 = GLOBALS.get("AM_MON_2", 0)
AM_MON_3 = GLOBALS.get("AM_MON_3", 0)
AM_TYPE = GLOBALS.get("AM_TYPE", "Show channel")

# Опциональные настройки ТМ
AM_NO_MOTION_CHECK = GLOBALS.get("AM_NO_MOTION_CHECK", False)
AM_CHANGE_TEMPLATE_CHECK = GLOBALS.get("AM_CHANGE_TEMPLATE_CHECK", False)
AM_MAX_CHANS = GLOBALS.get("AM_MAX_CHANS", 24)
SAME_CELL = GLOBALS.get("SAME_CELL", False)

# """ Настройки SIMT/нейродетектора """
SIMT_BORDER_ALARM = GLOBALS.get("SIMT_BORDER_ALARM", "")
SIMT_BORDER_ALARM_DIR = GLOBALS.get("SIMT_BORDER_ALARM_DIR", "A -> B")
SIMT_PRESENCE_CHECK = GLOBALS.get("SIMT_PRESENCE_CHECK", False)
SIMT_CHECK_ZONES = GLOBALS.get("SIMT_CHECK_ZONES", "")
SIMT_PRESENCE_DELAY = GLOBALS.get("SIMT_PRESENCE_DELAY", 10)
SIMT_SIZE_ALARM = GLOBALS.get("SIMT_SIZE_ALARM", False)
SIMT_SPEED_ALARM = GLOBALS.get("SIMT_SPEED_ALARM", False)
SIMT_LENGTH_ALARM = GLOBALS.get("SIMT_LENGTH_ALARM", False)
SIMT_ENTER_ALARM = GLOBALS.get("SIMT_ENTER_ALARM", "")
SIMT_LEAVE_ALARM = GLOBALS.get("SIMT_LEAVE_ALARM", "")
SIMT_SIMILAR_EVENTS_DELAY = GLOBALS.get("SIMT_SIMILAR_EVENTS_DELAY", 5)

# """ Операции со СКУД """
ACS_TYPE = GLOBALS.get("ACS_TYPE", "Sigur")
ACS_DOOR = GLOBALS.get("ACS_DOOR", "")
ACS_LOGIC = GLOBALS.get("ACS_LOGIC", "open the door")
ACS_DELAY = GLOBALS.get("ACS_DELAY", 5)
ACS_MAN_ACTIV = GLOBALS.get("ACS_MAN_ACTIV", "Ctrl+F17")

# """ Операции с тревожными выходами """
OUTPUTS = GLOBALS.get("OUTPUTS", "")
OUTPUT_ACTION_TYPE = GLOBALS.get("OUTPUT_ACTION_TYPE", "3.close-open")
OUTPUT_DELAY = GLOBALS.get("OUTPUT_DELAY", 5)
OUTPUT_MAN_ACTIV = GLOBALS.get("OUTPUT_MAN_ACTIV", "Ctrl+F41")

# """ Операции с тревожными входами """
INP_ACTIV_1 = GLOBALS.get("INP_ACTIV_1", "")
INP_ACTIV_1_CHAN = GLOBALS.get("INP_ACTIV_1_CHAN", "")
INP_ACTIV_2 = GLOBALS.get("INP_ACTIV_2", "")
INP_ACTIV_2_CHAN = GLOBALS.get("INP_ACTIV_2_CHAN", "")
INP_ACTIV_3 = GLOBALS.get("INP_ACTIV_3", "")
INP_ACTIV_3_CHAN = GLOBALS.get("INP_ACTIV_3_CHAN", "")
INP_ACTIV_4 = GLOBALS.get("INP_ACTIV_4", "")
INP_ACTIV_4_CHAN = GLOBALS.get("INP_ACTIV_4_CHAN", "")
INP_ACTIV_5 = GLOBALS.get("INP_ACTIV_5", "")
INP_ACTIV_5_CHAN = GLOBALS.get("INP_ACTIV_5_CHAN", "")

# """ Тревога Orion """
ORION_ALARM_NODES = GLOBALS.get("ORION_ALARM_NODES", "")
ORION_EVENT_REACTION_ALL = GLOBALS.get("ORION_EVENT_REACTION_ALL", True)
ORION_EVENT_REACTION_1 = GLOBALS.get("ORION_EVENT_REACTION_1", "no")
ORION_EVENT_REACTION_2 = GLOBALS.get("ORION_EVENT_REACTION_2", "no")
ORION_EVENT_REACTION_3 = GLOBALS.get("ORION_EVENT_REACTION_3", "no")
ORION_EVENT_REACTION_4 = GLOBALS.get("ORION_EVENT_REACTION_4", "no")
ORION_EVENT_REACTION_5 = GLOBALS.get("ORION_EVENT_REACTION_5", "no")

# """ Настройки Sigur """
SIGUR_ALARM_NODES = GLOBALS.get("SIGUR_ALARM_NODES", "")
SIGUR_EVENT_REACTION_ALL = GLOBALS.get("SIGUR_EVENT_REACTION_ALL", True)
SIGUR_EVENT_REACTION_1 = GLOBALS.get("SIGUR_EVENT_REACTION_1", "no")
SIGUR_EVENT_REACTION_2 = GLOBALS.get("SIGUR_EVENT_REACTION_2", "no")
SIGUR_EVENT_REACTION_3 = GLOBALS.get("SIGUR_EVENT_REACTION_3", "no")
SIGUR_EVENT_REACTION_4 = GLOBALS.get("SIGUR_EVENT_REACTION_4", "no")
SIGUR_EVENT_REACTION_5 = GLOBALS.get("SIGUR_EVENT_REACTION_5", "no")

# """ Настройки GATE """
GATE_EVENT_REACTION_ALL = GLOBALS.get("GATE_EVENT_REACTION_ALL", True)
GATE_EVENT_REACTION_1 = GLOBALS.get("GATE_EVENT_REACTION_1", "no")
GATE_EVENT_REACTION_2 = GLOBALS.get("GATE_EVENT_REACTION_2", "no")
GATE_EVENT_REACTION_3 = GLOBALS.get("GATE_EVENT_REACTION_3", "no")
GATE_SUB_EVENT = GLOBALS.get("GATE_SUB_EVENT", "no")

# """ Настройки ВОРОН"""
VORON_EVENT_REACTION_1 = GLOBALS.get("VORON_EVENT_REACTION_1", "тревога в зоне")
VORON_EVENT_REACTION_2 = GLOBALS.get("VORON_EVENT_REACTION_2", "неисправность зоны")
VORON_EVENT_REACTION_3 = GLOBALS.get("VORON_EVENT_REACTION_3", "зона снята с охраны")
VORON_EVENT_REACTION_4 = GLOBALS.get(
    "VORON_EVENT_REACTION_4", "зона поставлена на охрану"
)
VORON_EVENT_REACTION_5 = GLOBALS.get(
    "VORON_EVENT_REACTION_5", "ручное подтверждение тревоги"
)
VORON_EVENT_REACTION_6 = GLOBALS.get(
    "VORON_EVENT_REACTION_6", "автоматическое подтверждение тревоги"
)

# """ Настройки нейронного детектора"""
DD_SAME_EVENT_IGNORING = GLOBALS.get("DD_SAME_EVENT_IGNORING", 10)

# Реакция на нахождение объекта в зоне
DD_DETECTOR_TYPE = GLOBALS.get("DD_DETECTOR_TYPE", "immediate")
DEEP_DETECTIONS_ZONES = GLOBALS.get("DEEP_DETECTIONS_ZONES", "")
DEEP_DETECTIONS_CONFIDENCE = GLOBALS.get("DEEP_DETECTIONS_CONFIDENCE", 95)
DEEP_DETECTIONS_MAX_PERSONS = GLOBALS.get("DEEP_DETECTIONS_MAX_PERSONS", 1)
DEEP_DETECTIONS_MAX_VEHICLE = GLOBALS.get("DEEP_DETECTIONS_MAX_VEHICLE", 0)
DEEP_DETECTIONS_MAX_BICYCLE = GLOBALS.get("DEEP_DETECTIONS_MAX_BICYCLE", 0)
DD_OBSERVATION_TIME = GLOBALS.get("DD_OBSERVATION_TIME", 10)
DD_MATCH_DETECTIONS = GLOBALS.get("DD_MATCH_DETECTIONS", 60)

# Границы для реакции
AB_DD_BORDERS = GLOBALS.get("AB_DD_BORDERS", "")
BA_DD_BORDERS = GLOBALS.get("BA_DD_BORDERS", "")
CROSS_PERSON = GLOBALS.get("CROSS_PERSON", True)
CROSS_VEHICLE = GLOBALS.get("CROSS_VEHICLE", False)
CROSS_BICYCLE = GLOBALS.get("CROSS_BICYCLE", False)

# """ Настройки детектора аруко"""
ARUCO_CODES = GLOBALS.get("ARUCO_CODES", "")
ARUCO_IGNORING_MODE = GLOBALS.get("ARUCO_IGNORING_MODE", False)

STARTUP_DELAY = GLOBALS.get("STARTUP_DELAY", 0)

VORON_PARAMETERS_TO_CODES = {
    host.tr("тревога в зоне"): [1, 2, 3, 4, 5],
    host.tr("неисправность зоны"): [255],
    host.tr("зона снята с охраны"): [-1],
    host.tr("зона поставлена на охрану"): [0],
    host.tr("ручное подтверждение тревоги"): [11, 12, 13, 14, 15],
    host.tr("автоматическое подтверждение тревоги"): [21, 22, 23, 24, 25],
}


from reactions import Reactions
from constants import EVENTS_TRANSLATION, EVENTS_TRANSLATION_REVERSED
from tbot import *


# ---------------------------------------------------------------------
# Initialization functions (new )
# ---------------------------------------------------------------------


def split_object_names(names):
    if names:
        return set(names.split(","))


def _is_channel_enabled(sett):
    info = sett.cd("info")
    if info and info["grabber_path"]:
        try:
            grabber = host.settings(info["grabber_path"])
        except KeyError:
            return False

        if grabber["grabber_enabled"]:
            n = info["grabber_channel_n"]
            return (
                grabber["channel%02d_main_enabled" % n]
                or grabber["channel%02d_ext_enabled" % n]
            )
    return False


def collect_channels_and_inputs_names_for_associations():
    """
    Collects channels and input names if script activates by
    input high to low or input low to high
    result adds to channels to work variable.

    Returns:

    """
    all_channels_names = ""
    all_inputs_names = ""

    for indx in xrange(1, 21):
        input_name = GLOBALS.get("INP_ACTIV_{indx}".format(indx=indx))
        if not input_name:
            continue
        chans_names = GLOBALS.get("INP_ACTIV_{indx}_CHAN".format(indx=indx))
        if not chans_names:
            continue
        all_channels_names = "{},{}".format(all_channels_names, chans_names)
        all_inputs_names = "{},{}".format(all_inputs_names, input_name)

    logger.debug(
        "channels for associations: %s, inputs: %s",
        all_channels_names,
        all_inputs_names,
    )

    return all_inputs_names, all_channels_names


class TRObject(py_object):
    spec_symbols = re.compile(r'[|\\/:*?"<>]')

    def __init__(self, sett):
        self.sett = sett
        self.name = self.spec_symbols.sub("", sett.name.strip())

    def __getattr__(self, name):
        return getattr(self.sett, name)


class ServerObj(TRObject):
    def __init__(self, sett):
        super(ServerObj, self).__init__(sett)

    def __repr__(self):
        return "<server: {}-{}>".format(self.name, self.guid)


class ChannelObj(TRObject):
    def __init__(self, sett, server):
        super(ChannelObj, self).__init__(sett)
        self.server = server

    def __repr__(self):
        return "<channel: {}-{}>".format(self.name, self.guid)

    @property
    def full_guid(self):
        return "{s.guid}_{s.server}".format(s=self)

    @property
    def state(self):
        return host.object(self.guid).state("motion")


class InputObj(py_object):
    def __init__(self, guid, name, device_guid):
        self.guid = guid
        self.name = name
        self.device_guid = device_guid


class OutputObj(py_object):
    def __init__(self, obj, name, guid, parent_device_guid):
        self.obj = obj
        self.name = name
        self.guid = guid
        self.parent_device_guid = parent_device_guid

    def __repr__(self):
        return "{}({})".format(self.name, self.guid)

    def set_output_high(self):
        self.obj.set_output_high()

    def set_output_low(self):
        self.obj.set_output_low()


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


def channels_generator(server_guids, channel_names=None):
    """
    Args:
        server_guids (list): list of servers guids
        channel_names (Set('name_1', 'name_2')):
    Returns: Channel

    """
    logger.debug("servers guids: %s", server_guids)
    for channel_name, channel_guid, _, server_guid in host.objects_list("Channel"):
        if channel_names and channel_name not in channel_names:
            logger.debug(
                "object name: %s not in %s, continue", channel_name, channel_names
            )
            continue

        server_guid = server_guid[0:-1]
        if server_guid not in server_guids:
            logger.debug(
                "the server (%s) of channel (%s) not belong to %s",
                server_guid,
                channel_guid,
                server_guids,
            )
            continue
        try:
            _channel_obj = host.settings(
                "/{srv}/channels/{channel}".format(
                    srv=server_guid, channel=channel_guid
                )
            )
        except EnvironmentError as err:
            logger.error(
                "Can't get settings object for channel: %s (%s), err: %s",
                channel_name,
                channel_guid,
                err,
            )
            raise EnvironmentError(
                "Can't get settings object for channel: %s (%s)"
                % (channel_name, channel_guid)
            )
        else:
            yield ChannelObj(_channel_obj, server_guid)


def input_generator(input_names=None):
    """

    Args:
        input_names (set, optional):

    Returns:
    """
    logger.debug("input_names to search: %s", input_names)
    for input_name, input_guid, _, device_guid in host.objects_list("GPIO Input"):
        if input_names and input_name not in input_names:
            continue
        yield InputObj(input_guid, input_name, device_guid)


def get_outputs(names=None):
    """

    Args:
        names (set):

    Returns:

    """
    _gpios = []
    for x in host.objects_list("GPIO Output"):
        if names and x[0] not in names:
            continue
        obj = host.object(x[1])
        if hasattr(obj, "set_output_high") and hasattr(obj, "set_output_low"):
            try:
                name = obj.name
                guid = obj.guid
            except EnvironmentError:
                raise EnvironmentError(
                    "Can't get access to %s, check script user rights" % x[0]
                )
            else:
                _gpios.append(OutputObj(obj, name, guid, x[3]))
    return _gpios


def simt_borders(names=None):
    """

    Args:
        names:

    Returns:

    """
    _borders = []
    for x in host.objects_list("SIMT Border"):
        if names and x[0] not in names:
            continue
        _borders.append(x[1])
    return _borders


class ObjectsStorage(py_object):
    def __init__(self):
        self._servers = {}
        self._channels = {}
        self._channel_by_name = {}

        self._inputs = {}
        self._input_by_name = {}
        self.all_channels_in_work = False

    @property
    def servers(self):
        return self._servers

    @servers.setter
    def servers(self, servers_names):
        duplicate_server_count = 0
        servers_count = 0

        for server in servers_generator(servers_names):
            if server.guid == "client":
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
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, channels_names):
        channels_count = 0
        for channel in channels_generator(self.servers.keys(), channels_names):
            self._channels[channel.guid] = channel
            if channel.name in self._channel_by_name:
                self._channels_with_same_name_warning(
                    self._channel_by_name.get(channel.name), channel
                )

            self._channel_by_name[channel.name] = channel
            channels_count += 1
        logger.debug("found  %s channel(-s). All channels: %s", channels_count, self._channels)

    @staticmethod
    def _channels_with_same_name_warning(channel_already_added, channel_going_to_add):
        msg = "Обнаружены каналы с одинаковыми именами {}".format(
            channel_already_added.name
        )
        logger.debug(
            "channels with same name found: %s and %s have same name: %s",
            channel_already_added.guid,
            channel_going_to_add.guid,
            channel_already_added.name,
        )
        raise ValueError(msg)

    def channel_by_name(self, channel_name):
        if not self._channel_by_name.get(channel_name):
            logger.debug("channel with name %s not found", channel_name)
            return
        return self._channel_by_name[channel_name]

    @staticmethod
    def _inputs_with_same_name_warning(input_already_added, input_going_to_add):
        try:
            device_1 = host.object(input_already_added.device_guid).name
        except EnvironmentError:
            logger.error(
                "Can't get name for device 1: %s", input_already_added.device_guid
            )
            device_1 = input_already_added.device_guid
        try:
            device_2 = host.object(input_going_to_add.device_guid).name
        except EnvironmentError:
            logger.error(
                "Can't get name for device 2: %s", input_going_to_add.device_guid
            )
            device_2 = input_going_to_add.device_guid

        # TODO: make translate
        msg = (
            "Обнаружено совпадение имён тревожных входов."
            " Устройство {} и устройство {} имеют тревожные входы"
            " с одинаковыми именами {}".format(
                device_1, device_2, input_already_added.name
            )
        )
        raise ValueError(msg)

    def inputs(self, input_names):
        for input_obj in input_generator(input_names):
            self._inputs[input_obj.guid] = input_obj.name
            if input_obj.name in self._input_by_name:
                self._inputs_with_same_name_warning(
                    self._input_by_name.get(input_obj.name), input_obj
                )

            self._input_by_name[input_obj.name] = input_obj

    def input_by_name(self, input_name):
        if not self._input_by_name.get(input_name):
            logger.warning("input with name %s not found", input_name)
            return
        return self._input_by_name[input_name]

    def search_objects(self, servers_names, channels_names):
        self.servers = servers_names
        self.channels = channels_names


def template_exists(template_name):
    """
    Check existence of alarm template
    Args:
        template_name (str):

    """

    _found_alarm_templates_guids = set()
    for sett in host.settings("templates").ls():
        if sett.name == template_name:
            _found_alarm_templates_guids.add(sett.guid)
    assert _found_alarm_templates_guids, (
        loc.main.selected_template_not_found % template_name
    )
    assert (
        len(_found_alarm_templates_guids) == 1
    ), "found several templates with the same name: {}".format(template_name)


# ---------------------------------------------------------------------
#  Initializing starts here
# ---------------------------------------------------------------------
if __name__ == host.stats().parent().guid:

    if TOKEN and host.settings("").guid == "client":
        raise RuntimeError(loc.main.alarms_can_only_be_generated_on_servers)

    STARTUP_TS = int(host.settings("health")["startup_ts"]) / 1e6
    TIMEOUT = STARTUP_DELAY - (time.time() - STARTUP_TS)
    function_by_guid = {}
    if TIMEOUT < 0:
        TIMEOUT = 0

    def start_script():
        global AM_MAX_CHANS, SAVE_BUFFER_DELAY, function_by_guid, SAME_CELL
        schedule = None
        input_filter_obj = None
        input_state_to_react = "Input High"

        if AM_SCHEDULE:
            from schedule import ScheduleObject

            schedule = ScheduleObject(AM_SCHEDULE)

        if INPUT_FILTER_REACTIONS:
            try:
                input_filter_obj = host.object(INPUT_FILTER_REACTIONS)
            except EnvironmentError:
                raise EnvironmentError(
                    loc.main.input_not_found % INPUT_FILTER_REACTIONS
                )
            if INPUT_STATE_TO_MAKE_REACTION == loc.main.opened:
                input_state_to_react = "Input Low"

            logger.debug(
                "Input state to make reaction filter: %s", input_state_to_react
            )

        reactions = Reactions(schedule, input_filter_obj, input_state_to_react)

        inputs_name_to_work = set()
        associated_channels = set()

        if INPUT_HIGH or INPUT_LOW:
            inputs_name_to_work, associated_channels = (
                collect_channels_and_inputs_names_for_associations()
            )
            inputs_name_to_work = split_object_names(inputs_name_to_work)
            associated_channels = split_object_names(associated_channels)

        servers_names = split_object_names(SERVER_CHECK_LIST)
        channels = split_object_names(CHANS_CHECK_LIST)

        if channels:
            channels = channels.union(associated_channels)

        obj_storage = ObjectsStorage()
        obj_storage.search_objects(servers_names, channels)

        if not CHANS_CHECK_LIST:
            obj_storage.all_channels_in_work = True

        if inputs_name_to_work:
            obj_storage.inputs(inputs_name_to_work)

        # -------------------------------------------------------
        #                   Reactions
        # -------------------------------------------------------
        # 1. Show channel in Alarm Monitor
        # -------------------------------------------------------

        if SHOW_CHAN:
            from reactions import AlarmMonitorManager

            all_displays = []
            if AM_MON_1:
                if AM_MON_1 > 3:
                    raise ValueError(host.tr("Display number can't be greater than 3"))
                all_displays.append(AM_MON_1)
            if AM_MON_2:
                if AM_MON_2 > 3:
                    raise ValueError(host.tr("Display number can't be greater than 3"))
                if AM_MON_2 in all_displays:
                    raise ValueError("Display number can't repeat: %s", AM_MON_2)
                all_displays.append(AM_MON_2)
            if AM_MON_3:
                if AM_MON_3 > 3:
                    raise ValueError(host.tr("Display number can't be greater than 3"))
                if AM_MON_3 in all_displays:
                    raise ValueError("Display number can't repeat: %s", AM_MON_3)
                all_displays.append(AM_MON_3)

            assert all_displays, host.tr("at least one display must be chosen")
            assert AM_ALARM_TEMPLATE, loc.main.choose_alarm_template

            template_exists(AM_ALARM_TEMPLATE)

            if AM_TYPE == loc.main.am_playback_archive:
                am_type = 2
                AM_MAX_CHANS = 1
                SAME_CELL = None
            else:
                am_type = 1

            logger.debug("am_type is %s. 1 - show online, 2 - show archive", am_type)

            if SAME_CELL:
                channels_quantity = len(obj_storage.channels)
                logger.debug(
                    "same cell is True, channels quantity is: %s", channels_quantity
                )
                host.alert(
                    "same cell is True, quantity channels found for work: %s",
                    channels_quantity,
                )

                assert len(all_displays) * AM_MAX_CHANS >= channels_quantity, \
                    "Channels quantity is greater than max channels possible to show"
                channels_for_same_cell = obj_storage.channels
            else:
                channels_for_same_cell = None

            am_manager = AlarmMonitorManager(
                AM_ALARM_TEMPLATE,
                am_type,
                AM_MAX_CHANS,
                display_duration=AM_DISPLAY_DURATION,
                base_template=AM_BASE_TEMPLATE,
                no_motion_check=AM_NO_MOTION_CHECK,
                delay_before_assign=1500,
                channels_for_same_cell=channels_for_same_cell,
                all_displays=all_displays,
            )

            reactions.add_executor(am_manager)

            if AM_CHANGE_TEMPLATE_CHECK:
                logger.debug("Drop template enabled")
                host.activate_on_gui_event("", am_manager.drop_template)

        # -------------------------------------------------------
        # 2. Send SMS
        # -------------------------------------------------------

        if SEND_SMS:
            from reactions import SMSCSender, SMSSendText

            assert SMSC_LOGIN, host.tr("Enter smsc login")
            assert SMSC_PASSWORD, host.tr("Enter smsc password")
            assert PHONE_NUMB, host.tr("Enter phone number")
            sms_sender = SMSCSender(SMSC_LOGIN, SMSC_PASSWORD, PHONE_NUMB)
            reactions.add_executor(SMSSendText(sms_sender))

        # -------------------------------------------------------
        # 3. Show message
        # -------------------------------------------------------
        if SHOW_MESSAGE:
            from reactions import ShowMessage

            reactions.add_executor(ShowMessage(show_message_delay=SHOW_MESSAGE_DELAY))

        # -------------------------------------------------------
        # 4. Play sound
        # -------------------------------------------------------
        if PLAY_SOUND:
            from reactions import PlaySound

            reactions.add_executor(PlaySound(CUSTOM_SOUND_PATH or SOUND_NAME))

        # -------------------------------------------------------
        # 5. Show POPUP window
        # -------------------------------------------------------
        if SHOW_POPUP:
            from reactions import ShowPopup

            reactions.add_executor(
                ShowPopup(
                    monitor_to_show_archive_from_popup=MON_POPUP,
                    display_duration=POPUP_DURATION,
                )
            )

        # -------------------------------------------------------
        # 6. Make reaction with output
        # -------------------------------------------------------

        if OUTPUT_ON:
            if OUTPUT_ALGORITHM == "type_1":
                from reactions import OutputReactions
            else:
                from reactions import OutputReactionsII as OutputReactions

            assert OUTPUTS, loc.main.outputs_selection_required
            _outputs = get_outputs(split_object_names(OUTPUTS))

            out_reactions = OutputReactions(
                gpios=_outputs, delay=OUTPUT_DELAY, reaction_type=OUTPUT_ACTION_TYPE
            )
            reactions.add_executor(out_reactions)
            if OUTPUT_MAN_ACTIV:
                host.activate_on_shortcut(
                    OUTPUT_MAN_ACTIV, out_reactions.manual_activation_of_outputs
                )

        # -------------------------------------------------------
        # 7. Operations with physical system control ("СКУД")
        # -------------------------------------------------------
        if ACS_ENBL:
            from reactions import AccessControlOperations

            assert ACS_DOOR, loc.main.pacs_name_required
            acs_door_obj = host.object(ACS_DOOR)

            if ACS_TYPE == "Sigur":
                assert hasattr(
                    acs_door_obj, "workmode_alwaysopen"
                ), "{} is not Sigur access point. Only one access point can be specified".format(
                    ACS_DOOR
                )
            elif ACS_TYPE == "Orion":
                assert hasattr(
                    acs_door_obj, "grant_access_once"
                ), "{} is not Orion access point. Only one access point can be specified".format(
                    ACS_DOOR
                )
            elif ACS_TYPE == "Hikvision":
                assert hasattr(
                    acs_door_obj, "permanently_open_door"
                ), "{} is not Hikvision access point. Only one access point can be specified".format(
                    ACS_DOOR
                )
            else:
                raise ValueError("ACS_TYPE must be Sigur, Orion or Hikvision")

            if ACS_LOGIC not in [
                loc.main.pacs_open_the_door,
                loc.main.pacs_close_the_door,
            ]:
                raise ValueError(
                    loc.main.wrong_type_of_work_assertion
                    % (loc.main.pacs_open_the_door, loc.main.pacs_close_the_door)
                )

            if not 1 < ACS_DELAY < 3600:
                raise ValueError(loc.main.wrong_time_of_door_open_close)
            acs = AccessControlOperations(
                access_point_name=ACS_DOOR,
                access_point_type=ACS_TYPE,
                operation_type=ACS_LOGIC,
                delay_operations=ACS_DELAY,
            )
            reactions.add_executor(acs)
            if ACS_MAN_ACTIV:
                host.activate_on_shortcut(ACS_MAN_ACTIV, acs.manual_execute)

        # -------------------------------------------------------
        # 8. Send SIP code
        # -------------------------------------------------------
        if SEND_SIP_CODE_ENBL:
            if host.settings("").guid == "client":
                raise ValueError(loc.main.sip_code_sent_on_the_server)

            assert SIP_NUMBER, loc.main.specify_sip_number
            assert SIP_CODE, loc.main.specify_sip_code

        # ----------------------------------------------------
        # 9 Push alarm
        # ____________________________________________________
        if TOKEN and not ADD_SCREEN_TO_ALARM:
            from reactions import FireAlarmExecutor

            fae = FireAlarmExecutor(TOKEN, ADD_VIDEO_TO_ALARM, obj_storage)
            reactions.add_executor(fae)

        # -------------------------------------------------------
        # Al screenshot_senders_adopters
        # -------------------------------------------------------
        ALL_SENDERS = []

        # -------------------------------------------------------
        # Initializing email sender
        # -------------------------------------------------------
        if SEND_SCREEN_EMAIL or SEND_EMAIL:
            from reactions import AdoptedEmailSender
            from email_sender import EmailSender

            assert EMAIL_ACCOUNT, loc.main.trassir_email_account_not_found
            assert EMAIL_ADDRESSES, loc.main.specify_email_recipients
            mail_sender = EmailSender(EMAIL_ACCOUNT)
            if SEND_SCREEN_EMAIL:
                ALL_SENDERS.append(
                    AdoptedEmailSender(
                        mail_sender=mail_sender, email_recipients=EMAIL_ADDRESSES
                    )
                )
            else:
                from reactions import MailTextSender

                reactions.add_executor(MailTextSender(mail_sender, EMAIL_ADDRESSES))

        # -------------------------------------------------------
        # Initializing Telegram sender
        # -------------------------------------------------------
        if SEND_SCREEN_TELEGRAM:
            assert TG_IDS, host.tr("No telegram user id")
            from reactions import AdoptedTelegramSender

            opener = None

            if TG_PROXY:
                import ssl
                import urllib2

                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE

                https_handler_ = urllib2.HTTPSHandler(context=context)
                proxy_handler_ = urllib2.ProxyHandler({"https": TG_PROXY})

                opener = urllib2.build_opener(proxy_handler_, https_handler_)

            host.exec_encoded(tbot_service)
            tbot_api = TBotAPI(opener=opener)
            telegram_users = tbot_api.prepare_users(TG_IDS)
            ALL_SENDERS.append(AdoptedTelegramSender(tbot_api, telegram_users))

        # -------------------------------------------------------
        # Initializing FTP sender
        # -------------------------------------------------------
        if SEND_FTP:
            from ftp import FTPClient
            from reactions import AdoptedFTPSender

            ftp_c = FTPClient(
                FTP_HOST,
                FTP_PORT,
                FTP_USER,
                FTP_PASSWD,
                FTP_PATH,
                passive_mode=FTP_PASSIVE_MODE,
            )
            ALL_SENDERS.append(AdoptedFTPSender(ftp_c))

        # -------------------------------------------------------
        # Fire Alarm
        # -------------------------------------------------------
        if TOKEN and ADD_SCREEN_TO_ALARM:
            from reactions import FireAlarm

            ALL_SENDERS.append(FireAlarm(TOKEN, ADD_VIDEO_TO_ALARM))

        # -------------------------------------------------------
        # Reactions with screenshots add here
        # -------------------------------------------------------

        _clear_folder_name = re.compile(r"[\/:*?\"<>|]")

        if FOLDER_NAME == "default" or not FOLDER_NAME:
            folder_name = "AlarmMonitor_{script_guid}".format(
                script_guid=host.stats().parent().guid
            )
        else:
            folder_name = _clear_folder_name.sub("_", FOLDER_NAME)

        BASE_SCREENSHOT_FOLDER = os.path.normpath(
            os.path.join(
                host.settings("system_wide_options")["screenshots_folder"], folder_name
            )
        )

        if (
            SEND_SCREEN_EMAIL
            or SEND_FTP
            or SAVE_SCREEN
            or SEND_SCREEN_TELEGRAM
            or (TOKEN and ADD_SCREEN_TO_ALARM)
        ):
            from shot_saver import ShotSaver
            from reactions import ReactionsWithScreenshots
            from reactions import ShotSpamFilter

            shot_spam_filter = None
            if SHOT_SPAM_PERIOD:
                shot_spam_filter = ShotSpamFilter(SHOT_SPAM_PERIOD)

            if SAVE_SCREEN_DELTA > 0:
                SAVE_BUFFER_DELAY = SAVE_SCREEN_DELTA / 1e3 + SAVE_BUFFER_DELAY

            assert (
                -7000 <= SAVE_SCREEN_DELTA <= 7000
            ), "save_screen_delta should be in [-7000, 7000]"
            reactions_with_screenshots = ReactionsWithScreenshots(
                delta=SAVE_SCREEN_DELTA,
                base_folder=BASE_SCREENSHOT_FOLDER,
                online_shot=ONLINE_SHOT,
                save_screen=SAVE_SCREEN,
                figures=FIGURES,
            )
            shot_saver_obj = ShotSaver()
            shot_saver_obj.max_tries = 4
            shot_saver_obj.buffer_ts = SAVE_BUFFER_DELAY
            reactions_with_screenshots.shot_saver_obj = shot_saver_obj
            reactions_with_screenshots.save_substream = SUBSTREAM_SHOT
            reactions_with_screenshots.shot_spam_filter = shot_spam_filter
            for sender in ALL_SENDERS:
                reactions_with_screenshots.add_sender(sender=sender)

            reactions.add_executor(reactions_with_screenshots)

            from delete_old_shots import Worker

            if DAYS_TO_STORE:
                shot_cleaner = Worker(BASE_SCREENSHOT_FOLDER, DAYS_TO_STORE)
                shot_cleaner.run()

        # -------------------------------------------------------
        # Add handlers below
        # ------------------------------------------------------
        simple_events_handler = None

        # ----------------------------------------------------------------------
        # 1. Simple events handler
        # ----------------------------------------------------------------------
        if any(
            [
                MOTION_ALARM,
                SOUND_ALARM,
                FIRE_ALARM,
                FIRE_STOPPED_ALARM,
                FACE_DETECTOR_ENABLE,
                CROSSLINE_ALARM,
                INTRUSION_ALARM,
                LEFT_OBJ_ALARM,
                SABOTAGE_ALARM,
                SCRIPT_NO_HELMET,
                SCRIPT_NO_UNIFORM,
                WARNING_TERMAL_SIGNAL,
                SCRIPT_AU,
                PEOPLE_DETECTED,
                NO_MASK_DETECTION,
                DISTANCE_VIOLATION,
                SIGNAL_LOST,
                SIGNAL_RESTORED,
                SUSPICIOUS_POSE,
            ]
        ):
            from event_handlers import SimpleEventsHandler

            simple_events_handler = SimpleEventsHandler(
                obj_storage, reactions.make_reactions
            )

            if MOTION_ALARM:
                host.activate_on_events(
                    "Motion Start", "", simple_events_handler.event_handler
                )
            if SOUND_ALARM:
                host.activate_on_events(
                    "Sound Detected", "", simple_events_handler.event_handler
                )
            if FIRE_ALARM:
                host.activate_on_events(
                    "Smoke Detected", "", simple_events_handler.event_handler
                )
                host.activate_on_events(
                    "Fire Detected", "", simple_events_handler.event_handler
                )
            if FIRE_STOPPED_ALARM:
                host.activate_on_events(
                    "Fire Stopped", "", simple_events_handler.event_handler
                )
            if FACE_DETECTOR_ENABLE:
                host.activate_on_events(
                    "Face Detected", "", simple_events_handler.event_handler
                )
            if CROSSLINE_ALARM:
                host.activate_on_events(
                    "CrossLine Detected", "", simple_events_handler.event_handler
                )
            if INTRUSION_ALARM:
                host.activate_on_events(
                    "Intrusion Detected", "", simple_events_handler.event_handler
                )

            if LEFT_OBJ_ALARM:
                host.activate_on_events(
                    "Left Object Detected", "", simple_events_handler.event_handler
                )
                host.activate_on_events(
                    "Item Abandoned", "", simple_events_handler.event_handler
                )
                host.activate_on_events(
                    "Item Missing", "", simple_events_handler.event_handler
                )
                host.activate_on_events(
                    "Slow Down Detected", "", simple_events_handler.event_handler
                )

            if SABOTAGE_ALARM:
                host.activate_on_events(
                    "Tamper Alert", "", simple_events_handler.event_handler
                )
                host.activate_on_events(
                    "Tamper Alert: Defocus", "", simple_events_handler.event_handler
                )
                host.activate_on_events(
                    "Tamper Alert: Covered", "", simple_events_handler.event_handler
                )
                host.activate_on_events(
                    "Tamper Alert: Flashlight", "", simple_events_handler.event_handler
                )
                host.activate_on_events(
                    "Tamper Alert: Shift", "", simple_events_handler.event_handler
                )

            if WARNING_TERMAL_SIGNAL:
                host.activate_on_events(
                    "Warning: Thermal Signal", "", simple_events_handler.event_handler
                )

            if SIGNAL_LOST:
                host.activate_on_events(
                    "Signal Lost", "", simple_events_handler.event_handler
                )

            if SIGNAL_RESTORED:
                host.activate_on_events(
                    "Signal Restored", "", simple_events_handler.event_handler
                )

        # ----------------------------------------------------------------------
        # 2. Fired events prehandler
        # ----------------------------------------------------------------------

        script_event_types = {}

        if SCRIPT_NO_HELMET:
            script_event_types[
                "without helmet detected"
            ] = "Person without helmet detected"

        if SCRIPT_NO_UNIFORM:
            script_event_types[
                "without uniform detected"
            ] = "Person without uniform detected"

        if SCRIPT_AU:
            script_event_types["plate detected"] = "Plate detected"

        if NO_MASK_DETECTION:
            script_event_types["without mask"] = "Person without mask found"

        if DISTANCE_VIOLATION:
            script_event_types[
                "distance violation"
            ] = "Social distance violation detected"

        if VORON:
            script_event_types["VORON"] = "Voron event"

        if SUSPICIOUS_POSE:
            script_event_types["Позы"] = "Suspicious pose"

        if script_event_types:
            logger.debug("script event types to work: %s", script_event_types)

            def script_event_handler(ev):
                logger.debug("FIRE EVENT: %s %s %s", ev.p1, ev.p2, ev.data)
                if not ev.p2:
                    logger.debug("No channel in Script event")

                try:
                    ev_data = json.loads(getattr(ev, "data", "{}"))
                    _event_type = ev_data.get("event_type")
                    time_best_view = ev_data.get("ts")
                except ValueError:
                    _event_type = ""
                    time_best_view = None

                if _event_type == "VORON" and _event_type in script_event_types:
                    voron.event_handler(ev)
                    return

                for key, ev_type in script_event_types.iteritems():
                    logger.debug(
                        "key (%s) in ev.p1 (%s), res: %s", key, ev.p1, key in ev.p1
                    )
                    if key in ev.p1 and simple_events_handler:
                        ev.type = ev_type
                        ev.origin = ev.p2
                        if key == "plate detected" and time_best_view:
                            ev.ts = time_best_view
                        simple_events_handler.event_handler(ev)
                        break

            host.activate_on_events("Script: %1", "", script_event_handler)

        # ----------------------------------------------------------------------
        # 3. Face recognizer handler
        # ----------------------------------------------------------------------
        if FR_ENABLE:
            from event_handlers import FaceRecognizerHandler
            from event_handlers import check_fr_master_guid
            from event_handlers import get_folders

            if FR_ALARM_TYPE not in [
                loc.main.fr_type_work_group,
                loc.main.fr_type_work_person,
                loc.main.fr_type_work_any,
                loc.main.fr_type_work_person,
                loc.main.fr_type_work_unrecognized,
            ]:
                raise ValueError(loc.fr.alarm_type_for_fr_activation_is_wrong)
            logger.info("face recognizer handler reaction type is: %s", FR_ALARM_TYPE)

            # Каналы с распознавателем лиц берем из "Каналы в работе"
            assert (
                obj_storage.channels and CHANS_CHECK_LIST
            ), loc.main.specify_channels_with_face_recognition

            assert FR_SERV, loc.main.select_server_with_persons_db

            check_fr_master_guid(FR_SERV)  # harvesting stats
            fr = FaceRecognizerHandler(
                fr_server=FR_SERV,
                obj_storage=obj_storage,
                callback=reactions.make_reactions,
                same_event_ignoring=FR_SAME_EVENT_IGNORING,
            )
            fr_min_score = int(FR_MIN_SCORE) * 100

            if FR_ALARM_TYPE == loc.main.fr_type_work_group:
                from event_handlers.face_recognizer import Group

                assert (
                    FR_ALARM_GROUP
                ), loc.main.fr_group_not_specified  # host.tr("Группа не выбрана")
                folders_names = [x.strip() for x in FR_ALARM_GROUP.split(",")]

                folders_dict = get_folders(FR_SERV, folders_names)
                assert folders_dict, loc.main.fr_group_not_found % FR_ALARM_GROUP
                fr.add_fr_filter(Group(fr_folders=folders_dict, min_score=fr_min_score))

            elif FR_ALARM_TYPE == loc.main.fr_type_work_person:
                from event_handlers.face_recognizer import Person

                assert FR_ALARM_NAME, loc.main.fr_person_not_specified
                alarm_persons = [x.strip() for x in FR_ALARM_NAME.split(",")]
                fr.add_fr_filter(
                    Person(alarm_persons=alarm_persons, min_score=fr_min_score)
                )

            elif FR_ALARM_TYPE == loc.main.fr_type_work_unrecognized:
                from event_handlers.face_recognizer import Unrecognized

                fr.add_fr_filter(Unrecognized(min_score=fr_min_score))

            elif FR_ALARM_TYPE == loc.main.fr_type_work_any:
                from event_handlers.face_recognizer import AnyFace

                fr.add_fr_filter(AnyFace(min_score=fr_min_score))
            else:
                raise ValueError("Face recognizer filter not added.")

            host.activate_on_events("Face Recognized", "", fr.event_handler)

        # ----------------------------------------------------------------------
        # 4. SIMT events handler
        # ----------------------------------------------------------------------
        simt_events = [
            "Object Track Length Alarm",
            "Object Size Alarm",
            "Object Speed Alarm",
            "Object Entered the Zone",
            "Object Left the Zone",
            "Object presence alarm",
            "Border Crossed A -> B",
            "Border Crossed B -> A",
        ]

        if SIMT_ALARM_ENABLE:
            from event_handlers import SimtHandler

            simt_borders_guid_list = None
            if SIMT_BORDER_ALARM:
                simt_borders_guid_list = simt_borders(
                    split_object_names(SIMT_BORDER_ALARM)
                )
                logger.debug(
                    "SIMT borders guids found: %s, for borders names: %s",
                    simt_borders_guid_list,
                    SIMT_BORDER_ALARM,
                )
                assert simt_borders_guid_list, "SIMT borders not found"

            simt_handler = SimtHandler(
                obj_storage=obj_storage,
                simt_borders_guid_list=simt_borders_guid_list,
                border_alarm_dir=SIMT_BORDER_ALARM_DIR,
                size_alarm=SIMT_SIZE_ALARM,
                speed_alarm=SIMT_SPEED_ALARM,
                length_alarm=SIMT_LENGTH_ALARM,
                presence_check=SIMT_PRESENCE_CHECK,
                presence_delay=SIMT_PRESENCE_DELAY,
                events_translation=EVENTS_TRANSLATION,
                callback=reactions.make_reactions,
                similar_events_delay=SIMT_SIMILAR_EVENTS_DELAY,
            )

            simt_handler.zones_check_enter_names = SIMT_ENTER_ALARM
            simt_handler.zones_check_leave_names = SIMT_LEAVE_ALARM
            simt_handler.zones_check_names = SIMT_CHECK_ZONES
            simt_handler.check_zones_with_objects_presence()

            for event_type in simt_events:
                host.activate_on_events(event_type, "", simt_handler.event_handler)

        # ----------------------------------------------------------------------
        # 5. Neuro detections handler
        # ----------------------------------------------------------------------
        observable_types = OrderedDict(
            {
                "person": DEEP_DETECTIONS_MAX_PERSONS,
                "head": DEEP_DETECTIONS_MAX_PERSONS,
                "bicycle": DEEP_DETECTIONS_MAX_BICYCLE,
                "vehicle": DEEP_DETECTIONS_MAX_VEHICLE,
            }
        )

        if DD_OBJECT_IN_ZONE or DD_CROSS_BORDER:
            from event_handlers import SameEvent

        # ----------------------------------
        # Обнаружение пересечения границы
        # ----------------------------------
        cross_line_detector = None
        if DD_CROSS_BORDER:
            assert AB_DD_BORDERS or BA_DD_BORDERS, loc.main.specify_borders_names

            cross_observable_types = []
            if CROSS_PERSON:
                cross_observable_types.append("person")
                cross_observable_types.append("head")
            if CROSS_VEHICLE:
                cross_observable_types.append("vehicle")
            if CROSS_BICYCLE:
                cross_observable_types.append("bicycle")

            from event_handlers import CrossLineDetector

            cross_line_detector = CrossLineDetector(
                obj_storage,
                AB_DD_BORDERS,
                BA_DD_BORDERS,
                cross_observable_types,
                SameEvent(DD_SAME_EVENT_IGNORING),
                callback=reactions.make_reactions,
            )

        # ----------------------------------
        # Обнаружение объекта в зоне
        # ----------------------------------
        zone_detector = None
        if DD_OBJECT_IN_ZONE:
            assert DEEP_DETECTIONS_ZONES, loc.main.specify_zones_names
            zone_names = DEEP_DETECTIONS_ZONES.split(",")

            if DD_DETECTOR_TYPE == loc.main.long_lasting:
                from event_handlers import LongPresence

                zone_detector = LongPresence(
                    obj_storage,
                    zone_names,
                    DEEP_DETECTIONS_CONFIDENCE,
                    observable_types,
                    observation_duration=DD_OBSERVATION_TIME,
                    match_level=DD_MATCH_DETECTIONS,
                    same_event_filter=SameEvent(DD_SAME_EVENT_IGNORING),
                    callback=reactions.make_reactions,
                )

            else:
                from event_handlers import ObjectsInZoneDetector

                zone_detector = ObjectsInZoneDetector(
                    obj_storage,
                    zone_names,
                    DEEP_DETECTIONS_CONFIDENCE,
                    observable_types,
                    SameEvent(DD_SAME_EVENT_IGNORING),
                    callback=reactions.make_reactions,
                )

        if DD_CROSS_BORDER or DD_OBJECT_IN_ZONE:
            from event_handlers import DeepDetections

            dd = DeepDetections(obj_storage, zone_detector, cross_line_detector)
            host.activate_on_deep_detection_events(dd.event_handler)

        # ----------------------------------------------------------------------
        # 5. Sigur events handler
        # ----------------------------------------------------------------------

        SIGUR_EVENTS = [
            "Deny: %1 (%2)",
            "Allow: %1 (%2)",
            "Pass: %1 (%2)",
            "Access Point Disconnected",
            "Access Point Connected",
            "Access Point Once Opened",
            "Access Point: %1",
            "Alarm: %1 (%2)",
            "Access Point Closed To All",
            "Access Point Opened To All",
            "Access Point Allows By Key",
        ]

        if SIGUR_ENABLE:
            from event_handlers import SigurEventsHandler

            sigur_events_handler = SigurEventsHandler(
                obj_storage,
                split_object_names(SIGUR_ALARM_NODES),
                callback=reactions.make_reactions,
            )

            if SIGUR_EVENT_REACTION_ALL:
                for event_reaction in SIGUR_EVENTS:
                    host.activate_on_events(
                        event_reaction, "", sigur_events_handler.event_handler
                    )
            else:
                sigur_event_reaction_list = [
                    SIGUR_EVENT_REACTION_1,
                    SIGUR_EVENT_REACTION_2,
                    SIGUR_EVENT_REACTION_3,
                    SIGUR_EVENT_REACTION_4,
                    SIGUR_EVENT_REACTION_5,
                ]

                for event_reaction in sigur_event_reaction_list:
                    if event_reaction != "no" and event_reaction:
                        _event = EVENTS_TRANSLATION_REVERSED[event_reaction]
                        host.activate_on_events(
                            _event, "", sigur_events_handler.event_handler
                        )

        # ----------------------------------------------------------------------
        # 6. Orion events handler
        # ----------------------------------------------------------------------

        ORION_EVENTS = [
            "Intrusion Alert",
            "Fire",
            "Allowed Access By Key",
            "Door Restored",
            "Door Broken",
            "Door Blocked",
            "No Access To All",
            "Access Denied %1",
            "Access Granted %1",
            "No Access %1",
            "Reader Contact Lost",
            "Walk Detected",
            "Free Walk Allowed",
            "Armed",
            "Orion Disconnected",
        ]

        if ORION_ENABLE:
            from event_handlers import OrionEventsHandler

            orion_events_handler = OrionEventsHandler(
                obj_storage,
                split_object_names(ORION_ALARM_NODES),
                callback=reactions.make_reactions,
            )
            if ORION_EVENT_REACTION_ALL:
                for event_reaction in ORION_EVENTS:
                    host.activate_on_events(
                        event_reaction, "", orion_events_handler.event_handler
                    )
            else:
                orion_event_reaction_list = [
                    ORION_EVENT_REACTION_1,
                    ORION_EVENT_REACTION_2,
                    ORION_EVENT_REACTION_3,
                    ORION_EVENT_REACTION_4,
                    ORION_EVENT_REACTION_5,
                ]

                for event_reaction in orion_event_reaction_list:
                    if event_reaction != loc.main.no and event_reaction:
                        _event = EVENTS_TRANSLATION_REVERSED[event_reaction]
                        host.activate_on_events(
                            _event, "", orion_events_handler.event_handler
                        )

        # ----------------------------------------------------------------------
        # 7. Input state change handler
        # ----------------------------------------------------------------------

        def input_events_handler(event):
            """
            function_by_guid (dict): key is guid of input (GPIO),
                                     value (tuple): (input trassir object, )

            Args:
                event (obj):

            Returns:

            """
            global function_by_guid
            logger.debug(
                "Input event: %s, input guid: %s, isinstance_by_gpio: %s",
                event.type,
                event.origin,
                function_by_guid,
            )

            if not function_by_guid.get(event.origin):
                return
            if gpio_handler is None:
                return

            input_obj, channels_objs = function_by_guid.get(event.origin)
            gpio_handler.event_handler(
                input_obj, channels_objs, event.type, event.origin
            )

        def all_channels_by_names(all_names):
            """

            Args:
                all_names (str):

            Returns:

            """
            all_names = split_object_names(all_names)
            return [
                obj_storage.channel_by_name(x)
                for x in all_names
                if obj_storage.channel_by_name(x)
            ]

        if INPUT_HIGH or INPUT_LOW:

            from event_handlers import InputStateChangeHandler

            gpio_handler = InputStateChangeHandler(
                EVENTS_TRANSLATION, INPUT_LOW, INPUT_HIGH, reactions.make_reactions
            )

            for indx in xrange(1, 21):
                input_name = GLOBALS.get("INP_ACTIV_{indx}".format(indx=indx))
                if not input_name:
                    continue
                chans_names = GLOBALS.get("INP_ACTIV_{indx}_CHAN".format(indx=indx))
                if not chans_names:
                    continue

                _channels = all_channels_by_names(chans_names)
                input_obj = obj_storage.input_by_name(input_name)

                function_by_guid[input_obj.guid] = (input_obj, _channels)

            logger.debug("Associations count: %s", len(function_by_guid))

            host.activate_on_events("Input High to Low", "", input_events_handler)
            host.activate_on_events("Input Low to High", "", input_events_handler)

        # ----------------------------------------------------------------------
        # 8. Gate (physical access control system events) handler
        # ----------------------------------------------------------------------
        GATE_EVENTS = [
            "Legal card authentication passed: %1",
            "Controller Disconnected",
            "Controller Connected",
            "Controller: %1",
            "Invalid card: %1",
            "Controller Alarm: %1",
        ]

        if GATE_PACS_EVENT:
            from event_handlers import GatePacs

            gate_pacs = GatePacs(obj_storage, reactions.make_reactions)

            def gate_controller_event_handler(ev):
                if ev.type == "Controller: %1":
                    if all(
                        [
                            ev.p1.startswith("Ключ найден"),
                            GATE_SUB_EVENT in ["Ключ найден", "любое"],
                        ]
                    ):
                        gate_pacs.event_handler(ev)
                    elif all(
                        [
                            ev.p1.startswith("Проход состоялся"),
                            GATE_SUB_EVENT in ["Проход состоялся", "любое"],
                        ]
                    ):
                        gate_pacs.event_handler(ev)
                    else:
                        logger.warning(
                            "Unhandled event for 'Controller: %%1', p1: %s", ev.p1
                        )
                else:
                    gate_pacs.event_handler(ev)

            if GATE_EVENT_REACTION_ALL:
                gate_events = GATE_EVENTS
            else:
                gate_events = [
                    x
                    for x in [
                        GATE_EVENT_REACTION_1,
                        GATE_EVENT_REACTION_2,
                        GATE_EVENT_REACTION_3,
                    ]
                    if x and x != loc.main.no
                ]
                assert gate_events, loc.main.at_least_one_event_gate

            for g_event in gate_events:
                host.activate_on_events(g_event, "", gate_controller_event_handler)

        # ----------------------------------------------------------------------
        # 9. Aruco handler
        # ----------------------------------------------------------------------
        if ARUCO_ENTERED or ARUCO_LEFT:
            assert ARUCO_CODES, loc.main.specify_aruco_codes
            aruco_codes = [i.strip() for i in ARUCO_CODES.split(",")]
            from event_handlers import ArucoEventsHandler

            aeh = ArucoEventsHandler(
                obj_storage,
                aruco_codes,
                ARUCO_IGNORING_MODE,
                ARUCO_ENTERED,
                ARUCO_LEFT,
                reactions.make_reactions,
            )
            if ARUCO_ENTERED:
                host.activate_on_events(
                    "Aruco %1 Entered Zone %2", "", aeh.event_handler
                )
            if ARUCO_LEFT:
                host.activate_on_events("Aruco %1 Left Zone %2", "", aeh.event_handler)

        # ----------------------------------------------------------------------
        # 10. Voron handler
        # ----------------------------------------------------------------------
        if VORON:
            from event_handlers import VoronEventsHandler

            def get_voron_codes_to_work_from_parameters():
                selected_codes = set()
                _selected_parameters = [
                    x
                    for x in [
                        VORON_EVENT_REACTION_1,
                        VORON_EVENT_REACTION_2,
                        VORON_EVENT_REACTION_3,
                        VORON_EVENT_REACTION_4,
                        VORON_EVENT_REACTION_5,
                        VORON_EVENT_REACTION_6,
                    ]
                    if x and x != loc.main.no
                ]
                assert (
                    _selected_parameters
                ), "Ни одного типа события для реакции не выбрано!"
                for param in _selected_parameters:
                    codes_list = VORON_PARAMETERS_TO_CODES.get(param)
                    if not codes_list:
                        raise ValueError(
                            "Can't get code list for parameter: %s" % param
                        )
                    for code in VORON_PARAMETERS_TO_CODES[param]:
                        selected_codes.add(code)
                logger.debug("Voron codes to react: %s", selected_codes)
                return selected_codes

            codes = get_voron_codes_to_work_from_parameters()
            voron = VoronEventsHandler(codes, obj_storage, reactions.make_reactions)

    host.timeout(TIMEOUT * 1000, start_script)
