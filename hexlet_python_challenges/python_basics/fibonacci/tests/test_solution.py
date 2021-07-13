from solution import fib


def test_fib_primary():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3


def test_fib():
    assert fib(5) == 5
    assert fib(10) == 55
