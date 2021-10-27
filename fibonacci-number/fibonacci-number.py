class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0 :
            return 0
        
        dp = [0,1]
        while len(dp) < n+1 :
            dp.append(dp[-1]+dp[-2])
        
        return dp[-1]
        