import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Compute distances and store as [distance, x, y]
        distances = [[(x ** 2) + (y ** 2), x, y] for x,y in points]

        # Convert the list into a Min-Heap
        heapq.heapify(distances)

        # Extract the k closest points using a single heappop per iteration
        res = [heapq.heappop(distances)[1:] for _ in range(k)]

        return res