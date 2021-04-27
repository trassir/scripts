# -*- coding: utf-8 -*-

import host

try:
    from helpers import get_logger
except ImportError:
    from logging import getLogger as get_logger

logger = get_logger()

__version__ = "1.0.1"
logger.debug("%s version: %s", __name__, __version__)


def line(x1, y1, x2, y2, color="#1FC619", width=2.0):
    """Draw line
    Args:
        x1 (int): point
        y1 (int): point
        x2 (int): point
        y2 (int): point
        color (str): line color, default: "#1FC619"
        width (int, optional): line width, default: 2.0

    Returns:
        string
    """
    return "line {x1:.1f} {y1:.1f} {x2:.1f} {y2:.1f} {color:s} {width:d}".format(
        x1=x1, y1=y1, x2=x2, y2=y2, color=color, width=int(width)
    )


def rect(x1, y1, x2, y2, color="#1FC619"):
    """Draw rect
    Args:
        x1 (int): point
        y1 (int): point
        x2 (int): point
        y2 (int): point
        color (str): rect color, default: "#1FC619"

    Returns:
        string
    """
    return "rect {x1:.1f} {y1:.1f} {x2:.1f} {y2:.1f} {color:s}".format(
        x1=x1, y1=y1, x2=x2, y2=y2, color=color
    )


def fillrect(x1, y1, x2, y2, color="#1FC619"):
    """Draw fillrect
    Args:
        x1 (int): point
        y1 (int): point
        x2 (int): point
        y2 (int): point
        color (str): fillrect color, default: "#1FC619"

    Returns:
        string
    """
    return "fillrect {x1:.1f} {y1:.1f} {x2:.1f} {y2:.1f} {color:s}".format(
        x1=x1, y1=y1, x2=x2, y2=y2, color=color
    )


def text_ext(
    x1, y1, x2, y2, text, bg_color="#C5CEC4", font_color="#000000", font_size_px=12
):
    """Draw text_ext
    Args:
        x1 (int): point
        y1 (int): point
        x2 (int): point
        y2 (int): point
        text (str): custom text
        bg_color (str): background color, default: "#C5CEC4"
        font_color (str): font color,  default: "#000000"
        font_size_px (int): font size,  default: 12

    Returns:
        string
    """
    return "text_ext {x1:.1f} {y1:.1f} {x2:.1f} {y2:.1f} {bg_color:s} {font_color:s} {font_size_px:d} {text:s}".format(
        x1=x1,
        y1=y1,
        x2=x2,
        y2=y2,
        bg_color=bg_color,
        font_color=font_color,
        font_size_px=font_size_px,
        text=text,
    )


def textbox(x1, y1, x2, y2, text, align="TL", fill=True, color="#1FC619"):
    """Draw textbox
    Args:
        x1 (int): point
        y1 (int): point
        x2 (int): point
        y2 (int): point
        text (str): custom text
        align (str): one of: TL, TR, BL, BR, default: TL
        fill (int): fill: 1 or 0, default: 1
        color (str): textbox color, default: "#1FC619"

    Returns:
        string
    """
    return "textbox {x1:.1f} {y1:.1f} {x2:.1f} {y2:.1f} {align:s} {fill:d} {color:s} {text:s}".format(
        x1=x1, y1=y1, x2=x2, y2=y2, align=align, fill=fill, color=color, text=text
    )


def polyline(x1, y1, x2, y2, color="#1FC619", width=2.0):
    """Draw polyline
    Args:
        x1 (int): point
        y1 (int): point
        x2 (int): point
        y2 (int): point
        color (str): polyline color, default: "#1FC619"
        width (int, optional): polyline width, default: 2.0

    Returns:
        string
    """
    return "polyline {color:s} {width:d} {x1:.1f} {y1:.1f} {x2:.1f} {y2:.1f}".format(
        color=color, width=int(width), x1=x1, y1=y1, x2=x2, y2=y2
    )


def poly(x1, y1, x2, y2, color="#1FC619", width=2.0):
    """Draw poly
    Args:
        x1 (int): point
        y1 (int): point
        x2 (int): point
        y2 (int): point
        color (str): poly color, default: "#1FC619"
        width (int, optional): poly width, default: 2.0

    Returns:
        string
    """
    return "poly {color:s} {width:d} {x1:.1f} {y1:.1f} {x2:.1f} {y2:.1f}".format(
        color=color, width=int(width), x1=x1, y1=y1, x2=x2, y2=y2
    )


def fillpoly(x1, y1, x2, y2, color="#1FC619", width=2.0):
    """Draw fillpoly
    Args:
        x1 (int): point
        y1 (int): point
        x2 (int): point
        y2 (int): point
        color (str): fillpoly color, default: "#1FC619"
        width (int, optional): fillpoly width, default: 2.0

    Returns:
        string
    """
    return "fillpoly {color:s} {width:d} {x1:.1f} {y1:.1f} {x2:.1f} {y2:.1f}".format(
        color=color, width=int(width), x1=x1, y1=y1, x2=x2, y2=y2
    )


def border_labels(x1, y1, x2, y2, font_color="#000000", bg_color="C5CEC4", swap=True):
    """Draw border labels
    Args:
        x1 (int): point
        y1 (int): point
        x2 (int): point
        y2 (int): point
        font_color (str): font color,  default: "#000000"
        bg_color (str): background color, default: "#C5CEC4"
        swap (int): swap labels 0: A - B, 1: B - A, default: 1

    Returns:
        string
    """
    return "border_labels {font_color:s} {bg_color:s} {swap:d} {x1:.1f} {y1:.1f} {x2:.1f} {y2:.1f}".format(
        font_color=font_color, bg_color=bg_color, swap=swap, x1=x1, y1=y1, x2=x2, y2=y2
    )


def draw(channel_guid, *args):
    logger.debug("figure_set('%s', %s)", channel_guid, args)
    """ Main draw func

    Args: 
        channel_guid (str): channel_guid

    """
    host.figure_set(channel_guid, list(args))
