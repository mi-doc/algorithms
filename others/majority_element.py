from typing import List

# The essence of the task
TASK = """
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""


class Solution:
    
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm (smart!)
        Time: O(n), Space: O(1)
        """
        candidate, count = None, 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate