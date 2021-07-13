def enlarge(image):
    output = []
    for line in image:
        row = []
        for pixel in line:
            # expand horizontally
            row.extend([pixel, pixel])
        row = "".join(row)
        # expand verticaly
        output.extend([
            row,
            row,
        ])
    return output
