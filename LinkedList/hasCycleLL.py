# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Tortoise and Hare algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        #if theyre the same value, a cycle exists
        while slow is not fast:
            #reached a point of no return
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
        