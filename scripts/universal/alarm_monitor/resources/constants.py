# -*- coding: utf-8 -*-
import os
import host
import localization as loc


EVENTS_TRANSLATION = {
    "Intrusion Alert": loc.events_loc.intrusion_alert,  # host.tr("Тревога проникновения"),
    "Fire": loc.events_loc.fire,  # host.tr("Обнаружен огонь"),
    "Allowed Access By Key": loc.events_loc.allowed_access_by_key,  # host.tr("Доступен доступ по ключу"),
    "Door Restored": loc.events_loc.door_restored,  # host.tr("Восстановлено состояние двери"),
    "Door Broken": loc.events_loc.door_broken,  # host.tr("Дверь взломана"),
    "Door Blocked": loc.events_loc.door_blocked,  # host.tr("Дверь заблокирована"),
    "No Access To All": loc.events_loc.no_access_to_all,  # host.tr("Доступ запрещен для всех"),
    "Access Denied %1": loc.events_loc.access_denied,  # host.tr("Доступ запрещен %1"),
    "Access Granted %1": loc.events_loc.access_granted,

    "No Access %1": loc.events_loc.no_access,
    "Reader Contact Lost": loc.events_loc.reader_contact_lost,
    "Walk Detected": loc.events_loc.walk_detected,
    "Free Walk Allowed": loc.events_loc.free_walk_allowed,
    "Armed": loc.events_loc.armed,
    "Left Object Detected": loc.events_loc.left_object_detected,
    "Item Abandoned": loc.events_loc.item_abandoned,
    "Item Missing": loc.events_loc.item_missing,
    "Slow Down Detected": loc.events_loc.slow_down_detected,
    "Tamper Alert": loc.events_loc.tamper_alert,
    "Tamper Alert: Defocus": loc.events_loc.tamper_alert_defocus,
    "Tamper Alert: Covered": loc.events_loc.tamper_alert_covered,
    "Tamper Alert: Flashlight": loc.events_loc.tamper_alert_flashing,
    "Tamper Alert: Shift": loc.events_loc.tamper_alert_shift,
    "Sound Detected": loc.events_loc.sound_detected,
    "Smoke Detected": loc.events_loc.smoke_detected,
    "Fire Stopped": loc.events_loc.fire_stopped,
    "Face Recognized": loc.events_loc.face_recognized,

    "FACS: %1": loc.events_loc.facs_1,
    "FACS Disconnected": loc.events_loc.facs_disconnected,
    "FACS Connected": loc.events_loc.facs_connected,
    "Alarm: %1 (%2)": loc.events_loc.facs_alarm,

    "Input Operations": loc.events_loc.input_operations,
    "CrossLine Detected": loc.events_loc.crossline_detected,
    "Intrusion Detected": loc.events_loc.intrusion_detected,
    "Face Detected": loc.events_loc.face_detected,
    "Object Track Length Alarm": loc.events_loc.object_track_length_alarm,
    "Object Size Alarm": loc.events_loc.object_size_alarm,
    "Object Speed Alarm": loc.events_loc.object_speed_alarm,
    "Object Entered the Zone": loc.events_loc.object_entered_the_zone,
    "Object Left the Zone": loc.events_loc.object_left_the_zone,
    "Object presence alarm": loc.events_loc.object_presence_alarm,
    "Max count people": loc.events_loc.max_count_people,
    "Max count vehicles": loc.events_loc.max_count_vehicles,
    "Max count bicycles": loc.events_loc.max_count_bicycles,
    "Input High to Low": loc.events_loc.input_high_to_low_event,
    "Input Low to High": loc.events_loc.input_low_to_high_event,
    "Orion Disconnected": loc.events_loc.orion_disconnected,
    "Person without helmet detected": loc.events_loc.person_without_helmet_detected,
    "Person without uniform detected": loc.events_loc.person_without_uniform_detected,
    "Warning: Thermal Signal": loc.events_loc.warning_thermal_signal,
    "Plate detected": loc.events_loc.plate_detected,
    "People Detected": loc.events_loc.people_detected_neuro,
    "Aruco entered the zone": loc.events_loc.aruco_entered_the_zone,
    "Aruco left the zone": loc.events_loc.aruco_left_the_zone,
    "Legal card authentication passed: %1": loc.events_loc.legal_card_authentication_passed,
    "Controller Disconnected": loc.events_loc.controller_disconnected,
    "Controller Connected": loc.events_loc.controller_connected,
    "Controller Alarm: %1": loc.events_loc.controller_alarm_proc_1,
    "VORON event": loc.events_loc.voron_event,
    "Person without mask found": loc.events_loc.person_without_mask_found,
    "Social distance violation detected": loc.events_loc.social_distance_violation_detected,
    "Access Point Disconnected": loc.events_loc.access_point_disconnected,
    "Access Point Allows By Key": loc.events_loc.access_point_allows_by_key,
    "Access Point Connected": loc.events_loc.access_point_connected,
    "Access Point Once Opened": loc.events_loc.access_point_once_opened,
    "Access Point Opened To All": loc.events_loc.access_point_opened_to_all,
    "Access Point Closed To All": loc.events_loc.access_point_closed_to_all,
    "Controller: %1": loc.events_loc.controller_proc_1,
    "Deny: %1 (%2)": loc.events_loc.access_deny,
    "Allow: %1 (%2)": loc.events_loc.access_allow,
    "Invalid card: %1": loc.events_loc.invalid_card,
    "Border Crossed B -> A": loc.events_loc.border_crossed_b_a,
    "Border Crossed A -> B": loc.events_loc.border_crossed_a_b,
    "Motion Start": loc.events_loc.motion_start,
    "Access Point: %1": loc.events_loc.access_point,
    "Pass: %1 (%2)":  loc.events_loc.pass_through,
    "Fire Detected": loc.events_loc.fire_detected,
    "Signal Restored": loc.events_loc.signal_restored,
    "Signal Lost": loc.events_loc.signal_lost,
    "Suspicious pose": loc.events_loc.suspicious_pose

   }


EVENTS_TRANSLATION_REVERSED = {
    value: key for key, value in EVENTS_TRANSLATION.iteritems()
}

