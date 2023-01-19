from typing import List

# The essence of the task
TASK = """
Given an integer array nums of unique elements, return all possible subsets 
(the power set). The solution set must not contain duplicate subsets. 
Return the solution in any order.
"""


class Solution:
    """
    My solution!
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        self.dfs(nums, [], res)
        return list(list(r) for r in res)
    
    def dfs(self, nums, path, res):
        res.add(tuple(sorted(path)))
        if not nums:
            return res
        
        for i, n in enumerate(nums):
            # res.add(tuple(path))
            self.dfs(nums[:i]+nums[i+1:], path+[n], res)
            
