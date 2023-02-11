import unittest
from ..factorial_trailing_zeroes import Solution


class FactorialTrailingZeroesTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().trailingZeroes
        return super().setUp()

    def test1(self):
        args = {
            'n': 3
        }
        expected_answer = 0

        res = self.sol(**args)
        assert res == expected_answer


    def test2(self):
        args = {
            'n': 5
        }
        expected_answer = 1

        res = self.sol(**args)
        assert res == expected_answer