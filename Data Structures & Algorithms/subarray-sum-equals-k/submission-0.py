class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = current_sum = 0
        sums = {0: 1}
        for i in nums:
            current_sum += i
            diff = current_sum - k

            ans += sums.get(diff, 0)
            sums[current_sum] = 1 + sums.get(current_sum, 0)
        return ans