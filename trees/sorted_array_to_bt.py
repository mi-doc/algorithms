from typing import Optional, List
from .binary_tree_tools import TreeNode, level_order_traversal


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        sep = (len(nums) - 1) // 2
        root = TreeNode(nums[sep])
        root.left = self.sortedArrayToBST(nums[:sep])
        root.right = self.sortedArrayToBST(nums[sep + 1:])

        return root


def test(vals):
    s = Solution()
    for val in vals:
        val.sort()
        res = s.sortedArrayToBST(val)
        print(val, ' -> ', level_order_traversal(res))


if __name__ == '__main__':
    vals = [
        [1,6,2,7,3,2,0,9,4],
        [-10,-3,0,5,9],
        [5,3,3,4,5,5,4],
        [2,1,3],
        [2,1],
        [1],
        [3,4,4],
        [],
        [6,3,8,1,4,7,10,2],
        [6,3,8,1,4,7]
    ]

    test(vals)
