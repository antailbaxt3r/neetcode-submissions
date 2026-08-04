class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == 'O':
                    q.append((r, c))
        
        while q:
            r, c = q.popleft()
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != 'O':
                continue
            board[r][c] = 'T'
            for x, y in [[0,1], [1, 0],[-1, 0],[0, -1]]:
                q.append((r+x, c+y))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'