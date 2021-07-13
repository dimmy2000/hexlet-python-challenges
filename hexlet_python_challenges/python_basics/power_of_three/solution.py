def is_power_of_three(number):
    counter = 1  # 3 ** 0
    while counter < number:
        counter *= 3
    return counter == number
