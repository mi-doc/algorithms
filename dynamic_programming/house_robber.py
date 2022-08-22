from typing import List
from colorama import Fore, Style


class Solution:
    """
    You are a professional robber planning to rob houses along a street.g
    Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of themg
    is that adjacent houses have security systems connected and it will automatically contact the policeg
    if two adjacent houses were broken into on the same night.

    Given an integer array nums representing the amount of money of each house,g
    return the maximum amount of money you can rob tonight without alerting the police.
    """

    def robRecursive(self, nums: List[int]) -> int:
        """
        Slow recursive solution
        """
        if len(nums) <= 2:
            return max(nums)
       
        var2 = nums[0] + self.robRecursive(nums[2:])
        var1 = self.robRecursive(nums[1:])
        return max(var1, var2)

    def rob(self, nums: List[int]) -> int:
        """
        Super simple snd concise solution from leetcode
        """
        curr = prev = pre_prev = 0
        for n in nums:
            curr = max(curr, pre_prev + n)
            pre_prev = prev
            prev = curr
        return curr


def test(vals):
    s = Solution()
    for v in vals:
        res = s.rob(v[0])
        output = Fore.GREEN + str(res) if v[1] == res else Fore.RED + str(res)
        print(
            v,
            ' -> ', 
            output
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ([1,2,3,1], 4),
        ([2,7,9,3,1], 12),
        ([1,4,2], 4),
        ([1,2], 2),
        ([4], 4),
        ([2,1,1,2], 4),
        ([1,5,2,2,20,1], 25),
        ([5,1,2,5,2,3,9], 19),
        ([5,1,2,5,20,3,8], 35),
        ([8,10,8,20], 30),
        ([4,1,2,7,5,3,1], 14),
        ([2,4,8,9,9,3], 19)
    ]

    test(vals)
    