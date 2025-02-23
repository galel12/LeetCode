from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0,  len(numbers) - 1
        curSum = numbers[l] + numbers[r]

        while l < r and curSum != target:
            if (curSum > target):
                r -= 1
            else:
                l += 1
            curSum = numbers[l] + numbers[r]

        return [l + 1, r + 1] 