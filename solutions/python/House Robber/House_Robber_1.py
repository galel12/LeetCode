from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1 for _ in range(len(nums))]
        
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
                
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        
        res = dfs(0)
        return res

