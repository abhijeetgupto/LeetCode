class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        def rec(i=0, j=0) :
            
            if (i,j) in memo :
                return memo[(i,j)]
            
            if i==m-1 and j==n-1 :
                return 1
            
            if i>=m or j>=n :
                return 0
            
            else:
                memo[(i,j)] = rec(i, j+1) + rec(i+1, j)
                return memo[(i,j)]
        return rec()
        
        
#         if m==n==1:
#             return 1
        
#         dp = [[1]*m]*n
#         for row in range(1,n):
#             for col in range(1,m):
#                 dp[row][col] = dp[row-1][col] + dp[row][col-1]
#         return dp[-1][-1]
        