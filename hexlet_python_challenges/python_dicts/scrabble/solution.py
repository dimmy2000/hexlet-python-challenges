from collections import Counter


def scrabble(string, word):
    letters = Counter(string.lower())
    for letter, count in Counter(word.lower()).items():
        if letters[letter] < count:
            return False
    return True

    # Можно было сделать ещё короче, если учесть то,
    # как работает вычитание для пары Counter!
    # Хватило бы: return not (Counter(word.lower()) - Counter(string.lower()))
