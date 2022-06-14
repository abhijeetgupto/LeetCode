from functools import lru_cache    
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)
        
        @lru_cache(None)
        def rec(i=0, j=0):
            
            if i==n :
                return m-j
            
            elif j==m:
                return n-i
            
            if word1[i] == word2[j]:
                return rec(i+1, j+1)
            
            else:
                x = 1 + rec(i+1, j)
                y = 1 + rec(i, j+1)
                return min(x,y)
        
        return rec()
        
            