from typing import List

# The essence of the task
TASK = """
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered 
to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
"""


class Solution:
    """

    """
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Slow and simple iterative approach.
        """
        for i, n in enumerate(nums):
            f = nums[i-1] if i > 0 else -float('inf')
            l = nums[i+1] if i < len(nums)-1 else -float('inf')
            if n > f and n > l:
                return i
            
    def findPeakElement2(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if mid == len(nums)-1 or nums[mid] > nums[mid+1]:
                if mid == 0 or nums[mid] > nums[mid-1]:
                    return mid
                # If we're on the descendig slope: inspect the left half
                r = mid - 1 
            else:
                l = mid + 1
            
            
            