# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        odd = head 
        even = head.next #if no head.next, it'll be None
        eHead = even #keep positions
        
        while even and even.next:
            #set next of odd to two positions right (the next odd)
            odd.next = odd.next.next
            even.next = even.next.next
            
            #move two pointers to next values
            odd = odd.next
            even = even.next
        
        #set odd.next (will be at end) to point to evenHead
        #properly set up the evens and odds
        odd.next = eHead
        
        return head