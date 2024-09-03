# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        
        root = newHead = ListNode(None)
        root.next = head
        
        for i in range(left-1):
            newHead = newHead.next
        
        newEnd = newHead.next
        
        for i in range(right-left):
            temp = newHead.next
            newHead.next = newEnd.next
            newEnd.next = newEnd.next.next
            
            newHead.next.next = temp
        
        return root.next