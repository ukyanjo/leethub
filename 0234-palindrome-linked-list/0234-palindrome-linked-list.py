# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         listed = []
        
#         if not head:
#             return True
        
#         node = head
#         while node is not None:
#             listed.append(node.val)
#             node = node.next
            
#         for idx in range(len(listed)//2):
#             if listed[idx] != listed[-1*idx-1]:
#                 return False
            
#         return True
        # 이중 연결 리스트 구조의 데크의 경우 처음, 끝 추출이 용이해서 처음 생각한 풀이와 더 밀접함
        q = collections.deque()
    
        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
            
        return True