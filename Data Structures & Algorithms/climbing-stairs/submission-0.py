class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {0: 0, 1: 1, 2: 2}
        for i in range(1, n+1):
            if i in dp:
                continue
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]