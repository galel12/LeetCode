from functools import lru_cache
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)

        def dfs(i, currSum):
            if i == len(nums):
                return 1 if currSum == target else 0

            # try adding and subtracting nums[i]
            return dfs(i + 1, currSum + nums[i]) + dfs(i + 1, currSum - nums[i])

        return dfs(0, 0)
