class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l = 0
        answer = 0
        count = {}

        for r, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            maxf = max(maxf, count[c])

            while r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            answer = max(r-l+1, answer)
        return answer