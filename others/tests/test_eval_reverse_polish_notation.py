import unittest
from ..eval_reverse_polish_notation import Solution


class EvalReversePolishNotationTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().evalRPN
        return super().setUp()

    def test1(self):
        res = self.sol(
          tokens = ["2","1","+","3","*"] 
        )
        assert res == 9

    def test2(self):
        res = self.sol(
           tokens = ["4","13","5","/","+"]
        )
        assert res == 6

