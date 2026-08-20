class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxl = 0
        for i in nums:
            if i-1 not in hashset:
                length = 1
                while i+1 in hashset:
                    length += 1
                    i += 1
                maxl = max(length, maxl)
        return maxl
