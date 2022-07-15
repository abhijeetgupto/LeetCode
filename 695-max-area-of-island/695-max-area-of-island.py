class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(i, j):
            
            drs = [(-1,0),(1,0),(0,1),(0,-1)]
            res = 0
            for x,y in drs: 
                r,c = i+x, j+y
                if 0<=r<n and 0<=c<m and grid[r][c] == 1:
                    grid[r][c] = 0
                    res += 1+dfs(r,c)

            return res
        
        res = 0
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    res = max(res, 1+dfs(i,j))
                    
        return res
                    
                    
            
        