import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            max1 = abs(heapq.heappop(maxHeap))
            max2 = abs(heapq.heappop(maxHeap))
            if max1 > max2:
                heapq.heappush(maxHeap, -(max1 - max2))
        
        return abs(maxHeap[0]) if maxHeap else 0