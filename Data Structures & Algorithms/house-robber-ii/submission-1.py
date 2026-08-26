class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(n):
            rob1, rob2 = 0, 0
            for i in n:
                val = max(rob1, rob2 + i)
                rob2 = rob1
                rob1 = val
            return rob1
        return max(dp(nums[1:]), dp(nums[:-1]), nums[0])

    