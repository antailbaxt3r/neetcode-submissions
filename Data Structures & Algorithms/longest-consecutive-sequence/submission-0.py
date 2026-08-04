class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memory = set(nums)
        count = 0
        answer = 0
        for i in nums:
            if i - 1 not in memory:
                u = i
                count += 1
                while u+1 in memory:
                    count += 1
                    u = u+1
                answer = max(count, answer)
                count = 0
        return answer