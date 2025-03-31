from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * (len(board[0])) for _ in range(len(board))]
        
        def isValid(r, c):
            if(min(r, c) < 0 or r >= len(board) or c >= len(board[0])):
                return False
            if(visited[r][c]):
                return False
            return True
        
        def dfs(r, c, l):
            if l == len(word):
                return True
            if(not isValid(r, c)):
                return False
            if board[r][c] != word[l]:
                return False

            visited[r][c] = True
            search = ( dfs(r + 1, c, l + 1) or 
                      dfs(r - 1, c, l + 1) or 
                      dfs(r, c + 1, l + 1) or 
                      dfs(r, c - 1, l + 1) )
            visited[r][c] = False
            return search

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False