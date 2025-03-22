from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
        res = 0

        def isValid(row, col):
            if(row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])):
                return False
            if(visited[row][col] or grid[row][col] == 0):
                return False
            return True
        
        def DFS(row, col):
            if(not isValid(row, col)):
                return 0

            visited[row][col] = True
            up = DFS(row + 1, col)
            down = DFS(row - 1, col)
            left = DFS(row, col - 1)
            right = DFS(row, col + 1)

            return 1 + up + down + left + right

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and not visited[row][col]:
                    island_area = DFS(row, col)
                    res = max(res, island_area)
        
        return res