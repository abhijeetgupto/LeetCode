class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        
        while k>0 :
            k-=1
            last = grid[-1][-1]
            for i in range(m):
                for j in range(n) :
                    temp = grid[i][j]
                    grid[i][j] = last
                    last = temp
        return grid
            
                        
                    
                    
                    
                    
                        
                        
                    
        