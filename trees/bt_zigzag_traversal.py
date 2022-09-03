from binary_tree_tools import create_tree, TreeNode
from typing import Optional, List
from colorama import Fore, Style
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # We are using stack, since we add a level info with the node and it
        # doesn't really matter in wich order we will prcess them
        stack = [(root, 0)] # Node and level in the stack
        res = []
        while stack:
            node, level = stack.pop()

            if level >= len(res):
                res.append([])

            if level % 2:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)

            stack.extend(
                (n, level + 1)
                for n in (node.left, node.right)
                if n
            )
        return res
    
    def zigzagLevelOrder2(self, root):
        """
        From leetcode
        """
        if not root:
            return []
        queue = deque([root])
        result, direction = [], 1
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(filter(bool, (node.left, node.right)))
            result.append(level[::direction])
            direction = -direction
        return result


def test(vals):
    s = Solution()
    for v in vals:
        head = create_tree(v[0])
        res = s.zigzagLevelOrder2(head)
        print(
            v,
            ' -> ',
            [Fore.RED,Fore.GREEN][v[1] == res] + str(res)
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ([3,9,20,None,None,15,7], [[3],[20,9],[15,7]]),
        ([1], [[1]]),
        ([], []),
        ([1,2,3,4,5], [[1],[3,2],[4,5]]),
        ([1,2,3,4,None,None,5], [[1],[3,2],[4,5]])
    ]

    test(vals) 