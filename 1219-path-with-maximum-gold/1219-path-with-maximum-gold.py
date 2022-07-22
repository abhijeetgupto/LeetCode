class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        m,n = len(grid), len(grid[0])
        
        def rec(i, j):
            
            res = temp = grid[i][j]
            k = 0
            grid[i][j] = 0
            dr = [(-1,0), (1,0), (0,-1), (0,1)]
            
            for x,y in dr:
                if 0 <= i+x < m and 0 <= j+y < n and grid[i+x][j+y] != 0 :
                    k = max(k, rec(i+x, j+y))
            
            grid[i][j] = temp
            return res+k
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    res = max(res, rec(i, j))
                    
        return res