from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        answer = 0
        visited = [[False] * len(grid[0]) for  _ in range(len(grid))]
        q = deque()
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append(((r, c), 0))
                    visited[r][c] = True
        
        while q:
            (r, c), time = q.popleft()
            answer = max(time, answer)
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for x, y in directions:
                if r + x in range(m) and c + y in range(n):
                    print(r, c, r+x, c+y, m, n)
                    if not visited[r+x][c+y] and not grid[r+x][c+y] == 0:
                        visited[r+x][c+y] = True
                        grid[r+x][c+y] = 2
                        q.append(((r+x, c+y), time+1))

        for r in range(m):
            for c in range(n):
                
                if grid[r][c] == 1:
                    return -1
        
        return answer

