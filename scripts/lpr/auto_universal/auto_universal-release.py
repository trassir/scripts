# -*-coding: utf-8 -*-
# TRASSIR Auto universal v2.3.2
# Скрипт запускается на сервере

'''
<parameters>
    <company>DSSL Mitrofanov</company>
    <title>TRASSIR Auto universal</title>
    <version>2.3.2</version>
    <parameter>
        <type>caption</type>
        <name>Общие настройки</name>
    </parameter>
    <parameter>
        <id>CHANNELS_NAMES</id>
        <name>Каналы с АТ</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>LIST_TYPE</id>
        <name>Машина в списке</name>
        <type>string_from_list</type>
        <string_list>белом,чёрном,информационном,любом,нет в списках,любой номер,не распознан</string_list>
        <value>любом</value>
    </parameter>
    <parameter>
        <id>NAME_LIST</id>
        <type>string</type>
        <name>Работать со списками (имена через запятую)</name>
        <value></value>
    </parameter>
    <parameter>
        <id>REPEAT_EV_DELAY</id>
        <name>Задержка перед повторным распознаванием одинакового номера (сек)</name>
        <type>integer</type>
        <value>15</value>
        <min>1</min>
        <max>600</max>
    </parameter>
    <parameter>
        <id>DIRECTION</id>
        <name>Направление движения</name>
        <type>string_from_list</type>
        <string_list>вниз,вверх,любое</string_list>
        <value>вниз</value>
    </parameter>
    <parameter>
        <id>HW_DET_ENABLE</id>
        <name>Используется детектор HW</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
     <parameter>
        <name>""" Реакции по событиям """</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>OUTPUT_ON</id>
        <name>Выполнить операции с тревожными выходами</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>ACS_ENBL</id>
        <name>Выполнить операции с точкой доступа СКУД</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SHOW_CHAN</id>
        <name>Включить вывод канала на отображение</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SAVE_SCREEN</id>
        <name>Сохранить снимок локально</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_FTP</id>
        <name>Отправить снимок по FTP</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_SCREEN_EMAIL</id>
        <name>Отправить снимок на e-mail</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_SCREEN_TELEGRAM</id>
        <name>Снимок на Telegram</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SEND_EMAIL</id>
        <name>Отправить уведомление на e-mail</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SHOW_MESSAGE</id>
        <name>Отображать текстовое сообщение</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SHOW_MESSAGE_DELAY</id>
        <name>Длительность отображения текcтового сообщения(сек)</name>
        <type>integer</type>
        <value>5</value>
        <min>1</min>
        <max>60</max>
    </parameter>
    <parameter>
        <id>PLAY_SOUND</id>
        <name>Проиграть звуковое оповещение</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SOUND_NAME</id>
        <name>Название звукового файла</name>
        <type>string_from_list</type>
        <string_list>alarm.wav,bell.wav,boxing-bell-1.wav,boxing-bell-3.wav,cardlock-open.wav,chime.wav,chip001.wav,chip019.wav,chip069.wav,cordless-phone-ring.wav,countdown.wav,dialtone.wav,ding.wav,horn-beep.wav,phone-beep.wav,police2.wav,ship-on-fog.wav,ships-bell.wav,SNES-startup.wav,spin-up.wav,tada1.wav,tape-slow9.wav</string_list>
        <value>bell.wav</value>
    </parameter>
    <parameter>
        <id>SHOW_POPUP</id>
        <name>Вывести всплывающее окно</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
      <parameter>
        <type>integer</type>
        <name>Номер монитора для перехода из всплывающих окон</name>
        <id>MON_POPUP</id>
        <value>1</value>
        <min>1</min>
        <max>15</max>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" Настройка e-mail """</name>
    </parameter>
    <parameter>
        <id>EMAIL_ACCOUNT</id>
        <name>Учетная запись отправителя, созданная в Trassir</name>
        <type>string</type>
    </parameter>
    <parameter>
        <id>EMAIL_ADDRESSES</id>
        <name>Список получателей через запятую</name>
        <type>string</type>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" Telegram """</name>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Telegram id пользователя</name>
        <id>TG_IDS</id>
        <value></value>
    </parameter>
    <parameter>
        <name>""" Дополнительно """</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <type>float</type>
        <name>Коррекция времени скриншота (до события), сек</name>
        <id>SAVE_SCREEN_DELTA</id>
        <value>0</value>
        <min>0</min>
        <max>7</max>
    </parameter>
    <parameter>
        <id>ONLINE_SHOT</id>
        <name>Скриншот с потока камеры</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
     <parameter>
        <id>FIGURES</id>
        <name>Скриншоты с фигурами</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>SCHEDULE</id>
        <name>Расписание (опционально)(работает, когда расп. в красной зоне)</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>""" Настройки ftp """</name>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Хост</name>
        <id>FTP_HOST</id>
        <value>172.16.12.69</value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Порт</name>
        <id>FTP_PORT</id>
        <value>21</value>
        <min>1</min>
        <max>999999</max>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Пользователь</name>
        <id>FTP_USER</id>
        <value>trassir</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Пароль</name>
        <id>FTP_PASSWD</id>
        <value>123456</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Папка на ftp сервере</name>
        <id>FTP_PATH</id>
        <value></value>
    </parameter>

     <parameter>
        <name>"""Тревожный монитор"""</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <name>Базовые настройки ТМ</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>AM_DISPLAY_DURATION</id>
        <name>Длительность отображения канала в тревожном шаблоне (сек)</name>
        <type>integer</type>
        <min>1</min>
        <max>9999</max>
        <value>30</value>
    </parameter>
    <parameter>
        <id>AM_ALARM_TEMPLATE</id>
        <name>Тревожный шаблон</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>AM_BASE_TEMPLATE</id>
        <name>Базовый шаблон (по окон-ю тревоги)</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>AM_MON</id>
        <name>Номер дисплея для тревожного шаблона</name>
        <type>integer</type>
        <value>1</value>
    </parameter>

    <parameter>
        <id>AM_TYPE</id>
        <name>Тип действия</name>
        <type>string_from_list</type>
        <string_list>Отобразить канал,Открыть момент в архиве</string_list>
        <value>Отобразить канал</value>
    </parameter>
    <parameter>
        <name>Опциональные настройки ТМ</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>AM_NO_MOTION_CHECK</id>
        <name>Сброс тревоги только при отуствии движения на канале</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <parameter>
        <id>AM_MAX_CHANS</id>
        <name>Лимит одновременно отображаемых каналов</name>
        <type>integer</type>
        <value>24</value>
        <min>1</min>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" Операции со СКУД """</name>
    </parameter>
    <parameter>
        <id>ACS_TYPE</id>
        <name>Тип СКУД</name>
        <type>string_from_list</type>
        <string_list>Sigur,Orion</string_list>
        <value></value>
    </parameter>
    <parameter>
        <id>ACS_DOOR</id>
        <name>Название точки доступа СКУД</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>ACS_LOGIC</id>
        <name>Тип работы</name>
        <type>string_from_list</type>
        <string_list>открыть дверь,закрыть дверь</string_list>
        <value>открыть дверь</value>
    </parameter>
    <parameter>
        <id>ACS_DELAY</id>
        <name>Время открытого/закрытого состояния двери,(сек)</name>
        <type>integer</type>
        <value>5</value>
        <min>1</min>
        <max>3600</max>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <name>Клавиша для ручной активации операций</name>
        <id>ACS_MAN_ACTIV</id>
        <string_list>нет,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,F18,F19,F20,F21,F22,F23,F24,F25,F26,F27,F28,F29,F30,F31,F32,F33,F34,F35,F36,F37,F38,F39,F40,F41,F42,F43,F44,F45,F46,F47,F48,F49,Ctrl+F1,Ctrl+F2,Ctrl+F3,Ctrl+F4,Ctrl+F5,Ctrl+F6,Ctrl+F7,Ctrl+F8,Ctrl+F9,Ctrl+F10,Ctrl+F11,Ctrl+F12,Ctrl+F13,Ctrl+F14,Ctrl+F15,Ctrl+F16,Ctrl+F17,Ctrl+F18,Ctrl+F19,Ctrl+F20,Ctrl+F21,Ctrl+F22,Ctrl+F23,Ctrl+F24,Ctrl+F25,Ctrl+F26,Ctrl+F27,Ctrl+F28,Ctrl+F29,Ctrl+F30,Ctrl+F31,Ctrl+F32,Ctrl+F33,Ctrl+F34,Ctrl+F35,Ctrl+F36,Ctrl+F37,Ctrl+F38,Ctrl+F39,Ctrl+F40,Ctrl+F41,Ctrl+F42,Ctrl+F43,Ctrl+F44,Ctrl+F45,Ctrl+F46,Ctrl+F47,Ctrl+F48,Ctrl+F49</string_list>
        <value>нет</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>""" Операции с тревожными выходами """</name>
    </parameter>
    <parameter>
        <id>OUTPUTS</id>
        <name>Тревожные выходы</name>
        <type>objects</type>
        <value></value>
    </parameter>
    <parameter>
        <id>OUTPUT_ACTION_TYPE</id>
        <name>Тип работы</name>
        <type>string_from_list</type>
        <string_list>1.замкнуть,2.разомкнуть,3.замкнуть-разомкнуть,4.разомкнуть-замкнуть,5.замкнуть-замкнуть,6.разомкнуть-разомкнуть</string_list>
        <value>замкнуть-разомкнуть</value>
    </parameter>
    <parameter>
        <id>OUTPUT_DELAY</id>
        <name>Задержка между парными операциями (напр. замкнуть-разомкнуть) (сек)</name>
        <type>integer</type>
        <value>5</value>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>OUTPUT_ALGORITHM</id>
        <name>Алгоритм работы шлагбаума с очередью</name>
        <value>type_1</value>
        <string_list>type_1,type_2,type_3</string_list>
    </parameter>
    <parameter>
        <id>DELAY_BETWEEN_ITERATIONS</id>
        <name>Таймаут перед обработкой следующего авто для type_3 (сек)</name>
        <type>integer</type>
        <value>2</value>
        <min>1</min>
        <max>3600</max>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <name>Клавиша для ручной активации операций</name>
        <id>OUTPUT_MAN_ACTIV</id>
        <string_list>нет,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,F16,F17,F18,F19,F20,F21,F22,F23,F24,F25,F26,F27,F28,F29,F30,F31,F32,F33,F34,F35,F36,F37,F38,F39,F40,F41,F42,F43,F44,F45,F46,F47,F48,F49,Ctrl+F1,Ctrl+F2,Ctrl+F3,Ctrl+F4,Ctrl+F5,Ctrl+F6,Ctrl+F7,Ctrl+F8,Ctrl+F9,Ctrl+F10,Ctrl+F11,Ctrl+F12,Ctrl+F13,Ctrl+F14,Ctrl+F15,Ctrl+F16,Ctrl+F17,Ctrl+F18,Ctrl+F19,Ctrl+F20,Ctrl+F21,Ctrl+F22,Ctrl+F23,Ctrl+F24,Ctrl+F25,Ctrl+F26,Ctrl+F27,Ctrl+F28,Ctrl+F29,Ctrl+F30,Ctrl+F31,Ctrl+F32,Ctrl+F33,Ctrl+F34,Ctrl+F35,Ctrl+F36,Ctrl+F37,Ctrl+F38,Ctrl+F39,Ctrl+F40,Ctrl+F41,Ctrl+F42,Ctrl+F43,Ctrl+F44,Ctrl+F45,Ctrl+F46,Ctrl+F47,Ctrl+F48,Ctrl+F49</string_list>
        <value>нет</value>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <name>log</name>
        <type>boolean</type>
        <value>False</value>
    </parameter>
    <resources>
        <resource>base_utils.py</resource>
        <resource>delete_old_shots.py</resource>
        <resource>email_sender.py</resource>
        <resource>en.ts</resource>
        <resource>ftp.py</resource>
        <resource>helpers.py</resource>
        <resource>schedule.py</resource>
        <resource>script_object.py</resource>
        <resource>shot_saver.py</resource>
        <resource>tbot.py</resource>
        <resource>lpr_handler/lpr_handler.py</resource>
        <resource>lpr_handler/not_recognized_handler.py</resource>
        <resource>lpr_handler/__init__.py</resource>
        <resource>reactions/access_control.py</resource>
        <resource>reactions/alarm_mon.py</resource>
        <resource>reactions/executor.py</resource>
        <resource>reactions/fire_event.py</resource>
        <resource>reactions/output_reaction.py</resource>
        <resource>reactions/output_reaction_type_2.py</resource>
        <resource>reactions/output_reaction_type_3.py</resource>
        <resource>reactions/play_sound.py</resource>
        <resource>reactions/reactions.py</resource>
        <resource>reactions/reactions_with_screenshots.py</resource>
        <resource>reactions/show_message.py</resource>
        <resource>reactions/show_popup.py</resource>
        <resource>reactions/telegram_text_sender.py</resource>
        <resource>reactions/__init__.py</resource>
        <resource>senders/senders.py</resource>
        <resource>senders/__init__.py</resource>
    </resources>
    </parameters>
'''

resources = {
    "base_utils.py": """
        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
    """,
    "delete_old_shots.py": """
        eNqVVW1v0zAQ/l6p/8FkmkighIIEHyYqMbYgJm0UNUUIIWSlzaXxSOLIduj67zk7L3OSFkQ+
        OXf3PPfi8x3LSy4U4XI6YfVRppVi2XQynSSC54TSTcUyxQpKSWPBN/ewVR0g5VJpcyUOF9MJ
        wc8AU8hKELIF7UDRjO92IKYTeNhCqciN0QRCcGEDtRUrdhbw1uBIJHssXQBxpECxHLSoVpKF
        Zel6WjGdbLNISvKNi18oq3PwGr/hbRB8oeubu2D5dU3D4AoJ3s41SGtjSLAMrGCKUldClszI
        JpJAy0ilM/R+kFQqLqBl05828/foS2eyIB+jTMJA23GgvjsPbBRHetS3KfrdoeB71zO/Or8+
        CPUxZCqygZ3Q1QEvrKgHaCpAV5W2DEY4LtDzU4qX5HVbuPdSRYptc1Apj61a6lio4lTC1jVn
        u3ICVCUKUiv8lFeCPMPLQIe1JGdFpcDrC5GJF3HntxQce08d7PvDjOk2jYodxOYSbZ//W+aG
        BxE18snCuq4TVzjQNWk2THarCcj5b6Ay5UqOImXJ4I4tXU1rwBtI8Gqpjhtdu32bfmhj3YuB
        i76F5zPJkT2PlF0S/dXvzY9hU+1c51w20ZCEZ7EeBXVU5Fw6MyuA2ZGgB8QoJ0WUA2EFjio/
        Y1LFTLj9Z+RdjFNJSkwfEVrv33NWDDAzQ+uNgVjnFsak9pWUx/gbUxPbuyN5nICMi7WqK2VK
        g65Owx6n7KmvHuC+yJUAcP9K1gziZWiGsB6wIMQ/6Ju4QSNc5yoqnuIEhgyw0xKWwUWdA6q9
        3vzUs5AyBQInAi9Gff34ouohZD/XXvc3skGQBtR7OJ33BmcP5AFYLzDT7bxS7qv5fI6z5fhw
        a9p2kEwvUVGNkxssg7WohrtgWJ5mZZ2R4CHKywxwepBKb5Az8uEyDGh4tQqCz+Gn5Zp+XN5e
        B6thm2vLXn4SFC7xnXQdeZAKcrpnMVBeanfS8X44covtUpji0frBOj9nxLnMIpHfcVx+XDgt
        q6cP15ffQ7pe0nC9XAXo/40W7s16xb9mzx6PdtYHe49IX9cP//8AacZ0Pw==
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
    "en.ts": """
        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
    """,
    "ftp.py": """
        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
        l0U=
    """,
    "helpers.py": """
        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
    """,
    "schedule.py": """
        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
    """,
    "script_object.py": """
        eNq9V1tr4zgUfg/kPwjBEBs8ppl9CwS2U8JSZrcdpmVfSnEUW0k840hGkkNLt/99ji625UvS
        MgObl9g653xH5/uOLs4PJRcKfZecTSe5fdlzqaaT6USJ58V0guC3FfyA9rQoqZDIee2oSgq+
        21ExndCnlJYKXRvLSggu/EDtlbOdF/i3iUNEdlCmE/uElt5wEGpDkhwhdc5ZkoAVz+OL+ALX
        /nFGN9UuwB8kcl4L9EHiCCUJIweaJPqpiTd4d1ffrr/eJzeX/6wATxccS0WUDMK4JIIyBQ86
        VvtOJ2lBpER3qchLdbv5TlMVmJB7AeO5sEMR4uY/dKVjjJ0dSRPp7BpQ2y/FTjpX/dPZUCCV
        AJxSwUxJES6QhTbGCGV0S6pCoQUALdY3nNF1G7+r8uxkvDa+EW/LHiJ8teP8XUBQc10e+ADr
        OctVkgSSFtvIVLHU3pHBcY82sXkJPT5kBc0W+JxHSMOEcYOKrRWHdU4Tl4rE1XJC2I43IMam
        S8Db/HGBvOboeUpoS+0VtHEjcEaKpVUE4PDL60dLH463XByICtpJxtorHEmjx4MWbyRNU6V7
        gFS2XqoULDcZYBwa+BF0x4UPNJJhy4vMLMdW1ta4p6RQe228/YL7xnRP0x+JYfVeVHQQreeg
        VcxJkWh9aPDgo0Y9mMfO5EyVltGEZJalkdmDR90C1vksnSlnij4pSMYqCHt4rD3+LAWHVlTP
        bV/bSdq8i5O8NLOIbYXYWrCntqCqEqwT2KS1r0ZNvTmO5I7QkRRVZ9XkWzuGcoYetDARwmY/
        xo+eV0cGR78JG+N9ENRWaGJaD1pI2ssiSC4p+lf7mWkEePVUghQ0Q7PbLzPdszNjmMGewBWa
        vbzOmlViqwvPCFHP84QUXhfmTbd7gtR2HA412XBeBF2Ydib1yECdzoTG9cllziA/S2ngONep
        Qk1FK908Qhd9xax1ieboY5/5MUG768kEjMvpsfRbguoydBXz/y5+ScxmY/UJ66yQ+kQ2APpl
        wH+D8V7u4bgLT60MA2Zhxnhzp8ZvcWZOW83Vy2vDlHou67RxfYM5S5zdps9TZ30aEPs6oM9D
        GieQwVTN+JslejcPlBI2U2hDET2U6rl7Xr9XFfDzK+lZ2218T9iOOqdR8UYE6qh+JrR3Kv7P
        ypv9xTulkk2lFGdOLT0cAdNFsSHpD589uJRdZlkdimwUUry+02ksX5HexVT/TGBgVEGfXTwM
        dZ3q3CjYVizVF0jwvqoH6zE/0zfTof1k9lZ5t0qu7IyviIItSqwBzJVgzmgQOivaljZ4mu4+
        XMv+Al1vbSm5tK3Y9bwH+p0jdFtTDjjrttfvZFPQDrGDxaHh32yCG278BgvBTxOMSdnCNXMN
        8IDi/oy7eTaK1dciAu5HOCwS+C7yO8u7KA0a68y1KSZlSVkWBN2QuP0Mg9xjR61ifo9vc0ET
        eoQraXL85Lr7QKUkO9gZ9PpmtFhiuNlkRBF46PX6X5RRAUUh5b6+DNQbDe7w6x5f6ZB2cL0u
        5+t1bzNwMxl+MdlgyM3TnOil3ngCzqcBjq7iFIi1QdgfnbCxxvM2UR01uocauKX52I+z6lBK
        4zq8C7cK1N9Y8EE9x0MZrAYA8BMTvrha
    """,
    "shot_saver.py": """
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
    "lpr_handler/lpr_handler.py": """
        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
    """,
    "lpr_handler/not_recognized_handler.py": """
        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
        QfA=
    """,
    "lpr_handler/__init__.py": """
        eNpLK8rPVcgpKIrPSMxLyUktUsjMLcgvKlHwKSjygIjwcqWB1OTll8QXpSbnp+dlVqWm4Fau
        kFis4JdfEgRXCjcGBAEyFyhC
    """,
    "reactions/access_control.py": """
        eNrNV81q20AQvhv8DotCqZQfY9+KqQ4huFBoySG9lbKspbGieqU1u6s6upVcm4cppaXQQ5/B
        fqPuriRrJUuuD0mpQqKf+fv2m9nZyQkKWBin0RRlcnHxYjgYDuJkxbhEMk5g93LLhBwOFpwl
        CO4gyCTjqBTNyndtKnk+HQ6QuozqLdAVcFFpRiAxZVEEShfuAlhJ9NpIZpwzbhtqLQXKMnxj
        7BARDS/FHfnWR9fTQIaDE3TxGJd2dBkEIIQiKpWcUSRyISERiAMJZMxS8YjB9E9AiYpWBL0q
        Yl4rGomJ5VZ0e1OtqxkLYYEwjtNYYuwWn/QlgC7O61di/OEVi1OJU5JAn0zmK1vGqtBtQQiU
        5HgnFqXIm9YqjuPUL5c8EpasExNyheTeIS0NotRCzk0cZdxBqhada64wOE3DJvTKSpfySHLX
        2fze3m9+bT9vv2zvtw9o833zbfNDvT44nnZZ6/3cfO3Ra8ZrM4JchbiXD52f0T4D/j4rh2zY
        /KMyMVjVIwTS7fbrHXJi6PH3iW7ZtPj0WwS3tPfY8PcIqip4ZyMFlgwHLAE8J8FSmYxbGjsZ
        1v2J41jgNeNL3Sx89IpQAY1toWKlOGSMG1rsXBTdQqGcZ5HbzKNzeXVTr21U7X/DC3omFBCp
        xenIOe/JYu3P4j1e9FLvV7XcKv3OfI/0ghMWAiZ0TXKhobgeQidolVOlMw1jQeYU/NlkMp7U
        DoEeRlBsoaMQRJyop/IzSwM4FN9KR0CZgCfJh/Ec/icZMWD+cUpCSHNM9K+RHJmQlPGE0L1k
        PD4xZSCDSmj7JyGBUMrWVV3Oc7yEvAjJtI/Gyk376F14uxG9NOPQSP9xvS4ouwV2yI7pWTUZ
        Alr+i4NIWbJMupPxeFzWeOHNs1eVkDQjFOu55JPZLIe3mfPW6KNaH7FFeQyU20tIwqVCOrIP
        O4NISaQqs/fPeZYqprJUPv+Aznw0aXXsYl4EtwGUBKI+B/ZA1mPkX04HKynorPvYafqp8tuf
        klZgfXGQGU+b3zvydFy+3/EM7HPPRtU+YP2jhpU+GNbh5x0P3u7RXcVcbhxLVI7yM3PTNaSG
        dOC8FaAsPKi0XMdM/YgFQab+l0irsqumbNU1MgpT1d9VT1fuGuVT1ZSZcdEpUaOlup0u1/rJ
        JqRsE3axKUd/AKPO5hw=
    """,
    "reactions/alarm_mon.py": """
        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
        rBw1KNzvS2YHaqhQSoH/avD/RxUb/Q/sAekV
    """,
    "reactions/executor.py": """
        eNpdUMFKxDAQvRf6D0P3sK10BS8iAcF18ehFvIdpmrbRJinJFPXvnWxla3cOgXnz5r152cHh
        5gDKt8b1AmbqDg8JybM8M3bygQAblWdd8BakbGYzknFSwt/QNx9aMSfC9COXJq3mmRoxRnj5
        1momH8rLtBJ5BlxSWk14ZrHaY3K5PT6fXhlM64nylDBsIgVUxOzBt8ug1R3os7Iuox67GtSA
        zukxedRAsQYcMVi2iBF7zX0cPEmHVlcCYLfIpCqKYm0w9Ez9/MIQV/DIoFjbVP/coBT8Ctif
        FmxfXXEpQmkcx4byPXBYE+DuHlrTGwIyfCChnartzvb4K8FLEij5Z5LdOn/TNAcXN9gm4cQX
        /AIh54l4
    """,
    "reactions/fire_event.py": """
        eNptUk1PwzAMvVfqf7DKpZ26HTihST0OCQnBgR8QhdYtgTSpHJcPIf47SdZu7cAXx87z87Pl
        K9hutlDbRpluDyO325uQSZM0acn24GpSAwv7/Io1g+oHSwxPMfkYcwHJ9LVPE/AWa15QD0hu
        RnfIQtuuQ0oT/KxxYLiLPwciS8vCgPI6FoX3sQ6kW7EcPVSLZF4EIWlSa+kc3CrCwzsazpdS
        i6lXgy0IoYxiIXKHui3ByB6rB2uwhG5UzfQcJHmOGMy1wdzox8tPPUoIHMXuRBnIjjwzRRQ3
        t8ZPrEfGqXP9Io1BHTZcArsSpJbUix6dkx36eCOpC27z9hFeSyHnvZ+kec5d65UJDNLE+3W+
        BgSbuKts0JLRa2K/HGyy8i90Ulf5RUtmyldqs3bUWoQ5s+Kf2kayrL4zdtk+DpatJ/PZdeLn
        gqM4h9PZHKJT1oSDQKKL4Y+XsMMZlXuIJ/kFSE7fJQ==
    """,
    "reactions/output_reaction.py": """
        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
    """,
    "reactions/output_reaction_type_2.py": """
        eNqlVcFu2zAMvQfIPxAZitmpE6S3oWiOGxBgwICtd0GxaUeoIxkSvSR/P8pxXdlxXWzzwTEo
        8vGRfFQ+wWq5gtRkShePUFO++uIt89l8po6VsQSkjjif5dYcwdRU1SQsypSU0dB6/GjMP1ur
        6yIPxpEHInt5nM+AnwblgGWF1r1GF0iiNEWBdj7Dc4oVwa45+WqtsWGg92KaQeD3Jg6k66Fc
        f2EbGKPYE5nP0lI6NyS820UDS9ymzTAHIZRWJETksMwTKCplXMInpbwk8NoKQZcKW6vYI50Q
        tVCEVvbw/ONqrj66oZCAx4/XXbqJRHGAxkHr99JyC947GiCQdC8iNbUmjtn4TnXl+/nbpviw
        CpW3gU6Q4cgjir1MX+Cp0cvav6LQ3z/XUTDbfV1EC+8CZCAtjeOPA0IhCddw5xjkzi2S0QRJ
        iB/38Rt/HjCJI9LBZNHYuam4D3kpCy70mywdjvgE3Vht4WGqCs8ZvD9c/TNMeVQOsyS0KvcY
        ltTBDwh2TX3L/wSbQRcDDidpNS9EtHh+S8XvMtOfCfYIGpme+o2wiG8xRuc+zWaEid/xZhp8
        N0STYmyL13imN2vAC3kWgwQ98IfNZtNiXDUZhzLtw97I9Wb0z7bG4Q4MpLwFpSkK5Qb3wb4N
        onNlR4UXEI56jNvLlElNcQ4GdN+T4rQMlf5HGb4OvevVYCQWqbZ6cmr/18zb2n5xyqpZe5uA
        X2/oegYnVZZe6TLn0V8vO18iI6dGZ12pzcFHt8GIJP56qHjGtCZs/yuW0has++Xy5eS/bgU5
        lECD9Qe1h0zn
    """,
    "reactions/output_reaction_type_3.py": """
        eNrtV1Fr40YQfjf4PwwOB3IqG6d9KaE5SqEFQ2mh3FspQieNZBFJK3bXdfx2JFAKV7i/krZ3
        bdrm0r+w+kedXcmyLK0Vcs/Vg23NzszOfjPzzfoEZqczCFiY5PE5rGU0+1RLxqPxKMkKxiXI
        JMPmJZHIJWOpGI8izjJga1mspcfRD2TCcqjVvjXi72qpaMxXTEjtWvLt+XgE9BgvK0wL5GJn
        HaP0UhbHyMcjvAqwkLA0K19yznjbUGtR4C3Dr40d+OLAS/UNFy2hM9WBjEdB6gvRDXi5XDod
        0bTeN8QIPC/JE+l5TiXSj8A0ciEuEiZc0kn9rQs7VDy5LbCWei9RbhBzTyPpG88unPo81l+n
        lxv9q/K629B4XxM+Tj9I1+w7nTcBDQQwPQx2fiwcQunYUsdDyljhbRi/1Cm4gK/8VGBHJWDr
        XNLaoiMvOP7oMTqUJ4Vl2ctQrljoSWb8k8Y3LO/67ul8b8RRwoWsHbh1oH4j+cEWSLVEHrra
        ukC06udCEgLBTtjUQSUQNUSMO7WgnbuIccggyfe9Mw+2QYo2Xf1sE0xDyJqtC65xktv9tocH
        d0wJtJxwlGueW4FsnB6K5wKl1H0ysIMLlniPJKsttoCzi0LvVBNI5uc+NaWnS6p3oDCJIvKq
        iWiuP5wpzPpltNdPosrkeavQwc9DS8brWNs100nHCajf1PvyprwuX6k7UA/qrXpPn3+Buiuv
        1TuS3pY/qTt155Imvb1T9+Ub/fO1+pNMb8nwF/16rR5o1Rjek9m19gQO6dyqv8tX5WujV/6s
        /iHB7+pXMrxR99PDYCrqohO9XMfO4ZJ+JstcJCGCXCE0XTuHF4QZSAZBygRC7EusZQVRHxIs
        SR5URrr0QeNpLMF5JqaEYgWgeZm4/V0fyYvFYp+WzmJTGhYSmV3A2QAak0orxIBYj041ByM4
        h2di4rb82Lfo8FHrSIfKR2q90045XknniamrKzL3M6xj7uxFJK8XPa+Pmf04Dav1SGDgRE4P
        H+qmVhY+g8V5P/r6cDS9cpoFzkQw7VWPhZihgA1neexWCYFE2HJiLRHL9LBEdDEUUl0cfppC
        a8RtkCNkfkhTWUhWgKadybEohsecfpAkj4ag7z6mpojyYDaDM9uGbSXnbLFY1DBZaLJljamN
        8myzfZAFW4OvT4LEWeoP9ba86fBe+YaWhrnvX6OthR3ue6BfH8Z9ky+qs4HcsFZiB3mtUTNU
        NumDv2/GHenZIDTG7oC1TsTQ+mCGBuym//PW8RMNht3rvY+7vfe0vmt3Xq/zT2DjJ5K44ikB
        fTKvpyzdE6s7O/2ZYJpw9NxeYXAJOjlWovqQ2PXVC68wWEusb3ed/yC9W15Fth8dDGHbAKae
        e3QA7+x3RN5m2A6a1WV2EHAbSb/gaxzC/0B9NntuDCa2krRdUEnvPxpyypI=
    """,
    "reactions/play_sound.py": """
        eNqVVt2K00AUvi/0HYaINilp8FIKRRe3QmGtC7soIhJm00kbTTNhZuJu/blSL8QLn8B3EHHR
        dVl9hekbeWaa/7RRc5OZM9/5zs+cc5JraNAfII/Ogmg+RInwB7eUpNvpdoJlTJlAjORLyvPl
        gnKRb3hyEjPqEQ7nPqNLRM6IlwjKUAoYp3tN6wOPE+ElQaMRMiJhDLsdBE+KPQ0iTpNoprCC
        rdJDTbsgYUwYz5BzItyQzucEeMmZR2KBJvpkzBhlZUWFggBLigdaD2FeYdm80agkNC3lSLfj
        hZhzdBji1ZHyzsxCslI7M+Ij1w2iQLiuyUno20iH4apIM5B61JnjxlgsXEHdDcYPQsgG6vVq
        sK2ogrZOCj7gJBQpPAZfQfQi8JTWlEZ1fBs8vSIVucLfgfuF1ItVEexObR19OWJGRMKiv/mY
        m9qJcDgRQl3Tv7lgQxCN7Ovqc7dUX9XZQoY1LSNzSAozTL7iqdXhbadvGQUwVleTN4JzCPmK
        zCq3ocnQ4MCA4oBiDkfHLCGwFjOaiFFZe3I41nLCWF1ecFrFEvTjRIALsePR5TKJAg8LYlpP
        bj4tQEssvIWKgzh+EM1wGJp5eHZKYf1PUWnCiolN00BpnSRz09CtglK46o0Ah8FLMhui61zl
        oN2A1VJ9zc5oL7smviBvHDUKbYc1G6nl/3Q4tJWSO89oEJmwgTnjnc5My0aGxqmsFJyVso2o
        yNXJWcAFN3cZsuo1jQNO0EMcJkSPRlNNb0cw05Cf5TmSV/KLvJDf5Lm8Qut3enOJYH+5/oTk
        d/l1/Vb+lL/g/XH9HsHit9rI8/UHpSF/yAvDstpLQIevHK3c/BbPs1vRWVeloM8ad1uzITBM
        dd1bGm5YtYZ3Who++944xWyvAlqmsd1E5nRH03333uRgPN27P0avq/K9o8fTu3Xh9MGjvclx
        jbIUCQk5qfkOkcFAEmS5xeVeOmz2kfFq4/Gmq94YIFDOq5zA5kbP8SmDTt7CoUMv6Y7avxv2
        dobM2GhHFptaViMJRVVs/i2yBuxjNufw6j8/VatGG5ZqCFj+AEsm0bI=
    """,
    "reactions/reactions.py": """
        eNqVVltrG0cUfjf4P5xuCdp15YW8lCKwoQRTQkNc5EAfQlhWuyN5m72ImdnWJgQkp25o3ct7
        H/obFNeiqi/yX5j5Rz0ze9HsRgqpjPdy7pfvnNlPYXdnF4IsjNJRD3I+3P1CUba3treiZJxR
        DscZ49tbQ5ol4HmDPIp5lHoelNxs8B0JOPgMxqde8VIKkxMS5DyjleRB+V6yWUCjMS9VKpkj
        TTwszag/Tk9721uAP611TOIxoaySHxHuxdloRNAqOQnImMNjzTmgNKOmopLCFA3FJ1pPRW5a
        Ke6wZxBtpwgliH3GoE/8gEdZyuw6Yad0ZFmW+FPciJmcyimIK7GQU3Ev5vJMvsXrRJFu5B8g
        LuWF+EcsxaWYqZcpMs+hg6SZnIi5+Bvfp6g0QQMTFFqKmbgTd/JCnncKT+ISkDIXt6AVZuJa
        /iQW4l9XxakEDk78ZBwTVkamfvv7+0Cr4DHBVSLOBiHXD0OvaqP9TeyfHmV5GtpMXb3UT4iz
        UTXxXxKvfrWDYz9NSdwFnjCejLvgxz5NvIQw5o8I62Jf1H3vaZYSp0pCZ/qXeCd/wRyv5Rms
        DUFVAiuOdZ+LK/lGl3uqqrxEDXFd9QNLXSEQxKIo3xJtn+MVOyVuxbK7civfyjPNvkA74g60
        wFzcgLpp1lUJcPL/cjN8YJ+vxBxKdbAZpw7sIhmTWKB9jF31faYyqIwj/xlFGEYUeIQeOLbZ
        MNn0DHYYITpRR5dH401O5K+g0ImFkb8jLmeY0QIsPyaUV5qWYRIslrAVA6zEj+J1gghf1QhE
        Ot4XmJj8TRUKnckfsRcT5QevOgoFZ3yaq8CWus4/12qI7YKK2pdlN8+Qs1Bh66d75N66Jkq+
        pCMT6urHgmMS5jHxgizGluvq9gDHRNtUczPT06lmVMWzUJAp5lPxxDsVALYf2ddqEsU9+p7V
        g155//aw//Xjp195jw6fHPZxqqw+CWtmSIa4M6M04p5nMxIPu3VYjhGu4rgVA21Ujy2JahLV
        8L56bfpozGnhp3o1/URDSDMOdsRYPtDbzK7EXM/TBM/r1mPigFreK9lmfddpNtd3Jek4rdZQ
        P2IEnp2OiV7TLcO6wK9eo2cdbeUesmEdmeUOM5r4fE34+KS2guc5TavGa7HV3SgdZrbVN5dd
        nVQPHjCrCx9nvtmc5x9QeoGdI/UxuOpfa1kWHSz3gjpjcPrZ+2tlx0fU423n5Q/qyayyAdAN
        42FYB7uH1x50HhW0TrtfHDdJlOIxB3a1fB5+DmE0ivhqC7Xq3Qy2ZVBH3qaVafTMwPuE5zRt
        0nRuBqSb01OiRu1a8NOwyXWLXfDJXkFuzG4rnBIkIRnko3UAPfiepBzCLO1wCPw4ro++Xj2+
        UHh7gD3iWcGHJGccBqTA1/tm10S7SaoRfHcj2PW86SquaOqLzsWmcTz6n1s0T3FH5im3XsBn
        e/DQrDWOGRAN3q7xPZe2IO9GnFD8T9Deh8poHXEfv70U2o1yFZNWnOWm78aSaZ21Hz8Uxafb
        f3OO6JM=
    """,
    "reactions/reactions_with_screenshots.py": """
        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
        oGDZ+TU7N1qHoNv/AJxIjDo=
    """,
    "reactions/show_message.py": """
        eNqVkk1rhDAQhu+C/2GwFD9wZXsrCz3uodCeeiwlpDpquposycju/vsmGqnuUkrnkmR8n5k3
        E+9gk22gVJWQzQ4GqjePLhMGYVBr1QOesRxIaRD9UWmCvT+HgU+0ylAYkL7swgBsjFSL3RG1
        maEGiXWqadBieC7xSPA8ftlrrfQSdCrrZAG+jBxws6oyrfC0SCapMz3tiwo/hyaJTatO0KMx
        vEHwzFQaq3jUh0HZcWPgzSpfJ2Ey3zH1ziqsgTEhBTGWGOzqHFxh5guzCjt+mcUunKa4lVi7
        t0lnYW4yDRt9j7LlUmLH1OdXDmRy4B3X/Uzbc8Z145bscHK7pQNRg1QEwghpiMsSk2u4EiUt
        CRd+eOheJYnWhK01lnTcDu5NdO0nXdfSSIOWP7mV2E5iDRf2HV1H1DTnovTmOivmP95bbmRM
        EK8awAEvcfSHbfd7Fx64muH7ld+P/NeHz+Bhu93aVt+VRho3
    """,
    "reactions/show_popup.py": """
        eNqdVs2K2zAQvgfyDsJLiJNuTPfQUgKB0hJooYXC0kNPQrEVR11bSiV5f27bhZ7aZ2hfYbsQ
        6KHdZ3DeqCPZji0nu9k2h8Qa6ftm5tPMOAdoNByhUESMx2OU6fnombF0O93OXIoURURTzVKK
        WLoUUiPzHNFEk3KfntMw00JW+9NyXW7PiKI40yxR1YEXYHlvDN1OaVkIpbsdLS/G3Q6CjwUu
        aLKkcoOKqcaJiGMKxPQ8pEuNXtudqZRCNoHmFOTSAL6xOESUw1L8oknD6A9M2t1OmBCl0PFC
        nL0Ty2zpVzkNSj8RnSOMGWcaY1/RZH6IUgErIbEWWAEOExku2CnFJiS8NCwV2HwMJtgPgeD2
        H2qx4jhjgDOaBmL2kYba9wQoSYAFtrCHHhWbimoNOim/3x8EsBPZ5Kv0AMIrZ2WK4YJwTpND
        pFOlUyefQr4gorMs9r1jTUB4Ey4qGTZgxNQY9VTFYZ69beaaWCusLNukrpsAjCBHpP3y+GhT
        kxBpKHikJk9cDsqjexmqzK2Kxh94NaVRuQ9gOTdefK/3oZf2Itx71XvbO/YabsBHjYLFQzCO
        brXZfLzyBox8aGQlKpSDiigebGTFI7grpHQ5Kl1d6wOLr42qZGnZy7RrY1P5TUtvlWjQ9Ooj
        dICWFwnjehwxRWYJnUyPjh4fueC7U/r/tO5LbWd6rRTLWTTlp0wKnlJeDCQzbKiUrezdNnlJ
        eN9tkwAVYBGGmSx7A1g25fkcItUsTKleiKju1ZDwkCZ4nvFQM8H9ZmcuYZI1+9qqYoXY6mqo
        I5LIFKcqflBvFyPqjPFInHlOC9n58imjyobjalC5aGltIVr6Xv59fZX/zlf5n/zaG+wq3Va6
        dxL9yG/Xn4Hqdn21vsxX8P0NgeE2/7n+Cj5+5SuU36D8en25/gKrm3y15S8h6Swi48KvMxIb
        srVBTx+jIXwdOi1R30DxwmwNVQyjuroCYgSiSpGYwnpIZGx+hidn5ql5M2yOuNAwUhmHwgBR
        /DY4YqEe7C5CairN91wEcFlKgyvrzz0wcLkk1Znktc05DJPQBQfwpjUeKXRbaWsOwzIdB/Mv
        sS+IMg3VdxygE3rR9/aEXb2c7H8BoqF6nGvpm7djfzvS8tDuGOG2OLxeqzYHYmRokBaN7tkX
        mK27Rsu2mrWRvi2xv+upAXA=
    """,
    "reactions/telegram_text_sender.py": """
        eNqVUktrwzAMvgfyH0TGqFPankdhx/2C9W5MorimfgRLYe2/n70mW5JtjOkiW/oe8uMB9ts9
        NKE1Xh9h4G7/lCtlURZdDA7wis3AIYJxfYgML+N+bJ/R9hhp6mpkaYPWmPr3DM+zoqizblk0
        VhHBCS3qqNwr+vaEVxaTdn0sC0jRYgdSGm9YSkFoux3wyJGUSPiJzJEBh1U/ua8q2X7Svp8N
        R+nmrLxHmzwcset3oKyKTjokUhppB1sVdU7by1tezb1NBz4wGDKeWPkGxZrcmobnjBz3Szlg
        jCGKaslIWh+SmXeER6rW89RLrYg8RP9VW4DTNSzJh/QmonLK2KlU1d9Os6D8Z/SzIr9h2Mz1
        N3DBW/XH0BxvK5+fHjXt02dZeM508dpgn/9pTiZ4UARpzF/mn1AiQZLIOy9c8m0=
    """,
    "reactions/__init__.py": """
        eNp9kdGKAjEMRd8F/2G+wf2CRXbBh0FxBB9DqRktTJuSZtb170211cHFfT333KQ0PZNvGI0V
        RyE1zkdiabYVzGd9FuJgLpBoDIdqbJR0GRSDRomjQJ1UtfUNv457kUEuEWHxprNa/df6eNuq
        NTMY9uCfb/rMoKXghLg1wRyRi5pOdAaPKSmrdqesvaOpFSmOcepsMqgrrdUGWArCNDz23ujy
        DtcR2Uz/5HEDODs5QbKMGHSV/D3KXoXumZcBggMe2XgQ/BVIGA7ItborWad0p3Gp9I4R8AeD
        VPFbyVcG89kVXnDMUQ==
    """,
    "senders/senders.py": """
        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
        h4omW1DRUuJ/Y+bMig==
    """,
    "senders/__init__.py": """
        eNpLK8rPVShOzUtJLSpWyMwtyC8qUXBMyS8oSU1xzU3MzAkGS/FypeFW5xYSQISqkNSc1PSi
        xFyYUl4uABdILK8=
    """,
}
t1utils.resources_check(script_path, resources)
import os
import re
from __builtin__ import object

from helpers import init_logger, set_script_name
import host
from tbot import *

GLOBALS = globals()

# Initialize logger before import another modules
DEBUG = GLOBALS.get("DEBUG", False)
logger = init_logger(name=host.stats().parent().name, debug=DEBUG)

logger.info(
    "SCRIPT START. Script info: %s, pc id %s, pc name: %s",
    set_script_name(),
    host.settings("").guid,
    host.settings("").name,
)


from reactions import Reactions
from reactions import PlaySound
from reactions import FireEvent


# """ Реакции по событиям """
SHOW_CHAN = GLOBALS.get("SHOW_CHAN", False)
SEND_FTP = GLOBALS.get("SEND_FTP")
SEND_SCREEN_EMAIL = GLOBALS.get("SEND_SCREEN_EMAIL", False)
SEND_EMAIL = GLOBALS.get("SEND_EMAIL", False)
SEND_SCREEN_TELEGRAM = GLOBALS.get("SEND_SCREEN_TELEGRAM", False)
PLAY_SOUND = GLOBALS.get("PLAY_SOUND", False)
SOUND_NAME = GLOBALS.get("SOUND_NAME", "bell.wav")
OUTPUT_ON = GLOBALS.get("OUTPUT_ON", False)
ACS_ENBL = GLOBALS.get("ACS_ENBL", False)
SHOW_MESSAGE = GLOBALS.get("SHOW_MESSAGE", False)
SHOW_POPUP = GLOBALS.get("SHOW_POPUP", False)
SHOW_MESSAGE_DELAY = GLOBALS.get("SHOW_MESSAGE_DELAY", 5)

CHANNELS_NAMES = GLOBALS.get("CHANNELS_NAMES")


# """Тревожный монитор"""
AM_ALARM_TEMPLATE = GLOBALS.get("AM_ALARM_TEMPLATE")
AM_MAX_CHANS = GLOBALS.get("AM_MAX_CHANS", 6)
AM_BASE_TEMPLATE = GLOBALS.get("AM_BASE_TEMPLATE")
AM_DISPLAY_DURATION = GLOBALS.get("AM_DISPLAY_DURATION", 30)

AM_TYPE = GLOBALS.get("AM_TYPE", host.tr("Отобразить канал"))
AM_NO_MOTION_CHECK = GLOBALS.get("AM_NO_MOTION_CHECK", False)
AM_CHANGE_TEMPLATE_CHECK = GLOBALS.get("AM_CHANGE_TEMPLATE_CHECK", False)
AM_MON = GLOBALS.get("AM_MON", 1)


# """ Операции со СКУД """
ACS_MAN_ACTIV = GLOBALS.get("ACS_MAN_ACTIV", host.tr("нет"))
ACS_TYPE = GLOBALS.get("ACS_TYPE", "Sigur")
ACS_DOOR = GLOBALS.get("ACS_DOOR")
ACS_DELAY = GLOBALS.get("ACS_DELAY", 5)
ACS_LOGIC = GLOBALS.get("ACS_LOGIC", "open the door")


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

# """ Операции с тревожными выходами """
OUTPUTS = GLOBALS.get("OUTPUTS", "")
OUTPUT_MAN_ACTIV = GLOBALS.get("OUTPUT_MAN_ACTIV", host.tr("нет"))
OUTPUT_ALGORITHM = GLOBALS.get("OUTPUT_ALGORITHM", "type_1")
OUTPUT_DELAY = GLOBALS.get("OUTPUT_DELAY", 5)
DELAY_BETWEEN_ITERATIONS = GLOBALS.get("DELAY_BETWEEN_ITERATIONS", 5)

SCHEDULE = GLOBALS.get("SCHEDULE")


class TrassirError(Exception):
    """Exception if bad trassir version"""

    pass


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


class OutputObj(object):
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


def parse_object_names(object_names):
    if object_names:
        return set(object_names.split(","))


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


class TRObject(object):
    spec_symbols = re.compile(r'[|\\/:*?"<>]')

    def __init__(self, sett):
        self.sett = sett
        self.name = self.spec_symbols.sub("", sett.name.strip())

    def __getattr__(self, name):
        return getattr(self.sett, name)


class Server(TRObject):
    def __init__(self, sett):
        super(Server, self).__init__(sett)


class Channel(TRObject):
    def __init__(self, sett, server):
        super(Channel, self).__init__(sett)
        self.server = server

    @property
    def full_guid(self):
        return "{s.guid}_{s.server.guid}".format(s=self)


def get_channels(server_guid, channel_names=None):
    """
    Args:
        server_guid (str):
        channel_names (Set('name_1', 'name_2')):
    Returns: List[ Channel_1, Channel_2]

    """
    channels_ = []
    server = Server(host.settings("/%s" % server_guid))
    for sett in host.settings("/%s/channels" % server_guid).ls():
        if sett.type == "Channel" and not sett["archive_zombie_flag"]:
            if channel_names is None or sett.name in channel_names:
                if _is_channel_enabled(sett):
                    channels_.append(Channel(sett, server))
    return channels_


# ---------------------------------------------------------------------
#  Initializing starts here
# ---------------------------------------------------------------------

if __name__ == host.stats().parent().guid:
    if host.settings("").guid == "client":
        raise TrassirError("Script starts on Trassir server only, not client")

    schedule_ = None
    if SCHEDULE:
        from schedule import ScheduleObject

        schedule_ = ScheduleObject(SCHEDULE)

    reactions = Reactions(schedule_)

    # -------------------------------------------------------
    # Setup channels to work
    # -------------------------------------------------------
    SELECTED_SERVER = host.settings("").guid
    assert CHANNELS_NAMES, host.tr("Необходимо выбрать каналы для работы!")
    selected_channels = get_channels(
        SELECTED_SERVER, parse_object_names(CHANNELS_NAMES)
    )

    # -------------------------------------------------------
    # Play sound
    # -------------------------------------------------------
    if PLAY_SOUND:
        reactions.add_executor(PlaySound(SOUND_NAME))

    # -------------------------------------------------------
    # Output reactions
    # -------------------------------------------------------

    if OUTPUT_ON:

        assert OUTPUT_ALGORITHM in ["type_1", "type_2", "type_3"], host.tr(
            'Output algorithm not in ["type_1", "type_2", "type_3"] '
        )
        if OUTPUT_ALGORITHM == "type_1":
            from reactions import OutputReactions
        elif OUTPUT_ALGORITHM == "type_2":
            from reactions import OutputReactionsII as OutputReactions
        else:
            from reactions import OutputReactionsIII as OutputReactions

        assert OUTPUTS, host.tr("Необходимо выбрать тревожные выходы")
        _outputs = get_outputs(parse_object_names(OUTPUTS))
        logger.debug("outputs objects found: %s", _outputs)

        output_reactions = OutputReactions(
            gpios=_outputs,
            delay=OUTPUT_DELAY,
            reaction_type=GLOBALS.get("OUTPUT_ACTION_TYPE"),
            delay_between_iterations=DELAY_BETWEEN_ITERATIONS,
        )
        reactions.add_executor(output_reactions)
        if OUTPUT_MAN_ACTIV not in [host.tr("Нет"), host.tr("нет")]:
            logger.debug("Output manual activation key is %s", OUTPUT_MAN_ACTIV)
            host.activate_on_shortcut(
                OUTPUT_MAN_ACTIV, output_reactions.manual_activation_of_outputs
            )

    # -------------------------------------------------------
    # Operations with physical system control ("СКУД")
    # -------------------------------------------------------

    if ACS_ENBL:
        from reactions import AccessControlOperations

        assert ACS_TYPE in ["Sigur", "Orion"], "ACS_TYPE must be Sigur or Orion"
        assert ACS_DOOR, host.tr("Необходимо указать название точки доступа")

        acs_door_obj = host.object(ACS_DOOR)

        if ACS_TYPE == "Sigur":
            assert hasattr(
                acs_door_obj, "workmode_alwaysopen"
            ), "{} не является точкой доступа Sigur. Только одно имя м.б. указано".format(
                ACS_DOOR
            )
        if ACS_TYPE == "Orion":
            assert hasattr(
                acs_door_obj, "grant_access_once"
            ), "{} не является точкой доступа Orion. Только одно имя м.б. указано".format(
                ACS_DOOR
            )

        assert ACS_LOGIC in [
            host.tr("открыть дверь"),
            host.tr("закрыть дверь"),
        ], host.tr("Тип работы должен быть 'открыть дверь' или 'закрыть дверь'")

        assert 1 < ACS_DELAY < 3600, host.tr(
            "Время открытого/закрытого состояния двери должно быть в диапазоне [1, 3600] сек"
        )

        aco = AccessControlOperations(
            access_point_name=ACS_DOOR,
            access_point_type=ACS_TYPE,
            operation_type=ACS_LOGIC,
            delay_operations=ACS_DELAY,
        )
        reactions.add_executor(aco)

        if ACS_MAN_ACTIV not in [host.tr("Нет"), host.tr("нет")]:
            host.activate_on_shortcut(ACS_MAN_ACTIV, aco.manual_activation)

    # -------------------------------------------------------
    # Show channel in Alarm Monitor
    # -------------------------------------------------------

    def template_exists(template_name):
        for sett in host.settings("templates").ls():
            if sett.name == template_name:
                return True

    if SHOW_CHAN:
        from reactions import AlarmMonitorManager

        assert AM_ALARM_TEMPLATE, host.tr("Тревожный шаблон не выбран!")
        assert template_exists(AM_ALARM_TEMPLATE), "{txt}: {template_name}".format(
            txt=host.tr("Шаблон не найден"), template_name=AM_ALARM_TEMPLATE
        )
        if AM_TYPE == host.tr("Отобразить канал"):
            am_type = 1
        elif AM_TYPE == host.tr("Открыть момент в архиве"):
            am_type = 2
            AM_MAX_CHANS = 1
        else:
            logger.error("AM_TYPE wrong value: %s", AM_TYPE)
            am_type = 1

        am_manager = AlarmMonitorManager(
            AM_ALARM_TEMPLATE,
            am_type,
            AM_MAX_CHANS,
            display_duration=AM_DISPLAY_DURATION,
            base_template=AM_BASE_TEMPLATE,
            no_motion_check=AM_NO_MOTION_CHECK,
        )

        am_manager.create_monitor(AM_MON)

        reactions.add_executor(am_manager)
        if AM_CHANGE_TEMPLATE_CHECK:
            logger.debug("Drop template enabled")
            host.activate_on_gui_event("", am_manager.drop_template)

    # -------------------------------------------------------
    # Show message
    # -------------------------------------------------------
    if SHOW_MESSAGE:
        from reactions import ShowMessage

        reactions.add_executor(ShowMessage(show_message_delay=SHOW_MESSAGE_DELAY))

    # -------------------------------------------------------
    # Show popup window
    # -------------------------------------------------------
    if GLOBALS.get("SHOW_POPUP"):
        from reactions import ShowPopup

        mon_popup = GLOBALS.get("MON_POPUP", 1)
        reactions.add_executor(ShowPopup(monitor_to_show_archive_from_popup=mon_popup))

    # -------------------------------------------------------
    # Fire event
    # -------------------------------------------------------
    random_guid = host.random_guid()
    reactions.add_executor(
        FireEvent(name="AutoUniversal-{}".format(random_guid), guid=random_guid)
    )

    # -------------------------------------------------------
    # Al senders
    # -------------------------------------------------------
    ALL_SENDERS = []

    # -------------------------------------------------------
    # Initializing email sender
    # -------------------------------------------------------
    if SEND_SCREEN_EMAIL or SEND_EMAIL:
        from senders import AdoptedEmailSender
        from email_sender import EmailSender

        assert EMAIL_ACCOUNT, host.tr("Учетная запись e-mail в Trassir не задана")
        assert EMAIL_ADDRESSES, host.tr("Получатели почтовых уведомлений не заданы")
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
    # Initializing ftp sender
    # -------------------------------------------------------
    if SEND_FTP:
        from ftp import FTPClient
        from senders import AdoptedFTPSender

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
    # Initializing Telegram sender
    # -------------------------------------------------------

    TG_IDS = GLOBALS.get("TG_IDS")

    if SEND_SCREEN_TELEGRAM:
        from senders import AdoptedTelegramSender

        assert TG_IDS, host.tr("Необходимо указать Ваш Telegram id")
        host.exec_encoded(tbot_service)
        tbot_api = TBotAPI()
        telegram_users = tbot_api.prepare_users(TG_IDS)
        ALL_SENDERS.append(AdoptedTelegramSender(tbot_api, telegram_users))

    # -------------------------------------------------------
    # Reactions with screenshots add here
    # -------------------------------------------------------

    BASE_SCREENSHOT_FOLDER = os.path.normpath(
        os.path.join(
            host.settings("system_wide_options")["screenshots_folder"],
            "AutoUniversal_{script_guid}".format(
                script_guid=host.stats().parent().guid
            ),
        )
    )
    DAYS_TO_STORE = int(GLOBALS.get("DAYS_TO_STORE", 5))
    SAVE_SCREEN = GLOBALS.get("SAVE_SCREEN", False)
    FIGURES = GLOBALS.get("FIGURES", False)

    if SEND_SCREEN_EMAIL or SEND_FTP or SAVE_SCREEN or SEND_SCREEN_TELEGRAM:
        from shot_saver import ShotSaver
        from reactions import ReactionsWithScreenshots

        SAVE_SCREEN_DELTA = GLOBALS.get("SAVE_SCREEN_DELTA", 0)
        assert 0 <= SAVE_SCREEN_DELTA <= 7, "save_screen_delta should be in [0, 7]"
        ONLINE_SHOT = GLOBALS.get("ONLINE_SHOT", False)
        reactions_with_screenshots = ReactionsWithScreenshots(
            delta=SAVE_SCREEN_DELTA,
            base_folder=BASE_SCREENSHOT_FOLDER,
            online_shot=ONLINE_SHOT,
            save_screen=SAVE_SCREEN,
            figures=FIGURES,
        )

        shot_saver_obj = ShotSaver()
        shot_saver_obj.max_tries = 4
        reactions_with_screenshots.shot_saver_obj = shot_saver_obj
        for sender in ALL_SENDERS:
            reactions_with_screenshots.add_sender(sender=sender)

        # Add all senders to send screenshots
        reactions.add_executor(reactions_with_screenshots)

        if DAYS_TO_STORE:
            from delete_old_shots import Worker

            shot_cleaner = Worker(BASE_SCREENSHOT_FOLDER, DAYS_TO_STORE)
            shot_cleaner.run()

    # -------------------------------------------------------
    # LPR handler
    # -------------------------------------------------------

    LIST_TYPE = GLOBALS.get("LIST_TYPE")
    direction = GLOBALS.get("DIRECTION")
    hw_det_enable = GLOBALS.get("HW_DET_ENABLE")
    list_name = GLOBALS.get("NAME_LIST")
    if list_name:
        list_name = [x.strip() for x in list_name.split(",")]
    repeat_ev_delay = GLOBALS.get("REPEAT_EV_DELAY")

    if LIST_TYPE == host.tr("не распознан"):
        from lpr_handler import NotRecognizedHandler as LprHandler
    else:
        from lpr_handler import LprHandler

    lpr_handler = LprHandler(
        channels_objs=selected_channels,
        direction=direction,
        hw_detector=hw_det_enable,
        list_type=LIST_TYPE,
        list_name=list_name,
        make_reactions=reactions.make_reactions,
        repeat_ev_delay=repeat_ev_delay,
    )
    # plates_from_files(lpr_handler.list_type)
    host.activate_on_lpr_events(lpr_handler.event_handler)
