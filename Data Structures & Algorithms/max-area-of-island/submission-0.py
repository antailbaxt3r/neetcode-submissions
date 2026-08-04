class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        max_area = 0

        def search (r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLUMNS or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            return 1 + search(r, c+1) + search(r, c-1) + search(r+1, c) + search(r-1, c)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    n = search(r, c)
                    max_area = max(n, max_area)
        return max_area  