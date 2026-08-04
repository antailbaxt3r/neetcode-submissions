class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for _ in range(2 * n)]
        for i, val in enumerate(nums):
            ans[i] = val
            ans[i + n] = val
        return ans