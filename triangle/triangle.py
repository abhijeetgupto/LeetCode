class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = copy.deepcopy(triangle)
        
        for i in range(1, len(dp)):
            dp[i][0] += dp[i-1][0]
            dp[i][-1] += dp[i-1][-1]

        
        for i in range(2,len(dp)):
            for j in range(1,len(dp[i])-1):
                dp[i][j] += min(dp[i-1][j-1], dp[i-1][j])
        
        return min(dp[-1])
        