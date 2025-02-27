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
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
    