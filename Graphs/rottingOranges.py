#O(n*m)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        if not grid:
            return -1
        
        fresh = 0
        rotten = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        minutes = 0
        
        while rotten and fresh > 0:
            minutes += 1
            #for loop to go through all current rotten oranges
            for i in range(len(rotten)):
                nR, nC = rotten.popleft()
                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dx, dy in directions:
                    nxtRow = nR + dx
                    nxtCol = nC + dy

                    #skip if OOB
                    if nxtRow < 0 or nxtRow >= rows or nxtCol < 0 or nxtCol >= cols:
                        continue

                    newSpot = grid[nxtRow][nxtCol]

                    #if empty cell or already rotted orange, skip
                    if newSpot == 0 or newSpot == 2:
                        continue

                    #otherwise this spot is a good orange and will rot
                    fresh -= 1
                    grid[nxtRow][nxtCol] = 2

                    #add new rotten spot to queue
                    rotten.append((nxtRow,nxtCol))
        
        if fresh == 0:
            return minutes
        else:
            return -1