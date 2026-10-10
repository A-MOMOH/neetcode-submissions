class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        max_profit = 0
        l = 0

        for r in range(1, n):
            if prices[r]  < prices[l]and l < r:
                l = r

            max_profit = max(max_profit, prices[r] - prices[l])

        return max_profit
        