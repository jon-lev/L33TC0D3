#Runtime: O(H*W)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])
        
        top = 0
        left = 0
        right = width - 1
        bottom = height - 1
        
        res = []
        while left <= right and top <= bottom:
            
            #top left -> top right
            for col in range(left, right+1):
                res.append(matrix[top][col])
            top += 1   
            
            #top right -> bottom right
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right-=1
            
            #bottom right -> bottom left
            for col in range(right, left-1, -1):
                res.append(matrix[bottom][col])
            bottom-=1
            
            #bottom left -> top left
            for row in range(bottom, top-1, -1):
                res.append(matrix[row][left])
            left+=1
            
        #ignore the rest, just return height * width matrix
        return res[:height * width]