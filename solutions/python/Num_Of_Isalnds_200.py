from collections import deque as queue
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Direction vectors
        dRow = [ -1, 0, 1, 0]
        dCol = [ 0, 1, 0, -1]
        islands = 0
        visited = [[ False for i in range(len(grid[0]))] for i in range(len(grid))]

        def isValid(row, col):
            # If cell lies out of bounds
            if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])):
                return False
        
            # If cell is already visited or it's a water cell (0)
            if (visited[row][col] or grid[row][col] == "0"):
                return False
        
            # Otherwise
            return True
        
        def BFS(row, col):
            # Stores indices of the matrix cells
            q = queue()

            # Mark the starting cell as visited
            # and push it into the queue
            q.append((row, col))
            visited[row][col] = True
        
            # Iterate while the queue
            # is not empty
            while (len(q) > 0):
                cell = q.popleft()
                x = cell[0]
                y = cell[1]
                #q.pop()
        
                # Go to the adjacent land cells ("1")
                for i in range(4):
                    adjx = x + dRow[i]
                    adjy = y + dCol[i]
                    if (isValid(adjx, adjy)):
                        q.append((adjx, adjy))
                        visited[adjx][adjy] = True
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and not visited[row][col]:
                    BFS(row, col)
                    islands += 1
        
        return islands
