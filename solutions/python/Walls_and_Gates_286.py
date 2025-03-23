from collections import deque as queue
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = queue([row, col] for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == 0)
        visited = set()
        for row, col in q:
            visited.add((row, col))
        
        def isValid(row, col):
            if(row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])):
                return False
            if((row, col) in visited or grid[row][col] == -1):
                return False
            return True

        def addCell(row, col):
            if(isValid(row,col)):
                visited.add((row, col))
                q.append([row, col])

        dist = 0

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                addCell(row + 1, col)
                addCell(row - 1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)
            dist += 1
