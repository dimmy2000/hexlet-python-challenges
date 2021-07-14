from collections import defaultdict


def merged(*dicts):
    aggregate = defaultdict(set)
    for source in dicts:
        for key, value in source.items():
            aggregate[key].add(value)
    return aggregate
