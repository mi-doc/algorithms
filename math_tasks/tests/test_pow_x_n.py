import unittest
from ..pow_x_n import Solution


class PowXNTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().myPow
        return super().setUp()

    def test1(self):
        args = {
            'x': 2.00000, 'n': 10
        }
        expected_answer = 1024.00000

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'x': 2.10000, 'n': 3
        }
        expected_answer = 9.26100

        res = self.sol(**args)
        res = int(res*100000) / 100000
        assert res == expected_answer
