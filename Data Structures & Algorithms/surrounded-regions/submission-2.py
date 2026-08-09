class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS-1] or c in [0, COLS-1]):
                    q.append((r, c))
        
        while q:
            r, c = q.popleft()
            if r in range(ROWS) and c in range(COLS) and board[r][c] == "O":
                board[r][c] = "S"
                for x, y in directions:
                    q.append((r+x, c+y))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
        
