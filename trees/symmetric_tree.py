from binary_tree_tools import create_tree, TreeNode
from typing import Optional


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        The function compares two subtrees for symmetry
        """
        if not root:
            return True

        queue = [(root.left, root.right)]
        while queue:
            l_tree, r_tree = queue.pop()
            if getattr(l_tree, 'val', "-") != getattr(r_tree, 'val', "-"):
                # If both nodes don't exist or exist and have same values - symmetric.
                # Otherwise the tree is asymmetric
                return False
            if l_tree:  # Could be r_tree since they are symmetric
                queue.extend((
                    (l_tree.left, r_tree.right),
                    (l_tree.right, r_tree.left)
                ))

        return True


def test(vals):
    s = Solution()
    for val in vals:
        root = create_tree(val)
        res = s.isSymmetric(root)
        print(val, ' -> ', res)


if __name__ == '__main__':
    vals = [
        # [1,2,2,None,3,None,3],
        [5,3,3,4,5,5,4],
        [2,1,3],
        [2,1],
        [1],
        [3,4,4],
        [],
        [6,3,8,1,4,7,10,2],
        [6,3,8,1,4,7],
        [9,-42,-42,None,76,76,None,None,13,None,13]
    ]

    test(vals)