class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = [[False for _ in range(n)] for _ in range(m)]

        def isValid(row, col):
            if(min(row, col) < 0 or row >= m or col >= n):
                return False
            if(visited[row][col]):
                return False
            return True
        
        def dfs(row, col):
            if(not isValid(row,col)):
                return 0
            if(row == m - 1 and col == n - 1):
                return 1

            visited[row][col] = True
            down = dfs(row + 1, col)
            right = dfs(row, col + 1)
            visited[row][col] = False
            return down + right

        res = dfs(0,0)
        return res