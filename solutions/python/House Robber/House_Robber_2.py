from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
            
        def maxRob(nums):
            memo = [nums[0], max(nums[0], nums[1])]
            memo.extend([0 for _ in range(2, len(nums))])

            for i in range(2, len(nums)):
                memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])

            return memo[len(nums) - 1]
        
        ans = max(maxRob(nums[1:]), maxRob(nums[:-1]))
        return ans
