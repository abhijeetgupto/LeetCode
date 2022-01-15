class Solution:
    def numDecodings(self, s: str) -> int:
        
        def rec(i,s,memo={}) :
            n = len(s)
            
            if i in memo :
                return memo[i]
            
            elif i>=n :
                return 1
            
            elif i == n-1 :
                if s[i] == "0" :
                    return 0
                else:
                    return 1
                
            elif s[i] == "0" :
                return 0

            else :
                if s[i+1] == "0" :
                    
                    if s[i] == "1" or s[i] == "2" :
                        memo[i] = rec(i+2,s)
                        return memo[i]
                    else:
                        return 0
                else:
                    
                    if (s[i] == "1") or (s[i] == "2" and s[i+1] in {"1","2","3","4","5","6"}) :
                        memo[i] = rec(i+1,s) + rec(i+2,s)
                        return memo[i]
                    else:
                        memo[i] = rec(i+1,s)
                        return memo[i]
    
        if s == "0":
            return 0
        return rec(0,s)
                

                
        
        
        