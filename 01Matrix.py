class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        numRow = len(mat)
        numCol = len(mat[0])
        
        queue = deque([])
        
        #Loop through all elements of matrix
        for row in range(numRow):
            for col in range(numCol):
                #If the element is already 0, keep it as 0 and append location to queue which will look through
                if mat[row][col] == 0:
                    queue.append((row,col))
                else:
                    #Set to -1 to show that it has to be processed
                    mat[row][col] == -1
        
        #Interesting DIR trick to check all directions
        #1st: nxtCol, 2nd: nxtRow, 3rd: prevCol, 4th: prevRow
        DIR = [0, 1, 0, -1, 0]
        while queue:
            #Get the unprocessed elements
            nR, nC = queue.popleft()
            for i in range(4):
                #Direction trick
                newRow = nR + DIR[i]
                newCol = nC + DIR[i+1]
                #Check if its OOB or an already processed position
                if newRow < 0 or newRow >= numRow or newCol < 0 or newCol >= numCol or mat[newRow][newCol] != -1: continue
                # +1 will increase distance, if a 1 is on an island (surrounded by other 1s) it'll increase how it's expected
                mat[newRow][newCol] = mat[nR][nC] + 1
                #Append the mat spot which was updated
                queue.append((newRow, newCol))
                             
        return mat