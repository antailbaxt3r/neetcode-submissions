class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        maxl = 0
        for r, c in enumerate(s):
            if c in hashmap and l <= hashmap[c]:
                l = hashmap[c] + 1
            hashmap[c] = r
            maxl = max(maxl, r-l+1)
        return maxl


            