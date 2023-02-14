from typing import List

# The essence of the task
TASK = """
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


class Solution:
    """
    O(logn) time complexity
    """
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            # x^12 == x^6 * x^6 == x^3 * x^3 * x^3 * x^3 ... 
            res = helper(x * x, n // 2)
            
            # If n is not even, like 5, we subtract 1 to make it even (4), and later
            # multiply the result once more:
            # x^4 == x^2 * x^2, but x^5 == x * x^2 * x^2
            return x * res if n % 2 else res
        
        res = helper(x, abs(n))
        # If we have negative power number, like n^-2, we would calculate everything 
        # the same way, but instead of returning n^2 we return 1 / n^2 (that's how it works)
        return res if n > 0 else 1 / res

