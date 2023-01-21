from typing import List
from collections import Counter

# The essence of the task
TASK = """
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
"""


class Solution:
    """
    My solution! Beats 97% or leetcode submissions on speed
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)
        nums[:] = [0] * count[0] + [1] * count[1] + [2] * count[2]
    
    
    def sortColors2(self, nums: List[int]) -> None:
        """
        Faster solution from leetcode
        """
        lo = 0
        hi = len(nums) - 1
        i = 0
        while i <= hi:
            if nums[i] == 2:
                nums[i],nums[hi] = nums[hi],nums[i]
                hi -= 1
            elif nums[i] == 0:
                nums[i],nums[lo] = nums[lo],nums[i]
                lo += 1
                i += 1
            else:
                i += 1