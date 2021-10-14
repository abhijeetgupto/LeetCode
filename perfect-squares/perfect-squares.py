class Solution:
    def numSquares(self, n: int) -> int:
   
        square = [1,4]
        dp = [1,2,3,1]
        
        if n<=4 :
            return dp[n-1]
        
        for i in range(5,n+1):
            if int(i**0.5) == i**0.5 :
                dp.append(1)
                square.append(i)
            else:
                m = math.inf
                for num in square :
                    m = min(m,dp[i-1-num])
                dp.append(m+1)
        
        return dp[-1]
            
            
        