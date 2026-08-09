class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(sources, ocean):
            q = deque(sources)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for x, y in directions:
                    if r+x in range(ROWS) and c+y in range(COLS) and not ocean[r+x][c+y] and heights[r+x][c+y] >= heights[r][c]:
                        q.append((r+x, c+y))


        pacific = []
        atlantic = []
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS-1, c))
        
        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS-1))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)

        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    ans.append([r, c])
        return ans