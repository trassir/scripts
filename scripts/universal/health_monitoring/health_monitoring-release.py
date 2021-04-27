# -*- coding: utf-8 -*-
# <h3>health_monitoring</h3><br>
#
# <code>Version: 3.6<br>
# Author: A.A.Trubilin, DSSL<br>
# E-mail: a.trubilin@dssl.ru<br>
# Help: https://scripts.page.link/health_monitoring
# </code>
"""
<parameters>
    <company>AATrubilin</company>
    <title>health_monitoring</title>
    <version>3.6</version>

    <parameter>
        <type>caption</type>
        <name>Base settings</name>
    </parameter>
    <parameter>
        <type>server</type>
        <id>SERVER</id>
        <name>Server</name>
        <value></value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Min. event duration, sec</name>
        <id>MIN_EVENT_DURATION</id>
        <value>5</value>
        <min>0</min>
        <max>100000</max>
    </parameter>
    <parameter>
        <type>objects</type>
        <name>Work by schedule (red zone)</name>
        <id>WORK_BY_SCHEDULE</id>
        <value></value>
    </parameter>
    <parameter>
        <type>integer</type>
        <name>Merge tracks cache, sec</name>
        <id>MERGE_TRACKS_CACHE</id>
        <value>2</value>
        <min>0</min>
        <max>10</max>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>DEBUG</id>
        <name>Debug mode</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Track events</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>ERROR_CPU</id>
        <name>CPU load > 90%</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>ERROR_CLOUD</id>
        <name>Cloud</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>ERROR_DISKS</id>
        <name>Disks</name>
        <value>True</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>COUNT_DISKS</id>
        <name>Count disks to write</name>
        <value>True</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>ERROR_DB</id>
        <name>Database</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>ERROR_IP_DEVICES</id>
        <name>IP Devices</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>ERROR_CHANNELS</id>
        <name>Channels</name>
        <value>True</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>ERROR_NETWORK</id>
        <name>Network</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>ERROR_SCRIPTS</id>
        <name>Scripts</name>
        <value>False</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Simple notifications</name>
    </parameter>
    <parameter>
        <type>string_from_list</type>
        <id>SIMPLE_PLAY_SOUND</id>
        <name>Play sound</name>
        <value></value>
        <string_list>,shots/alarm.wav,SNES-startup.wav,alarm.wav,bell.wav,boxing-bell-1.wav,boxing-bell-3.wav,cardlock-open.wav,chime.wav,chip001.wav,chip019.wav,chip069.wav,cordless-phone-ring.wav,countdown.wav,dialtone.wav,ding.wav,horn-beep.wav,phone-beep.wav,police2.wav,ship-on-fog.wav,ships-bell.wav,spin-up.wav,tada1.wav,tape-slow9.wav</string_list>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SIMPLE_POPUP</id>
        <name>Pop-up</name>
        <value>True</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SIMPLE_POPUP_WITH_BUTTON</id>
        <name>Pop-up with button</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SIMPLE_FIRE_EVENT</id>
        <name>Generate event</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>caption</type>
        <name>Telegram notification</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>TELEGRAM</id>
        <name>Enable</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Telegram id's</name>
        <id>TELEGRAM_IDS</id>
        <value></value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>Email notification</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>EMAIL</id>
        <name>Enable</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>ADD_DATE_TO_EMAIL</id>
        <name>Add date to Email</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>EMAIL_ACCOUNT</id>
        <name>Email account name</name>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>EMAIL_SPAMLIST</id>
        <name>Send to emails</name>
        <value></value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>SMSC.ru notification</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SMSC</id>
        <name>Enable</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>SMSC_LOGIN</id>
        <name>SMSC Login</name>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>SMSC_PASSWORD</id>
        <name>SMSC Password</name>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <id>SMSC_PHONES</id>
        <name>SMSC Phones</name>
        <value>79999999999,78888888888</value>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>SMSC_TRANSLIT</id>
        <name>Translit messages</name>
        <value>1</value>
    </parameter>

    <parameter>
        <type>caption</type>
        <name>POST request notification</name>
    </parameter>
    <parameter>
        <type>boolean</type>
        <id>POST_REQUEST</id>
        <name>Enable</name>
        <value>False</value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>Url</name>
        <id>POST_REQUEST_URL</id>
        <value></value>
    </parameter>

    <resources>
        <resource>helpers.py</resource>
        <resource>schedule.py</resource>
    </resources>
</parameters>
"""

resources = {
    "helpers.py": """
        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
        pVqZwf8P9W08Ug==
    """,
    "schedule.py": """
        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
    """,
}
t1utils.resources_check(script_path, resources)

# _SERVICE_VERSION = 0.66
_TBOT_SERVICE = """
    ws6NddMiBzOnv07z50KyTBIvoarbeMFBTRba1CEwNlGH3XVTTLfL1Jluc664MSlqqbrnjkwl
    g8smB1yytf2QdAoTovLH8EnQEcecN9pm/Maz88rY5hWuC+78NtM28dEzkiWIlQU/97yPV/tm
    gJ0ZiuzD+vaxheKeY2MuyyRhqByCwfYk7PTO2FyTVQxeuLKW4Bh2F0Ho/QnIGh4EqiHSUh+j
    n9F1gSNxLQdORHsB0lJiPvRnc8+0NqNcSgem5dG++ocOkJBUmN2CCnAvh7cXME57kzeO4rqM
    AL7HoTdf4DFxsSHQ/jH5jfZDi0AvP5UJ3Wy/QFL4sGA4pejHVD2v9/kAkMU7lly7JWDPH7hj
    IkiuzwT8lz38iuScIuERSP7Ztpao5Tt3i41pej7zxSzRRG/O+fKEFAlTe+pp/z+02jiW1JHs
    hrlnA404kFz+hblvMmnBT1fMfdVEHafATpixsF6QBWMbfp0qrqpgpmHil0/N/dMsZ0mL1lNI
    QJIfqE+rMy+6ZgPo5eslnulnMaCZ89d7Q9Kyh3LVE1QEGwTecXwRxTpYWrqtMbMm2sCOH9/c
    zeo6loMVyofJZ1LNrSUFsZXU74WWX5TjHiMHr4wEY8MA6QHOeJBk7L4PmrBsVHsuw1NyJYmq
    p71BUmdPXPNbO9jDWPlTC8/21/JCySIZN3SAYHRD9W3y1uS4mvNg/aKtZVkJGyNGZ7CowmbT
    sLSuSnqFAWtqZLe/kyjBjizWWV/xUvvtpbCrzQ5LGmbpVVCEs3cOQEoaVjBxRdBjmYWX4SvN
    2cTuKZ/nLCLQVbnxacwI592Hj31HqoLdgOawao6963QsXhaAlv75CTBkXXL96h72N8yKpmBf
    3KLPE59Nk3Ch1cokcI/S9B+GoxzyOo++1ZGUbMZCQ3I98QALJN7nr58NFKGuR1gf7VL2o3O9
    uIMHHYjA2/BeP9/Pn+IH3lF/byfYS5HFr7vHKTNnIOGvMBX6khyF5FqxWRU3hO5rKbNhvaKA
    8Zu8iMWyqTlIRuJZV7RAcireNF/DrmbZMDtWG4ig+6FqUAMJISO8k9UNoFy5+a9doOy/EovD
    ZnIgeh3srSZmogxkb6XW0tQ/axlmAmIQiQXC0RuDOuv7AXB9Mpn4UpHm/d3WRbRMLdQzSgp9
    AuRqvsEYP8sRVJBZCW5LMJWBT8eXPEUThsJD21X+aIIubtWu/Z+uM/iwifXH4fz4gzPMmBpC
    vGaB02dZN12lWgRw4Z4pZm5ceYJGbPPd9OBK/hmnR0xke8g1b7lt/ENk5Dv0bM3bj4Olt0Hp
    QRQevEuDL6IGOdiUDlUD3AD4bUFQOUfCYr3QZTSRcI7zaxvZ2lXtS9I4Lmxk+tk/SnDN3qSq
    JP3AgrU2rprkxtjzc2ThFDGI3oOCY7wx1bVvCE5NuZVGDCkzj89rx+frZfRHqol2V+sG21bi
    pnprK7JtReI5kNQ9jIediJ6hashZCzRlaai66l9P3hw391NKD8aCwcQ/hAY9ALtJWXoPLvAi
    hRH2Yn7vshhegbdL/VJOzXZGQddTtLb+qi3lkn9o6DwMbM3VBPaVo4S9aaU5rDZA2Us/nTo3
    3qM65qb4UOdfXNfbOVZpQk+F8lR5jrmYEWpD+wEbX9/sgwWU8tB7IllEucS/SfFS2i4rAGcs
    3zNaK9WQ1Q3PVgT8PgyiThXVVETFXosllAASopijze6Su6VQDR449rwHr9Yxi9EXlRcgSAHe
    +aFWzEFAtLzNbjMPwaTy6Vip+ccBesq+rQs/zMqnchoZGq2+8bFH6PPHIeXyh4c1Ml1hwx2O
    W8LaCw10yyZHRjUxO5GpbZSh7ymU7Z5oktVoDO46CECP6osG7plZttRY+2y/vvHARtqfjj6q
    biW6QwXcIKZDK3bMBF6Jjt/A9X3Ocksc65r2vrTgNeXWD+6WwwgXGl5iS/2wSjvODjTB6Ycy
    bEDYUuIrSNA5CDICf2p3e7JV3+UyxfO5+FUYIrc9vlWT2bokouTthby0pHWo+xfLDcGNHssy
    k1xf/446E8abjYUFFmoIUK1hCdx0JjZ8N49jgWi6cZ4+BaNkGIctD83eSmpg/hmAmyTeSyok
    PwQfwNdmRMXVpMZiAOPILTo4INPDcud2QvAEgymWcikl5QUPoXbYiFW8oUSn08SnZK5o2ghy
    xgKYv3MMawImbFLUy2AgV3Y0mwl5wzUDtB6zqL8X5GLgqK2Uiw2a4ipK8c1av+bQ+1+mWioE
    DtqRCrofvzZbFMpig07a5oa9Qn7zCmjed/SGOqthoNqSkKWhb1z/+YI9GcGtcbEKB+RcsnBP
    iAp8lGEfzVRkYmUuETDME2MkhbFnRpf31oIVpl6gIWq+cKZNzqBfmG4aCMMBniC+ZYhViUkM
    GWgCsPjdPVkjGK7ejf8HIMOj4S9A0bD0TeRk2MjO1RpwNF+HTAefeN9ZkTMbc+/QlCxxLAWA
    xbA3pOTZpZLPVXhbFeer4h34xy+OaYvHm8rBWjqFNpUKQgVnHGxfPVtPcPmEq21Sopf0BSg2
    mrW3OOtPx1J5VTxPexV2goK6jSBGs0cFHE8RQTdqs7x7Kpwgrv1gLlxYTYywn6LTZiLNQioy
    E51nYf9CmsqVyhdVBN5BbSQ9lIEg0uven7BIx7Q9vWTKpQJZEoOXjl3R3gtNqZsw2SvIPjk+
    dqMmCanyURW7I+rUTCJjTw71q46y9VEFpdx2FEgCTpF642eRm/+THOIg7HT38G1mx+feTvxK
    Zh2SDfPZAvJhHiDTghaPvStbWi37yR9Yr264ImdLNCANbU6we8WpUki3EZS51Hd1yWBJ0mrR
    cYIRF7z/IN/T3yE+1PegXJAu3yOmUShGWgCaygTpP6i4Kjwac/alBp/QdzjIHBrHTsGd51UJ
    Mkg2EsG+W+cxLJM5H/4Scxccu3HBGski06gKo3w6Fs8Oqx3fI4mSyzuduu6rqBcf/0KpzXYN
    2bhVF899IQhxK02Jcidn7yQ2B7L6y7Ohcqn7J8Qiwu8N4ZG7++KBpaaYk8EjQwlhw3ghpFRH
    3bs3w17CfaGmq+aQKCYEe+Bd6izrDzYu7jfXxsdZyvgCt29fMbs5qCYMUDTNdAysQckyBzJY
    0pN//6I7OV+fV2THxArhuRMfm5CP8hT1Lpj568qtDRVp8MOh5tlEEJkkzv3wd7+X0jzR2qj+
    cP4gacUA1+lyfuOWefLBn6QKNKHQuaMymfHDr/tI7hVScoFwVwP/N39RF/lm01FHe3sYwreJ
    i3vNtHqxzMazd2m4RCLZ/YlmdTLYwu5Hi0kHulM07ChaFPETrj2c6H8m0P3Hxzf+SySI3nH0
    hBL5f7rh6tVIa8Qc/YNTVbP/92nHAz+kha6ZPg12ipfO7L/LD22nfY/t8PPpPBaGgWVhKtPk
    5z3/ajGMeOk+Um6qAyxqCpZ2+mXkVgfsMVhfF3YooZ0EFSTTYuoD4j/ayObyuyzcswOh6KDK
    WJILOhExAU+M3wX1M159pa+814uiwTjDK0Dlj3M9bA1FCzEsXUy9wabIyFeNZzpWl24OMEXe
    cz6VXZkrtGRtBNzk1YWOGNtG3AwOG7qwUHJ04vT0QuuRJT6UhDxBPzLncchBdQS8CnT5Zf6R
    LPM3wnZ3WtpAbkkV7LgQ/0jompQE+d+KbFwmSdjTwmhaURhuiNfq4keh6JMpAv4mR/W7hcox
    k34g061wF4KUsI/OnHI52vBXlPni2KJLW6OUHXPss3LKj6N8Uth7V0IgBFH2wwPf38j758oh
    OOeVeViNvNRsyExXM+Np3D/oGH01s+t80E8rzsRKGAXMHdgK21OGWxHN41fhDDW0keVJXKQ7
    rP8jhaRsmvFvHYtmKT1TcW+HN3Ot8lPbUZp0MtLwIzDwDzuIXPimB6+M88j5yC6/kw+ShRM0
    HMD3QMx9K9xFRuPqxVu16uuR0hsrc78TJwIC5puKYSsoi5vyrvXC9/D8ZW/vgtE69JxPpiPS
    RCFIBZypuvwaXOwfpKfQKp5reSPD1GULnIRiOKfUBguhaWIc/4tBmkPRSNrg0z9MfFn+ZT5Q
    XswZKLF0qCxu3AR4u72BQE4DMtK72/R64dY4AmTalG3tLxn9stpMDmmhpxxwj3Cs6iqf8mYM
    wdSLzKmiQHP6FIl+Qc6gijYVgWohS/gPLLwAPt1TXIdE4u+egxQGDD0XKgh74ZVbiKPqwv1c
    V5uQgHv0u5Jh6b+PuCelTyZ5LJACkWbhQJ71+U4OmwdAyrKvxaQBhvco8pafJMKqbK6EzrHT
    v7cbb7XtvtLWIuLfvTdg0Z3q8a79rUeefZcVNRLSTxDaP0P35s8+F4QmzZkVeHUXHuHsHajs
    vlW+cp6QazGkMD5JkTMETr5ed5PyCT5VY0j3QGYwom/BXolSaELA4iE6blr5GxdnnjwReWB3
    yK9C6LjQIxFMakuQVqlyfSTa4q5l16WfxNKCLWcpDQwjNt91pNPqx6GHPx1h3xDjfvQrUBz9
    Kx6HQNunJwiNXzJaZskuQqwfFvi2VqkUI5751yDJ7DXgpI6GoPuY0uZ0Ps5ODQoG7bjyhiVm
    n41V1Ng+NiNA8hPA4gkhCh8YMD+WnO/RYlfSIsZkVrMgl/F+JuSsVplPmLumbLTJ08ZmL1ne
    4adS4YS0FQe7jE3Oj7vnS95STkH6XtPrzuFHgDWhphfcFBKu8v89d743CMarGAicuSY2PJQa
    /tD19Fl41sn8DGbGDG4JZSNnxKBxwqNl/exkevVvLcCHGWVSpHFLollZOEAC68ZVep5vOhFv
    CmoHM00HDond7qMYTG2vHB+y7pY+BZXp3PKEEh38jiYfxL14KAslMpocNuJxTH+SjzrRSJNj
    5uu810QVDxe5i8GSUbQy2Bo2fj2kvjjkinH5zvZnaWRXFrAZPqOXMoJg+mw5xidHdyE3ew97
    oAnv/Inh+obZCuC7X43RZ6pwnAQNNhNdGXx+g8Yg9dAdv232i+8NjevKGLK7raEkevd2Ytc1
    nqbgRTj2AURe9Cnv1hnQEB26nFt8Gpxq7G6luzJB1JAMyZ3fN5kqOvABPKc/WB2VJhyk25aA
    8yyDLmWBXoy0Qw1QPeIj9kHnS+EAIfyF1IivWuTIp11trsEZrhYlIiIIa37jf9tiz5wtaJHm
    Aw1JeDCFRORnq6S/9PNl+C4+M8LORXg4lbpbJs74m6kOIFxtOfUElek3lP/3vNU2ZxZAlShF
    PFKDXVht1LdWpgk2AuqLL/4ncgSBp0zuZnE9Mt8Fp6+ofblpKKnpLCS7KctQ4k7JcFmve1D+
    YH5Z6Hgzqj9oS5vK6sNcj8ZLJnRjL/eI6plX/1ic7eeMVBxUEiJZIae8qx5Pq/t2PbXmREVP
    szu/lyudVWnKoMYGD2Lbk2CJ6aewjcUayFlhv/t4sTbj+wsGAGiCZvMuaqXf7zhMYAWkvcdE
    r1NzgwByxSFipHKgJnLg7KcVeaMO3HNv/oF+dPIxvem6Gn8jmiFb7+/OmWKLuUm6mL/6uAjq
    9B0R8h8emNGIJrT2uD9PgdweEUHvRscl4FaFVQ1TtsIcACEyhzmiCUoJHYgO3nvWpUQUp0cE
    rvypvx29lwkJwM47SbKPVYkvCUhT5JzM7CQKQKtpDIXzUbH1B1IJKYHfaNPEitE53h+9Bl9e
    OYn5TDlX0ztGUn4dxeDPzK9IuZ5DrtBnAFZo3Y/tof9qSRzjpt516X3lolEEI8pVYKaTuw7h
    8CMgA+MSQ7Q/FOQi8czzrjmlhuXP+cm4W+j/CPhGH1iNo8X3xunC7TUPjQvb6t6k3RhF0Hxw
    etHrnQLT5Zbf0oK+PySAO087/qgaL5/l/sc4OcMjr/KtLAogofLKjMjZLrXCko1O7Dd6eXNF
    DvjjEpGnqOY2q76L4PsIDsYRA5SGHsS7T03RYF9EXKdhZMQdv2dp65USZNL/FwlDgINdfyOe
    dpq1fdp3iJd6ruR6EohMJsSSRFBCo8ObaSz6LDt6oxGKjcVN/mtuXPL7AyQk29LQHS3qEatw
    dvIZ1Mupfj+R6NclUiqNOoAqRfyCpQuzHuPl4TYzlgoPGPaa93pArUOdTbkJlEiAJBJiMbZA
    Iq9QQ1NYdinihG4Q5xyXdSmpNjvQOwQtNfMvyB9NvEXPsbkwclCyT7l9QWUV7PWQmJ4cvDg2
    Rwhw0hg8wXCSdPL6CTwsi0+wkS7KKvelk4wjAmGFqYjwLn/EP65EOBW/JIZu5/AZGQ1HOuM7
    hAZNN/PDsI28C33tJAChvAUgVNMK5aT1gYr5dyoCqIT8c1Eos95ngxb7qDCykgJII2lKNqnH
    Ao741lFMcAEP1Nwy53fdjwUdi3K7DQ6R1yNviXi75EaL9jzqIoJuDnz0AVJD/I1decHUyzRY
    rLoENvb5N+d01hVCW5NR2iUaphYdrzca8yx7+j5EqK7G5lDqJo3i7HnkuFnFwmElfGymCQt2
    l1JriPbYBvvsWRJ7l4WEhRF0BtPanQCS3CKb6tIMPdcySyNCImVmCG8dTfO1MEEZCF8PMl2o
    fmS3kQASSQ8LkL5tMXCY8dsxEmwnkH5Hg7n5XQSdkc8jxd0AGNAfmRBm6IpqQV7aHjC+c9Qk
    o5haWR8GMeltT1F6YLZ0NeBuToATzGH9HnJKtesCJmVuMKtYaKkFJLYOVOSUwTitM1vMG3m0
    qA08sSL5lo3jnwXCacLy2AiKHgCk5hHDbh83U5+GbakZC5Z/SONkKiak11zXnUeyJCzdCrAd
    1ZhqH6GE6fW2BbeA5m8McAWWhGODEmHQV6Q44P/sEHohjJRBIP9Kj+NZzZzCWkQSSHEurSWY
    Oa9Ko/Ly0gE6wX4wKtCr8awERSl97mhVXWB83ycN5PlQGqaqAEEfMDRBn+MbbTFwh3Kb6NvU
    TpXXVCrIsVD9YFfUWhSMB2OBgFBqq4y1QGQX30EC8X80+QZqdTOBqUHjL8zu02wFaVrel8hN
    wbn2/OfRIBHZVvzUWOYKFyamnnFmXqDWkZ9j4SMqwDOuWJY/Y9v3MPjFx9wDybJHT9liJNF5
    w1LPpwG11r/7UfiB03CP7l5r+rimlIoZ1O/0u2ta0sV+IDan6Os5XWwtVLaWnElw4+QR4Wzf
    cpPo8Jq7gyUAJ4FRFluzX0opPYJQxqDeyq3YKE9DxaaLcnYwJXOFjhMd3HKk95RUTjwSbVRl
    F2Z86cwX6M1INwH2x5QrBiUNOkP5Or3orIVJMsv1OZoTChqVqbwq+0zF1vf05RIyDQNyUm2X
    5x4XuxUtPDeP5UR6/H8f7tUwUGIuBQDNu1smOybZoSVdjEJ6fuAV6wx8j05EBNwXmUQV1GQz
    RUCvaH3xu21vzgSWELl2di0BgBleAYDLalmrgj7LaljgVfWjFqbw6x//dpWloGL42L0hu/5s
    1Fd9FxLgSpRaNdVzoiiY9JWC+1IEzpIdnFys6/XvacxS1fAW6vI/PssY6xgtefT0okgYw4pZ
    bpdMVrG7TXU/NNgVaRcyiKpxopsvuAdqyJSWxb82whEXdYKzYhvqKzwII8CpAG9qdb9BBP2i
    DqCjdUdpXP21bFwKxM62fNT4RiLCZa5Y3Vss546cC9kiunNGOroz1DK2fRuJ/MOJZIFtOH37
    Bo/1joiJ1o5jeg+BvXNgVbAdQl7viJVuh3D5gbIpLm2av0k8wuLbGXcYAdn1f1Co/6xccRn6
    Nuut5RpxWB+jstAhbU/MXgY4Bl6pM+FM6DG/I1VNrshF4pAuU/TYMxZ2HI5sIY0BL9Ny2EKU
    Eo1kgcTh7YJSYSci5MxYLZsNi1ng0uHQvTnGbYiSQBK1SltPxB0NWjCsyL2apKGkzcpU4tox
    /FyujV/iuISNPkHlMwNJz0E/AxwfOgAIXROwUKC8qjquAnZaZMPx7Znfuhon2wJo0tlWYGxz
    W3Pt8Fp85at3iZFcaLhOLWqzpcAGuMKRY1FNs+rxhwkxI6OEambkLgkA4IC37x+64fFVRffp
    aP0HMKAPmVFEIa6+ZwbWpNqR/hzrwIa0pA7bsQUW3pEDCVsf0cW70SeZiYw+CHviKkgh6BlM
    61ky5uC3rRvCr9NrauP7elLYorp/QeWD40ONORsD9lyjSfir9TAUWFiHTGnOj6VZnM/FlwxY
    tHGEulukD5KnmyCHJdX4EQpvOCyw8i9BIfbBt8nt0KldZdw0kAmSU0lFyNth08lDJknLlwkZ
    /25uOorq2Em5LO7rQbLZAOSVE+XzwmAdC+K4M5JmewonUr3MZ6ehiUw0y4CyD30w1lXBm/nW
    yeGj+i/Q286qWD6C4cOqIjFD6OhuQHP5OdFXWZKnrJLGAONMrdcgGJr0cPQaE+EgV+rAXysh
    K8cxxT7i7bLEBs+WJzcI5lUa6os8MQm7s/I3M+FP4ur/Q3wn8KgDad2p713tKN6knAfdZb4v
    MtSbDKxRFrSHa3/VunPlmebB+z9A/RVmzYcOGQQGib0+WByHu6sk3neEemGlF2IH7RyKTIVT
    gIVGWqAnRxSA0AmAHO1MAOLYesxDzP21UjL6p/wyLsyOFPWpdYIkQB7r/R98nF0RZXgAs1Nl
    hjyGTw6j/8CRedijpse57qGkIWn7xvDUWwXDhMti9L7yWuOUeqTeytd0dQtSFkqqyAKUTbLf
    oSKXskmeq+cCmV3uUCJ2Z6uFRPQ/xLF6yNkacHTL8JluoGPNaDPJNkmv9fqB7uWv0iKuzoML
    XKzuL/Io3GE6M0Z9V6dy/91xg9sUcCrVioNCQLLcajjF20AgI16O7gfsXS1uq81+x6la6K/J
    O7VfaMMVNfJw3qai+IHG98KUzEEIA6oDt80hZHjHSy3j9gJnYt/DrL9dgjvnPZUUaAZdYP+Z
    VMeYeJ7/O3UQO5UzHsX1ppfIGpSrXDuEEBE6OT/qmCObUrMtVRAmH9bK6wU/8jDY+Xg3utef
    7Cl+btqidomTyQIrKAHaC7WCH5wELt9tzNd4CTOAADGp1kzzgljevREcge8QB02PVQEupKbP
    LVg6IoAladV2FIQky8BryhiteJ8Ids9VTnMpAU/CX1uViGvpgHNvR43Xj446/cbOBX18nYJW
    enllwQ/4I+4YYfg5Bd3vq0p6UoUn1XEIgYRTsxZ/Tp7J6/7O9CI1CCbT5s/1mw/rTTLrvm0F
    KV20Vtdz8K5zBj66auAHoul8JfAyBrcEyZENfV/5erU13aB/VJZIigdfwkhzwI1OQ1olGvr2
    T+5tnUfehRqjadRpeHQY6HD4H9S8GQKV76xbTlNwRTdMV5LUI6AitrmudXoqs0nxq2odZmyd
    Z+wH4hYvuCEGbXRMOVwKFJ5hN74x1Si0jI35stDAab9Jc2bIj6VmtzptkUpCA9oFbxFrDvCl
    BN6dhnsVdeGigZMN6KnbEP+ixXuPXy0zwdQj/oMHPgxnqAlDVmh9p/eo+33Eq8aoZsxZfQq5
    Syb6flhvRQAw3stS959ipMobxSP3GYNL5sGf9f9PtlZB0k+R2VGnTruAAexwC7Atm6SJ4MeG
    h1Y9WnpTp6mJfMRjriTG09AlM1hSSlXJDCCWQS7xqlXvD9qbZb0jQLbqFenMmn7qnYIcy512
    yuufSoltQw1zhSWqlj7XgdNZOFO46LzrVJSfWi5O237O/QVcX9/QRFNwNtH7F3aNZijS3oNY
    GgfzUdxnCmjdwgve5/AQegLq1WQwBB9MGXjUiycnH3q9AZDK6rJY8O9yWegxgAg45TB0L8ML
    jBXCZmmEgIIY+LiAe768TTstwT//LHVWB5KpqPqMtCRHrqUS3oyfa14AbTNMTcRAQM0XxWZ7
    3SuaC+JKEeF9SoLA6GWy5dlvTH3PNwtnlEUA0wVPRLhbjpwl5jrrhaj5D/YEgz065l4utivN
    rGPIk34rFwgjQz/x6kSFR8Yv5B18Zn4DWyrp7AexwIJeutomr73q6AxJWfe9zwJ+B1YG8Sx1
    77pdv74qW/z3VQiH4829uge4SHX+1dPSZ9uEZV4Nw3sz4WICA9GK3UbS1gMy8g+r0Gn1ikok
    bwM6wsusBD0El0S5CJX+123YQA8wqrSAt/9xvc67kTv036T6Ceft6tSvZlaSQbrbV9QX13yA
    0VjZMaShcoMUepZpzMJptrzbd2CHKhczGIA0jVL+2RA7pumVRGpJ+dMGRCUVMCWKcAa2FFCD
    FXvKSuzLRf1CkKKB/uGasPJ04aMUBZWgdgf+snju1/ZoCvHjrdYnyYfDMQl2Gpl1kXN7V/ru
    TU8XFmP9XxWtlRJX31xsgMsU5pNndorW8l+ax30pRXEa2giv581o3adaA7a/mnD7ypy9gLcu
    o9tY/VjEq5rX0XPuKSA2mrIfo/yqOE/Yxt0YJntrRQlU3gMVMEQtj0eSte3IASCb+xURsx0f
    0EvwrwIVZdN+3DtkWCjcIqQ/ki96h8YanpDEeRdAnzK59n+Y6Za83CUfKeH+jOTCdOSNQ3al
    JMvo3ZABxZVEt+x1ZBmcUmu0C+CqAu5xfB/7JYP4X50u8U/Zcdx4b1GCvEaFZUm5r9pME4RL
    N1qi4oOHk8oSc/2IORfk9ZzqGbcSGIj5iW4vbCqFuldqpwS+4vQ3j1R7KYyt3FNWbE60uRfA
    dv/hQWYpd9UkMvJf6102pg2gOKGB1xVMBj1I+24MYsOgHthkelX6mn/EWVs7NmqK0RGy+Mlv
    zt8PU+vge1Dk4VpGsaEAqSSZbMpDaBsQXw4OJDjeSzaYrBf0QLFxJSG/meaHTRPthUFWWYcC
    OZkXygt8egGuQs3ZhkACjAIHJfJoAl1IlclwR2jIrSymv7BAt7YdTGyVAtCH2/uiUWq8Hmwt
    2zB/SOThG8o5xLcPZnRd+a2HtgbFleut3vOjbUDC1mDfG4CUwEIjHhniiPjRFmRjqh8QHAbH
    UfCJf6FYGKtzKcQT9n/gjfI+6LQtzUsktL/fO5h4GB9aFx1wUZZz3/okcp+jK7NGJ0/3SgjR
    Pqq+Rhx+vE1Aw2Dmnbe9izDgPhFv258cW4g16lMkgvMpNlNU4HPvscYpTfkGz1HAgNTT9VVp
    mKY2IEsH0XUyKNMBba3K8ZQscutV3JUEffeGrf3hI+A9SaMifyZod9iMpW9UZAtE6eyUmZSD
    3uLDG/zI+4pslifWIcYyhvsrbY3pk8MUJqps9lSFwYNp3VVx+jKtlzDt/Tsa6dH4qCiMKNBZ
    2EIIQq2ZoJEJmBrXNgLEz6Yk29Y8cEVgQwRION3e78iZwpt2f2qoODoZGd6fvUyxecGPRhgB
    K+zmClPDgP4y9ULmUIGHk3HpR2ZMX6d5BN4/3MD+feZAcC0G4vaymdQ1R0+1jasWoJKdsneH
    et7aqmElp7Mv7gw3Zyh1dli+2tslGGdMZmIFiTBL+hOy29wzDgsTcLC2zKmcLlqOV0+ktzjx
    xgMXgriZV2mqZ+MUo+tUIg4ZIhMfCp/jfjnia6U7S6umwiY9VftnepHt3fDrvbm3jQVGU+dC
    mNOnFbB14zbi17jPjReA93dsYsne6Knd5Bu1rhO/y3RUUJGoPN+ixdxS2KBmkU5mAmGy5BpA
    AHupmu0/4g+DhfAVCycR94Tmi2DYgvCgJ1O+RSdSSWWtWqSeFex1Dx9/LNy43sfZCaUjj/Zn
    y5VBJEzGemJRUNCzB8IWbkOrz5qcbczLRpOuRRgC6VJkH1l1HXcGGfcW9dHchvbjsggioPtG
    5DINldpdBV6fjDQE51nZZ4Swoz6kG5wXA5FGcrq0ZgkAB05p8vB4Yx5WezSBuQlMyqOEuoN9
    cOC/e4Cj29WnfoMF/HjJLDgNzge0aqWswtvV7LwVrcXu4/F8eeDpmfqYyf67QKZT84RV+sEX
    4NHXqwH7nWkWT5BEvgVXUki4vqTHQv3mz6/iutYXxV427y9faoMLHRKWcu+3YmSi47KTVKgw
    6U0MioTsqAvjYlC57rw2aCzu6cU3g4tI+n7F9R+RtOY72PLVOh37yv4CL19mm8tEi72uoNBi
    RZl/+Yj4otkRQqiGdmpNzhZPzGmYHsGhWu8Cnfj3I5nvGdUyeKkkvDXqHwkX2SqHxeRsSpdG
    8tFShml6L77bF7t6d8jFfyQGorA6ZQiUns6CfDgtGUQBfbR8ewbJJP9mDg5NiyllCmCW+fpJ
    XR89fqoVPZ3EcV0W7hSzVVe63dv85s2TjLnMcw0fhE3LSyq4t3bTOr0p/thzqqN475uaIUn9
    j8RrstjAjJhkMo1nm5kKAfQLPwuH1DDU54TLcNbCtuNVg6sCONi6Lc7U+c5opClEIja6okgQ
    YCDiwmdJWQA9k7s3Irl0/hF9co/LLxQK0POefm/pp99M5Jq6tB3FkPw6lJGL2oZ151c/v+dn
    d4LbkPeyOYfAlaClF+AZvb4ynOip8TwznVdAQgosBi157FwgFO4O2eLIgBaIRS6MlMxDZfIC
    eiftahPVEzpUsQ6/bX8YdMjIzUMbIO/slzxSjwO1dyePY4neltztg3zIUkU0xCpnHV22vX3S
    B4M1r9jv+8hW+Xvxf4ePQFEbbd65znf9E7Foi+0HFibDSzSrYK4shX2gwmvfD67bschjB1x7
    nPHbX2+GbH9liCewzR1jVCQH0zXiW7/O2seW765G5+L5UhTilssWjC63hmt+f1Rk7t8EHD6z
    qdMhn7gqQqRQfuKAk0YKre0Z2QOeHV2Mm41F66EHlGk58o8QlYOFizJ2yytshtIkcrYqM66b
    HlQ2WdfKJDBNdTes/atvakM+nwUDgqBVHYoHdOTOcFJf241AYcXxnoDn1S2hzSUI9Yo4yUTK
    wH0uDFduL4IJ3MN/5IiD/k34BXblH4MMSPWZZbXg+ee3+bq0EfcvZ6/NJDEEu28MPzvZDItk
    zEe2gIxhOR7Qm06S3KnxVDXYh5iAWtia3oiJYokv8BMw0uR/+2g8uAyPlGYD6uQNjkguYpxY
    BQDMh0sJ+oRzJLW+l0+dtGxC0DbYGtu51FV9+6Uq7voCzJqTuuR5jay0ZfvNlpAlNlouDbyP
    5hEH15PUQz7C26gKrHWecCOq3JhHFvLVsaHWiBfrREmFzb8nKfm1DSoL8A5ZyYgWAk3zKQk5
    GhX4WBoV02IXNbl5j5DArHuoV3IJEIvz0Xt8Wvn8fGpDstoelpcIXRvBPKAnfuOqhadRmGHM
    PDU0uzyyN9uk71YnptBmHck+n/Urc4zKVv/eB3umKGFxDGbtrIu1XPVjyP4mtOdt0GpDc1uA
    xeERFmwEY6dBKYbGiECeWKnLRDeglbNVuPDxsMSQpWY2bcTMkviwNaTrRuvmbs0vs36tnxVy
    013LgbSBoY1VKZ0OlWD5Jmq35xyzSYF/LhfoC0hZ+t5X8GT1RpE6klxL41iHofXmJvmj9kg+
    166EQCcc06ZfAqrsfrWPKQj9RMJSbQJ3EfoyqNUurM0osUOt+u/d61aAWKWhLTXRrlox/5bY
    1Ykewp6FuKwzxKr4xGML80ZyEiFyeOQNbwv6VjPnLgZFL1GUHqXFCyVwfXps6C7Fdbx+UpXN
    K7ZC7NXlybZ3c7Fro6muMf5TWchM15RgCFMPlZq+DgUoV6HjTf3jOmJiZsddsYxNKF3QAC+v
    YznUYvFqdarUe8dG7x9fUT4RGG5HaroSJII5loIceEJh4t8ECEKcMYhKYnKP9X0LqD/ZJCMH
    CXp2duDRNQ2jh0qU6Bq9uBeLJa+uKEhrtOlYzL65BFbnde0pHZFWIyNaznG4nFavAZPES5eK
    Ke3JkWoYBQsvd/eS45JHBnq4wbmtdtSnMzlJj1F+xuX/m8Q+ADe9xvoCOngBY+44xjMAmY7a
    plWF3ESPTwKe0dG+nYYPsylon4IotOOX7A13foJN8nOM9Pm2tspi5tvMyPuSqwdUg4JKPecp
    HjluD1TOKxlHGl2dqBD+Nk4v236gawcl29A+KdMsPshdqHl8af5i69ULQdWj5zY0H+dsenuT
    pgsN9gRmsFlF36L1hePMazRGBm4alPZk0qbhemkexd4TA+tjutgjrLBL5lkkXcJrsxjz3FPU
    hVvJw15gArGeI5/4Xh7WWAkLeFDpLEgWENrRayZt4AgLETyOAjFL3++caFMsGPuqhRqi1xzw
    0vMvrHJA5bORnTnbrq8x9q8xJCXb1JkcjWSLTfslvvb7XqMzCBCSDt4SUJ15+j8eOENI0vzc
    z4fyQSwGwM/bLi/HBCod1qeYpNf7YAEfGweKZPSuexo/HqGuMXXI9nrVAlNAV6LHWci05D9v
    ApoQdp3YSfuayipYG3sTcZ4T/Asrf1JLPAyDbWZJ7rALGKEUk3JYe44rcRDDF9qkWJnrZUp/
    +GPkP+Ck6bcuiVPdAp2pHZpQ6HrPWsCrxSa2BHM1s2yLy4MrBgc+h27BbOEfo6Bp936i2DjU
    XdwkaPtmm19uBDjssr3xzaTy8FVf/1rA0Vg75QQqyaGKbItcbqgPb2abDurmfVIsU8cQLJCG
    I00LbhWBy+wp7W0meGpfHKVLzxFYUJ1HSWhnphudrHK9TcbHkz/a2drYipO7w11DmAyFuGR+
    k1p6VKJ2GOj1dc7PKnLmW5e45rYVh8AKNShT9vp0zCh6aTFlwVDuWqwLJ5XnTKW+oJ48SQ0z
    oU4xPqBqt/19MSMx/Xid+swvOkFt4z0nO41wzSRal0Ouhsrqt/QgpPDmtKJGY3HUcnp14xjw
    mBmBswJ14tE5TUE7qQ7bJDj9yemJLMV3Tm5CaDMcg2DyCuYnDAmSpWRxSYSBrBW6gZVfSI8A
    gu5xUgNiXz4kj4dbM3dIiFmFXpGT89C+rqiUNjHjbqhmzFlgPslS1JOaCvCJSkKdqD0G7DDQ
    VvXuCPKWMdyMIRMC3s5ToYb3wRsBtRwNIsw06Hrs9eh3m0pyPyuWKtO8kS5oJnwL/TGOC3CT
    l4YApHGvvfNLYyBB1MMAH4rKZui2VTr1tByElW4fFkx2i+O++QgG8Qdyqp/tQtwdK/+m6VhH
    ExjPJuTzX2qQfuHJUdzjBS9w3fvmtII2XPOl4zRaf7qg4A725xSAhp3YUYorIV8w4IF0qdPn
    1JAkk7DCclE3Z6CXrej6W9JK+7POZme5NZJBBLpBa0xY/MwjEfGa9nCzXCHd8ZB8jC4Ute6/
    WRRa3U/U2jZRKkUZ2s2zHbymlrNbdqAff61b6YOg56D51UKPzzYmZAA1mDWw2sM4Uf0bRR3V
    IX02SjxiRhWRndn3x0PsTqA4d40QqI59cnG08mPF2IG0wJHJ2Vb0DZGP7Q48lFiOGzEOW7x8
    sTZnfdVcedSAz72bGGoO52sZ+brT4lmeZ9HJ5M+LQm1kLdChbYZwm94bjxsRhW2celhCd6fR
    12aKVY8O3LFYkuO7Lu7cbd3J3hlR9xIEGvqXH+Q4gyV3l6j8KBgl4kY00E1FRmKEUNy9srZI
    gYeibDIXZVo1RO+AVGnp8i7V2SEYpKcBMSg8xyuPWtXBMz/PsCiJkEfMZ/Rj3vAlCVTBMntV
    CQeE5coZotero0kvK0bvMdUjuFGr7W4pD1m1Cg6lK8q0LwPJib/K0i50RILmnq+C/zSbwq/k
    YWrjrdm09HkfK7uWEvhhcHDeuo6MAZm8PiXjCIyR6SYwen0ZLwjT6XzN5B9CImOTeW3B5Vez
    gI4q0b3tnnKernwB616DCpX+0AaZv0yWnWsDg9KkO8j8N/g3NFLe2ScAxh4SXNECbT056Nd3
    dgNbRJ8guixeN7VzW1kXZFDzadO6YTvRLIb5ffa1/T52SHaopWfaxD27isqChRUpT20yBrVH
    Rt7Nebpk8+8UZHGHay8XLm+HJd22Zy0Bt5VWp7Kp0JU0P1NZBRfH7wRyfEkk7b7BYROJOICu
    JW9Jf2+M3Qi7eWgmHiTRbPB0hrg2ay7jvD7kJE+GgmsmJWccnAj7wAoMS3xCWfZ5eurPWOco
    fnQFGOt8htfX7IpNaSog2DdNpEnPKLouOZqyvlwn7Qf/vXDjm+a7zi8NXUEvn/mJb9A831Dk
    rOok/Xcsoatdzthm2t+FGTQqhgUFrNz1/FyWWiZ1BrdZ5ejwr3DCB1wredi3MIMPE1s6Gq1J
    DYQ4BFZLVKyDw8ii7+Le13dLnAXhqjuO6cThl4vdBbrXjRX/+1pqqtBik1aaa+3fSUmfAqA5
    UDfdK0pq7uk53lpmGeGkKnYAaPdlWUE62+JNB6sPjWn/BIQaI0MOEyzuerkROkfHR3uP4K+0
    NUKrTdkemJG1vb+pWDv5KOLasTXMOhVB6+Avs/9Z2ZXF1HI08CnrkIbMYuYkHkRJwTHt71J/
    yTudex+sidGFDTfjaBaDjVApRgFFYheCWk/oEae02NmAI/v8USlLUZccVM1b0MF6ndLz3Q6a
    h/Uqw6LzkCOXY0BNRqSGosyswl3+d5JZeOrM0LEF1Lh4YnPO+j+uZeYmwgQEq+WjAC/t7bVR
    o+DKuE2SVbjnlhfmQ3Pvy5y1yfgvHoJH9+0uCHXuq1xxO+Mzxz0+2rPp2/x3FeGudDYgPQFM
    +LXxLCXNgIleBgXNbb5SCyaiHexJSTqIR772XeTufb0SMEJuAGqGxM5Ea6kJu5qTMrMXaVrm
    Egrer+LEy61/Ob0xqwY5vlGfBnbR+Ok9Fmo0ZCXakCdaZouDFSFzuHTed2Rcp8R1ZNoIeCed
    ScrIbahFXuagLLOND0UORr4Q1k+WVJPHrByQvAlY+sspfBd7LRjmMaegWo+zH6VNQaGgxkCE
    RaMOAUtixCl85yQrmSnZUoQq4l3B1OuDU4979yqzpxra9MA18Ajxn3a+I3GA+aFgpyvGB2wH
    Kv41SdGJ/U9SII/EaI+8mBUiQhmZyHCsjkU4xoxAlmdl+ucHVC5kQ5iWjMtjAGvDG1Zy5r7t
    o200BIBMQY1K2bvlBYQNQ5nJ+EOB/mRbx0KPSO6D2HmJfMnWUPPszRftQYIJ/8EUc4pbbN7R
    iG3Ka8Xh+VNCd8P7K+iaMkBtdOlTuOKOf02KU/fBEA65k2088Q878GxNeND79tm9BS1tTOY2
    XEmGj3nB6zDU1NVYkyyMBZgrzPOiT4F1b+oUalhV9q34U5lEHJaEJI8RJxRmDfMMu7JE3HIt
    2n0gyxmGA6FDsbdVy0WmGXPN58LUE/Bq/i3oFTV4JimPnIxbzER1EGE9S59eZ+nIpb2iS232
    GnmpXEiKyCRBOMgcY6bNvWrsRchw9hgMxJ4dju8Dxa5I/gW0t4WMj06cGvHyBst5TJWRtVXl
    eZtDLM3TfFTlHeuo8tvY2PiXcqFXZS7Q/dsVbW7fIhxvOPRgqaA++8/4XC/T8P5LK2u/8/yn
    ksOyU36UAUUDy0YDHsnLnSPn19YQmagtRtCKTRu5iBiuAJYAsSvEb7tgG6ri3pbonodNZ/Sq
    a5+tacWTsyl6RS+9BvUOiCfCN2DxSt+rCsG7+5brhVKCM5lulyU1CKQc9WsZbhsHWoz+E+hW
    dJvJD2ReubSk7bbubhXjkCfphWrb3Gk9dj9RHwchkC8mie/aaQzlUeSkgRls7qxkjB/UBi2X
    snA9HflcCUA1z/BchvrDpLqdbrGeHfY/TK/eVPA2v9ahhayZ11e1CdR63cWBZ1HLFbZP+75/
    6DIiS6kdd6fsQg4hm/KQMdC55SuGaaIwltQsFCUjXM3sAZzzPnwEncc16YKM+eE1WLOJRM9N
    t7iPZ1PRQW6BvWLIbLuoET11RaKDm1Gc1QvE27bFu7ovu72AO9elr60dBoLFOOK04JQFDs+0
    qzX/ydE9SAPHg3Pn300Rc7QXtbDfdJzKDEXRypJGfjgLpgL0/bWfug0DxgKhZxBGHdBgMU8E
    ROxrsjmSRgbY0LPGkzGQGIEZjDYIW6Xtq6zn4v0lJFsBSwhVbCcxDmDtbith/BLH/S+gpj0n
    j4LSBO5wLwidO9j+qDqYyXOn9lelT76JSaDhWvjI6LS+qqM5FBUmAxZm7NhUocsY0vdMIw7p
    e501qiK6Fx69P8PLU8AJ6PC09JLhqwxqYccMgPgCMtxSpOZiDeYhMeCYz+uVah1mEVqEQfac
    HP+aNtiJdwSarMn8Ev/ZOoJvQCVfkZsaRWAg6HgMSywwPF7U1e8jxovpMSAS9i1rxSo5qT4Z
    AbMwKYeOFIgWWOcRHtbFipUbE5RP8AxEx/2QUutuVHc2uXJwwlJWPgHU35Vi0woompjizqLv
    p+zVnGiPD855va6c3DwAVrKpXpeh6iS9J07gy1xRy5SfNbO+iKGga1wWWXwWi3e2P7IlFpkW
    STTg9+RuQIePav1xUsa69vuO1YratWnQIYkxt7g6J/WTu1Qo6ehPXIuNhk1UE6zPtgRFRdZg
    m5l83bqlL/dI39+VCnqMX8XfDLG8IetcBJxU+ZHV7GoNyOnZkI4XhpfLrsccYWZ+QkYBg6pE
    sTHllJl6ZHSfRS3BHILRTiB7aCNLm7GNlFljP1eyiq0paw0FIKJ2768cbD4SlGeoW44hg4lK
    X1ThD1KtuI9OZgBaTKYb9+a+GOqXaUJyZmPGkgblXNHLPioaaCpFvlnA1+ekMBN7O51lAtWe
    IqYOta+sm5Vmitzr+c8dnRcYOrm0esQnP90nGkQjVKRBvou2k+H9hK1OhXng8AILSy1trn7a
    xlg8bl0GL12ExADqpmw7pc0tP/sqR9XBtosOumUJlCuT3Mt9CjlM6TbHg+PT2y1Y/ZPPGX93
    CZGO6l0r/HlFYT29W4MILdtYzhiswMSowXIF0h29a1xZAJYPz2gDGwg60SiDYWBWDgFCxMMB
    F4aHcIoJMNw+BlD1gInAdmyqKDYXvKDSmtrWMmVpjgcDPf4qp1jBuIW7dpPYylNAXnIIfjvb
    R0d4DC9Ysbm/g2c7PTvJJzBBHprmWNBwMwV6bfXzUwWTt5+SNPul9yGdC2Q4eU8lAXAR5hSw
    XuurwZk5dR1egh1izbWPTyRU7XraVEjVtIWb7FQZO1miO/eTX4tMpx3ZAkNYDihLScsgB7ah
    Krog4WPf5ZxSYc9ZkmUifmB1Rc8/gvGXDvJg6XlT12XYG4jFlfBrvBHsWXgb2dBv7dZ/2RfG
    zYL+fjC04hxGk95kCJvstZeMyVJ1Vidz+YWRV+bvTQtWg9Phz9cgmjLMtqb+ijsVWjngxzEx
    FepTSU6QFVlA9EPcc42GRhELYWoinc6Ol8lWLq5EaoIF0ixS75p0BM9aMWIm4j59zl9vCs9i
    jUUe0umTont6BLq0xpwJaacGBHJ4MSaV+1h1dP9hU3lP+/PW+67r7P9TVnoFRmaZccZbigSN
    DB9RJaIa/ljxAnizacTNRoPqkvrmF1UgIy9gYK93gF5WGGk3hltsecZ4q236HjMoSnXaVtJy
    bNaBCaF9F1o43Zl7XNUtyj9pDNJDrAlJkBiui1YoNoiwsLQoO8y4tHPnHExsugP+I55FDN5+
    PxIgixQEpuInoOmBk24qH1CBxYleyAlQ3ADUPwvppcN0gziLdI8BlUz8HSMGJ3rkUeA4UMPm
    Mpx1xtiZ0U1belTM+hq/wB9N+qfh9pVtvhNLmD8eju05LwQT+jBJZt4aBS07AKscb62BNjK0
    eNCU3UymFZEVnEJJfA+mzipRO+SmD8UUcaPIgcG/ldzh45aizM15Lxgqcf4wctVl6T7PH5kp
    hTztznE1Z+vVQNyhxu924QYshmY975/tzK0u3P31xs7iBwsfPWTEnVmWlVarPN+fyrtJoudu
    EbdUc3FXi4NblKMOxHoh7e+CyrZk2X/O+QLsDC3XOMnAUCe39ZzPVmzWwHIQzbM0Pv2RvQu3
    agAAlgq6jiMbrdCXD+NebIUlOMqwMHGxruxP6fhQlQYfTocC5g6BXunlhBr6uidSV3rwjOvz
    j3QFl79HowW88LKfHKi5PqvmVHh26kzG571HnejgitG1LIw/MKI/lbWyJAfpxzLbUb3UOWyP
    NA+9HUETxMGZQblnfR6mey/TjqcD5rUt374UMcTAKiFh6cydu8cDFa6J8pHK6Mbzcuf3Yp1/
    E8XVm+CNB5YdLHhvGjvTqNj3ttk0XkdCd1DN1qaabPP5D5Z3kdk5ssp/nvwZL1hKc0iLBj2H
    7F1H2AnscWfqCBXpS1AVA9KJ0zyuTEE/l4Jg6neKyr9l9FXhryudEh0QZKFHWWn1DiLsfEBj
    dG51/Ii6mNZpMxr7XCpK9fHmVg6C6C57bVjo0UxJLdgfseSQh9TKKnPqIlGYMVUiovEbhsia
    nc9qjXcT6Oe+vX2rsf5xXDiZwFesDituN8bLGroZ7uJHrpCyQFKp8Rb8Z11xg9HQQbqL77eC
    NbdfrgHXXkbkjo2rBUpL4U//Nn+0loIJMP5EF9aCVyYmOCyy+iE7Dqc/PtGAT7IXDUXCon64
    CKR6rutzlQKfHq1+8dLoTloLVA+SaYEkKFj6MIdbFaa5VXKouhsqdwY+vBDhznLD0GxGT68C
    ne3E1YCXGP5Eqw2KN+K0hnfQxyDVfI2AcudU9HLNjAFyHpJe/dZy+0WmifmsJ1uXtfZEGKdd
    P/z4woF94iYNgJn4mcX8+AKPE/8RLmYgkfC0sJI5thopNDQgicPUEsK83trvSBRGNoyNruWY
    PHdx1ootUFkKGk8RWnQQx8PzI5nC4GT2g8cFSX6vuK3IFYKhzzOfysYm3On6YXKTVSmju6Bb
    b6JGWqMgGaFrTy1fIvMZMEkDYxp3wEOMiqwQZMVT2HiX257wNR0eOG4xBhhmkZzvlQ7LfUUW
    bBDlg4/72YZFo+nrN79nRw+R+Tyk5dYpMps7Gz7/dfiwCTqbLgLcIzwvEpyRGp6BsbiDqUHG
    UywvQY3XlqXlRQrUNlXZ3mNR2LryE0JRYeYCIy80JFZnyIcGJduSr4108Q52NFFf5PpPs8hi
    Z2iJGYFpEGOtjmKwnyvrQHhU+QCW0Ks+1iWjoXcpgVHzL9nSP/5nUXCLMSdcV8dO1875TfuN
    l2Fnx/AizL9rAqfxQzeQM2eS70HXUo1ypgJSRNnIrl3KjlSr8GEOsk1mGrlmWN7YoKKtUOn4
    E175AVvehcxm6NFnAakyjysFZAOiRZYh2jLPWNjVzyv8kbB0v4GrJf1gYbMPOZ4YOg3+/jXw
    nRFax7dtuQJ51rzxaG7deHqiicy3nMWyYG8QAbOIqmX+lfp5ekvoQK/xr5Ixh+7pC8LRnjiu
    zovNQNY0eZwjUkAcHE6vV6aIFInqPWdZe5/VtEqkuI+XODYsmrfxT9gfTr4m7uSBn7f6z4kf
    jVvL5QDuKG/dSKkq72sAOfnQfQ/TUWWDiEZ61s8iHnijSizIzXZ/nahDp+rzf0WYBOJnPIGG
    mPpzf+hSQ96CwIG090SLnKk/ExRQOy1TPrrUEFn/bA4uVNpNzD/7jefu6k7EwCqoL5n9Ky0c
    TwduKKgi3m+cubuRX6Nn40WOsgNWCtXL6AzdcRz1hdZkW9kS8ePjCBhvQRBIBqO1Fkx3DLpz
    US5jQKjZWpl6lvJV1MahYz5+as1/qG/Jyggj1YoMIo9ycY63qS5r+WN0BYZehixQdo5EdtqS
    ezchYEtphReWIJANVuHfGXv1BEOQYGgr7X2fT2/74zAXSXNly4aJ5iZm4sU+kZRxw6ijt7rS
    TU4F/vWNVTbaeNsSD1lteiHHtkKObewZXXp1tiaU95EiU0c45hjUfbJjoNqUbRGM6/IMvsQh
    7/9iqfWIaxxWSFKBy0kSL791tOCc1CG/wQjsuigJgbXMMf1OhR8RQ5QppGomH7G13GxmNlyg
    bEB9PmD/3hQ7l4SDOLHIIk5BEnAqF2nNXQsh8n/GLrgwBLsaYoz+YShJQLGR+OHOFXCvRh8j
    5zTdPY0S+X9w7GgtTpx4U95ypZDZ4hzQk5t8duNLnbTXVyJb9KW/aYm91P9iG4/0chZ384bZ
    9wpiaXM4RdstA92LN3QBFWkUnse3deN0LKyOOALuFKIHHV6mLBzPypYgbDmDJtw+nc6q67aU
    uLRXJ0vSUx+9UronICEtAhnegpIIA0pJ+dQgiqjmiqi/cxO9SnVvjLAm7+gHffsAR2mZ9tD4
    epVkgh2baRwIqn58hjEBly3ZjFlUUvQjUSvJyvvkC2qPXwIQOrQIedNc/fN3gxwldaB97F4i
    qWtWJicP2PUtLh6wiEer1CryeoImfwi3JxIEAs5w3hFw57MFGPAGu1AFwACQruwO4DBoQHDH
    +v8KppCFYP9AHL+9ucmyrK+m0o/Uu+FhkWaGt/dwhugwFVSSjh/JGf9n1p9EoO6nRPR8IJUO
    gWqHMMH7X4W0I7fkq5Bwo6whS2M8Q/5tA1iSs7Dy2XSSNzm56yyoNJXsKdlwIgHs2S0Cwh88
    N5X0NrgDM6nsh36o9Hjj2F+23zSA3S6PXAKiFp+PnKz9iMW3IEnIOXZHnpi51ADoryzGKRMq
    7Sq2I6OXhKe09tePmOvxrIpyv2UjmO3s4zNptlZLG/zdbZ+0Zpjewd+qAmS68zp/cN/7bBlS
    zogIZ3WF8EkInvhJ+CD761tjKOIabNOZrgjdTU0abaR9AnynOCi9XTrbnEAx7N0Pjxd42QIE
    FX84+Qwim1coLMsaWhHNbF9aFaifgPhkWT+x5MKkjppNXzeqEb40bGEr0lk73maVwuVmXqVL
    1/qMEdK5T/BL/qjVcNXCPAvXIyOda5iSPWpRq4VJn7NGfU89ZkpugoJhFCMi3hqQgcs8bY0n
    2ugNVjXtf5M4cAunD2JIqoWA5aNr/9EI2svIOJpRz5bxHv/n22ZKwd/hEKFATjhVo0m9EMl7
    qqrjStFff+S9stdEEg1ShtbU9mg9ubO7YWAcDrfnjs5BiNcwNmmkEqAki+5GtjM1b7sHTVA9
    75FkbBxWcVXg0F3eBEua3HkL5wfpIWu8tJ45oJPHEEPwEZ8A5exDhsWv4ck32VN+zTI08bvO
    fHzxVDJRrPKc3fvtIGG+z2cXB5peD+JmYiSaBemhEGMn4PIg5aQ9hguH82QpuP6q/Hpj2wi2
    QNkdpIeLxp6d7xqsvGqbp8p0NTMHf39ifKnp17ppFqAe3cRQyTOmPE7Y8RTVZHky7EbeZO9d
    RMJZER1Zg22IdyfmRIkP6Bkecfy5yC3pmF185zDzZLXo1LiJsE4xrxmOzy5//QSuZP9tIgRB
    p0cWqRLDPQPbl/xARdL5tnAM3K+Q/Uc/94sutPnGTZYEvP2hx23Llq29KF6HsO1ewGkbLJuf
    9Uv3ftXj6w182Ad7m51Hayoblvqhv0M0abOehukzMZ6TSTk/yXEQrmETg4hUEuXKJzWxrdF2
    ppNxFpkoXqpuf4UQnNpGrT3BtzSFx6DUB0JbxyVEDnnIEn9Scl0RWdy7aRhUIhF9pOvR0mMO
    ukMOD/wMd/m3K22nKjfBJvmjmmzgkFtMjROb9ZKQrTvyJafjXkqZ9UwoGSlvGK/srNehv0NO
    Uc5UmCXCz1Q+H4QfNqYHjiK+b4PYmMKh/MW+b3olOnGKkuiK/WplwQ9JW8Tu1yV4smmdwl/A
    cYBivfMwjv0x5L93yk9NOW3JNskxXgwjxb23HCBVay+erqXbyeHBN3fHzBfS3db54gpOjvKh
    XdaApynN7GkT/oW2x5tPeDtueiRuIKDEAGb1mEvMB63oBE4I0+oOOgliRT9CPRdn/YjPfWJG
    rnZNbNXDPitdu1nzeWnHDaYJABrojqUxtKELVNmhCdg/dJUC+liJPqNXZ0zNmGzg26qN63Dg
    yWtYHRXslGjjVjrly3ifu6qdgwV5PDiK5+39g6fEq8KPobrBbGPQXhs6sBlGz7IWfUObzRjr
    HazBjk+n58+n+hkOGrRB2RvEBwJsGAJGrYUHC2wp6/hedIGqX+JgLXktfvMFrI6AvyQ0OOA0
    R43Jurnfb5Rsc1yFaGVhBAdPJoFrNtdHEP+EEGIWi+wcd7PBP9fqvSqboVSGLaXQnVSz7FA6
    TO4QWQL0pj9j//RlCLp3FL7fT9Q/x4SBgBoeOjwEOnrPbq0Wl1tc2E5+nH2Ype6Q6yU37aPX
    NQGM5BFolotbOKhK4Orqh05TVE7BQOpR8sNRbLCNksH+8DsB3Ksw2H5t6dfBcLO2QJ2dD/Cr
    V4vJCdY6tMwJ1JfaPy9/H14RGOW/o685JXNuZKCiEo1oxRnSwnQKn1EEWnleRg87XQLhYySE
    xPG2/MceVjOrPtpDRo0pmOO6umNBGZOXr+drOhpPV/xu97Sb2D8Wn03D5ivhpmWqBBhqTO6X
    6+h/IsjdbYWE1R3/uTVur40pE5PLJpJxQ/Z0B9We9vBKElq8ZMd0RWKnlHJZoIKpVvJYuiT7
    MNlfMYo9EijheLnIAwp1vPbyRe0OFFgDjsJfxYUaRWy4aqb0ljJhrmyLRJnlAD0rXwjiwLxu
    X1uOgi3pbR61G7mN39BmmCZNmyRXzB+aqPRO7FSXYi2gcKxTz1FP4yBgpb77ALaWJafGu8AB
    4p5XpL7KNI1913ic1DoUlbbD37uCQdnSrmmRq5XTz7zKpUwX0CDLQI+XV8uIo/p3y0zUcR0a
    AT3DYZXdA8YP49dIqt6e4sRsv4pqGV1re4saWNN7jz7V/8jbbAa6H/VZvb79LjxjQUbCn/uU
    BXZy1MA8cmUBd9jRew9+1s/ogpYaJUyeke/PyXQxa6Hklh9GiFKYKH0DiRfgbuTc74jBamIX
    8bNOuIn3MbA91M+mRn0xkSnuflXmAPDXn/VE7yBjDJPxFap+cBacxocg1m94OLMwUvWEQ63c
    SllaCtemXeayIUAafv1ZWiLqR7MU4t0ectu/LwgqDSu4gWK7hCfPJToacyXlkVJGB02ixwRE
    zCVAPdcrZEmuXlgocNLDpets3fBOiaqOyp1bX4lDn2/e/JhiLP2BXzpKLPtwmJGa2GmV+O9x
    76Cdfg90qwXXMCxGN0i/C5fpsEqdJxQ9c7vLyzP7OLk6yzL2wotcL9EcQ6h2CREAA0rD3icb
    qpK8Exf/Y9DOpcDwFkhuD8PWq4l13henTe/MW7c/RypfUlnTpLETqyrNuICOWQBz6Oe97A8y
    OwexoMcluJ7jy/wLKnNX2/Lps/n2l+BnxBMJSN4oKbLHiLyehqITNFcH2FQgIextOAU9HbI4
    kOXRl83aGVBzu/CnQGTO8sih/KqmDIBi28Ki/EuC86ScLUU0DLDmlzq1beg7EG3pskBIEURG
    5WYPvrHYiAWY8uFwOrGZi4fIoed7RqKaHgBtIate0UmXSrg9pLG52ROYjVunS2YrkLsxOziJ
    VrdOGzyZg8UowHDriZ1GpvPXQw9p3Ve3f/MaGaNIK3W07LZjUPl0nIFGkCiUgwZ4UJbn37oc
    qqgpD9jptu+urIvLi9CVrOF9kiD0SXd8kzARzQ5Kp64bDFplFXBFZBoulfqyJIxFb2G+s77M
    H5+aDkBDcQOdgjYx9qAW1WTHrdeuQor5VuBMKO8t0qPHzSqcF/KcLfz52U437FBVcbHZY3Mr
    l6fy8abQTC1P/LbFY35m4w3CWHJgsmUoNL54V3EBRNiwsG4f2z55hp2vB6FMiBSBjQjjHYHR
    XiYeoVCWdv8yMTBdbR+qyjHzF8HbOtieJ6ywKfFeMObS2bTtnH//5u2Jlp00KuvwAx+ItXMV
    qtu+3NXdWRS0kEDyxgFX8gnilM3839wAbSuPO2dXqByNNNUxU21vbZCkYbhEsdWTDit7qna9
    72peS0LgeVHBJbrfihk5GA/F9l7ELdZgTwP2UpBr6TbkxIhVrKORWS39dkHh1fme40LJpf4C
    1s8bvJdXGsT6uU6xtVn+XLtmgFCJnOXdNXnUi41wZSLEXHidLSOnvQ9kCTrv8sfeEeGQ00Gu
    JUwHPK5hMnSLS0Ld1ivfGyprvvukRM2g3HjUyei+FO4iuUCMnzFHQgN1jh7/TI3rleDFVRJD
    hLw14xQ9gLYC69DY3wTeWlo9IFgAssvwkIhvweEiFLGoHm7DG6zU1cB6D2szQzF/SDJfeUCc
    87ONRQHQQ9w0rHBfym7FXHl55svBuJKvEP2W5LGYxfTpPtE5jREp2WElvC0pNkyEfeOQ3nFN
    3qXU4oOhM3o2wuwR49ARtVBTwT6+IpMdPNky8aNEkC2sv9vecnjpJ2lYfh0Ot9S0up0EQhyR
    RMUCkUkd7Ycswm63oWh9ruqwk1k+bAuxQqckB35SFj1f+SFsQmwprOM5PECQsTNWztsrlIOk
    BMxa0gA5NK4omvGMcSCWMXbm4K8RI0DlYhZlBvdozP7sshVQVuTtiribVRcwxYqaU8bxPrYI
    JGZhbS3ft5witwIN+ni6lWqGpA3ynlstM4YXxqDOomnR1RN6iH3RoiapRb1Zq4ZG7PsfodNd
    rKhxYpfuwwhnhyD84O9jO34CHXpqXRjhA2paMXIbo17QtMbmJC+92iAiWOXtHdTH5z2IcAUR
    sgy6bsrKAEICxxc21C/OA+RpI1xisgfwNZJ/iSJpqbDzaggItlu3W7T3+8GtIMGICNwqdTCf
    X9BiAQY90O2mGCps32/Nfqm30+sjEHG9gd11XQdIkjOsBuPnm8UVReB0+S1A10WwVr8IUsUK
    9bKQ+ZsPyTleTfWHXM6QDtgLPKu73my6nTPV8llO0MWIAJTg25jx6zhXh9pJXC77DupH1Nlh
    g5p5MS29aYZkXMnM3REBgEj7KSx7V/xsBHJ1Zy4NQ+LPwIhP3kbFDW/hLUySTymNoiMf7ZTy
    +qrS85rVT/N68eBGDMQJlT3WOlfHDD3noNca68J0VdUXpBsc9VBI39JVMdTgKc27c42FA2u7
    1X+mSTcgy3UWYsxH13Cu71OVeckuV3Xd+GQbwSF6x1Qj5g7r+Qj5uNMdJNG8PoP+mvX76R1u
    YIi4ufmUC03JIJqEy3VFYhPcie+rgWDrtP9NjwcGc/g49LYXTvSQ6XuWNTczgI/eo7P/PIcJ
    +v9q8WefxL99TxGyX0irVybifz1Ovxkf5+0eIKEyIK8zM7aI3eqFO732A7/Wo2iKOpYQBX/6
    tFFlcmIawrUyBxEcPbC8AfDfBCn0/fNTahe5eGRlaFyAOfr2W8+5hr/oTYX4XdFaqr0+uarX
    PojIvwq9XxAA0/n/WFxNlBx7Hvdc+BE4dRrk3+YDPJ9vjKgSzTO8EGsF/4EukRmzh47Yl0re
    PL/Hk8fdbuErsAGrIn6FJBIfm4fEsXgdIN2oLLR6n9lavIVIW3y7wunqVuvW2W5djSzmsAS7
    s9ZXDDqkGj7MipUAzurxA0Tqm+kfFQpaRmZS4+u9nLxIEjNSx7q8FHzHkg5vyF4j5SUd5ogX
    SXlMTtmhjJLL+d3oJJWXXolL6qlVByto4KE6x0UuxQKV0GZDS7F7ss/OGGNDxiz0gp1iDHJ4
    JlR+aYeOYJnar7AfUS83+gs8rnPmtusDRX56YMci8Ia9T2qhnemBz8vOsE6Htrpto9ms3hCO
    mHLu9Sl3QyIbIhwRxR+b2wRwB40jzyARCgaA9ToDQ/PGSAW1PmUd4vEZYuh+tZ7kQ84p+Kbv
    6wRKb2Pfpz+ZNSEp9VoIr3rZ/mg2c0aeRCF+VsIe+NZFU2zGk33eUDCK3hazCWZgj4H2bYTY
    JJu+FL8O2+/LiHMtrcnjClVfFWkVvOx0zqRCYQe0j2JaRz30zLTcPc2L8tUODnUjLYNTeUZV
    1VR3vNwmBfw1vF+NIdh5f1VYKC31bhUPf1FrU4vhtDUpCm4NU8M5P0h3mOIocqZgQ0pkRFov
    hZZOMnrrOsD7I/Qo71dmMRbhdYzZIQHM9LyVyte5PmUyorsR07qDv2HjFogirfOMUqPy/8pL
    ldyaQnNiPJyjX5GJRt8M6SvfvMIU81H/BCzuRS6ZRqlavb/xMYWHzccaP0PkmN2ZhL0Mafm0
    8Qcj+3YIgDEf2tFdQ0y18QlD1Zho/EQzDZDTiaOHTYB+665Eo5lG75DAeYyAYx8iCn+hoi1I
    q3rRAp9OhMqD352hDiU6cRMprKXkBKiPNZGkpcpZdXdiYa65e1TcCz5+lgnp5ZszHh2Q0Fo7
    6hxclyLbfzPbkemvBAgXnqu0r03XkwoeFr57d9D022wO17P4YBTWFnTp+Fn0N/lGrECBQbQI
    qLfbxezA5g4GdaOU4/a2RBaeTDA5ow4WB9SYV/PKKk20arNNDHnsDXGkGCLNQUlO1wFE5kLy
    1lU9dvYDUND2BSQ4bcpj/F+UmDa/tRiXVkT5hap0krpywTxlOZnbLD33efamiNaq4Y/By8Rv
    95UzY0eaN7expt8yfgpiBELlqXUx6TcbsmtjypsdeVi3+uGt1KY7DGsrHngpOYjYesSRVZH9
    sNNA3vWtmOVNdMEaM7F23H9u8Xlp3exj5f/Tm2LGNAYnTz1haW8dKW0E1IUmtnG9TLpFnf3g
    vbtBafW2bCX/IrwXmg71809IHiUI+i+rAa3xxDMssVHrVSrV7NibL2uqt+KpXCe8AfQVJ8x7
    rJf1sh5ViOUPWjDBkS8RKX0ZTsVda2xgXPBpgTmWt+AamN3G+hsllfRIHAYejxmflOkgQLLx
    03ywpU7ISjZrUFoiImDxZv9XU4UnhEkm9PIARjweqEwCpXGHtjmou2L1YkFyRPMZ4Mglmhdh
    ZCQn7kl8oyauClsJzQ7yQBPdJjxOy6ujlnF78GpFCrYB+IH8wsWjNv+tiJH0izRuZeQbXBFq
    5PCD8NAAuWNRhKDEF+arMoOXdZE2WfAV7vp85xSDQL5BM6CLgt+Jb6gO1OXoBSxBWwvvyhlp
    okXGniVZoQwRnZMyKjIHumn8g44koIPBb5XfHCKBOmpQpwQ9WRfp+xpe7sBJKDl3oJcJUKm1
    OaPA4Qd15omuhRF03q4ue0wdig7sGUUWuEJH5ZCZJhvH2jT2cefL/S3d7SaWw9UTJsIzivbM
    qodtZZAUXSimab14eH5Q86tuB/33zp7XqueVItU8yFsblNLl5Fh6QhRMeCSK4dEsKV++75qJ
    j4h/xKpRZsUn9bbRAk05EsDuNT0DY8BaheRvwjEAcIpcNfbbULdgGqE8m4CT1AR/96gfzC5M
    jSKFebyDeds2lBs2T82bPyULckiMG5WdfoQoi5mcZf16lG5OOM3NLsID93EIgXKym5fFcrEh
    bCLLgatDktug7RLvsoN+neppQY3HUIMIK7TTseZtzqweACi4HwnquAGyXlBqMbVW9ttobPdE
    21HrH5ljA4AAr0JWUO2hDoAT83/mPQl6A4/GJKOXu3xNxuEfCGQ0uW4z65bJntJEPTirL1Rj
    hcxvks5asmRpQsYFVlpbkvpyeg41ec6A+TyYKwZJeub7OVPACZL10cMhhgvTY1O7JeFqHcf5
    bES1JUymU3yNVd8b9s12EgnUi/sT7oXSeI4yJ9AjGx7Pno4Wog6UH3ZOdt8MguXpki85Xebn
    0CsXj0Om0DFCbu52ufzIWRGyDdYqcTvTTf4lfVsJdK+Z7zObh4lVAxGiDRGJ3WSJ0jvpIg+t
    fGlFEXCXYPfB4+ZwOgqGegL1uPAbkiZ36iClQBsoernc20ZglX2Eq4yIrpGg6uRdoETeRYYQ
    VRYYwYSI5EYw4qGpWStKf2gHyHpCOvfTTM3/RbxooJ1OKr1A01OUNw5/PJ2XKr1aN/kr00DC
    vMTZOG45bDY6WJ+j5MWwW8n8wQ13x0acnRoqDK/s9Ei6A4F5q0MD1MfKpazFM4G2grL+29y2
    yq56hJ1nBfMQlVVrQFrIV89liyc1NqzHcpcQMBh3/6O0fNCiX3tnwMSuvVAidPu9HLTDelP3
    rILZ25yLI7J1Ez+JF0eJ6cp0s23OhEtbjCrJ1l+/m8ShVubYhBveptWhElBicdZKNYp6eGt1
    r5XotPeVnO5APZBdSrSPSG3pKGmoCAWFRYHbCALGY/gSFMXq/pwawBoltzPvi0cA6KY9a1Ui
    Ig/XaWGUkolQ9CUrO/gjcIvAblDYYuRDtxlYxggkOpcwh+avxV+jUg88xuwpCIVBbbG0i/iQ
    aSYXPI04uLVmqX+hU6UH1BIgxSLU7byXCEa/A5XJJLKHvUe9i4T29PpaI547yOH6t06ZyKoP
    yH9MzruDqkShGgAD6QR1EphfOgiBxd3kIiN30zdAuc4UE1Fqt7bY44uu/iXu77Ou+P//X1Q0
    nzuQxkYn85/b+Bs4Rmq+z/J6cEfvRpp060RDgNJ5Uw3/VNTWyhNdJOoinT6diDHmkAQ+9a++
    KIbdEiXGCz1vnRvGLCAZiUbyMQrqDWJMmVcFf1tDoXeY6x/I6WmJO9vup2hgchAeH0dYH5sB
    0Zm8KTX5UYZcB3usN7VvO5IPayHhr8r+0WetbAw1m6OZLKYrKp5MBlK38zcvpruRSbRCHH/B
    6hKWX8UK1yX3zzfIH/kxJ/jltfvnDzhAIjiigw5p+P8Ijb5aHxSuuDaCKDvkQZ2bRV6p48ft
    0+MIGvW5kxtGt4tCicUhE9N9nHJOLE5Lv5FqKzWOZqqnZIHeLepVNWdE2UVMo6HQbV6zA9Vb
    9JUCAgHfaNZ2ySYQGU1yfiNdpKJTYGAv6hZhsSmA0vulZAoHoKo7R33/t+5fHbjaD6UvFDed
    cfxuCLR04DKSbrDA8ss0DKtvTaKCm18NthiQjZuyEJfqFLA5CLAHD+DZgagsDonv8TD11YCm
    TBCr1ErkeRtT46ISHkBALFDanl9wAERksFmAWgfl0RGAo7CmIasyue+pA8V0ctKSXewHtzQH
    kdauE7t1sKQXwm6DFJsObVw0mAXC16HW1GawARxxkVgwLXhqbP0AWPNI7XZ4o1eiz+xqMkBC
    ySG4Bin/ApbFeo5Ha9ID+V1YqcsLQxbws6dXBS62USjYwZ3nbTpTWSv8gcjPRD7D0xZABwTg
    IRvs8gKMXueWeWJD/dRBzPQMX3X13GDCLAKJqHrwJZogq3LwY64xAQ9C2jFDgob+d+UKpsXH
    tPfpwDiuHzT/tbMVqw0hQ9maBDZzFnziwwBxu6vezibQC/RcvDzw6dXAVZWHhTaTGqFq+Yt0
    U1dRErCUfg2/PTehaHaXqbVeF9jgaC15o5FN6fHojVOGCSphNH27CqS3UH0hNaDHy+DdJ2XZ
    lnHbbnJTjTG/N24qTy4Qft6XlxxNIdGoCY/BuW4VE2bU0liqozsYQ0U8pThIAd3J+h3IbBID
    SNGU3KPxmUaxt6cqpbcyHXxagmTFCe6w9YQLOoGL9tNoWXVwxMp/vnvnpSVr/YCED9s7sqLz
    BrF7CVzft2gVlMm3iWn98EOo3qLwdoripGmh6SSP0mKiWujpaBr+oW7EU+fB5EvGVZmnejHv
    iRhQX9i2JZaH+aMloV8TlFLSHfiLpCSQwt4YPCprj9c1KOvw3RbGhTI6hBhWQI+Lh2/1i08S
    tTSqCXkG0aABVWsxZoF6Oije1LKe11wJef26cWq9I4rPW6R8UXsBDdfw+C/Aui9qqmrLrn/k
    GAfdLdzib/slrJxa5V2IZ1EqI8aQ6Hi01+DlO42hhmWzYrHFJljkcNU7mwXDI/kNbJloWL/8
    QRUb1fQtmIHZGjg7olzVd4TXT1DAA2eL+TigZQQzkCP4TJK0sg7DP+Rlo20fyXy1X4/bmyS8
    /WZlHEy/Sg/A8KHU4zoLmlMETHgfXrf2/NqPehJRX/rPQzEhuicVasrdPVCl6+FkB+MqIPwI
    Un6VuKf7EIvZodqF56AxZImeaE+YEzETEtgGHqSKqde60OuwuPYyIJ2tJ4KjTYl4KuOKtWD1
    ZVMTFfFMki1opomOnvguADNEr3/8GdRRFmxbC8veevUvhfbTWw3mxUI/8OAZzXg6ENZOhsbl
    mjfeLKRqHRdEHlQDBzF2vF2/1sODfwjzrhfkrK//O2vpPakIb+iinY6ecq1i/OU2A3xwaclh
    2xpVF6lqgzdC+YuKQhpMEoQFKN0eyIYKhPNrm1QJdCnXLM5d2SZrpFz3uHW88Iy7E/PNgAMd
    +s7bE3vsAeDuyL6nj4/x4lFDMKD8fAp11lETWqWqTI7TcRVt/Ub99SgjOO4LjUCEEQHG48n2
    XvhHVZILlvWoYH/ipY5oYQ2AEpsOdWpHW+WPhixY9zKHqO4M9DtTBTxjK4oaz+3iRXBAe1OD
    bOqPg84Bt/4zgDVgRa9dfipLAQEXL71eZMJb6nXp+b2uzfD6iV3HOkDEnYY3Kr6a8Lv4YynW
    lWKU/WyyrG6e1R3GYlg9S/rY/ReQQJpAQrdgRg5G477i02cPWUeP+SDWpwQ1rcBfAhUPDN6F
    jy8VYYXThc1eX1cR2Ur+H836vLPxdbqaGPm3KybX/Pq32noFiz91JOpMT1vhIvoeHlseM8Db
    x1yn1BD6IYhDBXbzAO/DveLYOlf1CWhwP7p0KSn+NInivWezKAXx3GIDXxFTGe34472w51so
    LZ15e99rsQv10Q6l792xuT6AWhydYXKM7Ul5shv6sbzcyBA++13geSbwDUNefgkrXOvmIBIw
    ke06HBVgb2zXd569Y44lXoDd6EEabfdbk/N+QGVYuF4cd/voWouJSxL3TvAZ9OD7VqW/j+a8
    biMCobAn/0gQymru6jZiHm4q1COkorL1HRUQsKUwtG3h/g2mrG84ApJF/jRzAm1ascd33fqz
    PFVEQwaHLySd1Lb7Rt6HJ2qJFx76xLKqUEnWqPPkLRXRbWHtwv4WU/dg8PT5M6j1MHafD5q9
    7S95rDrI0Bf32XTGQNhMmAVZqsbjVs0SCE4FRrGx8cj5ANL7hHbUW6+uDFQDEts3Lw65G9SN
    MhfTv6EOOjQDXiYDNq4IzkY3e5Eimb9hNhEpAdh3CFFnLhsjz/YJXsLVYBu9jtwAerOPYyC9
    q51RrkIeGJ+VWs/Tn3bOKI8ajgsemSSKQzup8aWBWsvgEPoQfGuo2ioy6KlHbJ+oq8gPsAS2
    V7XFKTs7Z7/b8Lc4zQfghBOBb3in5JFxubBVdRbPOyfKGxei4OGuEXKev4UVI5ayF89EekhL
    ClX+y9N16s9/eeL+BB818PT6xNTSmHsvWj3hwZ+rjBjc+vTf6jPwPR2NfoWrYodF3VUmEP+p
    j8IDBLtTyJZGyAh4waDhcQXSjQyIF85m4ZIAOb/WTL2xSmVR1ueBSPmzLfKkz0fTofB4r8ig
    eel0XmBdqP3uOhFx3bJtFtsasBiRzwD0YRy/bMUUE+I82V47DLI/mbVzzpBut1GztPd/FIQT
    /Ihv8l3Pyk8AiTB92Y/mEXVmjSVV0mqTxlAfCBa7RsMQlE2oO5d2jQobnEoomBEimVqAhWy1
    PiM7uBT/kDEXT79HkkobM9QyAD2z8a9yfriDXcUbCrpxbTDuAiqvrmI0YolTxhkqnAzy/U2d
    Xw6ePuPKgEXJpvOTLekhCR2BAMp1elcjWcien+sJxv+w+mlss1YfJ1F+aCjBtmS0NBfqPb4p
    i8GeoMn6YiEh69R25Zuu7o7oQeuTCZLHQ2StbwKzNLnUUv839cHT62In6h6UIseyXIUMQXno
    bYZoej1oKdyqENqNjOXvOsJCXWFlab8YoUIMxbssoWghQYb9YsaKjF0cbjP+fvoRGXyIahdo
    /K1aMdXL+9gMeSNGqez5izPldbcniwQqVFwv3WyfWOPOrD4GMzTVzhIogg7IBxj219zTsfjq
    EwI3txlyEPhN0Gu6SPPHYDOQwtFL3dIPhd8xjljtLiCwlwDgSw1uLx2owH1YN9Zr4gFD0ZDV
    9PNkwfYOaCsMv1SzK6PT74YUVGjncUjVuoMLk+MVykC46EzKNHHLHv078Zvnj5APnYbNgMEr
    WJ+Av92G0BjT//731uc/PMhS1pNj5kBZdlh857JkkzW/XZ+tqFkhVPvMKEkCv6k9YlZ7uOAL
    p4e1BbUlSvfDdDIKvCjl4W+arOPdPOKstgqIRC5JaDPUvvQRz7uNiWJQKYcpCortJd4zZMh1
    wa/02gfynajkEagON5okZlKOv7Dpg0/CeFSfU/YRXCSQAeP/YrglfuhxpSpU99FeETAq7OUo
    gzxLiQ7kYDWQfgWv8YkXJOOJh7Q6TFOZOD+5e6N7F6j78OAFt8cgx+dwwgJ6zhjZozaOpol0
    D/zc1VpLcWn6N3biu8M1+22cFwJ4oGy1clMBHVvgJG6xL2cVGExz+WxwA9D8fC5+9LTWcvep
    VZPuLJ9zopPWGZE1hLKS5nhA5rjbOOu4xRV/DH+iskzZhm17VaoLeszBDoqPVrP2QOTN9BIi
    mbE53JCJeNgYISuxgfu5otC8EUoFoL1WGNkDBwIH0JdoTMXGHQWBjfeUMYg2//HpLNrTzzbB
    fxPNsXcV4szlbcrMxxOiOaY3swKmeWnLyZ/PE7nb6MHIyOggJ/Vn5A5PSOz3gzX9pcuWLMW7
    4HtXHjVoI5a3egcbh9zoUQQZ23fQdnYY4E0hPw6N3/VSSYMXZJCfV56tqqIHdG/6VJIJXMaE
    9WUlC4ePpup1O40OIunMHOpDDg50m6Pcp2IwHSCQAmB9OX+vcEfJcTn2B7EKZAibWyfXVScg
    m0/TgEu1Zgwdhoz6C12iGsRqxSpO3xsN5oAfP6aYAPcw/VIKb4fsmLJ3xTZ9XuJItO4e+qvd
    /n2l8oBx+OI28L5Izi1mTgMdvTZ9e1IRndCRzEnPzFrXYw3j7UZRp+yetL1YUM+/fT57A5AG
    6/JVA85k4bGRN4V/S/Pg7Q0BxCfhGnCdZiSX8nx1V38OzwtE0m9jEqBbdXksPKwWvI0NB34d
    af2WF0F6D7vxOQI3dwXVETYE44rkYhnqW5al7qpLz/rwf+UlMIFw9961mcS10UziENbxS9Ys
    YtykdOJV77yOxUaz/IhByo5aO32v1RTbHfrkRvhDxyjTVY8XrdIQ3fPcr7BufeCnpwCSc792
    RMy0zY6NUXxsqjKZoiRQ+rg/p0mqZMrwr1DXGYxCPP1JA6miqZfcx1Q9g7nd2meeCoKD4y4L
    wj5Wkv4u/j36M5Y9tde1q1XJknGNAMUDvDYMmQROcBmXqEHUaYK4CKnOyEODipYFbIO5oG8T
    rPokYNdNho+LYJKokzEh440E6UpA9u93fiivC7GphvUrUcSFjpg71rxMzZZ5Pq7Qa4GYtrGY
    p7313JjQMJPuaReA6Y1IeCdRL+q6H2U0e9YnJbSS8vmR5g0qoDbIgxhpsPUGQS0vUOsJPacz
    ZENKn7e0e5Q0qFlYCK1x/2da4RPBt/29gBGgISj2FHr6M/bGI1cwrcSlyPZf2y0lq5LfLYxR
    ehjifE2LRMbyJ7dkzJ7ZY2u7iBXbLdRUM6mAAnaf8hegh0zQ6jqmgPpIE71RHREj9Cy1wHg4
    3lqOfleajKB6yjJybOhqsNczJpOp71CET7oOV5qLHDybz5huEtybDXorfM/H8i1qpWooIOlQ
    0NLx6Ue2DUFIY4Rppm2g2Tt4GIwvw210zaMKSRAdNpC/7N3n3qwCI8SaLNr/wS9jsJ0p3bwU
    ApeKQrtp7bhjxC5ib8o9IEtN/lmVC2wIwOFS3vNBSHvKbmx5L5mhvJL4j+L5zyK2snOq13Wd
    SWj9IHMiEiiKz6VCVBQN83K8Hfnf3KY/mNzi8Q+yAMJWM2QhVnTNj7T8kjT518UENPhMgKFA
    zKPofTGIvAjCCRLgJ4bTR6YYWO2L1X1c7lT5OdXZofulHhtjcpah0PySMhd+owdNKwa6pEju
    NQ8nSH9AYxLRaL4PyeM3lXhXrquhsmdCkYwxXH+mOJfHtmXv+hlhdA8FfeSZajMmqlJ48Nqe
    qLE2xZpG/UPeV/3Xu7ovsdT7VxYkCJwJcwcHNLmnuglfjwrl9dmPJmVz4bXaTXU3eqSldl53
    W0liXq3ciDzbupRO4AR9QgcepqGlL0ezo0iuE/uUHUE8juT/NmSUc1mULR5QV+q53gVwUfwe
    BSDHwpT5ZztD7GUH4JuQ5PUoJAoQLXDSzRNrbEzfE2g0oR2T5uITjuPGXiRW6sgiNj5jAXWU
    uf0NrBQlXsN5PxCnP4UYLcFYbrBj2/ub9XsKgLuDYh6CzVpX6YnNXVw0C6DzrKjGBFgIY3Sq
    tx9mZOURpix7luvup2Ubd0qDBR3oR1gln/kGzeBBJ5nIv7HhvwoZFpS4UYa+pC7tmxRN5m7j
    X/maxCc+eWw+M9n/3kcUuvamhjjskn3wm3/EXJufooYmab9HWt3kNJjMSqM1QoVRhsCOjvj5
    OUI8cDOmCIPeLGTTdsOncPukyyY24fSgj48i6BjI0WbCj/ZhRT345aV5RAf1aSv6pmf7QXd/
    WdxnqojS+ZBSsgMN+vOOTK04dX2lErJIVk6Mf3+cAcmiO3Rpyz6gWCx2oEPb2DSy/k+F/oFE
    EedOekJw1O2RdI2ednuEob3r2wTa2LiNZ5ggbX0dXcIQSwAEzDuYogq235ZxMogZ1GH4hklh
    fu0cI9etk5qGNpXBUtO56VPO+Upo+LJ0MAQBHmbRMiQyqgU4RLzVT78hRe6avNQ9YTEF983T
    pp9feV/ID1HHvdUjRiWNwiUxQuMWtZiPkQ06CmLEX0FygvXHIJBJE3Wgb0u9glQ+Pkq+g9WE
    4Zn6HyJYOKzjCc7k9OlEQYCefrd5J2rMpFDHckZN4Dt/JHkTgdvKRA7B+eSsk94CnQ+gmVMZ
    hVmcqnMMwCwlBPbUiy7of2MRoT92YHTKaCnxTSYWvP5M3vbouG6b86jpyIIcrT3Ek+ZeOY5s
    WxQUNtyvBRaIJmy5W8qyjra1ZJ4SubGe4lgupX2ktE3MebZmQrv8i623hnYav0o495Fq60Vz
    9+azr3uHu9/R2Fn9vR2f64JDApMcaNKPtQyNvDfmm8R0C1WwILFzcSM5pu/5CRZMGbepnVNV
    Jy2nejj5z5PnC6eVYmJ+vxZYGBH6DwkCMUcOOiUNestFI0PQypPrxi/Vp8hbKgBMFxt5G24t
    eunzHcvz37DVtu2c4cn9Krf9aXYvQo85mPJfLHnX4wZ5kOJw9NOuFTgU9cpCnywD8XXYSWDV
    4TkfZEEeV54F9fIB/sCRf9BKNfSeTo0qcj03W2LpRpvJYS+xNOOumqQ+Ynfm/RMSQIwYHdbj
    ssz2CYNYT1iim62zr5XtR54wS4XvK1RComF5I/1SuZWiN94+JlkzRlSAjICZPc0h7zYKQx/t
    HZnKIZBMUlXynmOBKlYnnBfqpsrT9iUdpIzAbgG2q3yMd2O4Bjx3N67tueuzonlaenSymN3h
    uolHkOFGLEhDhT5Yf4mJ3X/Ega89xOkfPw8AxzVTovKUlGd2K05MWf7k+/Xv7/L1yzkkv9IW
    To/XK35aCh9ZdxbE5T5IE7yaRRkjkWMiYQLdw1kYI7283ZeUeqMhwfweh8pOiMn3jSnmtc8q
    gAfwi2+7RdSz+cGtdHJvzA4fgB4SzpSWrDcFwow4fSI62rNj8aFgvX06JbZ5P297B2xHZNHV
    kGKF3tsH+QXu9jB8197O1uiNK0Wi8w19PHOppSUA7fbpAmI4p+7zve1ziJh4yCGsxfI1jXql
    nnrt7aOBPi+iMbyvd9N9tSTa7YHUDsmomKJm18p0ACRC22IeGYvEuH6Y/aPGR/2lh6YRuNr4
    psTENFmxijYvGtkEfsPoFCFVwFZPFOD/yNqFhAkhQg1Xx0cn8z2Apyz+lSBJLMQx/nCQB3P/
    5np3JZJHRxSUlyye2G2K3Or77x8nBNEm9pG6wtiyBlA0IxtB2b27IMDVH+fdrpv0ir6C7xS0
    Nb+Orq2Hm5w5DsJHcr1TaslmDa4+Kn0+l7JPW4N0JvwmBCXEmKjl961YaQenmdBntTEs466Y
    4WRpKAKsa/v6e34kmfOcs5mFvlQQvRa+HZZz01mg6C4rKBXdBvHYRV2EixdhySnryZ+0dC7K
    XEEoX/rcbS6FxGXG4bJ5bCfW5lopj9traqzZ6hiTYrISBEbtGsEx4piObJsKrUlXW8yTvomM
    4JflWnEeQW26bJ729Kt0571I2U8PlYkYUHeCDGzVEBsTt5sC4Ad+HCtymrmb2zGryUt+kphs
    Kgy372VsuPgRVRgDtNRnevogp89pDdLvesdYpN4Un4EvXgmjEapIWIZ4P/6k1maTCXtHsml2
    mZBeFaIXAqmjrz7RELKaNgDZ9KDEZnPUV0G21jlKUxZ4QgRYlBy7HmE8ekfnfmyE1O/G+jst
    ziuuEfmDCnvaoHnUowpJJfFN4EGyPedqv5YYtWl+uTU4kmMzIrih3NKQEeJoefszvXjY9fhu
    Yv+L+FcLCntFURF8Mmbt43kXa5G5/vANhSIxeLp2rUQ36MvLaqZj5GHMzwg+CkLtOSx+h59q
    ilIV4qNQ5IwOos1Va9EwTY3dlyqGCqVE1In4CBvFCf3vyaBzaGeBGEm4Hqq70mVvpRh0K14u
    +qDM4Hl2I5JTxNfxCVaVcMkFDScGNl5nIMjdiIxCvaYB34kvisi9Acg7GFjdHzBsYMNSDHBd
    YQToA6tCNWWEmZSKmkk01jxi0UlmZOJhILYQGec3+Kzr+IR3oa13K0LAWCiwhyR0F9NhnlLI
    mHdQBHVRw1P5ZPTX5nsM0WOBz53bfZVxDxxjaQzcTzfM8Pxx9meZpWZu4jku08vZfS1IucVB
    c1fO5IQ5r4sB41Ahsaln6/29hxvRFNewnJYavw/kTVdFLwDRA8xsiIYa+madEb0H5WyE9N7F
    aeXx0UxdzkotatZnIKFi5rGE2Esng3gOq7Z/oVA/TgwLKdNBmO7seQC/GwMUEzbuYWflKcp8
    Xeb71pWoINCgZTd8Ua+7CfUgWgbYI8j1xLe6mmUWlqZzHkcrNk4RpXZ3WkYp6KjSXR6opD/X
    BOf+J6eCRmjKxbmKSVM7ZVw91yRXMRdHK1FKQVcx1wzHepuuiaswcKAOz8nRxNj5RyfB84U6
    5kMtbr8lJ5q6g30iW8i+dpYiG2nKIhB/bq0+oiSE6jH4c/wqp7emAWw8pT31KfmqdOkZgoJV
    FjZCn55jJOtfwu+I9JXJhGLoY+uVPyTHU+kIfwhRdiyBmWeONoCAwjyQpFtUbNyNzrCWWwFE
    BEOETiKWuUmNeX61y1A6+wpqdhJD5V7srQvkqC3Fc8Of1JzDIgy5NJItuKPlyi0iHo2lFl9e
    93JVJswTn+T0KRPDUvkx7KYq1BGq98ajzBV0VvSe7zIpJgJphmL3kSR4yWxPqaP/0mz4U8Fu
    7L22OqNda5ND5LhnN3329O3SsHkmk2Gkx4CJyo+JhBMC0BISuWgs0AeI2hITMDklZvDZiIAj
    y1Aqe6X6yRvWoslcF+DPWMfqRTmgdOEKuLkyqA4aPBwAKUBq8lrjojDxUipSr1EvYUL7h2VZ
    Z4CWey/dSdEW0RnHdxvwvdZMzw6gVUNOnFFsrSVfQ2c43ODpJtk/7yTRScESmMBWJHjXBZ86
    M4rMtuNeLApJdWfqFaX4nfU5Gefedy8WdeXsRWB+EoC50Me0JBwaWmPAtDO35GLeLkaNMhKw
    5F1BBCefylN7d7SyCS1QEVYfWTVAPaqucGBmKBm+PZHEz/TeBUB1Ls+OPMq44aXbFd7EaBnV
    HgaDnJ+nrsJG9SvM2489bDlBkdBC1ANlDv8geSu3hW2yC0KLsr+2txD4eVyl2wh+W/CQjEO9
    ruxgiYkjiywW4VAK1aadv3xqa2q3wSiSuEdRzif2eGItvrBTlsfHLfe0RDCM7U5Vx5gk2yrV
    kfvFj2AFBEki9KdsmRm9icsNUhjj356/mPXZ+JsZ74uNxrbH2K6gnCN2X51LwV4Yk2EsZeqa
    Ff2N18ewnEXUb4v3/26xrfkeitHpj8kIgYdD8SYKwUnCNm5nhHljGOgAWRio9kzkMspf9GMO
    wriGrAWkBmPivFIxe/qRR+pBoCWEJjsUAYEHFoPKs0XBULuclr9ZeToOda2McA9Aoe5btqIA
    GTNgl2TeI07VrCG3qomR1VKKtz5NFSfsp5FGeK8UNR4xrItMwZ82F3fV4Z9WVw5g+dI6bDr1
    kdTkMruS+b231A11GKzPq/R0aIed3oX0EL0CTLu9Z2ZTc6WcYkL8Sz1jWw5v16lRE7bdCaZX
    +jXl4Z0DZQJxwiV7QqEKdyTDfXwNvtv58uflHy/HiHQ6T2sImJPqKDBM6yF02iKhuD90uv1G
    cLvkLlZxEveO7sunHumnaKMn92h81+Mkh4+25jreX7GobH/S95hfYo940hYfSEnLTOGHxEGe
    KeSMRGVaTi80Fzb4CGQHF+f03YaQFwcbPYRmE/2nMJlw0Y6WkgwvueUG8/hEaGHlOOr40+Vt
    swIN58WM6kPlv7yZ8adhJp8GQ5Wtq4UmYDTtReOEBORQrqlsgenY0o2v8jisrutD2NHMeCgh
    +9dOBMD6RYY1mzRCBmEcDbN3v/mZSI8QF9iZQidPYniIu4VhzgfqdOfbZn20ykMu6Iv4iT86
    VP2OW55SS9jT2fOmwD8rpcKOHphpcMtw9thvjQCXCOsGGUAjtkCaXAB4ibQ8pdiYCeJVAIi5
    vWijw/9PLFC/g7qUNZBnDGHiDGwrhGQuQAmUCzP8HruXiuT78/vvj2MrzWXUTJTGI9HYG/8n
    JtySb2NsPK/BfXqOGCOZFb3ZiAZlVcbwBuObLH1tYX/EQEx0HpIn9zvs6kQ8C3HUbHkhWB4m
    GynP2PP1JL3jYpFWIV8YmJJM8YGgtdWjuQjmuzReuAbu7YT8H00+31vI8Wac9GFiyx837Ja7
    kn1Jhh5imEaBNyCldh9SsJSiZZ3XAxfcgWlz35s6q/oa1FAh+NsYCEm0Yz2+6h5Ip8GMuQok
    X7R84JBADOE2yyYJtiBWRFDkJKKH5px3FULbQWwdTvNfBl4lbp4EKZunxopNHn2KHuufKIkE
    2DRSyxLUzCx/kl+ei+03kCseTGYpl5y7uzudd3TwYAvMDqrO/jf/mJd5nsZ4oehIRDTZGTFN
    0Z5Ars8rADkIDXBaaO2f8HoLI1IbtF8rKfWeXmYlNcd8G0kLM+PCwbxZR6JeVeQV61Le0EIb
    hSIzSv2m7mU0JgjyPZ8oEyNKrFZFOiG/QQTSolOEb7aEJiAQoSElcZIh6XDkweidXAoYkgfK
    dqnuNP+PFnlWDd6VKBbNP7XqOZKjpFwUKkpVsone4ATcaU6C9Lr3FlNLMlG41eOk910VH376
    6+9ItHWDV9MqJVVySuLAzSRtKtLq07D1Rh0r2oaMdvKDI7TU05n3DDHCWZjbkH957dOjEulZ
    8dpmoqeJQaoSYd4FR5qUD0vlGt8HbYkeX1NocY8occu5LYMKxrZb9Oj9bc7ORUg4H7FGZT3Z
    W0V2IzjKARYJDsGWV7bwePhM0UEw2yiF8xXdzjWLQ2TmdVYBfOcUDGiPtnJDuH0JimPCc6+r
    ECcGenOpkH24uidcEkB5IW1NsCE7GbrRrykV3J9iSh6+01quUY1DaOgqUrUL1cpEDVKlQL5P
    OyzuvUUnQ/0c0eZ4fbQyl9jn9WjRSzEnM89NClaxZWZxwS5M/Y4EVgriADyhu6NvyI6QRrek
    ipvcobADHX79UvHuXin8Pm4Ij0j4Jg/TjRoZ5SEh/oYJFmC4M8iq684GnHau7m2R0sFdVtRe
    wmq5tRf5BOM/hkShSMAss1vpALhuMBZlGyxsYSnRLca1BTvK1JV4wvbqN7NjBt+u5+3UCuAt
    x+RdUQbqKbhdPa09F6p6qQq03aLrzM7OirnzY+rs/FP4hJ000jB+CN7TkUcOmafhCTmlrxrI
    LMDE4mBfscuyLT7XVFtpmGyrcAChxKF5Bh75a0+SS+guF/JaKZOQSy/ej4IO7DBSN7HSxgnK
    YPX1LbRlcu68G0tkxWcxbCwOdWFyWIqhMXMJQxQwOVrmDzYUZI7ulfQ8NJDfe5GpBu9qGGNb
    N7vejM+307jGr9kDRgBP2+oRHxsttZTMVX0iLIZOx1nK5hniwOTkSRJRyX9zeJD9MF0EjaBW
    wss9NvA6+9y4focxV0idOxvlNfVBaRs06wBkw5Xd6EfXu30YHp2tmWevlnhU345vraKk00mP
    AJmtzrkDdfpg1BfOqtrdyu1uIC1qmU7I4jLBYOEcWraltKxLYQ0VP7UuxkMEq/CU6JjJazUP
    6TG6GCtB94w1OBBBQ+3I4FdJ3W3C/TZd8WF/zSE1ZbEhAzPfHzHRh/jN0RDCDZDgZemSbp6J
    2vnJQTC6aLonEsjIChXsGiKMEgF4BEAYrJdH7731Ecaww+SE6HbSwTn/nzjcoalqvYX6gRjl
    2muaJ/Ch3Zu8A8nvvbbJ2xjYFJQaKfbIeoIuvMANDr2cf36OV8Sf6fYPcErIH6xJZ8AqQkWU
    ByfT8iyK5psuN5fQMtGVu9A/zoBJBm0QudpYJvnwi2/g/awdOHetApfoxM13n5lQRfIiCSAW
    w5Gb7g1Tjkg9GeId3TySyZ6HPjiwrU1mZLEYCqpgK0barhQHA2uhTKcejCX2nyrcU59/VSMZ
    ERRLAucc2yzUt1NqNMCdNxth+dOfWvgxr5dkUr3F1ICyr5ExYYHNtBSc+oZ0xgE7iHsTe/of
    UL1BUYmSuD8AsXkhBSvIqO3qSvzPBUSbH/aT7GV37jMLVv9eXifzTmE125wn9XUbWDOpmo3+
    V991DefmkeGy7Wjll4s/sfT58FbosAqjaIHzmAS9aNRm+Yke0kUKscA5MzkpdnnHwhLwFDQ/
    3kqwMgpok8rlVoNOvgZzsTje+oy9QnL1/YpFJjcLVeiLb35+rFx9WKlXWyYbmgvehs4xKIr7
    PqO8MRuU1tO3XJ396v68nFKlh73FCFRJhQIIBRKL0E56m1YC00ofiMdzPGWcirUUXPLmotQo
    5JKMhstejnZsi13GoJHTy0cB03SzQna6Sxrym7qP2TnKc7TSeUcBaGVQ7AKlrFVrrdWM4Rd+
    w5RhB5ZJjK2I4DHWrtiM4pR7mCoM0vqQh8AnYmqwcvFCRk0ji0rOnQkRCu3QFeNjoNpDNVN0
    +3Sx1eXZgZANWc3ErxXytX3Z7AV0mbYuVHyhnZSoLnHeTu16XOeReS2MwzEQE77ondHQp+ra
    XlLXLA7EIY8WSrtcXE+o+sqXWK3e3t8UUsj7Ca6giQ152Ekzi817zR3d6DSVFlRkZXlwNwY4
    MmfOUCeuBFgHI2iUaGa4OdOhkoe8xu2KzpizbvxYlNk7FN12o/vDK75PgeBOSiDIAch1JD81
    a9/fhMzhHc5SwwiwMf3GL5rVv3NsCCUK+CPIBXPTOfrlBHY2S/QE7vHWO4EJZCpqXvxQ9PjO
    uawI7ithXibs6+HbTNEUaFIRNB8B7e4J/yM/v7NYSlDXZUSh49eTwdmmhgEakRIjteKkYUUq
    gTDy+WfZ7Tc3+4WC5FmHeMWBK9qtYwjYVDocZ/Bgt4a0LBDt61wXQhX3jj4dR6EH+8dQil8g
    rkQfMbKMBpRO2hZFMkBnjBESJnWRyCDMGPBDmA/7vDrSoY/cK7dAiWrqyDik6ULd4/aHo/+e
    zGaDWXgT2rE/XjH2koeG6EMKOT97qW2toMWpIWAktApUq8grmx4NfGJSuReyuTOz715HoCmN
    M0kDPGE92FFRjYRXxh5FkicWP8dXVi6Ymkj2Qk173w8ZFpiKIGzzcIleqkPupQ3ZBq8HIJfj
    05fLEKcB/VQvSiV025zMgiJygitS9OYA4W4FfZ/1UY4FBsDT0faA9uIOBrMB2+Q+gjllPa42
    LVh6X4TadRRZu41yCzN904ukiz1DqcONC95veDv5utzBi+EOIzcMG05zo3cKDimA12ozRULn
    GIPb5EcmyYE6aESnz3cyX3qJ28aYUFSIznPpSulfedKP294pbKefbJGBy6IQMacKHmrrDg/O
    XkLdSGe3Na2AAz0WazPIdhFz3NykFsBXLFyMY9twNtID0Y0Olwv6xdzoqaUhonZZkzvceBzr
    /Kk9Twrjl+jZhq17J4ubudtjtEa7pZtovISmDw6eX+6VzUORsloaRhMrm32vIYLDRUG2eM9U
    tZklHFVj7lffH9izr5n+1LROMJisElzZC0ghsjRK/Il/BQqlXlWnJjYwKiKfDvvVjCWupZ2K
    Cm1+Y1/8rWQl8KlPntLwS+CCnYBUQbwyFkOyXEBmur1qqoaw+lXWgM2BywD2Lxt/MjcT5TGu
    1j+b4vk5r+zhYXL09D1sFWr1kR/eJ5DNiCUHaugVixTvEi5y/oeaGkOqsjw8cSW8xuYxfJiR
    IKFJCinJIHFeYkPZT4EdHEd/QBfaiqbkEcbc5I9vf63unwSN/NmHE0SBS1sisGKvV8niOjSO
    kUlU8rm85aaUuaqjiS4IejQOJOVbQ7k0P0B3Pgo/1iOdlnjkbK1rNxpyHne4TiHB806xqowg
    QYV/x7tawqQR8Lmt1QLyGILFKwXX1wjHodI5uPXKMQYuGoqyCtnLg7fw9ltOFrvwis1MdsGN
    f5yaYGeSpFj2ncv2cw0SVy4R+0nsr68axXvpKzoFUEZeFyEt1301eG4HV2K6jC6+uH+Xvx34
    0OMUtovIPbRsgtM8y5fPPfUa077u6qSqN7qsMojbHw2aTSuBKX4AeIfcjJ0GhmAMQhR2UA7t
    KWEU+J77jlUR/h3B2XM/O0/gYRJI7EYnGM3hKCxMKA6CSPIusnY1zLzgNtH+SmgG2DVScSsM
    WR9HFObo8XlqkJd5QBWR2L6bZDwwG43S/sfHPXc343Ie6Mvck228lxsmPlqywzrixcnh60XO
    XuTGsjstGKO0n7TNDKLlW/ui8MZaybxJICfl96e8+dYJ/5HVxTEe7WLtIFIGaXJpDcgx5TWJ
    TQ1k9wkjxLvl/xwMY+Put6RsFFT1VdheCrqf7PwMgR8RFZ0r85ujo+lBvvWC6aclHiZqTdgi
    Qm5FBkly5Yswy4D8bh+tehGRR3oo5E+rXBPaw6V5BGa2VdCMK5XSmpq+qqvkjyAoxA4aO4/Q
    ePpf4acZkPwqCF+bl47cfO6kfM8rBbqwaGk7CarjneJyf08LDQGOyNWe+kRp+fyuXj3cztFL
    cHp+43Ycr9r3dBf1Nmp/MOVH7jdwhYD0OJE/OUbo0yGP/K5w6ZzbHTijGG+BzYC7YdZRdQUo
    mswKGljr8axKvD4KUXxDnOhOnK6nLwrdfuqE9ajOK+i9CQF5JIPBENddEebDFLQuKH3n/9+x
    66grumZdh5iCUFqFDkD1+ooEWN/08P2v73UJ7BQB0DIBF7jFAiFWMSvikPkmVyiybR0M56+L
    SNtLP3MdcE+c/Og4zHGLGrfCFcVQmWwwxcTAdrFDkk1lqVI/YhTFzQrEzg+hxBhNcECMEd0J
    0yUKDKQ/Ivu+hUL8RgCyyzowsC6az6L4sapZSP16j1rLlmnniorkVyJK0swjXKhkC8mX4Zei
    6KKyEj9Odewr7Gdb9Jg1J4kv/dcp28WB56EJ1/VjOjLslvDaUoirtlqU4CueUYAxpI3Ob0lv
    dn7ya2pxMLrq9BPkEmR5zptMLXy3QwHHsUNsWqUBx8nOSxVk+dx09j+EFtHTmTsSkxovhn2l
    +6NqX98y86hUQ0GKPTWQZIilQA4q8+ao2aQVwUlt2xcZiVHM7JKk0G1NX4I4roKjQp6+MfRF
    LtZjRqs8RejsGojTXA1wFa0Iy14skiydH+BLTDk06Cu61bpyw2Oc+gbot5V4V/CGRc2CyL7c
    BSNzUxBvcVPMGSz+8nGUykO0X6gCuuOSX+MXo8Es05m59QCERwVlbKKKoX0E7Te8ehN9YUwI
    G+X3WzE/J2ZEZ8VoWc7NfmWvvFmoHkejFuygichFMW8yzQzA+I+BzOb7RnZb7FWJrIOKma6+
    st9l74tliPKcXfuCSvFMjZOqfNSWR+p+PNf907kvo+36xv5cahM+Fp549PaMVD2IyHFRLETy
    tC47odTzmGHvM3YE77Nyx/EZ0J5vEJ1Br20Dx20s2fyRobVlF8XSefuZmmJAkV1/dcEUnR2d
    aUonSqg/Q/d36napuXXxuIGVMiJnoy9BqFFO0mZ7yMBimHWJ+Bfjs2803dEwUohgD0z+aXm6
    3JbJhC+ooABlpEdp7gYjV872cwZnOdV8hqT3ck8V/eHZrLF8l5hSNwKat2b+FAw4uWLNGKEt
    CcIQOIcKYmr7Ce4q3O6jFRNQzhtpgEmm7f2ispFJs5HQTi32mbR8/rjVmhI5HihM0YJl8YqQ
    6tg9StYf0AH8VbKqbXHTcVea0L0N74AN6I0EGaZ26JPFQvdgeQ+thpC7FHME0vZPGiNeIeBH
    j0K4yUpjKFWOM9n6Et2fCbSJ3598FypF0yy1MxiTm+nzsxTnZsrEF1LGnFN3xxPh3YjMAn9J
    rqVzFoa2f8jWIbUauOKHYek38upPXQyeTaD5Zy+OKEd9CdzRJ+YkymKMMHI+IAzUadrr186u
    /nVXQIPbHPSs+swv0wVDS8P4qSOtksMU6fHX5zlygWmKQ8V9YuKdh9TFMZZ1WIQ9B6SDIfuX
    svN5c02TvSylqTJPCblLAS4r/MuAJr7JerHkn9lSyKUJC+zZfFzuN7p5FMrMAhW0lnI8cD0X
    kmR4djWxr1ebZCGbY6Z7zQC2gvrkvojY8i5YvNEu4kXWR1kHfVwFX6eZPtcPS03EUn/sqoig
    WVd5KUnIn68rLuXj3aEwMWzFDH9iJG+27Vnotjtc4YvVxOjPSWDkir8BYDY/q+3EVhGm19YX
    A2GpwYXOxJdupZ8YPj9OEgH9R4X6qapmhnCy0hrmiMrh1Ts8Qdsxe4wSAEmxtVZ5DumEW7rd
    TN0dLUzF8Gt9NPwJO7eCWo6BJXdE/7ySPsreJnv2UhVQEbY/t6bTqUcRb6NJQWMj6gQrxWLi
    BMFFeR7RFlTTTfbqI4dUeY38J7981vd7fNtfIv9EZ/AlJmA5hGSr2opqs8EinccwYtI2lrjd
    QuXCuFzAh4xOR7GtHJE1c8YMqJ5Ft2tm9zjtajQfAbvYgMujBJCwRutbu9NhqpoU3RemYQUl
    JKsYoJ4Y7EmRtDiv54x3tYzBtScGhysMgXxfddfdxZu7HMRGOuAlEDYtBzUB/yzhhlJl855Q
    Fi64U5l7Y8pjy9bgAKzxeoIL/CNCzzciivEn5KslH1bWtys+XcTXpkimrakUfojO9lA0lPLM
    GLKrryb8+VrsB9PPVBLyO7ptptl/hRa/A8R2s99ZByC7MWwSbq4CGLpHhf/9q/qG3S7Wx1p5
    gTrk73EXxNmIvuoN4ME3mmDcI/ZHX9tbWMchXWPUv2BCR/GOPNLajOuV/e2s0eCZeJpshaJW
    kmuz5q1G7LUbbm3wjR/mshmJYtVO7xLOtM7/povmz0FrM5jOWNvWRz+7fLJbjccMVj60u+QT
    +fXhd3By/VARGsYkQ3slwxG86H/s7EGX3RglPefCj7kDAJdsLOicd+S+iQRKDzsBilWoJeW7
    vU2MSVGoJEs2iFC6R3D6SW1dVtqYebnLOkQBN4iDFebdTepbmOFu9frV4KpMydAhPk6Osr1d
    zod/dyuyG5zO/E6ui5QG0lAt2S0YDP8LELvgk3KGMjM3EIREDHjgQbCmUAawwbtfjG1hCB5H
    0psz6qXKY4OuXnEfpSA9Yi5MRLcP6YlNxINHWeLgMnZNnlVVqwfvx/ojJ0JpLC0WNee6C/FU
    mTJttDSW5Spx43E9h79uy6nDoHE1Md4/PUkQPirSx3+r8WwWdRuKl2Nyt0UQHEeFigcOXbR0
    ViyBVuWS60mCN+ttTZfvhifzFZ+NQIwHtBY0cUMvT8nkX3j9QmOWawGtUJmoca+ytixaOiFW
    GYXrlsx4bOYdbECnwIoizf80uTBtizJOeBBfzkw55Qjth9olUku1jXG0NCEhMrmTBb2YBc+V
    PXfxUp25vyFKPj5iVaqlv9hrz8dkFzoKBzgETaz/0okRPZBstuZE0bVUfSsbqUthoijWWO5t
    CJjLjOfYHn9d7Q3XO6A2twKSo0bTrnq/IeLJ/aKqF5OJHpKZiTaO8Az7tjSA7V+TN3hMN0eO
    4AgWQ0jWrWoIx+z0tC27FiGyzT7OgxLm/e/pKsIfIULzfg+tEnztjMzv1JXdOZCVUZ5iFJLB
    H0ToWLBFKuCWmVnUSKHXwX6Bt3AHGi3QgUKyQU+nuctvadSgj/eaMvKdYGKCEZ7xmyIEnrhm
    5sPaodcgh85g97GuMqOyLCvv46maISif0odTKRf0ZvXM6X/7zr+Hw8nm+TffYlm85sGeasz4
    ZTeq6z/zJ0c12khsyaUJaD6VOqf1HMMKve12+Lgmnz5CY8BPWYfluCoCh5VYcO9CS/w+iOoW
    gP3sHTfEJeSdubOyrz4mdwzAsO0+ps34qiaeuBHAFkiUypqXvP0OfeUgbtXcFWM9kzY9wTv1
    iNYpG1iFHOiyi3KU3M4pjq24GDBn8sEORxpfIYIsqhrFYgQx/rndDtVTYnoNNwQWKLqRjFul
    fA29GB4ehGXp0GE8sNOJnSS69aFwgZ4heOPLI4xTB5dNcaU7ydACNYhmAE6zb9oIyYEPKJiN
    HMOFVwIbaY6e4GtHaCwLtMt5fLbD0CO1sgiqsrOb4zsj8BNot/LBZdWxXeLwhsfV7Se0Jsn2
    ADHCLu/VsFB3g3szJwC49tqxd8joc7V8KL1csITTd4VxXIkcoCNnCcr0U4DXkbFwwA5LjHB+
    2p7ycfOTWig8GivSdbgJfsCGjAzKVnG4uq6cONxtbfpJ72Kn2TU8vXh1gy6VPxnfuXpfgYw5
    cuCrSPle7Drx3Zxg2DjRKyc9b5z8JLcg0iVARh798ToYV4HZw7Hv/N3C/1y7VttIZMrob0rj
    UrH4eUa41vwTa9jMZlu1n2KsRE+iphAcEuAySKajSwyEv2Z21Jb8ZZj2nN7DgDo6sVSg3Xf0
    6oJrjo5AIFixlNWaDojcSO+qGaI3tUBQleMiS1meIBOsA/fm9Jv+niLzKEKzuvntsGqsI3m8
    OUEazGJQAmqkDTIwxY7XWTAzb1wjrb20J0LFLzcS69NLhWs9kKWGx/uMAPer079Vx1lNBO6t
    1kFhq3r00DJ4oI2iAPoBFvCpQvWaYPsnXEUms4O0FNWTDqdmp5Kvd2ybByU2eN7e89BRAu/y
    r4aO6mOGzfEmfOMxuCkJWSqpWaaASXoZdf5WWK8TAwfd2LVwxTehql+qQWpcLqcv0ZdcyYdq
    pVDmDvwNdAlpBbCs5ef3qFraq4NJbFJAkKOL67A2YEjAmKKfIYnzEWWDmNUe1McqMattNQog
    eXqYJ+cWmqcktrhF+HCdXACDN+fVijXsKh89611Iew8SPc0B4Xk/cplOVOeRflGgt7SIqruZ
    VlK5RakVN6WN88I7S+9qnB5XmH9Vek7Cm3MSoQZ4sAb2FJ08h8455KruNZZIGe5F7woDnJ8W
    iCD9ClFZsLCph0XorhnUKn8i230+XEZcsuH4nQjjEA66AWtm6yqCZqHZjGiH8DDpegam/egh
    GJy78fsJlgY2qFF/VlNR7T45A77rHTGhR/cqF5C3bKnGp6ODPSXVSNeQ8i+tealo50NWNa/T
    fbIrEn2dVPWLQDe7gO46JMYkn9/QiZIsyd9yi0rV0y5RulJ5WYex8JqXxzJXHgIX+0ONw0iv
    SCGU59Az9lmIO6Yk9tlfDErIBuTVaUQ/ECpMqx89fgkQUIHPhQpjvN1BpqQy8tp223jij2oW
    clm3lvxu++2Imut0icuw2wwK399IWPG09VibcdxdQYjcLv+5ofv1ciPX8w+hDbQ6FixPW94t
    kdp6iiuBEUUEFS+keHbw4D9rZYegMabTqfKkCOIwuHE0dXRpdfNwQQhnJXJwGCNoUsJlQdlt
    8IUg2led+/ibGJWsPQluHiIlSIstLGmJlTbpjMxh9Gge9Fy+jwngvW+8Gks3j0kjNF8OSCvN
    /wzL1TR5F1ndiV/jYBWwtrvRuw+csS+b68dKEJ8w37ds621Tp2uuTc5S//n0RYIOzPVkcR3m
    +k+7MORuDBbPAU4zhjPiA/WLyvjO6Lw8f7uWyK00vIpLZEcepfH3pj42V+NlLiap5j5sd6aG
    J6RsvoOLrqWYm7tze2948Yik2wFJtTHk1zYQsFpqY+eHUFbUJSdjZCTPzooTAMTzmjZPZOzl
    MlZAXyCX4MQ8qHm+26ig9MQ+gcXdQYUvqkCANz0YC9SB5/oZWaA0VsfapvzciAK+Xl9LP427
    iisVjuM49+KmjSkJ5uUQN+iL8DJQF8gt5qgjkVb+2GoSSak75nDjcKRCCcYy/FvzwWiyFFQK
    GYl8mDCirQiX1x0l7oVujyXYRoPSl+zBWXw9WeGCt7TKUGwQbiYPn9lEwLXtqp9+rStL1+ef
    Bjfuqy0AEfzcVxRsgPPwTe+B4cmzspgq7zIgSo1Nnx3CaZ+hq4sdBxI1UA9WT7e75hqhp0MP
    KG2uzNsyX09z5I7+woT97xe7Qqb8jSJX2x2rFTVOXd6CBg/8fNUFbXSbtVajXuVCSUo9wG2V
    xDKS2H+fwhkeVV4mraGe7+8bC0zaT6NWqr0OGhRQrmEUjquk//9mbfGnQeQTxcDeUjABp0+T
    3bWvR4T0PkvUGkaeRYuKtLQdp3WD/39ne3Ct0y2AZ85YdyuLA/S+m+YcbhhG3ibElebW2tSU
    FTF8RpVhLRoARSEX4Q/DHXrCHO08N7zG2FGVS/KDlxwt9Cpwl5uN7YpQyF1eSL8vHmwcVHjI
    A3ljWSAEDYvhlfNOyV24tFlLMKk4vpbgt71aDfkFqd9WR7M21ac+me8s2SbZ06I1f065oE1n
    TLU+FkSv0ui2VJGUNhUFOxV2FO4rD176dHwiqfMxqKR5BY/MoAN1ZPHHpoiFv6Y2ih7OuJC1
    E7yFKuVgmHMZL5VLX1k+72mPgvljSgtd32MuazpV/H8tD1RKx2wNuGPvpA6dWgFR9IPnRrx8
    kjn2okpW17vxwgANGwVp/NcrOrZ6eiS5E7JL7+mD4CdRImQr/04VcipeBqrduKG32Z55uSyZ
    I68oNcYukpCSiZek16jgkvPIDvXkDMWae9o6clqqKnOR4/YGiukBsaY3usKIyuNr2hiL381X
    EC2gfaUmdRoDqm2KXSato0CVy/FPVT5VS+ncWln2Ea1RVbOAqXieCsFtpo6SmI96oSNTxD1D
    gZ6Kzk2jclyM5gHtOdwEQkJmmNlp6iwmoBTpWfRoJVE7lblUsmVUbSBGW1zTZjiDtWPpsW6S
    F0dBk/27TiElPTRXNV3ePfTa8di8WK9W/IIKZAhrMWb4kUkGQis80NdHSFJdUgLWfGfPB0QS
    T0aFT2kD11GCHROdUlXx7TZkJu654bhClVVqRWj/bmk=
"""

GLOBALS = globals()
# Base settings
SERVER = GLOBALS.get("SERVER", "")
MIN_EVENT_DURATION = GLOBALS.get("MIN_EVENT_DURATION", 5)
WORK_BY_SCHEDULE = GLOBALS.get("WORK_BY_SCHEDULE", "")
MERGE_TRACKS_CACHE = GLOBALS.get("MERGE_TRACKS_CACHE", 5)
DEBUG = GLOBALS.get("DEBUG", False)
# Track events
ERROR_CPU = GLOBALS.get("ERROR_CPU", False)
ERROR_CLOUD = GLOBALS.get("ERROR_CLOUD", False)
ERROR_DISKS = GLOBALS.get("ERROR_DISKS", False)
COUNT_DISKS = GLOBALS.get("COUNT_DISKS", False)
ERROR_DB = GLOBALS.get("ERROR_DB", False)
ERROR_IP_DEVICES = GLOBALS.get("ERROR_IP_DEVICES", False)
ERROR_CHANNELS = GLOBALS.get("ERROR_CHANNELS", False)
ERROR_NETWORK = GLOBALS.get("ERROR_NETWORK", False)
ERROR_SCRIPTS = GLOBALS.get("ERROR_SCRIPTS", False)
# Simple notifications
SIMPLE_PLAY_SOUND = GLOBALS.get("SIMPLE_PLAY_SOUND", "shots/alarm.wav")
SIMPLE_POPUP = GLOBALS.get("SIMPLE_POPUP", True)
SIMPLE_POPUP_WITH_BUTTON = GLOBALS.get("SIMPLE_POPUP_WITH_BUTTON", False)
SIMPLE_FIRE_EVENT = GLOBALS.get("SIMPLE_FIRE_EVENT", False)
# Telegram notification
TELEGRAM = GLOBALS.get("TELEGRAM", False)
TELEGRAM_IDS = GLOBALS.get("TELEGRAM_IDS", "")
# EMAIL
EMAIL = GLOBALS.get("EMAIL", False)
ADD_DATE_TO_EMAIL = GLOBALS.get("ADD_DATE_TO_EMAIL", False)
EMAIL_ACCOUNT = GLOBALS.get("EMAIL_ACCOUNT", "")
EMAIL_SPAMLIST = GLOBALS.get("EMAIL_SPAMLIST", "")
# SMSC.ru notification
SMSC = GLOBALS.get("SMSC", "")
SMSC_LOGIN = GLOBALS.get("SMSC_LOGIN", "")
SMSC_PASSWORD = GLOBALS.get("SMSC_PASSWORD", "")
SMSC_PHONES = GLOBALS.get("SMSC_PHONES", "")
SMSC_TRANSLIT = GLOBALS.get("SMSC_TRANSLIT", False)
# POST request notification
POST_REQUEST = GLOBALS.get("POST_REQUEST", False)
POST_REQUEST_URL = GLOBALS.get("POST_REQUEST_URL", "")

import re
import os
import sys
import ssl
import time
import json
import pickle
import base64
import ftplib
import urllib
import urllib2
import httplib
import requests
import threading
import subprocess
from Queue import Queue
from functools import wraps
from collections import deque
from __builtin__ import object as py_object
from datetime import datetime, date, timedelta

import host

import helpers

helpers.set_script_name()
logger = helpers.init_logger("health_monitoring", debug=DEBUG)

from schedule import ScheduleObject

if os.name == "nt":
    import winsound

if WORK_BY_SCHEDULE:
    WORK_BY_SCHEDULE = ScheduleObject(WORK_BY_SCHEDULE)

if not SERVER:
    raise ValueError("Need to choose server")


class ScriptError(Exception):
    """Base script exception"""

    def __init__(self, *args):
        super(ScriptError, self).__init__(*args)
        host.timeout(1, self.rise_from_thread)

    def rise_from_thread(self):
        raise self


class BaseUtils:  # pylint: disable=R0904,C1001
    """Base utils for your scripts"""

    _FOLDERS = {obj[1]: obj[3] for obj in host.objects_list("Folder")}
    _TEXT_FILE_EXTENSIONS = [".txt", ".csv", ".log"]
    _IMAGE_EXT = [".png", ".jpg", ".jpeg", ".bmp"]
    _HTML_IMG_TEMPLATE = """<img src="data:image/png;base64,{img}" {attr}>"""

    def __init__(self):
        pass

    # noinspection PyUnusedLocal
    @staticmethod
    def do_nothing(*args, **kwargs):  # # pylint: disable=W0613
        """Ничего не делает.

        Returns:
            :obj:`bool`: ``True``
        """
        return True

    @staticmethod
    def run_as_thread(func):
        """Декоратор для запуска функций в отдельном потоке.

        Returns:
            :obj:`threading.Thread`: Функция в отдельном потоке

        Examples:
            >>> import time
            >>>
            >>>
            >>> @BaseUtils.run_as_thread
            >>> def run_count_timer():
            ...     time.sleep(1)
            ...     host.stats()["run_count"] += 1
            >>>
            >>>
            >>> run_count_timer()
        """

        @wraps(func)
        def run(*args, **kwargs):
            thread = threading.Thread(target=func, args=args, kwargs=kwargs)
            thread.daemon = True
            thread.start()
            return thread

        return run

    @staticmethod
    def catch_request_exceptions(func):
        """Catch request errors"""

        @wraps(func)
        def wrapped(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except urllib2.HTTPError as err:
                return err.code, "HTTPError: {}".format(err.code)
            except urllib2.URLError as err:
                return err.reason, "URLError: {}".format(err.reason)
            except httplib.HTTPException as err:
                return err, "HTTPException: {}".format(err)
            except ssl.SSLError as err:
                return err.errno, "SSLError: {}".format(err)

        return wrapped

    @staticmethod
    def win_encode_path(path):
        """Изменяет кодировку на ``"cp1251"`` для WinOS.

        Args:
            path (:obj:`str`): Путь до файла или папки

        Returns:
            :obj:`str`: Декодированый путь до файла или папки

        Examples:
            >>> path = r"D:/Shots/Скриншот.jpeg"
            >>> os.path.isfile(path)
            False
            >>> os.path.isfile(BaseUtils.win_encode_path(path))
            True
        """
        if os.name == "nt":
            try:
                path = path.decode("utf8")
            except (UnicodeDecodeError, UnicodeEncodeError):
                pass

        return path

    @staticmethod
    def is_file_exists(file_path, tries=1):
        """Проверяет, существует ли файл.

        Проверка происходит в течении ``tries`` секунд.

        Warning:
            | Запускайте функцию только в отдельном потоке если ``tries > 1``
            | Вторая и последующие проверки производятся с ``time.sleep(1)``

        Args:
            file_path (:obj:`str`): Полный путь до файла
            tries (:obj:`int`, optional): Количество проверок. По умолчанию ``tries=1``

        Returns:
            :obj:`bool`: ``True`` if file exists, ``False`` otherwise

        Examples:
            >>> BaseUtils.is_file_exists("_t1server.settings")
            True
        """
        file_path_encoded = BaseUtils.win_encode_path(file_path)
        if os.path.isfile(file_path) or os.path.isfile(file_path_encoded):
            return True
        for _ in xrange(tries - 1):
            time.sleep(1)
            if os.path.isfile(file_path) or os.path.isfile(file_path_encoded):
                return True
        return False

    @staticmethod
    def is_folder_exists(folder):
        """Проверяет существование папки и доступ на запись.

        Args:
            folder (:obj:`str`): Путь к папке.

        Raises:
            IOError: Если папка не существует

        Examples:
            >>> BaseUtils.is_folder_exists("/test_path")
            IOError: Folder '/test_path' is not exists
        """

        if not os.path.isdir(folder):
            raise IOError("Folder '{}' is not exists".format(folder))

        readme_file = os.path.join(folder, "readme.txt")
        with open(readme_file, "w") as opened_file:
            opened_file.write(
                "If you see this file - Trassir script have no access to remove it!"
            )
        os.remove(readme_file)

    @classmethod
    def is_template_exists(cls, template_name):
        """Проверяет существование шаблона

        Args:
            template_name (:obj:`str`): Имя шаблона

        Returns:
            :obj:`bool`: :obj:`True` если шаблон существует, иначе :obj:`False`
        """
        for tmpl_ in host.settings("templates").ls():
            if tmpl_.name == template_name:
                return True
        return False

    @classmethod
    def cat(cls, filepath, check_ext=True):
        """Выводит на отображение текстовую инфомрацию.

        Tip:
            - *WinOS*: открывает файл программой по умолчанию
            - *TrassirOS*: открывает файл в терминале с помощью утилиты `cat`

        Note:
            | Доступные расширения файлов: ``[".txt", ".csv", ".log"]``
            | Если открываете файл с другим расширением установите ``check_ext=False``

        Args:
            filepath (:obj:`str`): Полный путь до файла
            check_ext (:obj:`bool`, optional): Если ``True`` - проверяет расширение файла.
                По умолчанию ``True``

        Examples:
            >>> BaseUtils.cat("/home/trassir/ Trassir 3 License.txt")

                .. image:: images/base_utils.cat.png

        Raises:
            :class:`TypeError`: Если ``check_ext=True`` расширение файла нет в списке :obj:`_TEXT_FILE_EXTENSIONS`
        """

        if check_ext:
            _, ext = os.path.splitext(filepath)
            if ext not in cls._TEXT_FILE_EXTENSIONS:
                raise TypeError(
                    "Bad file extension: {}. To ignore this: set check_ext=False".format(
                        ext
                    )
                )

        if os.name == "nt":
            os.startfile(filepath)
        else:
            subprocess.Popen(
                [
                    "xterm -fg black -bg white -geometry 90x35 -func "
                    "-misc-fixed-medium-r-normal--18-120-100-100-c-90-iso10646-1 -e bash -c \"cat '{}'; "
                    "read -n 1 -s -r -p '\n\nPress any key to exit'; exit\"".format(
                        filepath
                    )
                ],
                shell=True,
                close_fds=True,
            )

    @classmethod
    def _json_serializer(cls, data):
        """JSON serializer for objects not serializable by default"""
        if isinstance(data, (datetime, date)):
            return data.isoformat()

        elif isinstance(data, host.ScriptHost.SE_Settings):
            return "settings('{}')".format(data.path)

        elif isinstance(data, host.ScriptHost.SE_Object):
            return "object('{}')".format(data.guid)

        return type(data).__name__

    @classmethod
    def to_json(cls, data, **kwargs):
        """Сериализация объекта в JSON стрку

        Note:
            Не вызывает ошибку при сериализации объектов :obj:`datetime`,
            :obj:`date`, :obj:`SE_Settings`, :obj:`SE_Object`

        Args:
            data (:obj:`obj`): Объект для сериализации

        Returns:
            :obj:`str`: JSON строка

        Examples:
            >>> obj = {"now": datetime.now()}
            >>> json.dumps(obj)
            TypeError: datetime.datetime(2019, 4, 2, 18, 01, 33, 881000) is not JSON serializable
            >>> BaseUtils.to_json(obj, indent=None)
            '{"now": "2019-04-02T18:01:33.881000"}'
        """

        return json.dumps(data, default=cls._json_serializer, **kwargs)

    @staticmethod
    def ts_to_dt(ts):  # pylint: disable=C0103
        """Конвертирует timestamp в :obj:`datetime` объект

        Args:
            ts (:obj:`int`): Timestamp

        Returns:
            :obj:`datetime`: Datetime объект

        Examples:
            >>> BaseUtils.ts_to_dt(1564109694242000)
            datetime.datetime(2019, 7, 26, 9, 54, 54, 242000)
        """
        if ts > 1e10:
            ts_sec = int(ts / 1e6)
            ts_ms = int(ts - ts_sec * 1e6)
        else:
            ts_sec = int(ts)
            ts_ms = 0

        return datetime.fromtimestamp(ts_sec) + timedelta(microseconds=ts_ms)

    @staticmethod
    def dt_to_ts(dt):  # pylint: disable=C0103
        """Конвертирует :obj:`datetime` объект в trassir timestamp

        Args:
            dt (:obj:`datetime`): Datetime

        Returns:
            :obj:`int`: Trassir timestamp

        Examples:
            >>> BaseUtils.ts_to_dt(datetime(2019, 7, 26, 9, 54, 54, 242000))
            1564109694242000
        """
        return int(int(time.mktime(dt.timetuple())) * 1e6 + dt.microsecond)

    @classmethod
    def lpr_flags_decode(cls, flags):
        """Преобразует флаги события AutoTrassir

        Приводит флаги события человекочитаемый список

        Note:
            Список доступных флагов:

            - ``LPR_UP`` - Направление движения вверх
            - ``LPR_DOWN`` - Направление движения вниз

            - ``LPR_BLACKLIST`` - Номер в черном списке
            - ``LPR_WHITELIST`` - Номер в черном списке
            - ``LPR_INFO`` - Номер в информационном списке

            - ``LPR_FIRST_LANE`` - Автомобиль двигается по первой полосе
            - ``LPR_SECOND_LANE`` - Автомобиль двигается по второй полосе
            - ``LPR_THIRD_LANE`` - Автомобиль двигается по третей полосе

            - ``LPR_EXT_DB_ERROR`` - Ошибка во внешнем списке
            - ``LPR_CORRECTED`` - Номер исправлен оператором

        Args:
            flags (:obj:`int`): Биты LPR события. Как правило аргумент :obj:`ev.flags`
                события :obj:`SE_LprEvent` AutoTrassir. Например :obj:`536870917`

        Returns:
            List[:obj:`str`]: Список флагов

        Examples:
            >>> BaseUtils.lpr_flags_decode(536870917)
            ['LPR_UP', 'LPR_BLACKLIST']
        """
        return [bit for bit, code in cls._LPR_FLAG_BITS.iteritems() if flags & code]

    @classmethod
    def event_type_encode(cls, event_type):
        """Преобразует тип события :obj:`str` -> :obj:`int`

        Note:
            События в БД хранятся в :obj:`int`, в скриптах
            приходят в человекочитаемом, строковом формате.

        Args:
            event_type (:obj:`str`): Тип события как в скриптах.

        Examples:
            >>> BaseUtils.event_type_encode("Border Crossed A -> B")
            -2010220362

        Returns:
            :obj:`int`: Тип события как в БД
        """
        if not isinstance(event_type, str):
            raise TypeError("Expected str, got {}".format(type(event_type).__name__))
        return cls._EVENT_STR_TO_INT.get(event_type)

    @classmethod
    def event_type_decode(cls, event_type):
        """Преобразует тип события :obj:`int` -> :obj:`str`

        Note:
            События в БД хранятся в :obj:`int`, в скриптах
            приходят в человекочитаемом, строковом формате.

        Args:
            event_type (:obj:`int`): Тип события как в БД.

        Examples:
            >>> BaseUtils.event_type_encode(-2010220362)
            "Border Crossed A -> B"

        Returns:
            :obj:`str`: Тип события как в скриптах
        """
        if not isinstance(event_type, int):
            raise TypeError("Expected int, got {}".format(type(event_type).__name__))
        return cls._EVENT_INT_TO_STR.get(event_type)

    @classmethod
    def image_to_base64(cls, image):
        """Создает base64 из изображения

        Args:
            image (:obj:`str`): Путь к изображению или изображение

        Returns:
            :obj:`str`: Base64 image

        Examples:
            >>> BaseUtils.image_to_base64(r"manual/en/cloud-devices-16.png")
            'iVBORw0KGgoAAAANSUhEUgAAB1MAAAH0CAYAAABo5wRhAAAACXBIWXMAAC4jA...'
            >>> BaseUtils.image_to_base64(open(r"manual/en/cloud-devices-16.png", "rb").read())
            'iVBORw0KGgoAAAANSUhEUgAAB1MAAAH0CAYAAABo5wRhAAAACXBIWXMAAC4jA...'
        """
        _, ext = os.path.splitext(image)

        if ext.lower() in cls._IMAGE_EXT:
            image = cls.win_encode_path(image)
            if not BaseUtils.is_file_exists(image):
                return ""

            with open(image, "rb") as image_file:
                image = image_file.read()

        return base64.b64encode(image)

    @classmethod
    def base64_to_html_img(cls, image_base64, **kwargs):
        """Возвращает base64 изображение в `<img>` html теге

        Args:
            image_base64 (:obj:`str`): Base64 image
            **kwargs: HTML `<img>` tag attributes. Подробнее на `html.com
                <https://html.com/tags/img/#Attributes_of_img>`_

        Returns:
            :obj:`str`: html image

        Examples:
            >>> base64_image = BaseUtils.image_to_base64(r"manual/en/cloud-devices-16.png")
            >>> html_image = BaseUtils.base64_to_html_img(base64_image, width=280, height=75)
            >>> html_image
            '<img src="data:image/png;base64,iVBORw0KGgoAA...Jggg==" width="280" height="75">'
            >>> host.message(html_image)

                .. image:: images/popup_sender.image.png
        """
        html_img = cls._HTML_IMG_TEMPLATE.format(
            img=image_base64,
            attr=" ".join(
                '%s="%s"' % (key, value) for key, value in kwargs.iteritems()
            ),
        )
        return html_img

    @staticmethod
    def save_pkl(file_path, data):
        """Сохраняет данные в `.pkl` файл

        Args:
            file_path (:obj:`str`): Путь до файла
            data: Данные для сохранения

        Returns:
            :obj:`str`: Абсолютный путь до файла

        Examples:
            >>> data = {"key": "value"}
            >>> BaseUtils.save_pkl("saved_data.pkl", data)
            'D:\\DSSL\\Trassir-4.1-Client\\saved_data.pkl'

        """
        if not file_path.endswith(".pkl"):
            file_path = file_path + ".pkl"

        with open(file_path, "wb") as opened_file:
            pickle.dump(data, opened_file)

        return os.path.abspath(file_path)

    @staticmethod
    def load_pkl(file_path, default_type=dict):
        """Загружает данные из `.pkl` файла

        Args:
            file_path (:obj:`str`): Путь до файла
            default_type (optional):
                Тип данных, возвращаемый при неудачной загрузке данных из файла.
                По умолчанию :obj:`dict`

        Returns:
            Данные из файла или :obj:`default_type()`

        Examples:
            >>> BaseUtils.load_pkl("fake_saved_data.pkl")
            {}
            >>> BaseUtils.load_pkl("fake_saved_data.pkl", default_type=list)
            []
            >>> BaseUtils.load_pkl("fake_saved_data.pkl", default_type=int)
            0
            >>> BaseUtils.load_pkl("fake_saved_data.pkl", default_type=str)
            ''
            >>> BaseUtils.load_pkl("saved_data.pkl")
            {'key': 'value'}
        """

        if not file_path.endswith(".pkl"):
            file_path = file_path + ".pkl"

        data = default_type()

        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as opened_file:
                    data = pickle.load(opened_file)
            except (EOFError, IndexError, ValueError, TypeError):
                # dump file is empty or broken
                pass

        return data

    @classmethod
    def get_object(cls, obj_id):
        """Возвращает объект Trassir, если он доступен, иначе ``None``

        Args:
            obj_id (:obj:`str`): Guid объекта или его имя

        Returns:
            :obj:`ScriptHost.SE_Object`: Объект Trassir или ``None``

        Examples:
            >>> obj = BaseUtils.get_object("EZJ4QnbC")
            >>> if obj is None:
            ...     host.error("Object not found")
            ... else:
            ...     host.message("Object name is {0.name}".format(obj))
        """
        if not isinstance(obj_id, (str, unicode)):
            raise TypeError(
                "Expected str or unicode, got '{}'".format(type(obj_id).__name__)
            )
        obj = host.object(obj_id)
        try:
            obj.name
        except EnvironmentError:
            # Object not found
            obj = None
        return obj

    @classmethod
    def get_object_name_by_guid(cls, guid):
        """Возвращает имя объекта Trassir по его guid

        Tip:
            Можно использовать:

            - guid объекта ``"CFsuNBzt"``
            - guid объекта + guid сервера ``"CFsuNBzt_pV4ggECb"``

        Args:
            guid (:obj:`str`): Guid объекта Trassir

        Returns:
            :obj:`str`: Имя объекта, если объект найден, иначе ``guid``

        Examples:
            >>> BaseUtils.get_object_name_by_guid("EZJ4QnbC")
            'AC-D2141IR3'
            >>> BaseUtils.get_object_name_by_guid("EZJ4QnbC-")
            'EZJ4QnbC-'
        """
        guid = guid.split("_", 1)[0]
        obj = cls.get_object(guid)
        if obj is None:
            name = guid
        else:
            name = obj.name
        return name

    @classmethod
    def get_full_guid(cls, obj_id):
        """Возвращает полный guid объекта

        Args:
            obj_id (:obj:`str`): Guid объекта или его имя

        Returns:
            :obj:`str`: Полный guid объекта
        """

        tr_obj = cls.get_object(obj_id)
        full_guid = None
        if tr_obj is not None:
            for obj in host.objects_list(""):
                if tr_obj.guid == obj[1]:
                    full_guid = "{}_{}".format(obj[1], cls._FOLDERS.get(obj[3], obj[3]))
                    break
        return full_guid

    @classmethod
    def get_operator_gui(cls):
        """Возвращает объект интерфейса оператора

        Returns:
            :obj:`OperatorGUI`: Объект интерфейса оператора

        Raises:
            ScriptError: Если не удается загрузить интерфейс

        Examples:
            Открыть интерфейс Trassir а мониторе №1

            >>> operator_gui = BaseUtils.get_operator_gui()
            >>> operator_gui.raise_monitor(1)
        """
        obj = cls.get_object("operatorgui_{}".format(host.settings("").guid))
        if obj is None:
            raise ScriptError("Failed to load operator gui")
        return obj

    @classmethod
    def get_server_guid(cls):
        """Возвращает guid текущего сервра

        Returns:
            :obj:`str`: Guid сервера

        Examples:
            >>> BaseUtils.get_server_guid()
            'client'
        """
        return host.settings("").guid

    @classmethod
    def get_script_name(cls):
        """Возвращает имя текущего скрипта

        Returns:
            :obj:`str`: Имя скрипта

        Examples:
            >>> BaseUtils.get_script_name()
            'Новый скрипт'
        """
        return host.stats().parent()["name"] or __name__

    @classmethod
    def get_screenshot_folder(cls):
        """Возвращает путь до папки скриншотов

        При этом производит проверку папки методом
        :meth:`BaseUtils.is_folder_exists`

        Returns:

            :obj:`str`: Полный путь к папке скриншотов

        Examples:
            >>> BaseUtils.get_screenshot_folder()
            '/home/trassir/shots'
        """
        folder = host.settings("system_wide_options")["screenshots_folder"]
        cls.is_folder_exists(folder)
        return folder


class Worker(threading.Thread):
    """Thread executing tasks from a given tasks queue"""

    def __init__(self, tasks):
        super(Worker, self).__init__()
        self.tasks = tasks
        self.daemon = True
        self.start()

        self.task_working = False

    def run(self):
        while __name__ in sys.modules.keys():
            if not self.tasks.empty():
                self.task_working = True
                func, args, kwargs = self.tasks.get(timeout=1)
                # noinspection PyBroadException
                try:
                    func(*args, **kwargs)
                except:  # # pylint: disable=W0702
                    logger.exception("ThreadPool Worker error")
                finally:
                    self.tasks.task_done()
            else:
                self.task_working = False


class ThreadPool:  # pylint: disable=C1001
    """Pool of threads consuming tasks from a queue"""

    def __init__(self, num_threads):
        self.tasks = Queue()
        self.workers = [Worker(self.tasks) for _ in xrange(num_threads)]

    @property
    def working(self):
        for worker in self.workers:
            if worker.task_working:
                return True
        return False

    def add_task(self, func, *args, **kargs):
        """Add a task to the queue"""
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()


class HTTPRequester(py_object):
    """Framework for urllib2

    See Also:
        https://docs.python.org/2/library/urllib2.html#urllib2.build_opener

    Args:
        opener (:obj:`urllib2.OpenerDirector`, optional): Обработчик запросов.
            По умолчанию :obj:`None`
        timeout (:obj:`int`, optional): Время ожидания запроса, в секундах.
            По умолчанию :obj:`timeout=10`

    Examples:
        Пример запроса к SDK Trassir

        >>> # Отключение проверки сертификата
        >>> context = ssl.create_default_context()
        >>> context.check_hostname = False
        >>> context.verify_mode = ssl.CERT_NONE
        >>>
        >>> handler = urllib2.HTTPSHandler(context=context)
        >>> opener = urllib2.build_opener(handler)
        >>>
        >>> requests = HTTPRequester(opener, timeout=20)
        >>> response = requests.get(
        ...     "https://172.20.0.101:8080/login",
        ...     params={"username": "Admin", "password": "12345"}
        ... )
        >>>
        >>> response.code
        200
        >>> response.text
        '{\\n   "sid" : "T6LAAcxg",\\n   "success" : 1\\n}\\n'
        >>> response.json
        {u'success': 1, u'sid': u'T6LAAcxg'}
    """

    class Response(py_object):  # pylint: disable=R0903
        """Класс ответа от сервера

        Attributes:
            code (:obj:`str` | :obj:`int`): Код ответа сервера
            text (:obj:`str`): Текст ответа
            json (:obj:`dict` | :obj:`list`): Создает объект из json ответа
        """

        def __init__(self, *args):
            self.code, self.text = args

        @property
        def json(self):
            return json.loads(self.text)

    def __init__(self, opener=None, timeout=10):
        if opener is None:
            handler = urllib2.BaseHandler()
            opener = urllib2.build_opener(handler)
        self._opener = opener

        self.timeout = timeout

    @BaseUtils.catch_request_exceptions
    def _get_response(self, request):
        """Returns response

        Args:
            request (:obj:`urllib2.Request`): This class is an abstraction of a URL request
        """
        response = self._opener.open(request, timeout=self.timeout)
        return response.code, response.read()

    @staticmethod
    def _parse_params(**params):
        """Params get string params

        Args:
            **params (dict): Keyword arguments

        Returns:
            str: params string
        """
        return "&".join(
            "{key}={value}".format(key=key, value=value)
            for key, value in params.iteritems()
        )

    @staticmethod
    def _prepare_headers(headers):
        """Prepare headers for request"""
        if headers is None:
            headers = {}

        if "User-Agent" not in headers:
            headers["User-Agent"] = "TrassirScript"
        return headers

    def get(self, url, params=None, headers=None):
        """Создает GET запрос по указанному :obj:`url`

        Args:
            url (:obj:`str`): Url для запроса
            params (:obj:`dict`, optional): Параметры GET запроса
            headers (:obj:`dict`, optional): Заголовки запроса

        Examples:
            >>> requests = HTTPRequester()
            >>> response = requests.get(
            ...     "http://httpbin.org/get",
            ...     params={"PARAMETER": "TEST"},
            ... )
            >>> response.code
            200
            >>> response.text
            '{\\n  "args": {\\n    "PARAMETER": "TEST"\\n  }, \\n ...'
            >>> response.json
            {u'args': {u'PARAMETER': u'TEST'}, ...}

        Returns:
            :class:`HTTPRequester.Response`: Response instance
        """
        if params is not None:
            url += "?{params}".format(params=self._parse_params(**params))

        headers = self._prepare_headers(headers)

        request = urllib2.Request(url, headers=headers)
        response = self._get_response(request)
        return self.Response(*response)

    def post(self, url, data=None, headers=None):
        """Создает POST запрос по указанному :obj:`url`

        Args:
            url (:obj:`str`): Url для запроса
            data (:obj:`dict`, optional): Данные POST запроса
            headers (:obj:`dict`, optional): Заголовки запроса

        Examples:
            >>> requests = HTTPRequester()
            >>> response = requests.post(
            ...     "http://httpbin.org/post",
            ...     data={"PARAMETER": "TEST"},
            ...     headers={"Content-Type": "application/json"},
            ... )
            >>> response.code
            200
            >>> response.text
            '{\\n  "args": {\\n    "PARAMETER": "TEST"\\n  }, \\n ...'
            >>> response.json
            {u'args': {u'PARAMETER': u'TEST'}, ...}

        Returns:
            :class:`HTTPRequester.Response`: Response instance
        """
        if data is None:
            data = {}

        if isinstance(data, dict):
            data = urllib.urlencode(data)

        headers = self._prepare_headers(headers)

        request = urllib2.Request(url, data=data, headers=headers)
        response = self._get_response(request)
        return self.Response(*response)


class ScriptObject(host.TrassirObject, py_object):
    """Создает объект для генерации событий

    Args:
        name (:obj:`str`, optional): Имя объекта. По умолчанию :obj:`None`
        guid (:obj:`str`, optional): Guid объекта. По умолчанию :obj:`None`
        parent (:obj:`str`, optional): Guid родительского объекта. По умолчанию :obj:`None`

    Note:
        - Имя объекта по умолчанию - :meth:`BaseUtils.get_script_name`
        - Guid объекта по умолчанию строится по шаблноу ``"{script_guid}_object"``
        - Guid родительского объекта по умолчанию -
          :meth:`BaseUtils.get_server_guid`

    Examples:
        >>> # Создаем объект
        >>> scr_obj = ScriptObject()

        >>> # Проверяем текущее состояние объекта
        >>> scr_obj.health
        'OK'

        >>> # Установить флаг возле объекта
        >>> scr_obj.check_me = True

        >>> # Сгенерировать событие с текстом
        >>> scr_obj.fire_event_v2("New event")
    """

    def __init__(self, name=None, guid=None, parent=None):
        super(ScriptObject, self).__init__("Script")

        scr_parent = host.stats().parent()

        self._name = name or BaseUtils.get_script_name()
        self.set_name(self._name)

        self._guid = guid or "{}-object".format(scr_parent.guid)
        self.set_guid(self._guid)

        self._parent = parent or BaseUtils.get_server_guid()
        self.set_parent(self._parent)

        self._folder = ""

        self._health = "OK"
        self._check_me = True

        self.set_initial_state([self._health, self._check_me])

        host.object_add(self)

        self.context_menu = []

    @property
    def health(self):
        """:obj:`"OK"` | :obj:`"Error"`: Состояние объекта"""
        return self._health

    @health.setter
    def health(self, value):
        if value in ["OK", "Error"]:
            self.set_state([value, self._check_me])
            self._health = value
        else:
            raise ValueError("Expected 'OK' or 'Error', got '{}'".format(value))

    @property
    def check_me(self):
        """:obj:`bool`: Флаг ``check_me`` объекта"""
        return bool(1 - self._check_me)

    @check_me.setter
    def check_me(self, value):
        if isinstance(value, bool) or value in [1, 0]:
            value = 1 - value
            self.set_state([self._health, value])
            self._check_me = value
        else:
            raise ValueError("Expected bool or 1|0, got '{}'".format(value))

    @property
    def name(self):
        """:obj:`str`: Имя объекта"""
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.set_name(value)
            self._name = value
        else:
            raise ValueError("Expected str, got {}".format(type(value).__name__))

    @property
    def folder(self):
        """:obj:`str`: Папка объекта"""
        return self._folder

    @folder.setter
    def folder(self, value):
        if not value:
            raise ValueError("Object guid can't be empty")

        if isinstance(value, str):
            if self._folder:
                self.change_folder(value)
            else:
                self.set_folder(value)
            self._folder = value
        else:
            raise ValueError("Expected str, got {}".format(type(value).__name__))

    def context_menu_button(self, text, callback):
        """Добавляет кнопку в контекстное меню объекта

        Args:
            text (:obj:`str`): Текст кнопки
            callback (:obj:`function`): Функция, которая вызывается при нажатии
                на кнопку. В качестве единственного аргумента функция приимает
                текущий объект (:obj:`host_ip.object(self.guid)`).

        Returns:
            :obj:`SE_ContextCatcher`: Хендлер контекстного меню

        Raises:
            ValueError: Если пустой текст кнопки.
            TypeError: Если callback нельзя вызвать в качестве функции.

        Examples:
            >>> scr = ScriptObject()
            >>>
            >>> def switch(obj):
            ...     scr.check_me = not scr.check_me
            ...     btn.set_name("OFF" if scr.check_me else "ON")
            >>>
            >>> btn = scr.context_menu_button("ON", switch)

                .. image:: images/context_menu_button.png

            >>> btn
            <host_ip.SE_ContextCatcher object at 0x17B01A98>
            >>> scr.context_menu
            [('ON', 'switch', <host_ip.SE_ContextCatcher object at 0x17B01A98>)]
        """
        if not text:
            raise ValueError("No text")

        if not callable(callback):
            raise TypeError("Callback function is not callable")

        btn = host.activate_on_context_menu(self._guid, text, callback)
        self.context_menu.append((text, callback.__name__, btn))
        return btn

    def fire_event_v2(self, message, channel="", data=""):
        """Создает событие в Trassir

        Args:
            message (:obj:`str`): Сообщение события (``p1``)
            channel (:obj:`str`, optional): Ассоциированный с событием канал (``p2``)
            data (:obj:`str`, optional): Дополнительные данные (``p3``)

        Examples:
            >>> scr = ScriptObject()
            >>> scr.fire_event_v2("Hello world")

                .. image:: images/fire_event_v2.png
        """
        if not isinstance(data, str):
            data = BaseUtils.to_json(data, indent=None)

        self.fire_event("Script: %1", message, channel, data)


class TrObject(py_object):  # pylint: disable=R0902
    """Вспомогательный класс для работы с объектами Trassir

    Attributes:
        obj (:obj:`SE_Object`): Объект trassir :obj:`object('{guid}')` или :obj:`None`
        obj_methods (List[:obj:`str`]): Список методов объекта :attr:`TrObject.obj`
        name (:obj:`str`): Имя объекта или его guid
        guid (:obj:`str`): Guid объекта
        full_guid (:obj:`str`): Полный guid :obj:`{guid объекта}_{guid сервера}`
            или :obj:`None`
        type (:obj:`str`): Тип объекта, например :obj:`"RemoteServer"`, :obj:`"Channel"`,
            :obj:`"Grabber"`, :obj:`"User"`, и др.
        path (:obj:`str`): Путь в настройках или :obj:`None`
        parent (:obj:`str`): Guid родительского объекта или :obj:`None`
        server (:obj:`str`): Guid сервера или :obj:`None`
        settings (:obj:`SE_Settings`): Объект настроек ``settings('{path}')`` или :obj:`None`

    Raises:
        TypeError: Если неправильные параметры объекта
        ValueError: Если в имени объекта есть запятые
    """

    obj, name, guid, full_guid, type = None, None, None, None, None
    path, parent, server, settings = None, None, None, None

    def __init__(self, obj):

        if isinstance(obj, host.ScriptHost.SE_Settings):
            self._load_from_settings(obj)
        elif isinstance(obj, tuple):
            if len(obj) == 4:
                self._load_from_tuple(obj)
            else:
                raise TypeError(
                    "Expected tuple(name, guid, type, parent), got tuple'{}'".format(
                        obj
                    )
                )
        else:
            raise TypeError("Unexpected object type '{}'".format(type(obj).__name__))

    @staticmethod
    def _check_object_name(object_name):
        """Check if object name hasn't got commas

        Args:
            object_name (str):

        Returns:
            str: object_name.strip()

        Raises:
            ValueError: If "," found in object name
        """
        if "," in object_name:
            raise ValueError(
                "Please, rename object '{}' without commas".format(object_name)
            )
        return object_name.strip()

    @staticmethod
    def _parse_server_from_path(path):
        """Parse server guid from full path

        Args:
            path (str): Full Trassir settings path;
                example: '/pV4ggECb/_persons/n68LOBhG' returns 'pV4ggECb'
        """
        try:
            server = path.split("/", 2)[1]
        except IndexError:
            server = None

        return server

    @staticmethod
    def _find_server_guid_for_object(object_guid):
        """Find server guid for object

        Args:
            object_guid (str): Object guid

        Returns:
            str: Server guid if server found
            None: If server not found
        """
        all_objects = {
            obj[1]: {"name": obj[0], "guid": obj[1], "type": obj[2], "parent": obj[3]}
            for obj in host.objects_list("")
        }

        def get_parent(child_guid):
            child = all_objects.get(child_guid, None)
            if child:
                if child["type"] == "Server":
                    return child["guid"]
                return get_parent(child["parent"])
            return ""

        return get_parent(object_guid)

    def _get_object_methods(self):
        """Get object methods"""
        if self.obj:
            return [method for method in dir(self.obj) if not method.startswith("__")]
        return []

    def _load_from_settings(self, obj):
        """Preparing attributes from SE_Settings object"""
        self.obj = BaseUtils.get_object(obj.guid)
        self.obj_methods = self._get_object_methods()

        try:
            obj_name = obj.name
        except KeyError:
            obj_name = obj.guid

        self.name = self._check_object_name(obj_name)
        self.guid = obj.guid
        self.type = obj.type
        self.path = obj.path
        self.server = self._parse_server_from_path(obj.path)
        self.settings = obj

        if self.server and self.server != self.guid:
            self.full_guid = "{0.guid}_{0.server}".format(self)

    def _load_from_tuple(self, obj):
        """Preparing attributes from tuple object"""
        self.obj = BaseUtils.get_object(obj[1])
        self.obj_methods = self._get_object_methods()
        self.name = self._check_object_name(obj[0])
        self.guid = obj[1]
        self.type = obj[2]
        self.parent = obj[3]
        self.server = self._find_server_guid_for_object(obj[1])

        if self.server and self.server != self.guid:
            self.full_guid = "{0.guid}_{0.server}".format(self)

    def __repr__(self):
        return "TrObject('{}')".format(self.name)

    def __str__(self):
        return "{self.type}: {self.name} ({self.guid})".format(self=self)


class ParameterError(ScriptError):
    """Ошибка в параметрах скрипта"""

    pass


class BasicObject(py_object):  # pylint: disable=R0903
    """Basic object class"""

    def __init__(self):
        self.this_server_guid = BaseUtils.get_server_guid()

    class UniqueNameError(ScriptError):
        """Имя объекта не уникально"""

        pass

    class ObjectsNotFoundError(ScriptError):
        """Не найдены объекты с заданными именами"""

        pass

    def _check_unique_name(self, objects, object_names):
        """Check if all objects name are unique

        Args:
            objects (list): Objects list from _get_objects_from_settings

        Raises:
            UniqueNameError: If some object name is not uniques
        """
        unique_names = []
        for obj in objects:
            if obj.name in object_names:
                if obj.name not in unique_names:
                    unique_names.append(obj.name)
                else:
                    raise self.UniqueNameError(
                        "Найдено несколько объектов {obj.type} с одинаковым именем '{obj.name}'! "
                        "Задайте уникальные имена".format(obj=obj)
                    )

    @staticmethod
    def _objects_str_to_list(objects):
        """Split object names if objects is str and strip each name

        Args:
            objects (str|list): Trassir object names in comma spaced string or list

        Returns:
            list: Stripped Trassir object names

        Raises:
            ScriptError: If object name selected more than once
        """
        if isinstance(objects, str):
            objects = objects.split(",")

        names = []
        for name in objects:
            strip_name = name.strip()
            if strip_name in names:
                raise ParameterError("Объект '{}' выбран несколько раз".format(name))
            names.append(strip_name)

        return names

    def _filter_objects_by_name(self, objects, object_names):
        """Filter object by names

        Args:
            objects (list): TrObject objects list
            object_names (str|list): Trassir object names in comma spaced string or list

        Raises:
            ObjectsNotFoundError: If len(object_name) != len(filtered_object)
        """
        object_names = self._objects_str_to_list(object_names)

        self._check_unique_name(objects, object_names)

        filtered_object = [obj for obj in objects if obj.name in object_names]

        if len(filtered_object) != len(object_names):
            channels_not_found = set(object_names) - set(
                obj.name for obj in filtered_object
            )

            try:
                object_type = objects[0].type
            except IndexError:
                object_type = "Unknown"

            raise self.ObjectsNotFoundError(
                "Не найдены объекты {object_type}: {names}".format(
                    object_type=object_type,
                    names=", ".join(name for name in channels_not_found),
                )
            )

        return filtered_object


class ObjectFromSetting(BasicObject):  # pylint: disable=R0903
    """Base class for setting objects"""

    def __init__(self):  # pylint: disable=W0235
        super(ObjectFromSetting, self).__init__()

    @staticmethod
    def _load_objects_from_settings(settings_path, obj_type, sub_condition=None):
        """Load objects from Trassir settings

        Args:
            settings_path (:obj:`str`): Trassir settings path. Example ``"scripts"``.
                Click F4 in the Trassir settings window to show hidden parameters.
            obj_type (:obj:`str` | :obj:`list`): Loading object type. Example ``"EmailAccount"``
            sub_condition (function, optional): Function with SE_Settings as argument to filter objects

        Returns:
            list: TrObject objects list
                Example [TrObject(...), TrObject(...), ...]
        """
        try:
            settings = host.settings(settings_path)
        except KeyError:
            settings = None

        objects = []
        if settings is not None:
            if isinstance(obj_type, str):
                obj_type = [obj_type]

            if sub_condition is None:
                sub_condition = BaseUtils.do_nothing

            for obj in settings.ls():
                if obj.type in obj_type:
                    if sub_condition(obj):
                        objects.append(TrObject(obj))
        return objects

    def _get_objects_from_settings(  # pylint: disable=R0913
            self,
            settings_path,
            object_type,
            object_names=None,
            server_guid=None,
            ban_empty_result=False,
            sub_condition=None,
    ):
        """Check if objects exists and returns list from _load_objects_from_settings

        Note:
             If object_names is not None - checking if all object names are unique

        Args:
            settings_path (:obj:`str`): Trassir settings path. Example ``"scripts"``.
                Click F4 in the Trassir settings window to show hidden parameters.
            object_type (:obj:`str` | :obj:`list`): Loading object type. Example ``"EmailAccount"``
            object_names (:obj:`str` | :obj:`list`, optional): Comma spaced string or
                list of object names. Default :obj:`None`
            server_guid (:obj:`str` | :obj:`list`, optional): Server guid. Default :obj:`None`
            ban_empty_result (:obj:`bool`, optional): If True - raise error if no one object found
            sub_condition (:obj:`func`, optional) : Function with SE_Settings as argument to filter objects

        Returns:
            list: Trassir list from _load_objects_from_settings

        Raises:
            ObjectsNotFoundError: If can't find channel
        """
        if object_names == "":
            raise ParameterError("'{}' не выбраны".format(object_type))

        if server_guid is None:
            server_guid = self.this_server_guid

        if isinstance(server_guid, str):
            server_guid = [server_guid]

        objects = []

        for guid in server_guid:
            objects += self._load_objects_from_settings(
                settings_path.format(server_guid=guid), object_type, sub_condition
            )

        if ban_empty_result and not objects:
            raise self.ObjectsNotFoundError(
                "Не найдено ниодного объекта '{}'".format(object_type)
            )

        if object_names is None:
            return objects
        return self._filter_objects_by_name(objects, object_names)


class Servers(ObjectFromSetting):
    """Класс для работы с серверами

    Examples:
        >>> srvs = Servers()
        >>> local_srv = srvs.get_local()
        [TrObject('Клиент')]
        >>> # Првоерим "Здоровье" локального сервера
        >>> local_srv[0].obj.state("server_health")
        'Health Problem'
    """

    def __init__(self):  # pylint: disable=W0235
        super(Servers, self).__init__()

    def get_local(self):
        """Возвращает локальный сервер (на котором запущен скрипт)

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._load_objects_from_settings("/", ["Client", "LocalServer"])

    def get_remote(self):
        """Возвращает список удаленных серверов

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._load_objects_from_settings("/", "RemoteServer")

    def get_all(self):
        """Возвращает список всех доступных серверов

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._load_objects_from_settings(
            "/", ["Client", "LocalServer", "RemoteServer"]
        )


class Channels(ObjectFromSetting):
    """Класс для работы с каналами

    See Also:
        `Каналы - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-channels-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> channels = Channels()
        >>> selected_channels = channels.get_enabled("AC-D2121IR3W 2,AC-D9141IR2 1")
        >>> selected_channels
        [TrObject('AC-D2121IR3W 2'), TrObject('AC-D9141IR2 1')]
        >>>
        >>> # Включим ручную запись на выбранных каналах
        >>> for channel in selected_channels:
        ...     channel.obj.manual_record_start()
        >>>
        >>> # Или добавим к имени канала его guid
        >>> for channel in selected_channels:
        ...     channel.settings["name"] += " ({})".format(channel.guid)
    """

    def __init__(self, server_guid=None):
        super(Channels, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных каналов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            not_zombie = 1 - sett["archive_zombie_flag"]
            if not_zombie:
                try:
                    return host.settings(sett.cd("info")["grabber_path"])[
                        "grabber_enabled"
                    ]
                except KeyError:
                    return 0
            return 0

        return self._get_objects_from_settings(
            "/{server_guid}/channels",
            "Channel",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных каналов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            zombie = sett["archive_zombie_flag"]
            if not zombie:
                try:
                    return (
                            1
                            - host.settings(sett.cd("info")["grabber_path"])[
                                "grabber_enabled"
                            ]
                    )
                except KeyError:
                    return 1
            return 1

        return self._get_objects_from_settings(
            "/{server_guid}/channels",
            "Channel",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех каналов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/channels",
            "Channel",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Devices(ObjectFromSetting):
    """Класс для работы с ip устройствами

    See Also:
        `IP-устройства - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-ip-cameras-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> devices = Devices()
        >>> enabled_devices = devices.get_enabled()
        >>> enabled_devices
        [TrObject('AC-D2121IR3W'), TrObject('AC-D5123IR32'), ...]
        >>>
        >>> # Перезагрузим все устройства
        >>> for dev in enabled_devices:
        ...     dev.settings["reboot"] = 1
    """

    def __init__(self, server_guid=None):
        super(Devices, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных устройств

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["grabber_enabled"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/ip_cameras",
            "Grabber",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных устройств

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["grabber_enabled"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/ip_cameras",
            "Grabber",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех устройств

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/ip_cameras",
            "Grabber",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Scripts(ObjectFromSetting):
    """Класс для работы со скриптами

    See Also:
        `Скрипты - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-script-feature.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> scripts = Scripts()
        >>> all_scripts = scripts.get_all()
        >>> all_scripts
        [TrObject('Новый скрипт'), TrObject('HDD Health Monitor'), TrObject('Password Reminder')]
        >>>
        >>> # Отключим все скрипты
        >>> for script in all_scripts:
        ...     script.settings["enable"] = 0
    """

    def __init__(self, server_guid=None):
        super(Scripts, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных скриптов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["enable"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Script",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных скриптов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["enable"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Script",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех скриптов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Script",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class StockScripts(ObjectFromSetting):
    """Класс для работы со встроенными скриптами

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> stock_scripts = StockScripts()
        >>> all_scripts = stock_scripts.get_all()
        >>> all_scripts
        [TrObject('MegaRAID Monitor')]
        >>>
        >>> # Отключим все скрипты
        >>> for script in all_scripts:
        ...     script.settings["enable"] = 0
    """

    def __init__(self, server_guid=None):
        super(StockScripts, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных скриптов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["enable"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "StockScript",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных скриптов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["enable"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "StockScript",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех скриптов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "StockScript",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Rules(ObjectFromSetting):
    """Класс для работы с правилами

    See Also:
        `Правила - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-rule.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> rules = Rules()
        >>> all_rules = rules.get_all()
        >>> all_rules
        [TrObject('!Rule'), TrObject('NEW RULE'), TrObject('Новое правило')]
        >>>
        >>> # Отключим все правила
        >>> for rule in all_rules:
        ...     rule.settings["enable"] = 0
    """

    def __init__(self, server_guid=None):
        super(Rules, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных правил

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["enable"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Rule",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных правил

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["enable"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Rule",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех правил

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен. По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "Rule",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class TemplateLoops(ObjectFromSetting):
    """Класс для работы с циклическими просмотрами шаблонов

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> tmplate_loops = TemplateLoops()
        >>> tmplate_loops.get_all()
        [TrObject('Новый циклический просмотр')]
    """

    def __init__(self, server_guid=None):
        super(TemplateLoops, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных циклических просмотров шаблонов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["enable"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "TemplateLoop",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных циклических просмотров шаблонов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["enable"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "TemplateLoop",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех циклических просмотров шаблонов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "TemplateLoop",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class EmailAccounts(ObjectFromSetting):  # pylint: disable=R0903
    """Класс для работы с E-Mail аккаунтами

    See Also:
        `Добавление учетной записи e-mail - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-email-account.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> email_accounts = EmailAccounts()
        >>> email_accounts.get_all()
        [TrObject('Новая учетная запись e-mail'), TrObject('MyAccount')]
    """

    def __init__(self, server_guid=None):
        super(EmailAccounts, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_all(self, names=None):
        """Возвращает список всех E-Mail аккаунтов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/scripts",
            "EmailAccount",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class NetworkNodes(ObjectFromSetting):
    """Класс для работы с сетевыми подключениями

    See Also:
        `Сеть - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-network-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> network_nodes = NetworkNodes("client")
        >>> network_nodes.get_enabled()
        [TrObject('QuattroStationPro (172.20.0.101)'), TrObject('NSK-HD-01 (127.0.0.1)')]
    """

    def __init__(self, server_guid=None):
        super(NetworkNodes, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных сетевых подключений

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["should_be_connected"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/network",
            "NetworkNode",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных сетевых подключений

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["should_be_connected"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/network",
            "NetworkNode",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех сетевых подключений

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/network",
            "NetworkNode",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class PosTerminals(ObjectFromSetting):
    """Класс для работы с POS Терминалами

    See Also:
        `Настройка POS-терминалов - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-pos-terminals-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> pos_terminals = PosTerminals()
        >>> pos_terminals.get_disabled()
        [TrObject('Касса (1)')]
    """

    def __init__(self, server_guid=None):
        super(PosTerminals, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_enabled(self, names=None):
        """Возвращает список активных POS Терминалов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return sett["pos_enable"]
            except KeyError:
                return 0

        return self._get_objects_from_settings(
            "/{server_guid}/pos_folder2/terminals",
            "PosTerminal",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_disabled(self, names=None):
        """Возвращает список неактивных POS Терминалов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        def sub_condition(sett):
            try:
                return 1 - sett["pos_enable"]
            except KeyError:
                return 1

        return self._get_objects_from_settings(
            "/{server_guid}/pos_folder2/terminals",
            "PosTerminal",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )

    def get_all(self, names=None):
        """Возвращает список всех POS Терминалов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        return self._get_objects_from_settings(
            "/{server_guid}/pos_folder2/terminals",
            "PosTerminal",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Users(ObjectFromSetting):
    """Класс для работы с пользователями и их группами.

    See Also:
        `Пользователи - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-users-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> users = Users()
        >>> users.get_groups()
        [TrObject('TEST')]
    """

    def __init__(self, server_guid=None):
        super(Users, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_groups(self, names=None):
        """Возвращает список групп пользователей

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_settings(
            "/{server_guid}/users",
            "Group",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_users(self, names=None):
        """Возвращает список пользователей

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_settings(
            "/{server_guid}/users",
            "User",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_users_by_groups(self, group_names):
        """Возвращает список пользователей из указанных групп

        Args:
            group_names (:obj:`str` | :obj:`list`): :obj:`str` - имена групп,
                разделенные запятыми или :obj:`list` - список имен.

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        if group_names is None:
            groups = [""]
        else:
            groups = [group.guid for group in self.get_groups(names=group_names)]

        def sub_condition(sett):
            return sett["group"] in groups

        return self._get_objects_from_settings(
            "/{server_guid}/users",
            "User",
            object_names=None,
            server_guid=self.server_guid,
            sub_condition=sub_condition,
        )


class Templates(ObjectFromSetting):  # pylint: disable=R0903
    """Класс для работы с существующими шаблонами.

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> templates = Templates(BaseUtils.get_server_guid())
        >>> templates.get_all()
        [TrObject('Parking'), TrObject('FR'), TrObject('AT'), TrObject('AD+')]
    """

    def __init__(self, server_guid=None):
        super(Templates, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_all(self, names=None):
        """Возвращает список шаблонов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_settings(
            "/{server_guid}/templates",
            "Template",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Persons(ObjectFromSetting):
    """Класс для работы с персонами и их папками.

    See Also:
        `Персоны - Руководство пользователя Trassir
        <https://www.dssl.ru/files/trassir/manual/ru/setup-persons-folder.html>`_

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
            >>> persons = Persons()
            >>> persons.get_folders()
            [TrObject('Мошенники'), TrObject('DSSL'), TrObject('persons')]
            >>> persons.get_persons()
            [
                {
                    'name': 'Leonardo',
                    'guid': 'cJuJYAha',
                    'gender': 0,
                    'birth_date': '1980-01-01',
                    'comment': 'Comment',
                    'contact_info': 'Contact info',
                    'folder_guid': 'n68LOBhG',
                    'image': <image, str>,
                    'image_guid': 'gBHZ2vpz',
                    'effective_rights': 0,
                },
                ...
            ]
            >>> persons.get_person_by_guid("cJuJYAha")
            {
                'name': 'Leonardo',
                'guid': 'cJuJYAha',
                'gender': 0,
                'birth_date': '1980-01-01',
                'comment': 'Comment',
                'contact_info': 'Contact info',
                'folder_guid': 'n68LOBhG',
                'image': <image, str>,
                'image_guid': 'gBHZ2vpz',
                'effective_rights': 0,
            }
    """

    _PERSONS_UPDATE_TIMEOUT = 10 * 60  # Time in sec between update _persons dict

    def __init__(self, server_guid=None):
        super(Persons, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        if isinstance(server_guid, str):
            server_guid = [server_guid]

        self.server_guid = server_guid

        self._persons = None

    def _update_persons_dict(self, timeout=10):
        """Updating self._persons dict"""
        persons = self.get_persons(timeout=timeout)
        by_guid, by_name = {}, {}
        for person in persons:
            by_guid[person["guid"]] = person
            by_name[person["name"]] = person

        self._persons = {
            "update_ts": int(time.time()),
            "by_guid": by_guid,
            "by_name": by_name,
        }

    def _check_loaded_persons(self, timeout=10):
        """This method check if self._persons dict is need to be updated"""
        ts_now = int(time.time())

        if (
                self._persons is None
                or (ts_now - self._persons["update_ts"]) > self._PERSONS_UPDATE_TIMEOUT
        ):
            self._update_persons_dict(timeout=timeout)

    def get_folders(self, names=None):
        """Возвращает список папок персон

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        try:
            folders = self._get_objects_from_settings(
                "/{server_guid}/persons",
                "PersonsSubFolder",
                object_names=names,
                server_guid=self.server_guid,
            )

            if names is None or "persons" in names:
                for guid in self.server_guid:
                    try:
                        settings = host.settings("/{}/persons".format(guid))
                    except KeyError:
                        continue

                    folders.append(TrObject(settings))

        except self.ObjectsNotFoundError as err:
            folders = []
            names = self._objects_str_to_list(names)

            if names is None or "persons" in names:
                for guid in self.server_guid:
                    try:
                        settings = host.settings("/{}/persons".format(guid))
                    except KeyError:
                        continue

                    folders.append(TrObject(settings))

            if not folders:
                raise err

        return folders

    def get_persons(self, folder_names=None, timeout=10):
        """Возвращает список персон

        Note:
            Данный метод работает только с локальной БД.

        Args:
            folder_names (:obj:`str` | List[:obj:`str`], optional): :obj:`str` -
                названия папок персон, разделенные запятыми или :obj:`list` -
                список папок персон. По умолчанию :obj:`None`
            timeout (:obj:`int`, optional): Макс. время запроса к БД.
                По умолчанию ``timeout=10``

        Returns:
            List[:obj:`dict`]: Список персон - если персоны найдены

        Raises:
            EnvironmentError: Если произошла ошибка при запросе в БД.
            TrassirError: Если в данной сборке Trassir нет метода :obj:`host_ip.service_persons_get`
        """
        tmp_server_guid = self.server_guid[:]
        self.server_guid = [self.this_server_guid]
        persons_folders = self.get_folders(names=folder_names)
        self.server_guid = tmp_server_guid[:]

        try:
            persons = host.service_persons_get(
                [folder.guid for folder in persons_folders], True, 0, 0, timeout
            )
        except AttributeError:
            raise TrassirError(
                "Данный функционал не поддерживается вашей сборкой Trassir. "
                "Попробуйте обновить ПО."
            )

        if isinstance(persons, str):
            raise EnvironmentError(persons)

        return persons

    def get_person_by_guid(self, person_guid, timeout=10):
        """Возвращает информацию о персоне по его guid

        Note:
            Для уменьшения кол-ва запросов к БД - метод создает локальную
            копию всех персон при первом запросе и обновляет ее вместе
            с последующими запросами не чаще чем 1 раз в 10 минут.

        Args:
            person_guid (:obj:`str`): Guid персоны
            timeout (:obj:`int`, optional): Макс. время запроса к БД.
                По умолчанию ``timeout=10``

        Returns:
            :obj:`dict`: Даные о персоне или :obj:`None` если персона не найдена
        """
        self._check_loaded_persons(timeout=timeout)
        return self._persons["by_guid"].get(person_guid)

    def get_person_by_name(self, person_name, timeout=10):
        """Возвращает информацию о персоне по его имени

        Note:
            Для уменьшения кол-ва запросов к БД - метод создает локальную
            копию всех персон при первом запросе и обновляет ее вместе
            с последующими запросами не чаще чем 1 раз в 10 минут.

        Args:
            person_name (:obj:`str`): Имя персоны
            timeout (:obj:`int`, optional): Макс. время запроса к БД.
                По умолчанию ``timeout=10``

        Returns:
            :obj:`dict`: Даные о персоне или :obj:`None` если персона не найдена
        """
        self._check_loaded_persons(timeout=timeout)
        return self._persons["by_name"].get(person_name)


class ObjectFromList(BasicObject):  # pylint: disable=R0903
    """Base class for object from objscts list"""

    def __init__(self):  # pylint: disable=W0235
        super(ObjectFromList, self).__init__()

    @staticmethod
    def _load_objects_from_list(obj_type, sub_condition=None):
        """Load objects from Trassir objects_list method

        Args:
            obj_type (str | list): Loading object type; example: "EmailAccount"
            sub_condition (function, optional): Function with SE_Settings as argument to filter objects

        Returns:
            list: TrObject objects list
                Example [TrObject(...), TrObject(...), ...]
        """
        if sub_condition is None:
            sub_condition = BaseUtils.do_nothing

        objects = []
        for obj in host.objects_list(obj_type):
            if sub_condition(obj):
                objects.append(TrObject(obj))

        return objects

    def _get_objects_from_list(  # pylint: disable=R0913
            self,
            object_type,
            object_names=None,
            server_guid=None,
            ban_empty_result=False,
            sub_condition=None,
    ):
        """Check if objects exists and returns list from _load_objects_from_settings

        Note:
             If object_names is not None - checking if all object names are unique

        Args:
            object_type (str|list): Loading object type; example: "EmailAccount"
            object_names (str|list, optional): Comma spaced string or list of object names; default: None
            server_guid (str|list, optional): Server guids; default: None
            ban_empty_result (bool, optional): If True - raise ObjectsNotFoundError if no one object found
            sub_condition (func, optional) : Function with SE_Settings as argument to filter objects

        Returns:
            list: Trassir list from _load_objects_from_settings

        Raises:
            ObjectsNotFoundError: If can't find channel
        """
        if object_names == "":
            raise ParameterError("'{}' не выбраны".format(object_type))

        if server_guid is None:
            server_guid = self.this_server_guid
        else:
            if isinstance(server_guid, str):
                server_guid = [server_guid]

        objects = self._load_objects_from_list(object_type, sub_condition)

        objects = [obj for obj in objects if obj.server in server_guid]

        if ban_empty_result and not objects:
            raise self.ObjectsNotFoundError(
                "Не найдено ниодного объекта '{}'".format(object_type)
            )

        if object_names is None:
            return objects
        return self._filter_objects_by_name(objects, object_names)

    @staticmethod
    def _zone_type(zone_obj):  # pylint: disable=R0911,R0912,R1710
        """Возвращает тип зоны для объекта

        Args:
            zone_obj (:obj:`SE_Object`): Объект trassir ``object('{guid}')``

        Returns:
            :obj:`str`: Тип объекта
            :obj:`None`: Если тип зоны неизвестен
        """

        if not isinstance(zone_obj, host.ScriptHost.SE_Object):
            raise TypeError(
                "Expected SE_Object, got '{}'".format(type(zone_obj).__name__)
            )

        try:
            guid = zone_obj.guid
            channel, server = zone_obj.associated_channel.split("_")
        except (AttributeError, ValueError):
            return

        try:
            zones_dir = host.settings(
                "/{}/channels/{}/people_zones".format(server, channel)
            )
            for i in xrange(16):
                if zones_dir["zone%02d_guid" % i] == guid:
                    func_type = zones_dir["zone%02d_func_type" % i]
                    if isinstance(func_type, int):
                        return (
                            ["Queue", "Workplace"][func_type]
                            if func_type in range(2)
                            else "Queue"
                        )
                    return func_type
        except KeyError:
            # not a queue or workplace
            pass

        try:
            zones_dir = host.settings(
                "/{}/channels/{}/workplace_zones".format(server, channel)
            )
            for i in xrange(16):
                if zones_dir["zone%02d_guid" % i] == guid:
                    return "Workplace"
        except KeyError:
            # not a workplace
            pass

        try:
            zones_dir = host.settings("/%s/channels/%s/deep_people" % (server, channel))
            for i in xrange(16):
                if zones_dir["zone%02d_guid" % i] == guid:
                    if zones_dir["zone%02d_type" % i] in ["border", "border_swapped"]:
                        return "Border"
                    return "Queue"
        except KeyError:
            # not a deep people queue
            pass


class GPIO(ObjectFromList):
    """Класс для работы с тревожными входами/выходами

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> gpio = GPIO()
        >>> gpio_door = gpio.get_inputs("Door")[0]
        >>> gpio_door.obj.state("gpio_input_level")
        'Input Low (Normal High)'
        >>> gpio_light = gpio.get_outputs("Light")[0]
        >>> gpio_light.obj.set_output_high()
    """

    def __init__(self, server_guid=None):
        super(GPIO, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_inputs(self, names=None):
        """Возвращает список тревожных входов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "GPIO Input",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_outputs(self, names=None):
        """Возвращает список тревожных выходов

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "GPIO Output",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Zones(ObjectFromList):
    """Класс для работы с зонами

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> zones = Zones()
        >>> zones.get_queues("Касса 1")[0].obj.state("zone_queue")
        '5+'
    """

    def __init__(self, server_guid=None):
        super(Zones, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_people(self, names=None):
        """Возвращает список PeopleZones

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "PeopleZone",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_simt(self, names=None):
        """Возвращает список зон SIMT

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "SIMT Zone",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_workplaces(self, names=None):
        """Возвращает список рабочих зон

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        people_zones = self.get_people(names=names)

        return [
            zone
            for zone in people_zones
            if self._zone_type(zone.obj) in ["Workplace", "Рабочее место"]
        ]

    def get_queues(self, names=None):
        """Возвращает список зон очередей

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        people_zones = self.get_people(names=names)

        return [
            zone
            for zone in people_zones
            if self._zone_type(zone.obj) in ["", "Queue", "Очередь"]
        ]

    def get_shelves(self, names=None):
        """Возвращает список зон полок

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "Shelf",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class Borders(ObjectFromList):
    """Класс для работы с линиями пересечения

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.

    Examples:
        >>> borders = Borders()
        >>> borders.get_simt()
        [TrObject('DBOP')]
        >>> borders.get_all()
        [TrObject('Вход в офис'), TrObject('DBOP')]
    """

    def __init__(self, server_guid=None):
        super(Borders, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_head(self, names=None):
        """Возвращает список HeadBorders

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "HeadBorder",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_people(self, names=None):
        """Возвращает список PeopleBorders

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "PeopleBorder",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_simt(self, names=None):
        """Возвращает список SIMT Borders

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "SIMT Border",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

    def get_deep_people(self, names=None):
        """Возвращает список DeepPeopleBorders

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        people_zones = self._get_objects_from_list(
            "PeopleZone",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )

        return [zone for zone in people_zones if self._zone_type(zone.obj) == "Border"]

    def get_all(self, names=None):
        """Возвращает список всех линий пересечения

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """
        all_borders = (
                self.get_head()
                + self.get_people()
                + self.get_simt()
                + self.get_deep_people()
        )

        if names is None:
            return all_borders
        return self._filter_objects_by_name(all_borders, names)


class Sigur(ObjectFromList):  # pylint: disable=R0903
    """Класс для работы со СКУД Sigur

    Args:
        server_guid (:obj:`str` | List[:obj:`str`], optional): Guid сервера или список guid.
            По умолчанию :obj:`None`, что соотвествует всем доступным серверам.
    """

    def __init__(self, server_guid=None):
        super(Sigur, self).__init__()
        if server_guid is None:
            server_guid = [srv.guid for srv in Servers().get_all()]

        self.server_guid = server_guid

    def get_access_points(self, names=None):
        """Возвращает список точек доступа

        Args:
            names (:obj:`str` | :obj:`list`, optional): :obj:`str` - имена,
                разделенные запятыми или :obj:`list` - список имен.
                По умолчанию :obj:`None`

        Returns:
            List[:class:`TrObject`]: Список объектов
        """

        return self._get_objects_from_list(
            "Access Point",
            object_names=names,
            server_guid=self.server_guid,
            sub_condition=None,
        )


class TrassirError(ScriptError):
    """Exception if bad trassir version"""

    pass


class PokaYoke(py_object):
    """Класс для защиты от дурака

    Позволяет блокировать запуск скрипта на ПО, где это
    не предусмотрено (например, на клиенте или TOS).
    А также производить некоторые другие проверки.
    """

    _EMAIL_REGEXP = re.compile(
        r"[^@]+@[^@]+\.[^@]+"
    )  # Default regex to check emails list
    _PHONE_REGEXP = re.compile(r"[^\d,;]")  # Default regex to check phone list

    def __init__(self):
        pass

    @staticmethod
    def ban_tos():
        """Блокирует запуск скрипта на `Trassir OS`

        Raises:
            OSError: Если скрипт запускается на `Trassir OS`

        Examples:
            >>> PokaYoke.ban_tos()
            OSError: Скрипт недоступен для TrassirOS
        """
        if os.name != "nt":
            raise OSError("Скрипт недоступен для TrassirOS")

    @staticmethod
    def ban_win():
        """Блокирует запуск скрипта на `Windows OS`

        Raises:
            OSError: Если скрипт запускается на `Windows OS`

        Examples:
            >>> PokaYoke.ban_win()
            OSError: Скрипт недоступен для WindowsOS
        """
        if os.name == "nt":
            raise OSError("Скрипт недоступен для WindowsOS")

    @staticmethod
    def ban_client():
        """Блокирует запуск скрипта на `Trassir Client`

        Raises:
            TrassirError: Если скрипт запускается на `Trassir Client`

        Examples:
            >>> PokaYoke.ban_client()
            TrassirError: Скрипт недоступен для клиентской версии Trassir
        """
        if BaseUtils.get_server_guid() == "client":
            raise TrassirError("Скрипт недоступен для клиентской версии Trassir")

    @classmethod
    def ban_daemon(cls):
        """Блокирует запуск скрипта на сервре Trassir, который запущен как служба

        Raises:
            TrassirError: Если скрипт запускается на сервре Trassir,
                который запущен как служба

        Examples:
            >>> PokaYoke.ban_daemon()
            TrassirError: Скрипт недоступен для Trassir запущенным как служба
        """
        if host.settings("system_wide_options")["daemon"]:
            raise TrassirError("Скрипт недоступен для Trassir запущенным как служба")

    @staticmethod
    def check_email_account(account_name):
        """Проверяет существование E-Mail аккаунта

        Args:
            account_name (:obj:`str`): Имя E-Mail аккаунта

        Returns:
             List[:class:`TrObject`]: Список объектов

        Raises:
            ParameterError: Если аккаунт не выбран
            ObjectsNotFoundError: Если аккаунт не найден

        Examples:
            >>> PokaYoke.check_email_account("")
            ParameterError: 'EmailAccount' не выбраны
            >>> PokaYoke.check_email_account("YourAccount")
            ObjectsNotFoundError: Не найдены объекты EmailAccount: YourAccount
            >>> PokaYoke.check_email_account("MyAccount")
            [TrObject('MyAccount')]
        """
        e_accounts = EmailAccounts(BaseUtils.get_server_guid())
        return e_accounts.get_all(account_name)

    @classmethod
    def parse_emails(cls, mailing_list, regex=None):
        """Парсит email дреса из строки и проверяет с помощью regex.

        Args:
            mailing_list (:obj:`str`): Список email адресов, разделенный запятыми
            regex (:obj:`SRE_Pattern`, optional): Новый regex шаблон для проверки.
                По умолчанию :obj:`None`

        Returns:
            List[:obj:`str`]: Список адресов

        Raises:
            ParameterError: Если найден невалидный email

        Examples:
            >>> PokaYoke.parse_emails("a.trubilil!dssl.ru,support@dssl.ru")
            ParameterError: Email 'a.trubilil!dssl.ru' is not valid!
            >>>
            >>> PokaYoke.parse_emails("a.trubilil@dssl.ru,support@dssl.ru")
            ['a.trubilil@dssl.ru', 'support@dssl.ru']
        """
        mailing_list = mailing_list.replace(" ", "")

        if not mailing_list:
            raise ParameterError("No emails to send!")

        if regex is None:
            regex = cls._EMAIL_REGEXP
        else:
            if not isinstance(regex, cls._EMAIL_REGEXP.__class__):
                raise TypeError(
                    "Expected re.compile, got '{}'".format(type(regex).__name__)
                )

        if isinstance(mailing_list, str):
            mailing_list = mailing_list.split(",")

        mailing_list = [mail.strip() for mail in mailing_list]

        for mail in mailing_list:
            if not regex.match(mail):
                raise ParameterError("Email '{}' is not valid!".format(mail))

        return mailing_list

    @classmethod
    def check_phones(cls, phones, regex=None):
        """Проверяет строку на валидность телефонных номеров с помощью regex.

        Args:
            phones (:obj:`str`): Список телефонов, разделенный запятыми или точкой с запятой
            regex (:obj:`SRE_Pattern`, optional): Новый regex шаблон для проверки.
                По умолчанию :obj:`None`

        Returns:
            :obj:`str`: Список номеров телефона

        Raises:
            ParameterError: Если найден невалидный номер телефона

        Examples:
            >>> PokaYoke.check_phones("79999999999,78888888888A")
            ParameterError: Bad chars in phone list: `A`
            >>>
            >>> PokaYoke.check_phones("a.trubilil@dssl.ru,support@dssl.ru")
            '79999999999,78888888888'
        """
        phones = phones.replace(" ", "")

        if not phones:
            raise ParameterError("No phones!")

        if regex is None:
            regex = cls._PHONE_REGEXP
        else:
            if not isinstance(regex, cls._PHONE_REGEXP.__class__):
                raise TypeError(
                    "Expected re.compile, got '{}'".format(type(regex).__name__)
                )
        bad_chars = regex.findall(phones)
        if bad_chars:
            raise ParameterError(
                "Bad chars in phone list: `{}`".format(", ".join(bad_chars))
            )

        return phones

    @classmethod
    def fire_recognizer_events(cls, enable=True, server_guid=None):
        """Проверяет "Режим для СКУД" настроек распознавания лиц.

        По умолчанию проверяет активирован ли "Режим для СКУД"
        на сервере, где запущен скрипт. По желанию можно указать
        удаленный сервер дял проверки.

        Args:
            enable (:obj:`bool`, optional): Состояние параметра. По умолчанию :obj:`True`.
            server_guid (:obj:`str`, optional): Guid сервера. По умолчанию :obj:`None`.

        Raises:
            RuntimeError: Если указанный сервер недоступен.
            EnvironmentError: Если моудль распознавания или режим для СКУД не доступны.
            TrassirError: Если текущее состояние не соотвествует необходимомому.

        Examples:
            >>> PokaYoke.fire_recognizer_events()
            TrassirError: Пожалуйста, активируйте 'Режим для СКУД' в настройках распознавания лиц
        """
        if server_guid is None:
            server_guid = BaseUtils.get_server_guid()

        try:
            srv_sett = host.settings("/%s" % server_guid)
        except KeyError:
            raise RuntimeError("Сервер '%s' не доступен" % server_guid)

        fr_sett = srv_sett.cd("face_recognizer")

        if fr_sett is None:
            raise EnvironmentError(
                "Модуль распознавания лиц не доступен на '%s'"
                % (srv_sett.name or srv_sett.guid)
            )

        try:
            if fr_sett["fire_recognizer_events"] != enable:
                raise TrassirError(
                    "Пожалуйста, {} 'Режим для СКУД' в настройках распознавания лиц".format(
                        "активируйте" if enable else "отключите"
                    )
                )
        except KeyError:
            raise EnvironmentError(
                "'Режим для СКУД' не доступен. Пожалуйста, обновите сервер trassir."
            )


class SoundPlayer(py_object):  # pylint: disable=R0903
    """Класс для проигрывания выбранной мелодии.

    Можно указать один из стандартных зуков или
    указать полный путь до своего файла.

    Note:
        Список стандартных файлов

        .. raw:: html

            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/SNES-startup.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"SNES-startup.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/alarm.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"alarm.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/bell.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"bell.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/boxing-bell-1.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"boxing-bell-1.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/boxing-bell-3.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"boxing-bell-3.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/cardlock-open.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"cardlock-open.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/chime.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"chime.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/chip001.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"chip001.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/chip019.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"chip019.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/chip069.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"chip069.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/cordless-phone-ring.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"cordless-phone-ring.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/countdown.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"countdown.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/dialtone.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"dialtone.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/ding.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"ding.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/horn-beep.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"horn-beep.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/phone-beep.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"phone-beep.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/police2.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"police2.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/ship-on-fog.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"ship-on-fog.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/ships-bell.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"ships-bell.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/spin-up.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"spin-up.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/tada1.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"tada1.wav"</span>
            </code>
            <br>
            <audio controls="controls" style="height: 20px; margin-bottom: -5px;">
              <source src="https://github.com/aatrubilin/trassir_script_framework/raw/master/docs/source/sounds/tape-slow9.wav" type="audio/wav">
              Your browser does not support the <code>audio</code> element.
            </audio>
            <code class="xref py py-obj docutils literal notranslate">
                <span class="pre">"tape-slow9.wav"</span>
            </code>
            <br>

    Args:
        sound_file (:obj:`str`): Имя файла с расширением
    """

    _DEFAULT_SOUNDS = {
        "SNES-startup.wav",
        "alarm.wav",
        "bell.wav",
        "boxing-bell-1.wav",
        "boxing-bell-3.wav",
        "cardlock-open.wav",
        "chime.wav",
        "chip001.wav",
        "chip019.wav",
        "chip069.wav",
        "cordless-phone-ring.wav",
        "countdown.wav",
        "dialtone.wav",
        "ding.wav",
        "horn-beep.wav",
        "phone-beep.wav",
        "police2.wav",
        "ship-on-fog.wav",
        "ships-bell.wav",
        "spin-up.wav",
        "tada1.wav",
        "tape-slow9.wav",
    }

    def __init__(self, sound_file):
        self._play = self._get_player(sound_file)

    def _check_file(self, sound_file):
        _, ext = os.path.splitext(sound_file)

        if ext.lower() != ".wav":
            raise RuntimeError("Expected *.wav file, got {!r}".format(ext))

        if sound_file in self._DEFAULT_SOUNDS:
            if os.name == "nt":
                base_path = "sounds"
            else:
                base_path = "/opt/trassir/tech1/sounds"

            sound_file = os.path.join(base_path, sound_file)

        if not os.path.isfile(sound_file):
            raise IOError("File {} not found".format(sound_file))

        return sound_file

    def _get_player(self, sound_file):
        sound_file = self._check_file(sound_file)

        if os.name == "nt":

            def player():
                winsound.PlaySound(
                    sound_file,
                    winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NOWAIT,
                )

        else:

            def player():
                os.system('aplay -D "sysdefault:CARD=PCH" %s &' % sound_file)

        return player

    def play(self):
        """Проигрывает выбранный файл

        Examples:
            >>> player = SoundPlayer("alarm.wav")
            >>> player.play()
        """
        self._play()


class SenderError(Exception):
    """Base Sender Exception"""

    pass


class Sender(py_object):
    _HTML_IMG_TEMPLATE = """<img src="data:image/png;base64,{img}" {attr}>"""

    def __init__(self):
        pass

    @staticmethod
    def _get_base64(image_path):
        """Returns base64 image

        Args:
            image_path (str): Image full path
        """
        base64_image = ""
        image_path = BaseUtils.win_encode_path(image_path)
        if os.path.isfile(image_path):
            with open(image_path, "rb") as image_file:
                base64_image = base64.b64encode(image_file.read())

        return base64_image

    @staticmethod
    def _get_html_img(image_base64, **kwargs):
        """Returns html img

        Args:
            image_base64 (str): Base64 image
        """
        return BaseUtils.base64_to_html_img(image_base64, **kwargs)

    def text(self, text, **kwargs):
        """Send text

        Args:
            text (str): Text message
        """
        pass

    def image(self, image_path, text="", **kwargs):
        """Send image and optional text

        Args:
            image_path (str | List[str]): Image path or paths
            text (str, optional): Text message; default: ""
        """
        pass

    def files(self, file_paths, text="", **kwargs):
        """Send file or list of files

        Args:
            file_paths (str | List[str]): File path or list of paths
            text (str, optional): Text message; default: ""
        """
        pass


class PopupSender(Sender):
    """Класс для показа всплывающих окон в правом нижнем углу экрана

    Args:
        width (:obj:`int`, optional): Ширина изображения, px.
            По умолчанию :obj:`width=400`

    Examples:
        >>> sender = PopupSender(300)
        >>> sender.text("Hello World!")

            .. image:: images/popup_sender.text.png

        >>> sender.image(r"manual/en/cloud-devices-16.png")

            .. image:: images/popup_sender.image.png
    """

    def __init__(self, width=400):
        super(PopupSender, self).__init__()
        self._attr = {"width": width}

    def text(self, text, popup_type="message", **kwargs):  # pylint: disable=W0221
        """Показывает текст во всплывающем окне

        Вызывает один из методов Trassir :obj:`host_ip.alert`,
        :obj:`host_ip.message` или :obj:`host_ip.error` с текстом

        Args:
            text (:obj:`str`): Текст сообщения
            popup_type (:obj:`"message"` | :obj:`"alert"` | :obj:`"error"`, optional)
                Тип сообщения. По умолчанию :obj:`"message"`
        """

        if popup_type == "alert":
            host.alert(text)
        elif popup_type == "error":
            host.error(text)
        else:
            host.message(text)

    def image(
            self, image_path, text="", popup_type=None, **kwargs
    ):  # pylint: disable=W0221
        """Показывает изображение во всплывающем окне

        Args:
            image_path (:obj:`str` | :obj:`List[str]`): Полный путь до изображения
                или список путей.
            text (:obj:`str`, optional): Текст сообщения. По умолчанию :obj:`""`
            popup_type (:obj:`"message"` | :obj:`"alert"` | :obj:`"error"`, optional)
                Тип сообщения. По умолчанию :obj:`"message"`
        """
        if not isinstance(image_path, list):
            image_path = [image_path]

        images_base64 = [self._get_base64(img_path) for img_path in image_path]

        for image_base64, img_path in zip(images_base64, image_path):
            if not image_base64:
                self.text("<b>File not found</b><br>{}".format(img_path), popup_type)
                return

            html_image = BaseUtils.base64_to_html_img(image_base64, **self._attr)

            html = "{image}"
            if text:
                html = "<b>{text}</b><br>{image}"

            self.text(html.format(text=text, image=html_image), popup_type)


class PopupWithBtnSender(Sender):
    """Класс для показа всплывающих окон с кнопкой `Оk`

    Note:
        | Для закрытия окна необходимо нажать кнопку `Ok` в течении 60 сек.
        | После 60 сек окно закрывается автоматически.

    Args:
        width (:obj:`int`, optional): Ширина изображения, px.
            По умолчанию :obj:`width=800`

    Examples:
        >>> sender = PopupWithBtnSender()
        >>> sender.text("Hello World!")

            .. image:: images/popup_with_btn_sender.text.png

        >>> sender.image(r"manual/en/cloud-devices-16.png")

            .. image:: images/popup_with_btn_sender.image.png
    """

    def __init__(self, width=800):
        super(PopupWithBtnSender, self).__init__()
        self._attr = {"width": width}

    def text(self, text, **kwargs):
        """Показывает текст во всплывающем окне

        Вызывает метод Trassir :obj:`host_ip.question` с текстом

        Args:
            text (:obj:`str`): Текст сообщения
        """
        host.question("<pre>{}</pre>".format(text), "Ok", BaseUtils.do_nothing)

    def image(self, image_path, text="", **kwargs):
        """Показывает изображение во всплывающем окне

        Args:
            image_path (:obj:`str` | :obj:`List[str]`): Полный путь до изображения
                или список путей.
            text (:obj:`str`, optional): Текст сообщения. По умолчанию :obj:`""`
        """
        if not isinstance(image_path, list):
            image_path = [image_path]

        images_base64 = [self._get_base64(img_path) for img_path in image_path]

        for image_base64, img_path in zip(images_base64, image_path):
            if not image_base64:
                self.text("<b>File not found</b><br>{}".format(image_path))
                return

            html_image = BaseUtils.base64_to_html_img(image_base64, **self._attr)

            html = "{image}"
            if text:
                html = "<b>{text}</b><br>{image}"

            self.text(html.format(text=text, image=html_image))


class EmailSender(Sender):
    """Класс для отправки уведомлений, изображений и файлов на почту

    Note:
        По умолчанию тема сообщений соответствует шаблону
        ``{server_name} -> {script_name}``

    Tip:
        При отправке изображения с текстом предпочтительней использовать метод
        :meth:`EmailSender.image` с необязательным аргументом :obj:`text` чем
        :meth:`EmailSender.text` с необазательным аргументом :obj:`attachments`

    Args:
        account (:obj:`str`): E-Mail аккаунт trassir. Проверяется
            методом :meth:`PokaYoke.check_email_account`
        mailing_list (:obj:`str`): Список email адресов для отправки писем
            разделенный запятыми. Проверяется и парсится в список методом
            :meth:`PokaYoke.parse_emails`
        subject (:obj:`str`, optional): Общая тема для сообщений.
            По умолчанию :obj:`None`
        max_size (:obj:`int`, optional): Максимальный размер вложения, байт.
            По умолчанию 25 * 1024 * 1024

    Examples:
        >>> sender = EmailSender("MyAccount", "my_mail@google.com")
        >>> sender.text("Hello World!")

            .. image:: images/email_sender.text.png

        >>> sender.image(r"manual/en/cloud-devices-16.png")

            .. image:: images/email_sender.image.png

        >>> sender.files([r"manual/en/cloud.html", r"manual/en/cloud.png"])

            .. image:: images/email_sender.files.png
    """

    def __init__(self, account, mailing_list, subject=None, max_size=None):
        super(EmailSender, self).__init__()

        PokaYoke.check_email_account(account)

        self.max_size = max_size or 25 * 1024 * 1024

        self._account = account
        self._mailing_list = PokaYoke.parse_emails(mailing_list)

        self._subject_default = subject or self._generate_subject()

        logger.info(
            "EmailSender(%s, %s, subject=%s, max_size=%s)",
            repr(account),
            repr(mailing_list),
            repr(self._subject_default),
            repr(self.max_size),
        )

    @staticmethod
    def _generate_subject():
        """Returns `server name` -> `script name`"""
        subject = "{server_name} -> {script_name}".format(
            server_name=host.settings("").name or "Client",
            script_name=host.stats().parent().name,
        )
        return subject

    def _group_files_by_max_size(self, file_paths, max_size):
        """Split files to groups. Size of each group is less then max_size

        Args:
            file_paths (list): List of files
            max_size (int): Max group size, bytes
        """
        group = []
        cur_size = 0
        for idx, file_path in enumerate(file_paths):
            file_size = os.stat(BaseUtils.win_encode_path(file_path)).st_size
            if not cur_size or (cur_size + file_size) < max_size:
                cur_size += file_size
                group.append(file_path)
            else:
                break
        else:
            return [group]

        return [group] + self._group_files_by_max_size(
            file_paths[idx:], max_size  # pylint: disable=W0631
        )

    def text(
            self, text, subject=None, attachments=None, **kwargs
    ):  # pylint: disable=W0221
        """Отправка текстового сообщения

        Args:
            text (:obj:`str`): Текст сообщения
            subject (:obj:`str`, optional): Новая тема сообщения.
                По умолчанию :obj:`None`
            attachments (:obj:`list`, optional): Список вложений.
                По умолчанию :obj:`None`
        """
        if attachments is None:
            attachments = []
        host.send_mail_from_account(
            self._account,
            self._mailing_list,
            subject or self._subject_default,
            text,
            attachments,
        )

    def image(
            self, image_path, text="", subject=None, **kwargs
    ):  # pylint: disable=W0221
        """Отправка изображения

        Args:
            image_path (:obj:`str` | :obj:`List[str]`): Полный путь до изображения
                или список путей.
            text (:obj:`str`, optional): Текст сообщения.
                По умолчанию :obj:`""`
            subject (:obj:`str`, optional): Новая тема сообщения.
                По умолчанию :obj:`None`
        """
        if not isinstance(image_path, list):
            image_path = [image_path]
        self.files(image_path, text=text, subject=subject)

    def files(
            self, file_paths, text="", subject=None, callback=None, **kwargs
    ):  # pylint: disable=W0221
        """Отправка файлов

        Note:
            Если отправляется несколько файлов они могут быть разделены на
            несколько сообщений, основываясь на максимальном размере вложений.

        Args:
            file_paths (:obj:`str` | :obj:`list`): Путь до файла или список
                файлов для отправки
            text (:obj:`str`, optional): Текст сообщения.
                По умолчанию :obj:`""`
            subject (:obj:`str`, optional): Новая тема сообщения.
                По умолчанию :obj:`None`
            callback (:obj:`function`, optional): Функция, которая вызывается после
                отправки частей
        """
        logger.debug("EmailSender.files(%s, text=%s)", repr(file_paths), repr(text))
        if isinstance(file_paths, str):
            file_paths = [file_paths]

        if callback is None:
            callback = BaseUtils.do_nothing

        files_to_send = []
        for path in file_paths:
            if BaseUtils.is_file_exists(path):
                files_to_send.append(path)
            else:
                text += "\nFile not found: {}".format(path)

        file_groups = self._group_files_by_max_size(files_to_send, self.max_size)

        for grouped_files in file_groups:
            logger.debug("EmailSender.files: grouped_files: %s", repr(grouped_files))
            self.text(text, subject=subject, attachments=grouped_files)
            callback(grouped_files)


class TelegramSender(Sender):
    """Работа с телеграм ботом `@trassirbot <https://t.me/trassirbot>`_

    Warnings:
        | Cкрипт должен быть запущен на **сервере** Trassir.
        | На Клиенте скрипт вызовет ошибку ``ServerKeyError``

    Args:
        telegram_ids (:obj:`str`): Id пользователей, через запятую.

    Examples:
        >>> # Можно указать id для рассылки при инициализации
        >>> # класса, для всех уведомлений
        >>> sender = TelegramSender("123456789")
        >>> sender.text("Hello World!")

            .. image:: images/telegram_sender.text.png

        >>> sender.image(r"manual/en/cloud-devices-16.png")

            .. image:: images/telegram_sender.image.png

        >>> sender.files([r"manual/en/cloud.html", r"manual/en/cloud.png"])

            .. image:: images/telegram_sender.files.png

        >>> # Или можно опередовать telegram id при вызове методов
        >>> sender = TelegramSender()
        >>> sender.text("Hello World!", tg_users=[123456789])

            .. image:: images/telegram_sender.text.png

        >>> sender.image(r"manual/en/cloud-devices-16.png", tg_users=[123456789])

            .. image:: images/telegram_sender.image.png

        >>> sender.files([r"manual/en/cloud.html", r"manual/en/cloud.png"], tg_users=[123456789])

            .. image:: images/telegram_sender.files.png
    """

    def __init__(self, telegram_ids=None):
        super(TelegramSender, self).__init__()
        host.exec_encoded(_TBOT_SERVICE)
        self._tbot_api = TBotAPI()  # pylint: disable=E0602
        if telegram_ids is not None:
            self.telegram_ids = TBotAPI.prepare_users(  # pylint: disable=E0602
                telegram_ids
            )
        else:
            self.telegram_ids = None

    def text(self, text, tg_users=None, **kwargs):  # pylint: disable=W0221
        """Отправка текстового сообщения

        Args:
            text (:obj:`str`): Текст сообщения.
            tg_users (List[:obj:`int`], optional): Список id пользователей
                telegram для отправки отдельных сообщений. По умолчанию :obj:`None`
        """
        if tg_users is None:
            tg_users = self.telegram_ids

        self._tbot_api.send_message(tg_users, text)

    def image(
            self, image_path, text="", tg_users=None, remove=False, **kwargs
    ):  # pylint: disable=W0221
        """Отправка изображения

        Args:
            image_path (:obj:`str` | List[:obj:`str`]): Полный путь до изображения или
                список путей
            text (:obj:`str`, optional): Текст сообщения.
                По умолчанию :obj:`""`
            tg_users (List[:obj:`int`], optional): Список id пользователей
                telegram для отправки отдельных сообщений. По умолчанию :obj:`None`
            remove (bool, optional): Удалить файл после отправки или нет. По умолчанию :obj:`False`
        """
        if tg_users is None:
            tg_users = self.telegram_ids

        if len(text) > 150:
            self.text(text, tg_users=tg_users)
            text = None

        if isinstance(image_path, list):
            self._tbot_api.send_image_album(
                tg_users, image_path, captions=[text] or None, remove=remove
            )

        else:
            if not os.path.isfile(image_path):
                self.text("Image not found: {}".format(image_path))
                return

            self._tbot_api.send_image(tg_users, image_path, caption=text, remove=remove)

    def files(
            self, file_paths, text="", tg_users=None, remove=False, **kwargs
    ):  # pylint: disable=W0221
        """Отправка файлов

        Args:
            file_paths (:obj:`str` | :obj:`list`): Путь до файла или список
                файлов для отправки
            text (:obj:`str`, optional): Текст сообщения.
                По умолчанию :obj:`""`
            tg_users (List[:obj:`int`], optional): Список id пользователей
                telegram для отправки отдельных сообщений. По умолчанию :obj:`None`
            remove (bool, optional): Удалить файл после отправки или нет. По умолчанию :obj:`False`
        """

        if tg_users is None:
            tg_users = self.telegram_ids

        if isinstance(file_paths, str):
            file_paths = [file_paths]

        if text and len(file_paths) == 1:
            self.text(text, tg_users=tg_users)
            text = ""

        files_not_found_text = ""
        for path in file_paths:
            if os.path.isfile(BaseUtils.win_encode_path(path)):
                self._tbot_api.send_document(
                    tg_users, path, caption=text, remove=remove
                )
            else:
                files_not_found_text += "\nFile not found: {}".format(path)

        if files_not_found_text:
            self.text(files_not_found_text, tg_users=tg_users)


class SMSCSenderError(SenderError):
    """Raises with SMSCSender errors"""

    pass


class SMSCSender(Sender):
    """Класс для отправки сообщений с помощью сервиса smsc.ru

    See Also:
        `https://smsc.ru/api/http/ <https://smsc.ru/api/http/>`_

    Note:
        | Номера проверяются методом
          :meth:`PokaYoke.check_phones`
        | Также при первом запуске скрипт проверяет данные авторизации

    Warnings:
        | По умолчанию сервис smsc.ru отправляет сообщения от своего имени *SMSC.RU.*
          При этом отправка на номера Мегафон/Йота **недоступна** т.к. имя *SMSC.RU*
          заблокировано оператором.
        |
        | Мы настоятельно **НЕ** рекомендуем использовать стандартное имя *SMSC.RU.*
        |
        | Для отправки смс от вашего буквенного имени необходимо его
          создать в разделе - https://smsc.ru/senders/ и зарегистрировать для
          операторов в колонке Действия по кнопке Изменить (после заключения договора
          согласно инструкции - https://smsc.ru/contract/info/ ) а также приложить
          гарантийное письмо на МТС в личный кабинет http://smsc.ru/documents/ и
          отправить на почту inna@smsc.ru

    Args:
        login (:obj:`str`): SMSC Логин
        password (:obj:`str`): SMSC Пароль
        phones (:obj:`str`): Список номеров для отправки смс резделенный
            запятыми или точкой с запятой
        translit(:obj:`bool`, optional): Переводить сообщение в
            транслит. По умолчанию :obj:`True`

    Raises:
        SMSCSenderError: При любых ошибках с отправкой сообщения

    Examples:
        >>> sender = SMSCSender("login", "password", "79999999999")
        >>> sender.text("Hello World!")

            .. image:: images/smsc_sender.text.png
    """

    _BASE_URL = "https://smsc.ru/sys/send.php?{params}"
    _ERROR_CODES = {
        1: "URL Params error",
        2: "Invalid login or password",
        3: "Not enough money",
        4: "Your IP is temporary blocked. More info: https://smsc.ru/faq/99",
        5: "Bad date format",
        6: "Message is denied (by text or sender name)",
        7: "Bad phone format",
        8: "Can't send message to this number",
        9: "Too many requests",
    }

    def __init__(self, login, password, phones, translit=True):
        super(SMSCSender, self).__init__()
        if not login:
            raise SMSCSenderError("Empty login")
        if not password:
            raise SMSCSenderError("Empty password")

        self._params = {
            "login": urllib.quote(login),  # Login
            "psw": urllib.quote(password),  # Password or MD5 hash
            "phones": urllib.quote(
                PokaYoke.check_phones(phones)
            ),  # Comma or semicolon spaced phone list
            "fmt": 3,  # Response format: 0 - string; 1 - integers; 2 - xml; 3 - json
            "translit": 1 if translit else 0,  # If 1 - transliting message
            "charset": "utf-8",  # Message charset: "windows-1251"|"utf-8"|"koi8-r"
            "cost": 3,  # Message cost in response: 0 - msg; 1 - cost; 2 - msg+cost, 3 - msg+cost+balance
        }

        self._check_account()

    def _get_link(self, **kwargs):
        """Returns get link"""
        params = self._params.copy()
        params.update(kwargs)
        url = self._BASE_URL.format(params=urllib.urlencode(params))

        return url

    def _request_callback(self, code, result, error):
        """Callback for async_get"""
        if code != 200:
            raise SMSCSenderError("RequestError [{}]: {}".format(code, error))
        else:
            try:
                data = json.loads(result)
            except ValueError:
                data = {"error_code": 0, "error": "JSON loads error: {}".format(result)}

            error_code = data.get("error_code")
            if error_code is not None:
                error = self._ERROR_CODES.get(error_code)
                if not error:
                    error = data.get("error", "Unknown error")
                raise SMSCSenderError(
                    "ResponseError [{}]: {}".format(error_code, error)
                )

    def _check_account(self):
        """Send test request to smsc server"""
        url = self._get_link(cost=1, mes=urllib.quote("Hello world!"))
        host.async_get(url, self._request_callback)

    def text(self, text, **kwargs):
        """Отправка текстового сообщения

        Args:
            text (:obj:`str`): Текст сообщения.
        """

        url = self._get_link(mes=text)

        host.async_get(url, self._request_callback)


class FtpUploadTracker:  # pylint: disable=R0903,C1001
    """Upload progress class"""

    size_written = 0.0
    last_shown_percent = 0

    def __init__(self, file_path, callback):
        self.total_size = os.path.getsize(BaseUtils.win_encode_path(file_path))
        self.file_path = file_path
        self.callback = callback

    # noinspection PyUnusedLocal
    def handle(self, *args):  # pylint: disable=W0613,C1001
        """Handler for storbinary

        See Also:
            https://docs.python.org/2/library/ftplib.html#ftplib.FTP.storbinary
        """
        self.size_written += 1024.0
        percent_complete = round((self.size_written / self.total_size) * 100)

        if self.last_shown_percent != percent_complete:
            self.last_shown_percent = percent_complete
            host.timeout(
                100, lambda: self.callback(self.file_path, int(percent_complete), "")
            )


class FTPSenderError(SenderError):
    """Raises with FTPSender errors"""

    pass


class FTPSender(Sender):  # pylint: disable=R0902
    """Класс для отправки файлов на ftp сервер

    При инициализации проверят подключение к ftp серверу. Файлы отправляет
    по очереди. Максимальный размер очереди можно изменить. Во время
    выполнения передает текущий прогресс отправки файла в callback функцию.

    Note:
        Помимо прогресса в функцию callback может вернуться код ошибки.
            - -1 Файл не существует.
            - -2 Ошибка отправки на ftp, файл будет повторно отправлен.
            - -3 Неизвестная ошибка.


    Args:
        host_ip (:obj:`str`): Адрес ftp сервера.
        port (:obj:`int`, optional): Порт ftp сервера. По умолчанию :obj:`port=21`
        user (:obj:`str`, optional): Имя пользователя. По умолчанию :obj:`"anonymous"`
        passwd (:obj:`str`, optional): Пароль пользователя. По умолчанию :obj:`passwd=""`
        work_dir (:obj:`str`, optional): Директория на сервре для сохранения файлов.
            По умолчанию :obj:`None`
        callback (:obj:`function`, optional): Callable function. По умолчанию :obj:`None`
        queue_maxlen (:obj:`int`, optional): Максимальная длина очереди на отправку.
            По умолчанию :obj:`queue_maxlen=1000`

    Examples:
        >>> # noinspection PyUnresolvedReferences
        >>> def callback(file_path, progress, error):
        ...     # Пример callback функции, которая отображает
        ...     # текущий прогресс в счетчике запуска скрипта
        ...     # Args:
        ...     #   file_path (str): Путь до файла
        ...     #   progress (int): Текущий прогресс передачи файла, %
        ...     #   error (str | Exception): Ошибка при отправке файла, если есть
        ...     host.stats()["run_count"] = progress
        ...     if error:
        ...         host.error(error)
        ...
        ...     if progress == 100:
        ...         host.timeout(3000, lambda: os.remove(BaseUtils.win_encode_path(file_path)))
        >>>
        >>> sender = FTPSender("172.20.0.10", 21, "trassir", "12345", work_dir="/test_dir/", callback=callback)
        >>> sender.files(r"D:/Shots/export_video.avi")
    """

    # noinspection SpellCheckingInspection,PyShadowingNames
    def __init__(  # pylint: disable=R0913
            self,
            host_ip,
            port=21,
            user="anonymous",
            passwd="",
            work_dir=None,
            callback=None,
            queue_maxlen=1000,
    ):
        super(FTPSender, self).__init__()
        self._host = host_ip
        self._port = port
        self._user = user
        self._passwd = passwd
        self._work_dir = work_dir

        self.queue = deque(maxlen=queue_maxlen)

        self._ftp = None

        if callback is None:
            callback = BaseUtils.do_nothing

        self.callback = callback

        self._work_now = False

        self._check_connection()

    def _check_connection(self):
        """Check if it possible to connect"""
        try:
            ftp = ftplib.FTP()
            ftp.connect(self._host, self._port, timeout=10)
            ftp.login(self._user, self._passwd)
        except ftplib.all_errors as err:
            raise FTPSenderError(err)
        if self._work_dir:
            try:
                ftp.cwd(self._work_dir)
            except ftplib.error_perm:
                ftp.mkd(self._work_dir)
                ftp.cwd(self._work_dir)

        ftp.quit()

    def _get_connection(self):
        """Connecting to ftp

        Returns:
            ftplib.FTP: Ftp object
        """
        try:
            ftp = ftplib.FTP()
            ftp.connect(self._host, self._port, timeout=10)
            ftp.login(self._user, self._passwd)
            if self._work_dir:
                try:
                    ftp.cwd(self._work_dir)
                except ftplib.error_perm:
                    ftp.mkd(self._work_dir)
                    ftp.cwd(self._work_dir)
            ftp.encoding = "utf-8"
            return ftp
        except ftplib.all_errors:
            pass

    def _close_connection(self):
        """Close ftp connection"""
        try:
            if self._ftp is not None:
                self._ftp.close()
        finally:
            self._ftp = None

    def _send_file(self, file_path, work_dir=None):
        """Storbinary file with self.ftp

        Args:
            file_path (str): Full file path
            work_dir (str): Work dir on ftp
        """
        if work_dir is not None:
            if self._work_dir:
                work_dir = os.path.normpath("{}/{}".format(self._work_dir, work_dir))
            try:
                self._ftp.cwd(work_dir)
            except ftplib.error_perm:
                self._ftp.mkd(work_dir)
                self._ftp.cwd(work_dir)

        file_name = os.path.basename(file_path)
        upload_tracker = FtpUploadTracker(file_path, self.callback)
        with open(BaseUtils.win_encode_path(file_path), "rb") as opened_file:
            self._ftp.storbinary(
                "STOR " + file_name, opened_file, 1024, upload_tracker.handle
            )

    @BaseUtils.run_as_thread
    def _sender(self):
        """Send files in queue"""
        if self.queue:
            if self._ftp is None:
                self._ftp = self._get_connection()

            if self._ftp:
                work_dir = None
                file_path = self.queue.popleft()

                if isinstance(file_path, tuple):
                    file_path, work_dir = file_path

                if BaseUtils.is_file_exists(BaseUtils.win_encode_path(file_path)):
                    try:
                        self._send_file(file_path, work_dir)

                    except ftplib.all_errors as err:
                        host.timeout(
                            100, lambda: self.callback(file_path, -2, error=err)
                        )
                        self.queue.append(file_path)
                        self._close_connection()

                    except Exception as err:  # pylint: disable=W0703
                        host.timeout(
                            100, lambda: self.callback(file_path, -3, error=err)
                        )

                else:
                    host.timeout(
                        100,
                        lambda: self.callback(file_path, -1, error="File not found"),
                    )

            host.timeout(500, self._sender)
        else:
            self._work_now = False
            self._close_connection()

    def files(self, file_paths, *args, **kwargs):  # pylint: disable=W0221,W0613,
        """Отправка файлов

        Note:
            Можно указать отдельный путь на ftp сервере для каждого файла.
            Для этого список файлов на отправку должен быть приведен к виду
            ``[(shot_path, ftp_path), ...]`` При этом так же будет учитываться
            глобальная папка :obj:`work_dir` заданная при инициализации класса.

        Args:
            file_paths (:obj:`str` | :obj:`list`): Путь до файла или список
                файлов для отправки
        """
        if not isinstance(file_paths, list):
            file_paths = [file_paths]

        self.queue.extend(file_paths)
        if not self._work_now:
            self._work_now = True
            self._sender()


###############################################################################
import abc

tr = host.tr

_UNKNOWN_ERROR = tr("Unknown error")


class Indicator(py_object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, title, min_duration, health=None):
        """Base abstract indicator class

        Args:
            title (str): Used for generate messages.
            min_duration (int): Min. seconds for alarm.
        """
        logger.debug("%s uploaded", self.__class__.__name__)
        self._min_duration = min_duration
        self._health = health or host.settings("health")

        self.title = title
        self.cur_error = None
        self.changed_dt = None
        self.last_message = ""

    @abc.abstractmethod
    def state_ok(self):
        """Method to check current indicator state.

        Returns:
            bool: True if indicator health is ok, False otherwise.
        """
        return True

    @abc.abstractproperty
    def error(self):
        """Property, that shows current error.

        Returns:
            str: Current indicator error.
        """
        return ""

    def check_state(self):
        """Universal method to check indicator health

        Returns:
            Tuple[datetime.datetime | None, bool, str]: Last changed datetime
                or None, current state and current error.
        """
        state_is_ok = self.state_ok()
        cur_error = None if state_is_ok else self.error

        changed = cur_error != self.cur_error
        if changed:
            # changed_dt=None means that no changes.
            # We set None if event has changed_dt too quickly.
            now = datetime.now()
            if (
                    self.changed_dt
                    and (now - self.changed_dt).total_seconds() < self._min_duration
            ):
                self.changed_dt = None
            else:
                self.changed_dt = datetime.now()

            logger.debug(
                "%s ok: %s, prev_error: %s, cur_error: %s",
                self.__class__.__name__,
                state_is_ok,
                self.cur_error,
                cur_error,
            )

        self.cur_error = cur_error
        return self.changed_dt, state_is_ok, cur_error


class CPUIndicator(Indicator):
    """Alarmed if cpu load goes over 90 percents"""

    _MAX_CPU_USAGE_PERCENT = 90

    def __init__(self, min_duration, health=None):
        super(CPUIndicator, self).__init__(tr("CPU"), min_duration, health=health)

    def state_ok(self):
        return self._health["cpu_usage"] <= self._MAX_CPU_USAGE_PERCENT

    @property
    def error(self):
        return "\n" + tr("CPU overloaded ({cpu_usage}%)").format(
            cpu_usage=self._health["cpu_usage"]
        )


class CloudIndicator(Indicator):
    """Alarmed if server has errors with Cloud"""

    def __init__(self, min_duration, health=None):
        super(CloudIndicator, self).__init__(tr("Cloud"), min_duration, health=health)

    def state_ok(self):
        return not bool(self._health["cloud_have_error"] > 0)

    @property
    def error(self):
        return "\n" + (self._health["cloud_last_error"] or _UNKNOWN_ERROR)


class HDDIndicator(Indicator):
    """Alarmed if server has errors with HDD"""

    def __init__(self, min_duration, health=None):
        super(HDDIndicator, self).__init__(tr("HDD"), min_duration, health=health)

    def state_ok(self):
        return not bool(self._health["disks_error_count"])

    @property
    def error(self):
        return "\n" + (self._health["disks_last_error"] or _UNKNOWN_ERROR)


class HDDCountIndicator(Indicator):
    def __init__(self, min_duration, health=None):
        super(HDDCountIndicator, self).__init__(tr("HDD count"), min_duration, health=health)
        self.archive = health.parent().cd("archive")
        self.working_disks = self.collect_disks()
        self.last_check = None

    def collect_disks(self):
        _disks = set()
        for sett in self.archive.ls():
            if sett.type == "ArchiveMountPoint" and sett["enable"]:
                _disks.add(sett["path_local8bit"])
        return _disks

    def state_ok(self):
        self.last_check = self.collect_disks()
        return len(self.last_check) == len(self.working_disks)

    @property
    def error(self):
        disks_difference = self.working_disks - self.last_check
        return "\n".join("disk %s not found" % disk for disk in disks_difference)


class SQLIndicator(Indicator):
    """Alarmed if server has errors with database"""

    def __init__(self, min_duration, health=None):
        super(SQLIndicator, self).__init__(tr("Database"), min_duration, health=health)

    def state_ok(self):
        return bool(self._health["db_connected"])

    @property
    def error(self):
        return "\n" + (self._health["db_last_error"] or _UNKNOWN_ERROR)


class DevicesIndicator(Indicator):
    """Alarmed if server has errors with IP Devices"""

    def __init__(self, min_duration, health=None):
        super(DevicesIndicator, self).__init__(
            tr("Devices"), min_duration, health=health
        )
        self._ip_cameras = health.parent().cd("ip_cameras")

    def state_ok(self):
        return self._health["ip_devices_connected"] == self._health["ip_devices_total"]

    @property
    def error(self):
        error_str = ""
        idx = 1
        for device in self._ip_cameras.ls():
            if device.type == "Grabber":
                feedback = device.cd("feedback")
                if feedback and feedback["any_error"]:
                    error_str += "\n{idx}. {dev_name}: {err}".format(
                        idx=idx,
                        dev_name=device.name,
                        err=feedback["last_error_message"] or _UNKNOWN_ERROR,
                    )
                    idx += 1
        return error_str or "\n%s" % _UNKNOWN_ERROR


class ChannelsIndicator(Indicator):
    """Alarmed if server has errors with Channels"""

    def __init__(self, min_duration, health=None):
        super(ChannelsIndicator, self).__init__(
            tr("Channels"), min_duration, health=health
        )
        self._channels = health.parent().cd("channels")

    def state_ok(self):
        network_channels_ok = (
                self._health["channels_network_online"]
                == self._health["channels_network_total"]
        )
        board_channels_ok = (
                self._health["channels_board_online"]
                == self._health["channels_board_total"]
        )
        return network_channels_ok and board_channels_ok

    @property
    def error(self):
        error_str = ""
        idx = 1
        for channel in self._channels.ls():
            if channel.type == "Channel":
                flags = channel.cd("flags")
                if flags and flags["signal"] != 1:
                    error_str += "\n{idx}. {chan_name}: {err}".format(
                        idx=idx, chan_name=channel.name, err="No signal"
                    )
                    idx += 1
        return error_str or "\n%s" % _UNKNOWN_ERROR


class NetworkIndicator(Indicator):
    """Alarmed if server has errors with Network"""

    def __init__(self, min_duration, health=None):
        super(NetworkIndicator, self).__init__(
            tr("Network"), min_duration, health=health
        )
        self._network = health.parent().cd("network")

    def state_ok(self):
        return bool(
            self._health["network_really_connected"]
            == self._health["network_should_be_connected"]
        )

    @property
    def error(self):
        error_str = ""
        idx = 1
        for network in self._network.ls():
            if network.type == "NetworkNode":
                if network["should_be_connected"]:
                    stats = network.cd("stats")
                    if stats and not stats["connected"]:
                        error_str += "\n{idx}. {net_name}: {err}".format(
                            idx=idx,
                            net_name=network.name,
                            err=stats["last_error"] or _UNKNOWN_ERROR,
                        )
                        idx += 1
        return error_str or "\n%s" % _UNKNOWN_ERROR


class ScriptsIndicator(Indicator):
    """Alarmed if server has errors with Scripts"""

    def __init__(self, min_duration, health=None):
        super(ScriptsIndicator, self).__init__(
            tr("Scripts"), min_duration, health=health
        )
        self._scripts = health.parent().cd("scripts")

    def state_ok(self):
        return self._health["scripts_ok"] == self._health["scripts_total"]

    @property
    def error(self):
        error_str = ""
        idx = 1
        for script in self._scripts.ls():
            if script.type == "Script" or script.type == "StockScript":
                if script["enable"]:
                    stats = script.cd("stats")
                    if stats and stats["error_count"]:
                        error_str += "\n{idx}. {scr_name}: {err}".format(
                            idx=idx,
                            scr_name=script.name,
                            err=stats["last_error"] or _UNKNOWN_ERROR,
                        )
                        idx += 1
        return error_str or "\n%s" % _UNKNOWN_ERROR


class HealthWatcher(py_object):
    """Class to watch for server healths

    Args:
        min_event_duration (int): Min. seconds for alarm.
        working_schedule (str, optional): Working schedule name. Default None.

    Attributes:
        min_event_duration (int): Min. seconds for alarm.
        indicators (List[Indicator]): All added indicators.
        state_change_callback (function): Function that calls when indicator
            state states changed.
    """

    _CHECK_DELAY_MS = 500

    def __init__(self, server, min_event_duration, working_schedule):
        logger.debug(
            "HealthWatcher(min_event_duration=%r, working_schedule=%r)",
            min_event_duration,
            working_schedule,
        )
        self.min_event_duration = min_event_duration
        self.server = server
        self._health = host.settings("/{}/health".format(self.server))
        self.working_schedule = working_schedule

        self.indicators = []
        self.state_change_callback = BaseUtils.do_nothing

    def add_indicator(self, indicator):
        """Adding indicator to check list"""
        if not issubclass(indicator, Indicator):
            raise TypeError(
                "{} is not subclass of Indicator".format(indicator.__name__)
            )
        self.indicators.append(indicator(self.min_event_duration, health=self._health))

    def check_health(self):
        """Check health of all indicators and send event if alarmed."""
        alarm_dt = datetime.now() - timedelta(seconds=self.min_event_duration)
        for indicator in self.indicators:
            changed_dt, state_ok, error = indicator.check_state()
            logger.debug(
                "%s: changed_dt: %s, state_ok: %s, error: %s",
                indicator.__class__.__name__,
                changed_dt,
                state_ok,
                error,
            )
            if changed_dt and alarm_dt > changed_dt:
                logger.info(
                    "%s %s, Error:%s",
                    indicator.__class__.__name__,
                    "OK" if state_ok else "Error",
                    error,
                )

                self.state_change_callback(
                    changed_dt=changed_dt,
                    state_ok=state_ok,
                    title=indicator.title,
                    error=error,
                )
                indicator.changed_dt = None

    def _check_loop(self):
        """Check loop"""
        if self.working_schedule is None:
            self.check_health()
        else:
            if self.working_schedule.color == "Red":
                self.check_health()
            else:
                logger.debug(
                    "Schedule '%s' now in '%s' zone, skipping...",
                    self.working_schedule,
                    self.working_schedule.color,
                )

        host.timeout(self._CHECK_DELAY_MS, self._check_loop)

    def run(self):
        """Check if indicators is not empty and run check loop"""
        if not self.indicators:
            raise ParameterError(tr("No one event selected!"))

        self._check_loop()


class Notifier(py_object):
    """Preparing messages, merge them and send throw all added senders

    Args:
        merge_tracks_cache (int): Seconds to merge messages.

    Attributes:
        merge_tracks_cache (int): Seconds to merge messages.
        senders (Dict[Sender]): All added senders
        data (List[Dict[]]): List of messages kwargs.
    """
    _SMSCSENDER_REGEXP = re.compile(r"(<\/?(\s|\S)*?>)")

    def __init__(self, merge_tracks_cache, email_date):
        self.merge_tracks_cache = merge_tracks_cache
        self.senders = {}
        self.data = []
        self._last_errors = {}
        self.email_date = email_date

    def _is_duplicate(self, data):
        prev_err = self._last_errors.get(data["title"], "No error yet")
        if prev_err != data["error"]:
            self._last_errors[data["title"]] = data["error"]
            return False
        return True

    def _send_all(self):
        server_name = host.object(SERVER).name
        raw_text = "<b>{server_name}</b>".format(server_name=server_name)
        post_sender_data = {}
        for kwargs in self.data:
            if self._is_duplicate(kwargs):
                continue

            if raw_text:
                raw_text += "\n"

            if kwargs["state_ok"]:
                if POST_REQUEST:
                    post_sender_data[kwargs["title"]] = tr("OK")
                kwargs["msg"] = tr("OK")
            else:
                if POST_REQUEST:
                    sender_errors = kwargs["error"].split("\n")
                    post_sender_data[kwargs["title"] + " Error"] = sender_errors[1:]
                kwargs["msg"] = tr("Error <i>{error}</i>").format(error=kwargs["error"])

            raw_text += "<b>{title}</b>: {msg}".format(**kwargs)

        if raw_text:
            logger.debug("Send messages: %s", raw_text)

            for sender_name, sender in self.senders.iteritems():
                if sender_name == "PopupSender":
                    text = raw_text.replace("\n", "<br>")
                elif sender_name == "EmailSender":
                    if self.email_date:
                        dt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        text = raw_text.replace("\n", "<br>")
                        text = "{} {}".format(dt, text)
                    else:
                        text = raw_text.replace("\n", "<br>")
                elif sender_name == "SMSCSender":
                    text = self._SMSCSENDER_REGEXP.sub("", raw_text)
                elif sender_name == "PostRequestSender":
                    post_sender_data["server_name"] = "{server_name}".format(server_name=server_name)
                    text = post_sender_data
                else:
                    text = raw_text

                sender.text(text)

            host.stats()["run_count"] += 1

        del self.data[:]

    def add_sender(self, sender):
        """Adding sender"""
        if not issubclass(sender.__class__, Sender):
            raise TypeError(
                "{} is not subclass of Sender".format(sender.__class__.__name__)
            )
        logger.info("Notifier.add_sender(%s)", sender.__class__.__name__)
        self.senders[sender.__class__.__name__] = sender

    def notify(self, **kwargs):
        """Send alarm"""
        if not self.data:
            host.timeout(1000 * self.merge_tracks_cache or 10, self._send_all)
        self.data.append(kwargs)


class FakeSoundSender(SoundPlayer, Sender):
    """Fake sender that play selected sound"""

    def __init__(self, sound_file):  # pylint: disable=W0235
        super(FakeSoundSender, self).__init__(sound_file)

    # noinspection PyUnusedLocal
    def text(self, *args, **kwargs):  # pylint: disable=W0613
        self.play()


class FakeFireEventSender(Sender):
    def __init__(self):
        super(FakeFireEventSender, self).__init__()
        self._script_object = ScriptObject()

    def text(self, text, **kwargs):
        self._script_object.fire_event_v2("Health monitoring event", data=text)


class PostRequestSender(Sender):
    def __init__(self, post_url):
        super(PostRequestSender, self).__init__()
        self.post_url = post_url
        self.session = requests.Session()
        self.session.verify = False

    @BaseUtils.run_as_thread
    def text(self, text, **kwargs):
        try:
            response = self.session.post(self.post_url, data=BaseUtils.to_json(text))
            logger.debug("[%s] %s", response.status_code, response.text)
        except Exception as err:
            logger.warning(str(err))


if __name__ == host.stats().parent().guid:

    ntf = Notifier(MERGE_TRACKS_CACHE, ADD_DATE_TO_EMAIL)  # pylint: disable=C0103

    if SIMPLE_PLAY_SOUND:
        sound = SIMPLE_PLAY_SOUND
        if sound.startswith("shots/"):
            sound = sound.replace("shots/", "%s/" % BaseUtils.get_screenshot_folder())
        ntf.add_sender(FakeSoundSender(sound))

    if SIMPLE_POPUP:
        ntf.add_sender(PopupSender())

    if SIMPLE_POPUP_WITH_BUTTON:
        ntf.add_sender(PopupWithBtnSender())

    if SIMPLE_FIRE_EVENT:
        ntf.add_sender(FakeFireEventSender())

    if TELEGRAM:
        try:
            ntf.add_sender(TelegramSender(TELEGRAM_IDS))
        except EnvironmentError:
            raise EnvironmentError("Telegram notification is unavailable for client, run script on the server")
    if EMAIL:
        ntf.add_sender(EmailSender(EMAIL_ACCOUNT, EMAIL_SPAMLIST))

    if SMSC:
        ntf.add_sender(
            SMSCSender(
                SMSC_LOGIN,
                SMSC_PASSWORD,
                SMSC_PHONES,
                SMSC_TRANSLIT,
            )
        )
    if POST_REQUEST:
        if not POST_REQUEST_URL:
            raise ValueError("Url is a required parameter")
        ntf.add_sender(PostRequestSender(POST_REQUEST_URL))

    if not ntf.senders:
        raise ValueError("No notifications")

    hw = HealthWatcher(SERVER, MIN_EVENT_DURATION, WORK_BY_SCHEDULE or None)
    hw.state_change_callback = ntf.notify

    if ERROR_CPU:
        hw.add_indicator(CPUIndicator)

    if ERROR_CLOUD:
        hw.add_indicator(CloudIndicator)

    if ERROR_DISKS:
        hw.add_indicator(HDDIndicator)

    if COUNT_DISKS:
        hw.add_indicator(HDDCountIndicator)

    if ERROR_DB:
        hw.add_indicator(SQLIndicator)

    if ERROR_IP_DEVICES:
        hw.add_indicator(DevicesIndicator)

    if ERROR_CHANNELS:
        hw.add_indicator(ChannelsIndicator)

    if ERROR_NETWORK:
        hw.add_indicator(NetworkIndicator)

    if ERROR_SCRIPTS:
        hw.add_indicator(ScriptsIndicator)

    hw.run()
