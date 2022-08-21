from collections import defaultdict
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        The solution I came up with
        """
        if not prices:
            return 0

        profits = defaultdict(int)
        curr_index = 0
        for i, p in enumerate(prices):
            diff = p - prices[curr_index]
            if diff > profits[curr_index]:
                profits[curr_index] = diff
            elif diff < 0:
                curr_index = i

        # Sorting and returning the highest profit:
        # [(1, 3), (3,6), (5,4)] -> (3, 6) -> 6
        return sorted(profits.items(), key=lambda x: x[1])[-1][1]

    def smarter_solution(self, prices: List[int]) -> int:
        """
        Beteer and simplier solution from leetcode
        """
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit

def test(vals):
    s = Solution()
    for v in vals:
        # res = s.maxProfit(v[0])
        res = s.smarter_solution(v[0])
        print(v,' -> ', v[1] == res, ' -> ', res)

if __name__ == '__main__':
    vals = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([3,4,2,6,2,8,7], 6),
        ([1,1], 0),
        ([1], 0),
        ([1,2], 1),
        ([3,5,7,2,5], 4),
        ([], 0)
    ]

    test(vals)