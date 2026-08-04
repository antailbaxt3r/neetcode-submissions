class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        mini = prices[0]
        for i in prices:
            maxp = max(i - mini, maxp)
            mini = min(i, mini)
        return maxp

            