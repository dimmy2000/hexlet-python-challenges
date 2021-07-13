import unittest

import solution


class TestBinarySum(unittest.TestCase):

    def test_cases(self):
        def check(a, b, expected):
            self.assertEqual(
                solution.binary_sum(a, b),
                bin(expected)[2:],
            )
        check('1000', '10', 0b1000 + 0b10)
        check('1010', '101', 0b1010 + 0b101)
        check('1', '1', 0b1 + 0b1)
        check('1111', '1111', 0b1111 + 0b1111)
