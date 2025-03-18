from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates.sort()

        def dfs(i, target):
            if target == 0:
                res.append(comb[:])
                return
            
            if target < 0 or i >= len(candidates):
                return
            
            comb.append(candidates[i])
            dfs(i + 1, target - candidates[i]) 

            comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, target)
        
        dfs(0, target)
        return res