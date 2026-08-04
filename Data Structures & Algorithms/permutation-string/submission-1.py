class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = {}
        for i in s1:
            counts[i] = counts.get(i, 0) + 1
        
        for i, c in enumerate(s2):
            if c in counts:
                tempcounts = counts.copy()
                l = i
                while l < len(s2) and s2[l] in tempcounts and tempcounts[s2[l]] > 0:
                    tempcounts[s2[l]] -= 1
                    l += 1
                x = sum(tempcounts.values())
                if x == 0:
                    return True
        return False
                    

