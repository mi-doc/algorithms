from typing import Optional
from .binary_tree_tools import TreeNode

# The essence of the task
TASK = """
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""


class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            
            root = root.right
            