# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr, length = curr.next, length + 1
        
        #edge case of removing head
        if length == n:
            return head.next
        
        #go right before node needing to be removed
        curr = head
        for i in range(1, length - n):
            curr = curr.next
        
        #skip over dead node
        curr.next = curr.next.next
        return head
        
        