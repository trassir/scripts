# -*- coding: utf-8 -*-

from .translation_base import Translated


class Main(Translated):

    script_name = "AlarmMonitor"
    # handlers
    alarm_types = '""" Alarm types """'
    motion_alarm = "Motion detection alarm"
    crossing_line_alarm = "Crossing of line detection alarm (SMART event from camera)"
    intrusion_alarm = "Intrusion detection alarm (SMART event from camera)"
    people_detected = "People detected (SMART event from camera)"
    sound_alarm = "Sound detection alarm"
    fire_alarm = "Fire or smoke appears"
    fire_stopped_alarm = "Fire or smoke went out"
    left_object_alarm = "Item abandoned alarm"
    sabotage_alarm = "Sabotage alarm"
    orion_events_alarm = "Orion events alarm"
    sigur_events_alarm = "Sigur events alarm"
    face_recognition_alarm = "Face recognition alarm"
    face_detection_alarm = "Face detection alarm"
    simt_detector_alarm = "SIMT detector alarm"
    input_low_to_high = "Input low to high alarm"
    input_high_to_low = "Input high to low alarm"
    object_appearance_neuro_zone = "The appearance of an object in the neuro zone"
    border_crossing_neuro = "Neuro border crossing"
    no_helmet_detection = "Person without helmet"
    script_no_uniform = "Person without uniform"
    person_with_fever = "Person with fever"
    script_auto_universal = "Auto universal events"
    gate_pacs_events = "Gate PACS events"
    aruco_appeared = "Aruco appeared"
    aruco_disappeared = "Aruco disappeared"
    voron_events = "Voron events"
    person_without_mask = "Person without a mask"
    distance_violation = "Distance violation"
    add_an_image_to_the_alarm_content = "Add an image to the alarm content"
    add_a_video_to_the_alarm_content = "Add a video to the alarm content"


    reactions = '""" Reactions for events """'
    show_channel = "Show channel with alarm"
    save_screen = "Save screenshot in screenshot folder"
    send_ftp = "Send screen to FTP"
    send_screen_email = "Send screen to e-mail"
    send_screen_telegram = "Send screen to Telegram (only on server)"
    send_email_notification = "Send notification to e-mail"
    send_sms = "Send SMS notification"
    show_message = "Show text message"
    show_message_duration = "Text message showing duration(sec)"
    sound_notification = "Sound notification"
    sound_name = "Sound file name"
    custom_sound_path = "Custom sound path (.wav)"
    show_popup = "Show pop-up"
    mon_no_for_popup = "Display number to show pop-up"
    popup_duration = "Popup duration"
    output_on = "Make operations with outputs"
    acs_enable = "Make operations with PACS"
    send_sip_code_enable = "Send code to SIP (server only)"
    sip_number = "SIP number"
    sip_code = "SIP code"
    token_send = "Send cloud alarm by token"

    optional_settings = '""" Optional settings """'
    working_servers = "Working servers"
    channels_check_list = "Working channels"
    shot_folder_name = "Folder name for saving shots"
    save_screen_delta = "Shot time correction ('-' - before, '+' - after)(ms)"
    save_buffer_delay = "Buffering time before saving a shot (sec)"
    online_shot = "Online shot"
    figures_enable = "Shots with figures"
    substream_shots = "Screenshot of the sub-stream (experimental)"
    shot_spam_period = "Only one screenshot per period (sec)"
    shot_storage_time = "Shot storage time (days)"
    am_schedule = "Schedule for running the script"
    alarm_input_filter = "Alarm input for running the script (optional)"
    input_state_to_make_reaction = "Input state to make reaction"
    start_delay = "Delay the start of the script"

    email_settings = '""" E-mail settings """'
    email_account = "E-mail account, created in Trassir"
    email_addresses = "Mail recipient list separated by comma"
    tg_ids = "User Telegram id"
    ftr_settings = '""" FTP settings """'
    ftp_host = "FTP host"
    ftp_port = "FTP port"
    ftp_user = "FTP user"
    ftp_password = "FTP password"
    ftp_path = "FTP folder on server"
    ftp_passive_mode = "FTP passive mode"
    sms_settings = '""" SMS settings """'
    phone_number = "Numbers to send SMS messages(79999999999)"
    sms_login = "SMS service login"
    sms_password = "Password or MD-5 hash in lowercase"

    # Face recognizer
    fr_settings = '""" Face recognizer """'
    fr_server = "Server with the necessary folders of persons database"
    fr_min_score = "Minimal compliance percentage in recognition"
    fr_type_work_person = "Person"
    fr_type_work_group = "Group"
    fr_type_work_any = "Any person"
    fr_type_work_unrecognized = "Unrecognized person"
    fr_group_not_specified = "Specify alarm group name"
    fr_person_not_specified = "Specify person name"
    fr_group_not_found = "Group not found: %s"
    fr_alarm_person_name = "Alarm person name"
    fr_alarm_group_name = "Alarm group name"
    fr_activation_by = "Activation by"
    ignoring_identical_event = "Ignoring identical events for a period, (sec)"

    alarm_monitor_settings = '"""Alarm monitor"""'

    am_type = "Action type"
    am_base_settings = "Alarm Monitor base settings"
    am_display_duration = "The display duration of the channel in alarm template (sec)"
    am_alarm_template = "Alarm template"
    am_base_template = "Basic template (after alarm)"
    am_mon_1 = "Display number for alarm template 1"
    am_mon_2 = "Display number for alarm template 2"
    am_mon_3 = "Display number for alarm template 3"
    am_type = "Show channel,Playback in archive"
    am_show_channel = "Show channel"
    am_playback_archive = "Playback in archive"
    am_optional_settings = "Alarm Monitor optional settings"
    am_no_motion_check = "Alarm reset if no motion"
    am_change_template_check = "Alarm reset if another template choosing by user"
    am_max_channel = "Alarm channels displaying at once limit"
    am_same_cell_then_display_on_monitor = "Every time show a channel in the same cell"

    # SIMT
    simt_neuro_settings = '""" SIMT / Neurodetector settings """'

    crossing_simpt_border = "Crossing SIMT border"
    simt_events_in_the_selected_zones = "SIMT events in the selected zones"
    spam_filter = "Spam filter"

    simt_neuro_crossing_border_alarm = "Crossing border alarm (*simt)"
    simt_border_alarm_dir = "Crossing border direction (*simt)"
    simt_border_alarm_direction_choice = "A -> B,B -> A,any"
    simt_border_alarm_direction_choice_default = "A -> B"
    simt_presence_in_zone_check = "Continuous presence in zones alarm (*simt)"
    simt_zone_names_to_check_presence = "Zone names to check (for events in zone)"
    simt_presence_duration = "Time, spent by object in zone, before alarm(sec)"
    simt_size_alarm = "Object size alarm (*simt)"
    simt_speed_alarm = "Object speed alarm (*simt)"
    simt_length_alarm = "Object track length alarm (*simt)"
    simt_enter_alarm = "Entrance in zones alarm (*simt, neuro)"
    simt_leave_alarm = "Escaping from zones alarm (*simt, neuro)"
    simt_similar_events_delay = "Ignore same events in period (sec)"
    operations_with_pacs = '""" Operations with PACS """'
    pacs_type = "PACS type"
    pacs_door = "PACS name"
    pacs_operation_type = "Operation type"
    # pacs_operation_type_choice = "open the door,close the door"
    pacs_open_the_door = "open the door"
    pacs_close_the_door = "close thе door"
    pacs_delay = "Door open / close state duration, (sec)"
    manual_hotkey = "Hotkey for manual activation of operations"
    alarm_inputs_operations = '""" Operations with alarm inputs """'
    alarm_outputs = "Alarm outputs"
    operation_type = "Operation type"
    # operation_type_variants = "1.close,2.open,3.close-open,4.open-close,5.close-close,6.open-open"
    output_type_default = "3.close-open"
    close = "1.close"
    open = "2.open"
    close_open = "3.close-open"
    open_close = "4.open-close"
    close_close = "5.close-close"
    open_open = "6.open-open"
    output_delay = "Delay before next operation with alarm otput(sec)"
    alarm_inputs_settings = '""" Operations with alarm outputs """'
    input_for_activation = "Alarm input for activation of operations"
    associated_channels = "Associated channel(s)"
    orion_alarm_settings = '""" Orion alarm """'
    only_sensors_alarm = "Only sensors alarm"
    make_reactions_for_all_events = "Make reactions for all events"
    make_reaction_for_event = "Make reactions for event"
    orion_disabled = "Orion disabled"
    sigur_settings = '""" Sigur settings """'
    gate_settings = '""" GATE settings """'
    card_authentication_passed = "Card authentication passed"
    controller_disabled = "The controller is disabled"
    controller_enabled = "The controller is enabled"
    event_subtype = "Event subtype 'Controller: %1'"
    # all_possible_subtypes = "Key found,Pass happened,any"
    key_found = "Key found"
    pass_happened = "Pass happened"
    voron_settings = '""" Settings BOPOH """'
    # all_possible_events_voron = "No,alert in a zone,zone failure,the zone is unguarded,zone guarded,manual alarm confirmation,automatic alarm confirmation"

    alert_in_zone = "alert in a zone"
    zone_failure = "zone failure"
    zone_unguarded = "the zone is unguarded"
    zone_guarded = "zone guarded"
    manual_alarm_confirmation = "manual alarm confirmation"
    automatic_alarm_confirmation = "automatic alarm confirmation"

    neuro_detector_settings = '""" Neuro detector settings """'
    immediate = "immediate"
    long_lasting = "long-lasting"
    ignore_same_events = "Ignore same events by period (sec)"
    reactions_on_objects_in_zone = "Reactions on objects presence in neuro zones"
    type_of_work_in_zone_detection = "The type of work for detection in zone"
    zones_for_detections = "Zones names for detections (for all channels)"
    neuro_confidence = "Detector confidence coefficient (1-100 percent)"
    number_of_people = "Number of people for alarm"
    number_of_vehicle = "Number of vehicle for alarm"
    number_of_bicycle = "Number of bicycle for alarm"
    time_of_observation = "Time of observation before the alarm (*long-lasting), sec"
    successful_detections = "Successful detections, % (*long-lasting)"
    border_for_reactions = "Borders for reaction"
    border_ab = "Border Crossed A -> B"
    border_ba = "Border Crossed B -> A"
    react_to_people = "React for people"
    react_to_vehicle = "React for vehicle"
    react_to_bicycles = "React for bicycles"
    aruco_settings = '""" Aruco settings """'
    aruco_codes = "Aruco codes"
    aruco_ignoring_codes = "Aruco ignoring codes"
    logging_enable = "Enable logging"
    alarm = "Alarm"
    channel = "Channel"

    # Parameters / assertions / warnings

    closed = "closed"
    opened = "opened"
    servers_must_specify = "You must specify the server (s) from which the channels are used"  # Необходимо указать сервер (-ы) с которых используются каналы
    input_not_found = "Alarm input not found: %s"  #  "Тревожный вход ({filter_input_name}) не найден"
    choose_alarm_template = "Choose alarm channels template!"
    selected_template_not_found = "Selected template not found %s"
    outputs_selection_required = "Choose output"
    pacs_name_required = "Select PACS name"
    wrong_type_of_work_assertion = "The type of work should be '%s' or '%s'"
    wrong_time_of_door_open_close = "The time of the open / closed state of" \
                                       " the door must be in the range [1, 3600] sec"

    sip_code_sent_on_the_server = "The SIP code can only be sent on the server"
    specify_sip_number = "You must specify the SIP number"  # "Необходимо указать номер SIP!"
    specify_sip_code = "You must specify the SIP code"  # "Необходимо указать SIP код для отправки"

    trassir_email_account_not_found = "Specified E-mail account not found"
    specify_email_recipients = "Specify recipient(s) e-mail(s) separated by comma"

    # multiple_servers_found = "Multiple servers with the same name were found: %s"
    # server_not_found = "Server with name %s could not be found"
    specify_channels_with_face_recognition = "You must specify channels with face recognition" \
                                             " in the Working channels field"

    select_server_with_persons_db = "Select a server with persons db (Face recognizer section)"

    specify_borders_names = "Specify borders in section 'Borders' for reactions"
    specify_zones_names = "Specify zones names"
    no = "no"
    at_least_one_event_gate = "At least one event type for GATE access control system must be selected"  # "Хотя бы один тип событий для СКУД GATE должен быть выбран"
    specify_aruco_codes = "Specify aruco codes"  # Необходимо указать аруко коды для работы
    alarms_can_only_be_generated_on_servers = "Alarms can only be generated on servers"

    # Events in constants
    input_operations = "Input Operations"
    intrusion_detected = "Intrusion Detected"
    max_count_vehicles = "Max count vehicles"
    other_parameters = "Other"




