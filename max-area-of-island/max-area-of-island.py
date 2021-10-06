class Solution:
    def bfs(self,r,c,grid) :
        count = 0
        queue = [(r,c)]
        while queue :
            row,col = queue.pop(0)
            if 0<=row<len(grid) and 0<=col<len(grid[0]) and grid[row][col]==1:
                count += 1
                grid[row][col] = 0
                queue.append((row-1,col))
                queue.append((row+1,col))
                queue.append((row,col-1))
                queue.append((row,col+1))
        return count      
          
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        island = []
        for r in range(len(grid)) :
            for c in range(len(grid[r])) :
                if grid[r][c]==1:
                    island.append(self.bfs(r,c,grid))
        
        try:
            return max(island)
        except:
            return 0
                    
                    
        
        