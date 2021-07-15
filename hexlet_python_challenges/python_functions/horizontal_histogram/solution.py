from collections import Counter


def histo(samples, min_value=None, max_value=None, bar_char="#"):
    """Draws a horizontal histogram."""
    if min_value is None:
        min_value = min(samples)
    if max_value is None:
        max_value = max(samples)

    axis = range(min_value, max_value + 1)
    counts = Counter(samples)

    lines = map(
        lambda value, count: "{0}|{1}{2}".format(
            value,
            bar_char * count,
            " " + str(count) if count else "",  # noqa: WPS336
        ),
        axis,
        map(lambda key: counts[key], axis),
    )

    return "\n".join(lines)
