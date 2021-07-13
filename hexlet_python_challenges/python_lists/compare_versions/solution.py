def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def compare_version(first, second):
    [a1, b1] = first.split(".")
    [a2, b2] = second.split(".")

    major = sign(int(a1) - int(a2))
    minor = sign(int(b1) - int(b2))

    return major if major != 0 else minor
