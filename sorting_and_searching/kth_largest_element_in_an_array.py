from typing import List

# The essence of the task
TASK = """
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.
"""


class Solution:
    """
    My solution usin quick select
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pos = self.partition(nums)
        if k > pos + 1:
            return self.findKthLargest(nums[pos+1:], k-pos-1)
        if k < pos + 1:
            return self.findKthLargest(nums[:pos], k)
        return nums[pos]
    
    def partition(self, nums):
        l = 0
        r = len(nums) - 1
        low = l
        
        while l < r:
            if nums[l] > nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
            
        nums[low], nums[r] = nums[r], nums[low]
        return low
    
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """
        Here we manipulate one initial list with 'left' and 'right' arguments
        """
        def quickSelect(l, r):
            pivot = partition(l, r)
            if k > pivot + 1:
                return quickSelect(pivot + 1, r)
            if k < pivot + 1:
                return quickSelect(l, pivot - 1)
            return nums[pivot]
            
        def partition(l, r):
            low = l
            while l < r:
                if nums[l] > nums[r]:
                    nums[l], nums[low] = nums[low], nums[l]
                    low += 1
                l += 1
            nums[low], nums[r] = nums[r], nums[low]
            return low
        
        return quickSelect(0, len(nums) -1)