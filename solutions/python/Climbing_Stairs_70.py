class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1, 1 # base case - 1 way to climb 1 stair (last stair) and 1 way to climb 0 stairs (no stairs) 

        # loop n - 1 to get the nth stair (0 indexed)
        for _ in range(n - 1):
            prev1, prev2 = prev1 + prev2, prev1 # stairs can be climbed by taking 1 or 2 steps
        
        return prev1
    