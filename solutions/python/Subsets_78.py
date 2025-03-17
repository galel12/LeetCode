from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            include = dfs(i+1, subset + [nums[i]])
            exclude = dfs(i+1, subset)
        
        dfs(0, [])
        return res