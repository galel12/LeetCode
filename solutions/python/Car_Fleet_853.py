from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carsMap = dict(zip(position,speed))
        fleetStack = []

        for pos, mph in sorted(carsMap.items(), reverse=True):
            fleetStack.append((target - pos) / mph)
            if len(fleetStack) >= 2 and fleetStack[-1] <= fleetStack[-2]: # check if a car catches up to a fleet 
                fleetStack.pop()
        return len(fleetStack)
    
    