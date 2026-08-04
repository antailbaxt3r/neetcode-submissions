class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in s1:
            count[i] = count.get(i, 0) + 1
        w = len(s1)

        for i in range(len(s2)):
            if s2[i] in count:
                count[s2[i]] -= 1
            if i >= w and s2[i-w] in count:
                count[s2[i-w]] += 1
            if all(count[i] == 0 for i in count):
                return True
        return False
                    

