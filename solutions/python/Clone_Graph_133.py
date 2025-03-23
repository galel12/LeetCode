from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone = {}
        
        def DFS(node):
            if node in clone:
                return clone[node]
            
            clone[node] = Node(node.val)
            for nei in node.neighbors:
                clone[node].neighbors.append(DFS(nei))
            return clone[node]
        
        return DFS(node)