class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        maxlength = 0
        left = 0
        for i, c in enumerate(s):
            if c in hashmap and left <= hashmap[c]:
                left = hashmap[c] + 1
            hashmap[c] = i
            maxlength = max(maxlength, i - left + 1)
        return maxlength

                
            