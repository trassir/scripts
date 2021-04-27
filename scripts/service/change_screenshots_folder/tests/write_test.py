# pylint: skip-file
# -*- coding: utf-8 -*-
import os
import threading

from functools import wraps

import host


def run_as_thread(func):
    """Run function as thread"""

    @wraps(func)
    def run(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
        return thread

    return run


test_file = os.path.join(
    host.settings("system_wide_options")["screenshots_folder"], "testfile.txt"
)


def raise_from_thread(err):
    raise err


def working():
    host.stats()["run_count"] += 1
    host.timeout(1000, working)


@run_as_thread
def write_test():
    try:
        with open(test_file, "w") as f:
            f.write("hello from trassir")
        raise ValueError(test_file)
    except Exception as err:
        host.timeout(1, lambda: raise_from_thread(err))


working()
write_test()
