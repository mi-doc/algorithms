from typing import List

# The essence of the task
TASK = """
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    """

    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        My solution using binary search: O(logn)
        """
        l, r = 0, len(nums) - 1
        start = True # At first we will find the beginning of the range
        res = [-1, -1]
        first_encounter = 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                # We found target, now we need to find the beginning
                # and the end of the range:
                if not first_encounter:
                    # We need to remeber the mid and right indexes
                    # to use them after we found the start and then search
                    # for the end.
                    first_encounter = (mid, r)
                if start:
                    if mid == 0 or nums[mid - 1] != target:
                        res[0] = mid
                        start = False
                        l, r = first_encounter
                    else:
                        r = mid - 1
                else:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        res[1] = mid
                        break # We are done
                    else:
                        l = mid + 1
        return res
    
    
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        """
        Proper concise solutioin.
        """
        def binarySearch(leftBias):
            i = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    i = mid
                    if leftBias:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i
        
        # Calculate indexes for left and right borders of the range
        return [binarySearch(True), binarySearch(False)]
        