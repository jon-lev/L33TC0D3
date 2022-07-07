#Runtime: O(n^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Create an empty set
        checkSet = set()
        
        #Loop through all values in board
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                #Grab important values and convert to str for easier testing
                char = str(board[i][j])
                row = str(i)
                col = str(j)
                blockStr = char + "B" + str(int(i/3)) + str(int(j/3))
                
                #If the character a dot, can skip
                if(char == '.'): continue
                    
                #If the char has been seen in same row/col/block, return false
                if(char + "R" + row in checkSet 
                  or char + "C" + col in checkSet
                  or blockStr in checkSet):
                    return False
                
                #Add to set with specific formating
                checkSet.add(str(char) + "R" + str(row))
                checkSet.add(str(char) + "C" + str(col))
                checkSet.add(blockStr)
        #If never found dupes in set, return True
        return True      