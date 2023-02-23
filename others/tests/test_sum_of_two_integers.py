import unittest
from ..sum_of_two_integers import Solution


class SumOfTwoIntegersTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().getSum
        return super().setUp()

    def test1(self):
        args = {
            'a': 1, 'b': 2
        }
        expected_answer = 3

        res = self.sol(**args)
        assert res == expected_answer

    def test2(self):
        args = {
            'a': 3, 'b': 2
        }
        expected_answer = 5

        res = self.sol(**args)
        assert res == expected_answer

    def test3(self):
        args = {
            'a': -1, 'b': 1
        }
        expected_answer = 0

        res = self.sol(**args)
        assert res == expected_answer