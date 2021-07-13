def is_vertical(line):
    (x1, y1), (x2, y2) = line  # noqa: WPS414
    # ^ sometimes it is just fine to unpack such nested structures
    return x1 == x2 and y1 != y2


def is_horizontal(line):
    (x1, y1), (x2, y2) = line  # noqa: WPS414
    return x1 != x2 and y1 == y2


def is_degenerated(line):
    p1, p2 = line
    return p1 == p2


def is_inclined(line):
    return not (
        is_vertical(line) or is_horizontal(line) or is_degenerated(line)
    )
