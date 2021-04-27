import time
import datetime


def dt_to_ts(dt):
    return int(int(time.mktime(dt.timetuple())) * 1e6 + dt.microsecond)


def ts_to_dt(ts):
    if ts > 1e10:
        ts_sec = int(ts / 1e6)
        ts_ms = int(ts - ts_sec * 1e6)
    else:
        ts_sec = int(ts)
        ts_ms = 0
    return datetime.datetime.fromtimestamp(ts_sec) + datetime.timedelta(
        microseconds=ts_ms
    )