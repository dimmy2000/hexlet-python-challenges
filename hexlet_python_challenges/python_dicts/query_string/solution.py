def build_query_string(params):
    items = []
    for key, value in sorted(params.items()):
        items.append("{0}={1}".format(key, value))
    return "&".join(items)
