from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]

        for n in nums[1:]:
            currSum = max(currSum + n, n)
            maxSum = max(currSum, maxSum)

        return maxSum

    def smarter_solution(self, nums: List[int]) -> int:
        """
        From leetcode comments
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)