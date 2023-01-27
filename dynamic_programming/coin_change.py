from typing import List
from functools import lru_cache

# The essence of the task
TASK = """
ou are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
"""


class Solution:
    """
    Dynamic programming - Bottom up
    Time complexity : O(S*n)
    Space complexity : O(S) where S is the amount to change
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * (amount)

        for c in coins:
            for i in range(c, amount + 1):
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """
        Dynamic programming - Top down
        Time complexity : O(S*n)
        Space complexity : O(S) where S is the amount to change
        """
        
        @lru_cache
        def dfs(rem):
            if rem < 0: return -1
            if rem == 0: return 0
            
            min_coast = float('inf')
            for c in coins:
                res = dfs(rem - c)
                if res != -1:
                    min_coast = min(min_coast, res + 1)
            return min_coast if min_coast != float('inf') else -1
                
        return dfs(amount)

