class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            #oob check or not a 1 check
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1': 
                return
            #setting to # will avoid double counting 1s
            grid[i][j] = '#'
            
            #check around in other directions
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
            
        count = 0
        
        #empty grid
        if not grid: return 0
        
        #loop through the whole matrix
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #once find a 1, start dfs
                if grid[i][j] == '1':
                    dfs(i,j)
                    #increase island count
                    count = count + 1
        
        return count
    #O(row * cols)