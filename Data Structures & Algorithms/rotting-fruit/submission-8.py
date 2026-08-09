class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r, c))
        
        def add(r, c, t):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or grid[r][c] == 0:
                return
            q.append((r, c, t))
            grid[r][c] = 2
            visited.add((r, c))

        while q:
            r, c, t = q.popleft()
            time = max(time, t)
            add(r+1, c, t+1)
            add(r-1, c, t+1)
            add(r, c+1, t+1)
            add(r, c-1, t+1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return time