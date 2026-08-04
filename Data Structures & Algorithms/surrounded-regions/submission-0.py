from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        q = deque()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r == 0 or c == 0 or r == ROWS-1 or c == COLS-1):
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            if board[r][c] == "O":
                board[r][c] = "T"
            for x, y in directions:
                if r + x in range(ROWS) and c + y in range(COLS) and board[r + x][c + y] == "O":
                    q.append((r + x, c + y))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

