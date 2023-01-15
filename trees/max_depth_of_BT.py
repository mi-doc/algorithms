from .binary_tree_tools import create_tree, print_tree_breadth_first, TreeNode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.measure_depth(root, depth=0)

    def measure_depth(self, root: Optional[TreeNode], depth: int) -> int:
        """
        A recursive function calculating depth
        """
        if not root:
            return depth
        max_left = self.measure_depth(root.left, depth + 1)
        max_right = self.measure_depth(root.right, depth + 1)
        return max(max_left, max_right)


if __name__ == '__main__':
    l = [3,9,20,None,None,15,7,8,8,1,4,3,1,6,4,5]
    tr = create_tree(l)

    sol = Solution()
    res = sol.maxDepth(tr)
    print(res)
