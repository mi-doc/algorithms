from colorama import Fore, Style
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

def test(vals):
    s = Solution()
    for v in vals:
        res = s.smarter_solution(v[0])
        output = Fore.GREEN + str(res) if v[1] == res else Fore.RED + str(res)
        print(
            v,
            ' -> ', 
            output
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([4,-2,5,-1,2,-4,-5,2,5,-2], 8),
        ([1], 1),
        ([0], 0),
        ([-1], -1),
        ([1,-1,-2], 1),
        ([-2,-3,-1,-5], -1),
    ]

    test(vals)