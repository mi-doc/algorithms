import unittest
from ..happy_number import Solution


class HappyNumberTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().isHappy
        return super().setUp()

    def test1(self):
        args = {
            'n': 19
        }
        expected_answer = True

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'n': 2
        }
        expected_answer = False

        res = self.sol(**args)
        assert res == expected_answer
