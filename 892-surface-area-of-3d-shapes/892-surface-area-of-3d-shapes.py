class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        res = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    res += 2
                    v = [(i-1,j), (i+1,j), (i,j-1), (i, j+1)]
                    for r,c in v:
                        if r in range(n) and c in range(n):
                            res += max(grid[i][j]-grid[r][c],0)
                        else:
                            res += grid[i][j]
        return res
                    
                    
        