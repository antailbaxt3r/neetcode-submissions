class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxarea = 0

        def dfs(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
                grid[r][c] = 0
                area = 1
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                for x, y in directions:
                    area += dfs(r+x, c+y)
                return area
            else:
                return 0
        
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(area, max_area)
        return max_area