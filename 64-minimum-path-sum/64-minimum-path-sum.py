class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        #Recursive
        memo = {}
        def rec(i=0,j=0):
            
            if (i,j) in memo :
                return memo[(i,j)]
            
            if i==n-1 and j==m-1 :
                return grid[i][j]
            
            if i>=n or j>=m :
                return math.inf
            
            memo[(i,j)] = grid[i][j] + min(rec(i+1,j), rec(i,j+1))
            return memo[(i,j)]
        
        return rec()
    
        #Iterative 
        