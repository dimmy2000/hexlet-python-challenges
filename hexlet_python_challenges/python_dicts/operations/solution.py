def gen_diff(data1, data2):
    keys = data1.keys() | data2.keys()  # https://youtu.be/vkUTX1hruF8?t=929
    result = {}
    for key in keys:
        if key not in data1:
            result[key] = "added"
        elif key not in data2:
            result[key] = "deleted"
        elif data1[key] == data2[key]:
            result[key] = "unchanged"
        else:
            result[key] = "changed"
    return result
