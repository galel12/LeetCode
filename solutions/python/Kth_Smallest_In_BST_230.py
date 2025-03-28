# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def inorder(node):
            if node is None:
                return None
            
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
 
        inorder(root)
        return arr[k-1]