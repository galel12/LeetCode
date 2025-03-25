
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target =  sum(nums) // 2
        memo = [[False for _ in range(target + 1)] for _ in range(len(nums))]

        def dfs(i, target):
            if target == 0:
                return True
            if i >= len(nums) or target < 0:
                return False
            if memo[i][target]:
                return memo[i][target]

            memo[i][target] = (dfs(i + 1, target) or dfs(i + 1, target - nums[i]))
            return memo[i][target]
        
        res = dfs(0, target)
        return res