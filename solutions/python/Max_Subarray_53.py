from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, currSum = nums[0], 0
        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(maxSub, currSum)
        return maxSub
