class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsMap = {} # val:index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in numsMap:
                return [numsMap[diff], index] # return the correct indexes 
                
            numsMap[num] = index # update the hashmap