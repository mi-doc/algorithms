import unittest
from ..inorder_bt_traversal import Solution
from ..binary_tree_tools import create_tree


class InorderBtTraversalTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution().inorderTraversalMorris
        return super().setUp()

    def test1(self):
        head = create_tree([1, None, 2, 3])
        res = self.sol(
            head
        )
        assert res == [1, 3, 2]

    def test2(self):
        head = create_tree([1, 2, 3, 4, 5, 6])
        res = self.sol(
            head
        )
        assert res == [4, 2, 5, 1, 6, 3]

    def test3(self):
        head = create_tree([1])
        res = self.sol(
            head
        )
        assert res == [1]