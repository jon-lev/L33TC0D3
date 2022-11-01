class Solution:
    #idea of monostack: stack in increasing order
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        
        # +[0] accounts for last height and allows for comparison to end
        for i, h in enumerate(heights + [0]): 
            #while the previous height is greater than current height, potential for greater area
            while stack and heights[stack[-1]] >= h:
                #get previous height
                H = heights[stack.pop()]
                #if stack empty, all prev bars are bigger so width will be own index
                W = i
                if stack:
                    #otherwise, width = curr index - distance from left boundary (in stack after popping for height)
                    W = i - stack[-1] - 1
                ans = max(ans, H * W)
            #if current bar is larger than rest of stack, add its index to top of stack
            stack.append(i)
        return ans
    
    