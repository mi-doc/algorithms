import unittest
from ..construct_bt_from_pre_and_inorder import Solution
from ..binary_tree_tools import create_tree, tree_to_list


class IsSymmetricTestCase(unittest.TestCase):
    
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()
    
    def test(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        res = tree_to_list(self.sol.buildTree(preorder, inorder))
 
        assert res == [3,9,20,None,None,15,7]
