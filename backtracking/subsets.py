from typing import List

# The essence of the task
TASK = """
Given an integer array nums of unique elements, return all possible subsets 
(the power set). The solution set must not contain duplicate subsets. 
Return the solution in any order.
"""


class Solution:
    """
    My and leetcode solutions
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ My solution """
        res = set()
        self.dfs(nums, [], res)
        return list(list(r) for r in res)
    
    def dfs(self, nums, path, res):
        res.add(tuple(sorted(path)))
        if nums:
            for i, n in enumerate(nums):
                self.dfs(nums[:i]+nums[i+1:], path+[n], res)
            
    def subsets_cascading(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
    
    def subsets_backtracking(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            output.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        
        output = []
        n = len(nums)
        backtrack()
        return output