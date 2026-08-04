class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        answer = 0
        l = 0
        count = {}

        for i, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            maxf = max(maxf, count[c])

            while i - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            answer = max(answer, i - l + 1)
        return answer