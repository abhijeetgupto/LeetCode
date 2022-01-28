class Solution:
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(matrix)
        m = len(matrix[0])
        
        
        dp = [[0 for _ in range(m)] for _ in range(n)]
        curr = 0
        
        for i in range(m):
            curr += matrix[0][i]
            dp[0][i] = curr

        for i in range(1, n):
            curr = 0
            for j in range(m):
                curr += matrix[i][j]
                dp[i][j] = dp[i - 1][j] + curr
        
        result = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                row1,col1,row2,col2 = max(i-k, 0),max(j-k, 0),min(n-1, i+k),min(m-1, j+k)
                res = dp[row2][col2]
                
                if row1-1>=0 and col1-1>=0:
                    res += dp[row1-1][col1-1]

                if row1-1>=0:
                    res -= dp[row1-1][col2]

                if col1-1>=0:
                    res -= dp[row2][col1-1]
                    
                result[i][j] = res
                
        return result
                
                
                