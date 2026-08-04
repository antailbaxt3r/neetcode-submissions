class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            n = len(s)
            encoded += str(n) + '_' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []        
        i = 0
        answer = []
        while i < len(s):
            j = i
            while s[j] != '_':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            answer.append(s[i:j])
            i = j
        return answer

