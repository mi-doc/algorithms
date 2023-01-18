import unittest
from ..generate_parentheses import Solution


class GenerateParenthesesTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()
    
    def test(self):
        res = self.sol.generateParenthesis(3)
        assert res == ["((()))","(()())","(())()","()(())","()()()"]