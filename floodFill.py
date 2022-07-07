#DFS solution
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        ogColor = image[sr][sc]
        def fill(i, j):
            if(i < 0 or j < 0 or i >= row or j >= col): return
            curr = image[i][j]
            #If the current element is not the same as the original start or it equals the new color, return back
            if(curr != ogColor or curr == newColor): return
            
            #Set the current element to the new color
            image[i][j] = newColor
            
            #DFS
            fill(i+1,j)
            fill(i-1,j)
            fill(i,j+1)
            fill(i,j-1)
        fill(sr,sc)
        return image