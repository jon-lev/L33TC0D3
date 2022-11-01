class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = ((0,1), (0,-1), (1,0), (-1,0))
        
        def dfs(i,j,visited):
            if(i,j) in visited:
                return
            visited.add((i,j))
            
            for direction in directions:
                nextI, nextJ = i + direction[0], j + direction[1]
                if 0 <= nextI < rows and 0 <= nextJ < cols:
                    #little confusing, but we are trying to find a path from outer -> inner
                    if heights[nextI][nextJ] >= heights[i][j]:
                        dfs(nextI,nextJ,visited)
        
        for i in range(rows):
            #start on pacific ocean side
            dfs(i, 0, pacific)
            
            #start on atlantic ocean side
            dfs(i, cols - 1, atlantic)
            
        for j in range(cols):
            #start on pacific
            dfs(0, j, pacific)
            
            #start on atlantic
            dfs(rows - 1, j, atlantic)
        
        return list(pacific & atlantic)
            