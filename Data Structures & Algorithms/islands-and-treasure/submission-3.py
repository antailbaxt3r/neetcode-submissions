class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        def add(r, c):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or grid[r][c] == -1:
                return
            q.append((r, c))
            visited.add((r, c))

        d = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = d
                add(r+1, c)
                add(r-1, c)
                add(r, c+1)
                add(r, c-1)
            d += 1
