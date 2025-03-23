from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def isValid(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS):
                return False
            if(board[r][c] != "O"):
                return False
            return True
        
        def notSurrounded(r, c):
            if(not isValid(r, c)):
                return
            board[r][c] = "T"
            notSurrounded(r + 1, c)
            notSurrounded(r - 1, c)
            notSurrounded(r, c + 1)
            notSurrounded(r, c - 1)
        
        for r in range(ROWS):
            if board[r][0] == "O":
                notSurrounded(r, 0)
            if board[r][COLS - 1] == "O":
                notSurrounded(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                notSurrounded(0, c)
            if board[ROWS - 1][c] == "O":
                notSurrounded(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"