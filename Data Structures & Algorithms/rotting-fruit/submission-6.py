class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r, c))
    
        def rot(r, c, t):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or grid[r][c] == 0:
                return
            visited.add((r, c))
            grid[r][c] = 2
            q.append((r, c, t))

        answer = 0
        while q:
            r, c, t = q.popleft()
            answer = max(answer, t)
            rot(r+1, c, t+1)
            rot(r, c+1, t+1)
            rot(r, c-1, t+1)
            rot(r-1, c, t+1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return answer



