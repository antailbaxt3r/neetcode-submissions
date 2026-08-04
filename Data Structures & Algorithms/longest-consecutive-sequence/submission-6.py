class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        longest = 0
        for i in nums:
            seq = 1
            if i - 1 not in numset:
                while i + 1 in numset:
                    seq += 1
                    i += 1
                longest = max(longest, seq)
        return longest