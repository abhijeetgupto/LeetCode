class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        
        memo = {}
        def rec(i=0, k=0, star = 0) :
            
            if (i,k,star) in memo:
                return memo[(i,k,star)]
            
            if i>=n:
                return k==0
            
            if s[i] == ")" :
                if k>0:
                    memo[(i,k,star)] = rec(i+1,k-1, star)
                    return memo[(i,k,star)]
                
                elif star > 0:
                    memo[(i,k,star)] = rec(i+1,k, star-1)
                    return memo[(i,k,star)]
                
                else:
                    return False
            
            elif s[i] == "(" :
                
                memo[(i,k,star)] = rec(i+1,k+1,star)
                return memo[(i,k,star)]
        
            else:
                if k>0:
                    memo[(i,k,star)]= rec(i+1, k-1, star) or rec(i+1,k,star+1)
                    return memo[(i,k,star)]
                
                else:
                    memo[(i,k,star)] = rec(i+1,k,star+1)
                    return memo[(i,k,star)]
        return rec()
        