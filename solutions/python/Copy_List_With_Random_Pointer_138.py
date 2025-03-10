from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        # Create a new node for each node in the original list
        # and insert it in between the original nodes
        # e.g. next list: 1 -> 2 -> 3 -> 4
        # becomes: 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> 4 -> 4'
        curr = head
        while curr:
            l2 = Node(curr.val)
            l2.next = curr.next
            curr.next = l2
            curr = l2.next
        
        newHead = head.next # head of the new list

        # Set the random pointers of the new nodes
        # e.g. if 1.random -> 3, then 1'.random -> 3'
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next # curr.random.next is the new random node
            curr = curr.next.next # move to the next original node (skip the new node)
        
        # Separate the new list from the original list
        # e.g. 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> 4 -> 4'
        # becomes: 1 -> 2 -> 3 -> 4 and 1' -> 2' -> 3' -> 4'
        curr = head
        while curr:
            l2 = curr.next
            curr.next = l2.next
            if l2.next:
                l2.next = l2.next.next
            curr = curr.next

        return newHead
