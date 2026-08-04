class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxl = 0
        for i, val in enumerate(nums):
            if val-1 in hashset:
                continue
            x = val
            length = 1
            while x+1 in hashset:
                x += 1
                length += 1
            maxl = max(length, maxl)
        return maxl