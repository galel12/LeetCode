import collections
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = collections.defaultdict(int)

        def isValid(r, c, prev):
            if(min(r, c) < 0 or r >= len(matrix) or c >= len(matrix[0])):
                return False
            if(matrix[r][c] <= prev):
                return False
            return True
        
        def dfs(r, c, prev):
            if(not isValid(r, c, prev)):
                return 0
            if((r, c) in memo):
                return memo[(r, c)]

            down = 1 + dfs(r + 1, c, matrix[r][c])
            up = 1 + dfs(r - 1, c, matrix[r][c])
            right =  1 + dfs(r, c + 1, matrix[r][c])
            left = 1 + dfs(r, c - 1, matrix[r][c])
            memo[(r, c)] = max(down, up, right, left)
            return memo[(r,c)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r, c, -1)
        return max(memo.values())
            

            