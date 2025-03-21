from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currReach = 0  # Maximum index we can reach so far
        goal = len(nums) - 1

        for i in range(len(nums)):
            if i > currReach:       # If we can't reach index i, return False
                return False
            currReach = max(currReach, i + nums[i])  # Update the farthest reachable index

        return currReach >= goal    # If we completed the loop, we can reach the end