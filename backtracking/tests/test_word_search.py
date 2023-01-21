import unittest
from ..word_search import Solution
import time


class WordSearchTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.start = time.time()
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        print(time.time() - cls.start)
        return super().tearDownClass()
    
    def setUp(self) -> None:
        self.sol = Solution().exist_dfs
        return super().setUp()
    
    def test1(self):
        res = self.sol(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
        assert res == True

    def test2(self):
        res = self.sol(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
        assert res == True

    def test3(self):
        res = self.sol(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
        assert res == False
    
    def test4(self):
        res = self.sol(board=[['a']], word = 'a')
        assert res == True