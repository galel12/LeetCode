from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next
    
# def main():
#     # Input: 1->2->4, 1->3->4
#     # Output: 1->1->2->3->4->4
#     list1 = ListNode(1, ListNode(4, ListNode(5)))
#     list2 = ListNode(1, ListNode(3))
#     solution = Solution()
#     merged_list = solution.mergeTwoLists(list1, list2)
#     while merged_list:
#         print(merged_list.val, end="->")
#         merged_list = merged_list.next
#     print()
        
# # Ensuring the script runs only when executed directly
# if __name__ == "__main__":
#     main()