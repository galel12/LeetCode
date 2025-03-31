from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
 
        for i ,temp in enumerate(temperatures):
            # Monotonic decreasing stack
            while stack and  temp > stack[-1][0]:
                # Pop the top element from the stack
                _, stackInd = stack.pop()
                res[stackInd] = i - stackInd

            # Push the current element into the stack
            stack.append([temp, i])
        return res
            