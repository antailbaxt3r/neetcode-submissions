class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == ".":
                    continue
                if n in rows[r] or n in cols[c] or n in sqrs[r // 3, c // 3]:
                    return False
                cols[c].add(n)
                rows[r].add(n)
                sqrs[r // 3, c // 3].add(n)
        return True
