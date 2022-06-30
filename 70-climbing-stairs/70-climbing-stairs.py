class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        
        def rec(i=0):
            
            if i in memo:
                return memo[i]
            
            if i>n:
                return 0
            
            if i==n:
                return 1
            
            memo[i] = rec(i+1) + rec(i+2)
            return memo[i]
        
        return rec()


        