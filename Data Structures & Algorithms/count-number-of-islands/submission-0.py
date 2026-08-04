class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        count = 0

        def search (r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLUMNS or grid[r][c] == "0"):
                return

            grid[r][c] = "0"
            search(r, c+1)
            search(r, c-1)
            search(r+1, c)
            search(r-1, c)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == "1":
                    search(r, c)
                    count += 1
        return count  
        
        