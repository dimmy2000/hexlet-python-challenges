def chunked(size, source):
    output = []
    index = 0
    while index < len(source):
        output.append(source[index:index + size])
        index += size
    return output
