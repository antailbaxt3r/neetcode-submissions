class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1':
                grid[r][c] = '0'
                for x, y in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
                    dfs(x, y)
            else:
                return
        
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    ans += 1
                    dfs(r, c)
        return ans