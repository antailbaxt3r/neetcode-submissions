class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        def bs(l, r, target):
            mid = (l+r) // 2
            row = mid // COLS
            col = mid % COLS
            if l == r and matrix[row][col] != target:
                return False
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                return bs(l, mid, target)
            else:
                return bs(mid+1, r, target)
        return bs(0, ROWS*COLS - 1, target)