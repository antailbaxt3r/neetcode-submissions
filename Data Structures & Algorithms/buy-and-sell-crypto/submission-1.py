class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        n = len(prices)
        maxp = 0

        while l <= r < n:
            profit = prices[r] - prices[l]
            if profit < 0:
                l += 1
            else:
                r += 1
            maxp = max(maxp, profit)
        return maxp