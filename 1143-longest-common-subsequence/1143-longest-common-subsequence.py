class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1)
        m = len(text2)
        memo = {} 
        
        def rec(i=0,j=0) :
            
            if i>=n or j>=m :
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            else:
                if text1[i] == text2[j] :
                    memo[(i,j)] = 1 + rec(i+1,j+1)
                
                else:
                    memo[(i,j)] = max(rec(i+1,j), rec(i,j+1))
            return memo[(i,j)]
        
        return rec()
