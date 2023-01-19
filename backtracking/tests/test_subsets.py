import unittest
from ..subsets import Solution


class SubsetsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test(self):
        res = set(tuple(x) for x in self.sol.subsets([1,2,3]))
        answer = set(tuple(x) for x in [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        assert res == answer
    
    def test_subsets_cascading(self):
        res = set(tuple(x) for x in self.sol.subsets_cascading([1,2,3]))
        answer = set(tuple(x) for x in [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        assert res == answer

    def test_subsets_backtracking(self):
        res = set(tuple(x) for x in self.sol.subsets_backtracking([1,2,3]))
        answer = set(tuple(x) for x in [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        assert res == answer
        