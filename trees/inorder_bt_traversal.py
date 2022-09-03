from binary_tree_tools import create_tree, TreeNode
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


def test(vals):
    s = Solution()
    for v in vals:
        head = create_tree(v[0])
        res = s.inorderTraversalStack(head)
        print(
            v,
            ' -> ',
            [Fore.RED,Fore.GREEN][v[1] == res] + str(res)
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ([1, None, 2, 3], [1,3,2]),
        ([1], [1]),
        ([], [])
    ]

    test(vals) 