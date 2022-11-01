#Runtime O(N * log k)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #heapq are like min pqs
        heap = []
        
        for (x,y) in points:
            #make dist negative so it is a maxPQ (want largest to be popped to keep smallest)
            dist = -(x*x + y*y)
            
            #heap fill with K values
            if len(heap) == k:
                heapq.heappushpop(heap, (dist,x,y))
            else:
                heapq.heappush(heap, (dist,x,y))
        
        return [(x,y) for (dist,x,y) in heap]