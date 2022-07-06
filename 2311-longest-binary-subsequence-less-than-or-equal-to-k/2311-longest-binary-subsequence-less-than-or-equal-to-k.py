class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        if int(s,2)<=k:
            return len(s)
        
        t = bin(k)[2:]
        res = s[ : len(s) - len(t)].count("0") + len(t) -1
        if int(s[len(s)-len(t):], 2) <= k:
            res += 1
        
        return res

        
        
        
        
        
        
        