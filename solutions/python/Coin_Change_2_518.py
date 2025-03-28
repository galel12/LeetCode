from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[0 for i in range(amount + 1)] for i in range(len(coins) + 1)]
        memo[0][0] = 1

        for i in range(1, len(coins) + 1):
            for a in range(amount + 1):
                memo[i][a] += memo[i - 1][a]

                if coins[i - 1] <= a:
                    memo[i][a] += memo[i][a - coins[i - 1]]
   
        return memo[len(coins)][amount]
    