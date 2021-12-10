class Solution:
    def numTilings(self, n: int) -> int:
        
        if n==1:
            return 1
        if n==2 :
            return 2
        
        dp = [1,2,5]
        while len(dp) < n :
            dp.append((2*dp[-1]) + (dp[-3]))
        return dp[-1]%(10**9 + 7)
            
        