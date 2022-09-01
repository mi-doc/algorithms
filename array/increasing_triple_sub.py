from typing import List
from colorama import Fore, Style


class Solution:
    """
    Given an integer array nums, return true if there exists a triple of indices (i, j, k)
    such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
    """
    def increasingTriplet(self, nums: List[int]) -> bool:
        # The "seq" dictionary has numbers as keys and the length of their sequence
        # (previous lesser numbers) as values
        seq = {}

        for n in nums:
            longest_seq = 0

            # Finding all previous numbers less then current:
            if smaller := list(filter(lambda x: x < n, seq.keys())):
                # Sort them by the lenght of the sequence (we need the longest)
                num_with_longest_seq = sorted(smaller, key=lambda x: seq[x])[-1]
                longest_seq = seq[num_with_longest_seq]

                # If longest sequence is already 2 nums long, then we
                # found the third one which is the goal
                if longest_seq == 2:
                    return True
           
            seq[n] = longest_seq + 1
        return False
       
    def increasingTriplet2(self, nums):
        """"
        Working solution from leetcode.
        Don't really get it, since indexes of nums can go in
        non-incremental order.
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

def test(vals):
    s = Solution()
    for v in vals:
        res = s.increasingTriplet(v[0])
        print(
            v,
            ' -> ',
            [Fore.RED,Fore.GREEN][v[1] == res] + str(res)
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ([1,2,3,4,5], True),
        ([5,4,3,2,1], False),
        ([2,1,5,0,4,6], True),
        ([20,100,10,12,5,13], True)
    ]

    test(vals)
