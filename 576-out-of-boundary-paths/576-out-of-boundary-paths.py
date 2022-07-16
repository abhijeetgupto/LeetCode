class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, r: int, c: int) -> int:
        
        @lru_cache(None)
        def rec(k=0, i = r, j = c):
            
            if k > maxMove:
                return 0
            
            if i<0 or i>=m or j<0 or j>=n:
                return 1
            
            dr = [(-1,0), (1,0), (0,-1), (0,1)]
            res = 0 
            for x,y in dr:
                res += (rec(k+1, i+x, j+y)%mod)
                res %= mod
            
            return res
        
        mod = 10**9 +7
        return rec()
            