class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        ans = ""
        i = 0
        while i < min(n1, n2):
            ans = ans + (word1[i] + word2[i])
            i += 1

        ans = ans + (word1[i:] + word2[i:])
        return ans