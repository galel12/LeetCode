from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(i, target):
            if target == 0:
                return 0  # Found a valid combination
            
            if i >= len(coins) or target < 0:
                return float('inf')  # Invalid path
            
            # Include the current coin
            include = 1 + dfs(i, target - coins[i])

            # Exclude the current coin and move to the next
            exclude = dfs(i + 1, target)

            return min(include, exclude)  # Find minimum number of coins

        result = dfs(0, amount)
        return result if result != float('inf') else -1  # If no valid solution, return -1