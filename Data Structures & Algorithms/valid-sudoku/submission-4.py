class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = [[] for _ in range(9)]
        COLS = [[] for _ in range(9)]
        SQRS = [[[], [], []] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                else:
                    val = int(val)
                if val in ROWS[r] or val in COLS[c] or val in SQRS[r//3][c//3]:
                    print(val, r, c, '\nROWS=', ROWS, '\nCOLS=',COLS, '\nSQRS=',SQRS)
                    return False
                else:
                    ROWS[r].append(val)
                    COLS[c].append(val)
                    SQRS[r//3][c//3].append(val)
        return True