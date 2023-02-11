from typing import List

# The essence of the task
TASK = """
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
"""


class Solution:
    
    def trailingZeroes(self, n: int) -> int:
        """
        Zeroes at the end are created by the nuber of 5s, that are in the line, 
        and number of all powers of 5:
        n//5 + n//25 + n//125 ...
        """
        power_of_5s, res = 5, 0
        while n >= power_of_5s:
            res += n // power_of_5s
            power_of_5s *= 5
        return res