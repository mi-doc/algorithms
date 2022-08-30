from binary_tree_tools import create_tree, print_tree_breadth_first, TreeNode
from typing import Optional, Union


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        The function checks all nodes in BST to follow the rules of BST
        """
        return self.isValid(root)

    def isValid(self, root: Optional[TreeNode], minval: Union[int, float] = float('-inf'), maxval: Union[int, float] = float('inf')) -> bool:
        """
        This recursive function assures that all left nodes are smaller than their parent and the root of the subtree,
        and vise versa with the right nodes.
        """
        if not root:
            return True

        if root.val >= maxval or root.val <= minval:
            return False

        return self.isValid(root.left, minval, root.val) and self.isValid(root.right, root.val, maxval)


def test(vals):
    s = Solution()
    for val in vals:
        root = create_tree(val)
        res = s.isValidBST(root)
        print(val, ' -> ', res)


if __name__ == '__main__':
    vals = [
        [5,3,8,2,4,6,9],
        [2,1,3],
        [5,3,8,2,4,6,7], # The last 7 is wrong
        [5,3,8,2,4,5,9], # The -2 index (5) is wrong
        [5,3,8,2,4,4,9]  # The -2 index (4) is wrong
    ]

    test(vals)