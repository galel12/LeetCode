from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = nums[:]

        def dfs(i):
            if i == len(nums):
                res.append(perm[:])
                return
            
            for idx in range(i ,len(nums)):
                perm[idx], perm[i] = perm[i], perm[idx]
                dfs(i + 1)
                perm[idx], perm[i] = perm[i], perm[idx]

        dfs(0)
        return res