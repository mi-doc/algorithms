import unittest
from ..kth_smallest_element_in_a_bst import Solution
from ..binary_tree_tools import create_tree


class KthSmallestElementInABstTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().kthSmallest
        return super().setUp()

    def test1(self):
        root = create_tree([3,1,4,None,2])
        output = self.sol(
          root = root, k = 1
        )
        assert output == 1

    def test2(self):
        root = create_tree([5,3,6,2,4,None,None,1])
        output = self.sol(
          root = root, k = 3
        )
        assert output == 3

