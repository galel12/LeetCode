from collections import deque as queue
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
        res = 0

        def isValid(row, col):
            if(row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])):
                return False
            if(visited[row][col] or grid[row][col] == 0):
                return False
            return True
        
        def BFS(row, col):
            q = queue()
            q.append((row, col))
            visited[row][col] = True
            area = 1

            while q:
                x, y = q.popleft()
                for dRow, dCol in directions:
                    adjx = x + dRow
                    adjy = y + dCol
                    if(isValid(adjx, adjy)):
                        q.append((adjx, adjy))
                        visited[adjx][adjy] = True
                        area += 1
            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and not visited[row][col]:
                    island_area = BFS(row, col)
                    res = max(res, island_area)
        
        return res