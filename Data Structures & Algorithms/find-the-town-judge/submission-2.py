class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        counts = [0 for _ in range(n+1)]

        for i, j in trust:
            counts[i] -= 1
            counts[j] += 1
        print(counts)
        for i in range(len(counts)):
            if counts[i] == n-1:
                return i
        return -1
            
