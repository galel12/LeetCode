class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def isValid(row, col):
            if(min(row, col) < 0 or row >= m or col >= n):
                return False
            return True
        
        def dfs(row, col):
            if(row == m - 1 and col == n - 1):
                return 1
            if(not isValid(row,col)):
                return 0
            if(memo[row][col] != -1):
                return memo[row][col]

            down = dfs(row + 1, col)
            right = dfs(row, col + 1)
            memo[row][col] = down + right
            return memo[row][col]

        res = dfs(0,0)
        return res