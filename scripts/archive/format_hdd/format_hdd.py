# -*- coding: utf-8 -*-
# format_hdd
"""
<parameters>
    <parameter>
        <type>string_from_list</type>
        <id>DSK</id>
        <name>Выберете HDD</name>
        <string_list>disk</string_list>
    </parameter>
</parameters>
"""
import os
from datetime import datetime

DEBUG = True


class Log:
    # Initialization
    def __init__(self, file_name='%s.log' % settings("scripts/%s" % __name__).name, write_log=True):
        self.dir_path = settings('system_wide_options')['screenshots_folder']
        self.file_name = file_name
        self.file_path = os.path.join(self.dir_path, self.file_name)
        self.write_log = write_log
        self.max_rows = 50000

    # Old rows removal
    def remove_old_lines(self):
        with open(self.file_path, 'rb') as f:
            text = f.read().split("\n")
        if len(text) > self.max_rows:
            text = text[len(text) - self.max_rows:]
            with open(self.file_path, 'wb') as f:
                f.write("\n".join(text))

    # Write to log
    def write(self, string):
        if not self.write_log:
            return 0
        with open(self.file_path, 'a') as f:
            f.write('%s:%s\n' % (datetime.now(), string))
        self.remove_old_lines()
        return 0


log = Log('%s.log' % settings("scripts/%s" % __name__).name, write_log=DEBUG)


class CollectHDD():
    def __init__(self, hdd):
        """del format_mark"""
        self.hdd = hdd
        self.del_format_mark_()

    def del_format_mark_(self):
        for x in settings("archive").ls():
            if not x['model']:
                name = x["path_local8bit"]
            else:
                name = '%s/%s' % (x['model'], x['serial'])
            log.write('name - %s' % name)
            if name == self.hdd:
                path = os.path.join(x["path_local8bit"], '.format_mark')
                if os.path.isfile(path):
                    log.write('Format mark catch!')
                    os.remove(path)
                else:
                    log.write('Not format mark')


dirs = []
for x in settings("archive").ls():
    if not x['model']:
        dirs.append(x["path_local8bit"])
    else:
        str_ = '%s/%s' % (x['model'], x['serial'])
        dirs.append(str_)
str_disk = ','.join(dirs)
log.write('list disk %s' % str_disk)
script_ = stats().parent()["script"]
strip_src = script_.split('string_list>')
strip_src_ = script_.split(strip_src[1])
if strip_src[1] != str_disk + '</':
    str_for_change = strip_src_[0] + str_disk + '</' + strip_src_[1]
    stats().parent()["script"] = str_for_change
else:
    if DSK:
        ch = CollectHDD(DSK)
    else:
        raise ValueError('Выберте диск!')