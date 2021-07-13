def is_palindrome(string):
    pointer1 = 0
    pointer2 = len(string) - 1
    while pointer2 - pointer1 > 0:
        if string[pointer1] != string[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True
