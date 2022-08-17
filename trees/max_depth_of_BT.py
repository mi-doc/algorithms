from binary_tree_tools import create_tree, print_tree_breadth_first, TreeNode
from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == '__main__':
    l = [3,9,20,None,None,15,7]
    tr = create_tree(l)

    print_tree_breadth_first(tr)



