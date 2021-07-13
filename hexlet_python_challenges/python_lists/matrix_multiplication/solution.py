def zero_matrix(rows, columns):
    matrix = []
    row = [0] * columns
    for _ in range(rows):
        matrix.append(row[:])
    return matrix


def multiply(a, b):  # noqa: WPS210
    rows_in_a = len(a)
    columns_in_b = len(b[0])
    c = zero_matrix(rows_in_a, columns_in_b)
    for row_a, row_c in zip(a, c):
        for x in range(columns_in_b):
            for y, row_b in enumerate(b):
                row_c[x] += row_a[y] * row_b[x]
    return c
