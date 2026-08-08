class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r, c):
            if 0 > r or r >= ROWS or  0 > c  or c >= COLS or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            visited.add((r, c))
            p = 0
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    p += dfs(r+x, c+y)
            return p
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)