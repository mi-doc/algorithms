from typing import List
from colorama import Fore, Style


class Solution:
    """
    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.
    """
    def missingNumber(self, nums: List[int]) -> int:
        set_given = set(nums)
        set_range = set(range(len(nums)+1))
        return set_range.difference(set_given).pop()

    def missingNumber2(self, nums: List[int]) -> int:
        """
        O(1) space complexity and O(n) time complexity
        """
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)


def test(vals):
    s = Solution()
    for v in vals:
        res = s.missingNumber2(v[0])
        print(
            v,
            ' -> ',
            Fore.GREEN + str(res) if v[1] == res else Fore.RED + str(res)
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ([3,0,1], 2),
        ([0,1], 2),
        ([9,6,4,2,3,5,7,0,1], 8)
    ]

    test(vals)



