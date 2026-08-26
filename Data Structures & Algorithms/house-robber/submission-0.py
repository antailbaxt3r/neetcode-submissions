class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {0: nums[0]}

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], (nums[i] + dp.get(i-2, 0)))
        return dp[len(nums)-1]
