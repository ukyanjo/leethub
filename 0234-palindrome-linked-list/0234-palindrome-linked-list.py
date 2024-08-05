# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        listed = []
        
        if not head:
            return True
        
        node = head
        while node is not None:
            listed.append(node.val)
            node = node.next
            
        for idx in range(len(listed)//2):
            if listed[idx] != listed[-1*idx-1]:
                return False
            
        return True