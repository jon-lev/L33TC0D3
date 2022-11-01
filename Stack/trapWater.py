#Iterate "bar by bar" to determine max amount of water stored at each location
class Solution:
    def trap(self, height: List[int]) -> int:
        #too small to store water
        if len(height) <=2: return 0
        
        n = len(height)
        maxLeft, maxRight = height[0], height[-1]
        
        left = 1
        right = n - 2
        
        ans = 0
        
        while left <= right:
            if maxLeft < maxRight:   #if the water level is limited by the left value
                if height[left] > maxLeft:   #no water can be trapped here, new max
                    maxLeft = height[left]
                else:                               #can trap water here
                    ans += maxLeft - height[left]
                left += 1
           
            else:  #water is based on right side (right bar is smaller)
                if height[right] > maxRight:  #no water can be trapped here, new max
                    maxRight = height[right]
                else:
                    ans += maxRight - height[right]
                right -=1
                
        return ans
                
                
                