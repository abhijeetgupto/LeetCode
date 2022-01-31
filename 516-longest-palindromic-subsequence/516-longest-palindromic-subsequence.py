class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        memo = {}
        
        def rec(i=0,j=n-1) :
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i==j :
                return 1
            
            if i>j :
                return 0
            
            if s[i]==s[j] :
                memo[(i,j)] = 2 + rec(i+1, j-1)
            
            else:
                memo[(i,j)] = max(rec(i+1,j), rec(i,j-1))
            
            return memo[(i,j)]
        
        return rec()
            
            
        