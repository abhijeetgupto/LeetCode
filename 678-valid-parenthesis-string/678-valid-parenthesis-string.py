class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        
        def rec(i=0, k=0, star = 0) :
            
            if i>=n:
                return k==0
            
            if s[i] == ")" :
                if k>0:
                    return rec(i+1,k-1, star)
                
                elif star > 0:
                    return rec(i+1,k, star-1)
                
                else:
                    return False
            
            elif s[i] == "(" :
                
                return rec(i+1,k+1,star)
        
            else:
                if k>0:
                    return rec(i+1, k-1, star) or rec(i+1,k,star+1)
                
                else:
                    return rec(i+1,k,star+1)
        return rec()
        