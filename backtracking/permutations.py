from typing import List

# The essence of the task
TASK = """
Given an array nums of distinct integers, 
return all the possible permutations. You can return the answer in any order.
"""


class Solution:
    """
    Solution from leetcode.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i, n in enumerate(nums):
            self.dfs(nums[:i]+nums[i+1:], path+[n], res)