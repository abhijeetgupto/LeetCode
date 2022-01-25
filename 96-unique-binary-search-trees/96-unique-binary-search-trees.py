class Solution:
    def numTrees(self, n: int) -> int:
        
        #this question is based on standard catalan numbers's formula
        #remember this series 1,1,2,5,14,42.....
        
        dp = [0]*((2*n)+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,len(dp)):
            dp[i] = dp[i-1]*i
        
        x = (dp[2*n])//(dp[n]*dp[n+1])
        return x
        