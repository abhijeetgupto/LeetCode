from functools import lru_cache
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        
        @lru_cache(None)
        def rec(i=0, j=0):
            
            if i==n-1:
                return triangle[i][j]
            
            else:
                return triangle[i][j] + min(rec(i+1,j), rec(i+1,j+1))
        
        return rec()
                
            
        