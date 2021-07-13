def rotate_left(triple):
    elem1, elem2, elem3 = triple
    return (elem2, elem3, elem1)


def rotate_right(triple):
    elem1, elem2, elem3 = triple
    return (elem3, elem1, elem2)
