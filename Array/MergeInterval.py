#Runtime = O(N lg N)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        #Edge case
        if(len(intervals) == 1): return intervals
        
        i=1
        while i < (len(intervals)):
            #If previous end >= current end
            if(intervals[i-1][-1] >= intervals[i][0]):
                #Set previous end to max between both ends
                intervals[i-1][-1] = max(intervals[i-1][-1], intervals[i][-1])
                #Delete interval
                del intervals[i]
            else:
                i+=1
        return intervals