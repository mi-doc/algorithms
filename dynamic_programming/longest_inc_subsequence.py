from typing import List

# The essence of the task
TASK = """
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub_len = [1] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    sub_len[i] = max(sub_len[i], sub_len[j] + 1)

        return max(sub_len)
