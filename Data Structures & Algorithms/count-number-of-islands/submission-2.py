class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == '1':
                grid[r][c] = '0'
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    dfs(r+x, c+y)
            else:
                return

        answer = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    answer += 1
                    dfs(r, c)
        return answer