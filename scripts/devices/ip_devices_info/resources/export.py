# -*- coding: utf-8 -*-
import host
import xlsxwriter
from collections import namedtuple
import os

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

__version__ = "1.0.4"
logger.debug("%s version: %s", __name__, __version__)


class ExportError(Exception):
    pass


def save_data(data, path):
    logger.debug("save data")
    filename = "IP_Device_info.xlsx"
    try:
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except Exception as err:
                raise ExportError("Can't make dirs %s. Error: %s" % (path, err))
        workbook = xlsxwriter.Workbook(
            os.path.join(path, filename.format()), {"tmpdir": path}
        )
        worksheet = workbook.add_worksheet("IP_Device_info")
        worksheet.set_column(0, 1, 20)
        worksheet.set_column(2, 2, 8)
        worksheet.set_column(3, 5, 20)
        worksheet.set_column(6, 8, 5)
        worksheet.set_column(9, 9, 10)
        worksheet.set_column(10, 12, 5)
        worksheet.set_column(13, 14, 13)
        worksheet.set_column(15, 15, 8)
        worksheet.set_column(16, 17, 15)

        Formatter = namedtuple("Formatter", ["header", "text"])
        formatter = Formatter(
            workbook.add_format(
                {"bold": True, "align": "center", "bg_color": "#e3e7e8", "border": 1,}
            ),
            workbook.add_format({"border": 1, "align": "center", "valign": "vcenter",}),
        )
        row = 0
        col = 0

        for server in data:
            worksheet.merge_range(
                row,
                col,
                row,
                col + 17,
                "Server name: %s" % server["server_name"],
                formatter.header,
            )
            row += 1
            worksheet.write(row, col, "Device", formatter.header)
            worksheet.write(row, col + 1, "IP", formatter.header)
            worksheet.write(row, col + 2, "Port", formatter.header)
            worksheet.write(row, col + 3, "Model", formatter.header)
            worksheet.write(row, col + 4, "State", formatter.header)
            worksheet.write(row, col + 5, "Channel", formatter.header)
            worksheet.write(row, col + 6, "Main", formatter.header)
            worksheet.write(row, col + 7, "FPS", formatter.header)
            worksheet.write(row, col + 8, "GOP", formatter.header)
            worksheet.write(row, col + 9, "Resolution", formatter.header)
            worksheet.write(row, col + 10, "Sub", formatter.header)
            worksheet.write(row, col + 11, "FPS", formatter.header)
            worksheet.write(row, col + 12, "GOP", formatter.header)
            worksheet.write(row, col + 13, "Resolution", formatter.header)
            worksheet.write(row, col + 14, "Video Codec", formatter.header)
            worksheet.write(row, col + 15, "Audio", formatter.header)
            worksheet.write(row, col + 16, "Audio Codec", formatter.header)
            worksheet.write(row, col + 17, "Motion Detector", formatter.header)
            row += 1
            for device in server["ip_device_info"]:
                channels_n = 0
                for channel in device["channel"]:
                    if channels_n:
                        row += 1
                    worksheet.write(row, col + 5, channel["ch_name"], formatter.text)
                    worksheet.write(row, col + 6, channel["main"], formatter.text)
                    worksheet.write(row, col + 7, channel["main_fps"], formatter.text)
                    worksheet.write(row, col + 8, channel["main_gop"], formatter.text)
                    worksheet.write(
                        row, col + 9, channel["main_resolution"], formatter.text
                    )
                    worksheet.write(row, col + 10, channel["sub"], formatter.text)
                    worksheet.write(row, col + 11, channel["sub_fps"], formatter.text)
                    worksheet.write(row, col + 12, channel["sub_gop"], formatter.text)
                    worksheet.write(
                        row, col + 13, channel["sub_resolution"], formatter.text
                    )
                    worksheet.write(row, col + 14, channel["codec"], formatter.text)
                    worksheet.write(
                        row, col + 15, channel["audio_enabled"], formatter.text
                    )
                    worksheet.write(
                        row, col + 16, channel["audio_codec"], formatter.text
                    )
                    worksheet.write(
                        row, col + 17, channel["motion_detector"], formatter.text
                    )
                    channels_n += 1
                if channels_n > 1:
                    worksheet.merge_range(
                        row,
                        col,
                        row - channels_n + 1,
                        col,
                        device["name"],
                        formatter.text,
                    )
                    worksheet.merge_range(
                        row,
                        col + 1,
                        row - channels_n + 1,
                        col + 1,
                        device["connection_ip"],
                        formatter.text,
                    )
                    worksheet.merge_range(
                        row,
                        col + 2,
                        row - channels_n + 1,
                        col + 2,
                        device["connection_port"],
                        formatter.text,
                    )
                    worksheet.merge_range(
                        row,
                        col + 3,
                        row - channels_n + 1,
                        col + 3,
                        device["model"],
                        formatter.text,
                    )
                    worksheet.merge_range(
                        row,
                        col + 4,
                        row - channels_n + 1,
                        col + 4,
                        device["state"],
                        formatter.text,
                    )

                else:
                    worksheet.write(row, col, device["name"], formatter.text)
                    worksheet.write(
                        row, col + 1, device["connection_ip"], formatter.text
                    )
                    worksheet.write(
                        row, col + 2, device["connection_port"], formatter.text
                    )
                    worksheet.write(row, col + 3, device["model"], formatter.text)
                    worksheet.write(row, col + 4, device["state"], formatter.text)
                row += 1
        row += 2

        workbook.close()

        logger.warning("Done! File created: %s" % workbook.filename)

        # automatic file opening on Windows, for debugging
        # if os.name == "nt":
        #     os.startfile(workbook.filename)

    except Exception as err:
        logger.exception("Unhandled exception in saving xlsx")
        raise ExportError(str(err))
