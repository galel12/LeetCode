from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            midRow, midCol = m // COLS, m % COLS
            if target > matrix[midRow][midCol]:
                l = m + 1
            elif target < matrix[midRow][midCol]:
                r = m - 1
            else:
                return True
        return False