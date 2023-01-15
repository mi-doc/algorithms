import unittest
from ..symmetric_tree import Solution
from ..binary_tree_tools import create_tree


class IsSymmetricTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()
    
    def test_is_symmetric_yes(self):
        vals = [
            [5,3,3,4,5,5,4],
            [1],
            [3,4,4],
            [],
        ]

        for v in vals:
            root = create_tree(v)
            self.assertTrue(self.sol.isSymmetric(root))

    def test_is_symmetric_no(self):
        vals = [
            [2,1,4],
            [2,1],
            [6,3,8,1,4,7,10,2],
            [6,3,8,1,4,7],
            [9,-42,-42,None,76,76,None,None,13,None,13]
        ]

        for v in vals:
            root = create_tree(v)
            self.assertFalse(self.sol.isSymmetric(root))
    
    def test_asym_01(self):
        r = create_tree([2,1,2])
        self.assertFalse(self.sol.isSymmetric(r))

    def test_asym_02(self):
        r = create_tree([2,1,4444])
        self.assertFalse(self.sol.isSymmetric(r))

    def test_asym_03(self):
        r = create_tree([2,1,3,21])
        self.assertFalse(self.sol.isSymmetric(r))

    def test_asym_04(self):
        r = create_tree([2,1,1,3,3,3,4])
        self.assertFalse(self.sol.isSymmetric(r))
