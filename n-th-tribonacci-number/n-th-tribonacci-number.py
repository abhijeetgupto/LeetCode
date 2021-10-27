class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = [0,1,1]
        while len(dp) <= n :
            dp.append(dp[-1]+dp[-2]+dp[-3])
        
        return dp[n]
        