# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (list1 is None) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
            
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
            
        print(list1)
        return list1
        
            