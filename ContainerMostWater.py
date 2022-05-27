#Runtime: O(N)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        maxArea = 0;
        
        #Start at both sides of array
        while left<right:
            #maxArea between diff of their indexes and minimum height between elements
            maxArea = max(maxArea, (right - left) * min(height[left], height[right]))
            
            #if left index is smaller than increase
            if(height[left] < height[right]): 
                left+=1
            else:
                right-=1
        return maxArea