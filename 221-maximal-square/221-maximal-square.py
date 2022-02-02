class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        flag = False
        for l in matrix :
            if "1" in  l :
                flag = True
                break
                
        if not flag :
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*cols for _ in range(rows)]
        
        for i in range(cols) :
            dp[0][i] = int(matrix[0][i])
        
        for i in range(rows) :
            dp[i][0] = int(matrix[i][0])
        
        res = 1
        
        for i in range(1,rows):
            for j in range(1,cols):
                
                if matrix[i][j] == "1" :
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
                    res = max(res, dp[i][j])
                else:
                    dp[i][j] = 0
                
        return res*res
        
        
        
        
                
        