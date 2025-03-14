# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if node is None:
                return 0

            maxVal = max(maxVal, node.val)
            if node.val >= maxVal:
                res = 1 + dfs(node.left, maxVal) + dfs(node.right, maxVal)
            else:
                res = dfs(node.left, maxVal) + dfs(node.right, maxVal)

            return res
    
        return dfs(root, root.val)