from textwrap import wrap


def hex2rgb(color):
    r, g, b = map(
        lambda channel: int(channel, 16),
        wrap(color[1:], 2),
    )  # noqa: WPS221
    return {"r": r, "g": g, "b": b}


def convert(channel):
    return hex(channel)[2:].rjust(2, "0")


def rgb2hex(r=None, g=None, b=None):
    return "#{0}{1}{2}".format(*map(convert, [r, g, b]))


# Альтернативное решение с использованием возможностей .format
# https://docs.python.org/3.4/library/string.html#format-specification-mini-language
# def rgb2hex(r=None, g=None, b=None):
#     return "#{:02x}{:02x}{:02x}".format(r, g, b)
