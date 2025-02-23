from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            length = 1 
            if (num - 1) not in numSet:
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest