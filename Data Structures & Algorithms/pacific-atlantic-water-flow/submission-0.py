class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS, COLS = len(heights), len(heights[0])
        
        def dfs(r, c, visit, h):
            if (r, c) in visit or r not in range(len(heights)) or c not in range(len(heights[0])) or heights[r][c] < h:
                return
            visit.add((r, c))
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for x, y in directions:
                dfs(r+x, c+y, visit, heights[r][c])
        
        for c in range(len(heights[0])):
            dfs(0, c, pacific, heights[0][c])
            dfs(len(heights) - 1, c, atlantic, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
        
        answer = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    answer.append([r, c])
        return answer