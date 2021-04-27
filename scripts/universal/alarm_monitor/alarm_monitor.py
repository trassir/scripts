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
