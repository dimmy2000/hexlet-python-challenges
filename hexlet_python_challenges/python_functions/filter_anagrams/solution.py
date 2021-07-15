def normalized(string):
    return list(sorted(string))  # noqa: C413


def filter_anagrams(word, words):
    norm = normalized(word)
    return filter(lambda item: normalized(item) == norm, words)
