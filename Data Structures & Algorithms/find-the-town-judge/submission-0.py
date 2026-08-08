class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        counts = [0 for _ in range(n)]
        for j, i in trust:
            counts[i-1] += 1
            counts[j-1] -= 1
        
        for i in range(1, n+1):
            if counts[i-1] == n-1:
                return i
            
        return -1
            
