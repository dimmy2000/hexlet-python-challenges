def diff(angle1, angle2):
    turn_degrees = 360
    return min(
        (angle1 - angle2) % turn_degrees,
        (angle2 - angle1) % turn_degrees,
    )
