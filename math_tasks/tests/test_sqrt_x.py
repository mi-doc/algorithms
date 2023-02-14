import unittest
from ..sqrt_x import Solution


class SqrtXTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().mySqrt
        return super().setUp()

    def test1(self):
        args = {
            'x': 4
        }
        expected_answer = 2

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'x': 8
        }
        expected_answer = 2

        res = self.sol(**args)
        assert res == expected_answer

    def test3(self):
        args = {
            'x': 1
        }
        expected_answer = 1

        res = self.sol(**args)
        assert res == expected_answer

    def test4(self):
        args = {
            'x': 3
        }
        expected_answer = 1

        res = self.sol(**args)
        assert res == expected_answer

    def test5(self):
        args = {
            'x': 5
        }
        expected_answer = 2

        res = self.sol(**args)
        assert res == expected_answer