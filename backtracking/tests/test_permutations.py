
import unittest
from ..permutations import Solution


class PermutationsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()
    
    def test(self):
        res = self.sol.permute([1,2,3])
        answer = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        assert tuple(tuple(x) for x in res) == tuple(tuple(x) for x in answer)
        