class Solution(object):
    def maxProfit(self, prices: list[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        curr = prices[0]

        for p in prices:
            if p > curr:
                profit += p - curr
            curr = p

        return profit

if __name__ == '__main__':
    s = Solution()
    prices = [7,1,4,2,6,7,5,3,5]
    res = s.maxProfit(prices)
    print(res)
