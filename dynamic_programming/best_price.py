from collections import defaultdict
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        Solution from leetcode
        """
        min_price, max_profit = float('inf'), 0

        for p in prices:
            max_profit = max(max_profit, p - min_price)
            min_price = min(min_price, p)

        return int(max_profit)
