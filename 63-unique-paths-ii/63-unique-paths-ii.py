class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        memo = {}
        
        def rec(i=0, j=0) :
            
            if (i,j) in memo :
                return memo[(i,j)]
            
            if i>=n or j>=m:
                return 0
            
            if i==n-1 and j==m-1 :
                if grid[i][j]==1 :
                    return 0
                return 1
            
            if grid[i][j] == 1 :
                return 0
            
            memo[(i,j)] = rec(i+1, j) + rec(i, j+1)
            return memo[(i,j)]
        
        return rec()
            
            
            
            
            
            
            
            
    