from functools import reduce

POWERS_OF_TWO = (2 ** 24, 2 ** 16, 2 ** 8, 2 ** 0)  # noqa: WPS221, WPS345


def ip2int(ip):
    return sum(map(
        lambda x, y: int(x) * y,
        ip.split("."),
        POWERS_OF_TWO,
    ))


def _make_octet(accumulator, divider):
    ip, remainder = accumulator
    octet, new_remainder = divmod(remainder, divider)
    return ip + (str(octet),), new_remainder


def int2ip(integer):
    octets, _ = reduce(_make_octet, POWERS_OF_TWO, ((), integer))
    return ".".join(octets)
