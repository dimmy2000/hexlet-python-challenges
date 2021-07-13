from solution import is_power_of_three


def test_is_power_of_three_positive():
    assert is_power_of_three(1)
    assert is_power_of_three(9)
    assert is_power_of_three(81)


def test_is_power_of_three_negative():
    assert not is_power_of_three(0)
    assert not is_power_of_three(2)
    assert not is_power_of_three(10)
    assert not is_power_of_three(18), "Делится на 3, но не степень тройки!"
