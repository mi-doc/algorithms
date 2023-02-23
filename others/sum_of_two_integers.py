from typing import List

# The essence of the task
TASK = """
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""


class Solution:
    
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff # Longest 32 bit integer
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a & mask if b > mask else a