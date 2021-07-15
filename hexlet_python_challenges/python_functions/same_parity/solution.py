def is_even(number):
    return number % 2 == 0


def same_parity_filter(numbers):
    if not numbers:
        return []

    first_number_parity = is_even(numbers[0])

    filtered_numbers = filter(
        lambda number: is_even(number) == first_number_parity,
        numbers,
    )

    return list(filtered_numbers)
