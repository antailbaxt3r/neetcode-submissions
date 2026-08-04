class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashmap = {}
        maxl = 0
        for i, c in enumerate(s):
            if c in hashmap and hashmap[c] >= l:
                l = hashmap[c] + 1
            hashmap[c] = i
            maxl = max(i - l + 1, maxl)
        return maxl
