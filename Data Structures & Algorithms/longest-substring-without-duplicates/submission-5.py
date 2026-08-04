class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        answer = 0
        for i, c in enumerate(s):
            if c in hashmap and hashmap[c] >= l:
                l = hashmap[c] + 1
            hashmap[c] = i
            answer = max(answer, i - l + 1)
        return answer
