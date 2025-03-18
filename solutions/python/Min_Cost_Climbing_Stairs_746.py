class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       
        def path(i, price):
            if i >= len(cost):
                return price
            
            path1 = path(i + 1, price + cost[i])
            path2 = path(i + 2, price + cost[i])
            return min(path1, path2)
        
        res = min(path(0,0), path(1,0))
        return res
        
