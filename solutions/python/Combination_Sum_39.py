from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        comb = []

        def dfs(i, target):
            if target == 0:
                res.append(comb[:])
                return

            if target < 0 or i >= len(nums):
                return

            curr = nums[i]
            comb.append(curr)
            include = dfs(i, target - curr)
  
            comb.pop()
            exclude = dfs(i + 1, target)


        dfs(0, target)
        return res