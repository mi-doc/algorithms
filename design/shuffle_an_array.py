from typing import List
import random


class Solution:
    """
    Given an integer array nums, design an algorithm to randomly shuffle the array.
    All permutations of the array should be equally likely as a result of the shuffling.

    Implement the Solution class:
    Solution(int[] nums) Initializes the object with the integer array nums.
    int[] reset() Resets the array to its original configuration and returns it.
    int[] shuffle() Returns a random shuffling of the array.
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.orig_ord = self.nums.copy()

    def reset(self) -> List[int]:
        self.nums[:] = self.orig_ord
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums

if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    s = Solution(nums)
    res = s.shuffle()

    print(res)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()