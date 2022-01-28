class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        curr = 0
        for i in range(m):
            curr += matrix[0][i]
            dp[0][i] = curr

        for i in range(1, n):
            curr = 0
            for j in range(m):
                curr += matrix[i][j]
                dp[i][j] = dp[i - 1][j] + curr
                
        self.dp = dp
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        res = self.dp[row2][col2]
        
        if row1-1>=0 and col1-1>=0:
            res += self.dp[row1-1][col1-1]
        
        if row1-1>=0:
            res -= self.dp[row1-1][col2]
        
        if col1-1>=0:
            res -= self.dp[row2][col1-1]
        
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)