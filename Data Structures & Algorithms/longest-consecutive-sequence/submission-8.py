class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for i in nums:
            length = 1
            if i-1 not in hashset:
                while i+1 in hashset:
                    length += 1
                    i += 1
            longest = max(longest, length)
        return longest
