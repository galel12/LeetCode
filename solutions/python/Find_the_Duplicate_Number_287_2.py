from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums), curr, next
        
        # rearrange the array so that the number at index i is i + 1
        for i in range(n):
            curr = nums[i]
            next = nums[curr - 1]
            while 1 <= curr <= n and curr != next:
                nums[curr - 1] = curr
                curr = next
                
        # find the first number that is not i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return nums[i]
        return -1