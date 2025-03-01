from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd's Tortoise and Hare (Cycle Detection)
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = fast = nums[0]
        while True:
            slow = nums[slow]       # Move 1 step
            fast = nums[nums[fast]] # Move 2 steps
            if slow == fast:        # Cycle detected
                break
        fast = nums[0]              # reset fast to the start to find the start of the cycle
        while slow != fast:
            slow = nums[slow]       # Move 1 step
            fast = nums[fast]       # Move 1 step
        return slow                 # slow is the start of the cycle (duplicate number)
    