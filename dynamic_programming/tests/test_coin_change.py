import unittest
from ..coin_change import Solution


class CoinChangeTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().coinChange2
        return super().setUp()

    def test1(self):
        args = {
            'coins': [1,2,5], 'amount': 11
        }
        expected_answer = 3

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'coins': [2], 'amount': 3
        }
        expected_answer = -1

        res = self.sol(**args)
        assert res == expected_answer
