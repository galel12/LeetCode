from collections import Counter
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counterMap = Counter(nums)
        
        for count in counterMap.values():
            if count % 2 != 0:
                return False
        
        return True
    
        