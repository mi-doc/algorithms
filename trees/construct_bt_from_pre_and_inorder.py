from typing import Optional, List
from .binary_tree_tools import TreeNode, level_order_traversal


class Solution:
    """
    The solution from leetcode.
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def list_to_tree(left, right):
            if left > right:
                return None

            nonlocal preorder_index
            root_value = preorder[preorder_index]
            preorder_index += 1
            node = TreeNode(root_value)

            node.left = list_to_tree(left, inorder_index_map[root_value] -1)
            node.right = list_to_tree(inorder_index_map[root_value] + 1, right)
            return node
        
        preorder_index = 0
        inorder_index_map = {v: i for i, v in enumerate(inorder)}

        return list_to_tree(0, len(preorder) - 1)