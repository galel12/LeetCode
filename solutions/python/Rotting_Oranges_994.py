from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) 
        rotten = deque([r, c] for r in range(ROWS) for c in range(COLS) if grid[r][c] == 2)
        
        # If there are no rotten oranges and there are no fresh oranges then return 0 
        if(len(rotten) == 0 and not any(1 in num for num in grid) and grid):
            return 0
        vis = set()
        for r,c in rotten:
            vis.add((r, c))
        
        def isValid(r, c):
            if(min(r,c) < 0 or r >= ROWS or c >= COLS):
                return False
            if((r,c) in vis or grid[r][c] == 0):
                return False
            return True

        def addCell(r, c):
            if(isValid(r, c)):
                vis.add((r, c))
                rotten.append([r, c])
        
        minute = 2
        while rotten:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                grid[r][c] = minute
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            minute += 1

        # If there are any fresh oranges left then there is no way to rot them all (return -1)
        if any(1 in num for num in grid):
                return -1  # Unreachable fresh orange found

        # Find the max minute in the grid
        maxTime = max(max(row) for row in grid)
        return maxTime - 2  # Subtract the base (2) to get total minutes elapsed
