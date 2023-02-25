import unittest
from ..set_matrix_zeroes import Solution


class SetMatrixZeroesTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().setZeroes
        return super().setUp()

    def test1(self):
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        self.sol(
            matrix = matrix
        )
        assert matrix == [[1,0,1],[0,0,0],[1,0,1]]

    def test2(self):
        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        self.sol(
            matrix = matrix
        )
        assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

