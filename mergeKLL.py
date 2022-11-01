# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Runtime: O(n * log n)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        #root points to dummy node which will be adding to
        root = res = ListNode(None)
        
        #go through the linked lists 
        for l in lists:
            while l:
                #add values to heapq
                heappush(heap, l.val)
                #next val in ll
                l = l.next
        while heap:
            #pop smallest value off heap and turn it into a node
            res.next = ListNode(heappop(heap))
            #move to node just created
            res = res.next
        return root.next