from typing import List


class Solution:
    #Bucket Sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqBuckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freqBuckets[cnt].append(num)
        
        res = []
        for i in range(len(freqBuckets) - 1, 0, -1):
            [res.append(num) for num in freqBuckets[i]]
            if len(res) == k:
                return res