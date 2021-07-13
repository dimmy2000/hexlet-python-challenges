def binary_sum(number_a, number_b):
    binary_a = int(number_a, base=2)
    binary_b = int(number_b, base=2)
    return bin(binary_a + binary_b).replace("0b", "")
