from .binary_tree_tools import create_tree, TreeNode
from typing import Optional, List
from colorama import Fore, Style

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
    def inorderTraversalStack(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res

    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)

        res = []
        helper(root)
        return res

    def inorderTraversalMorris(self, root: Optional[TreeNode]) -> List[int]:
        res, curr = [], root
        
        while curr:
            if curr.left:
                pre = curr.left
                while pre.right and pre.right != curr:
                    # The rightest node of the curr.left tree (the 'pre' node) is the node, which value
                    # will be printed just before curr
                    pre = pre.right
                        
                if pre.right == None:
                    pre.right = curr
                    curr = curr.left
                else: # if pre.right == curr
                    pre.right = None
                    res.append(curr.val)
                    curr = curr.right
            else:
                res.append(curr.val)
                curr = curr.right
        
        return res
                
            