class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        #Recursive............
#         memo = {}
#         def rec(i=0,j=0):
            
#             if (i,j) in memo :
#                 return memo[(i,j)]
            
#             if i==n-1 and j==m-1 :
#                 return grid[i][j]
            
#             if i>=n or j>=m :
#                 return math.inf
            
#             memo[(i,j)] = grid[i][j] + min(rec(i+1,j), rec(i,j+1))
#             return memo[(i,j)]
        
#         return rec()
    
        #Iterative ...........
        dp = [[0]*m for _ in range(n)]
        curr = 0
        for i in range(m) :
            curr += grid[0][i]
            dp[0][i] = curr
            
        curr = 0
        for i in range(n) :
            curr += grid[i][0]
            dp[i][0] = curr

        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[n-1][m-1]
                
        