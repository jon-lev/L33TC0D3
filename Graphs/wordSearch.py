class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #DFS Search to find word
        def dfs(i,j,index):
            #start at 0 and go to len every DFS iteration
            #if its == len(word) we found word!
            if(index == len(word)): return True
            
            #if OOB or char does not equal curr position, pop out of iteration
            if(i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[index] != board[i][j]):
                return False
            
            #get currChar
            currChar = board[i][j]
            
            #mark as visited
            board[i][j] = '#'
            
            #look through every direction
            res = dfs(i-1,j,index+1) or dfs(i+1,j,index+1) or dfs(i,j-1,index+1) or dfs(i,j+1,index+1)
            board[i][j] = currChar
            return res
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j, 0): return True
        return False
    
    