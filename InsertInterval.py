#Runtime = O(N)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       
        if not intervals: return [newInterval]
        i = 0;
        N = len(intervals)
        
        #Set newStart, newEnd from newInterval
        newStart, newEnd = newInterval
        
        #return value
        output = []
        
        
        #Create an output of OGinterval start to values less than newStart
        while(i<N and intervals[i][0] <= newStart):
            #Appending all intervals that are less then newStart
            output.append(intervals[i])
            i+=1
       
        #If nothing added to output (b/c intervals > newstart) append newInterval to output
        if not output: output.append(newInterval)
              
        #If the last value in output is less than the new start, can add the new interval
        if output[-1][1] < newStart:
            output.append(newInterval)
        else:
            #Otherwise it's greater, set last value in output to max between newEnd and last value in output
            output[-1][1] = max(output[-1][1], newEnd)
            
        #Iterate from last interval that was not less than newStart
        while i < N:
            iStart, iEnd = intervals[i]
            #If lastvalue is less than interval 'i', append to output
            if output[-1][1] < iStart:
                output.append(intervals[i])
            #Else, lastvalue in output will be max between that value and end of interval 'i'
            else:
                output[-1][1] = max(output[-1][1], iEnd)
            i+=1
        
        return output
            