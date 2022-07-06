class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n,m = len(s),len(p)
        
        
        @lru_cache(None)
        def rec(i=0, j=0):
            
            if i==n:
                if j==m:
                    return True
                
                char = False
                for x in range(j,m):
                    if char:
                        if p[x] != "*":
                            return False
                        else:
                            char = False
                    else:
                        if p[x] != "*":
                            char = True
                            
                return not char
                
            
            if j==m:
                return False
            
            if s[i] == p[j] or p[j] == ".":
                if j+1<m and p[j+1] == "*":
                    return rec(i+1,j+1) or rec(i+1,j+2) or rec(i,j+2)
                return rec(i+1, j+1)

            
            if p[j] == "*":
                if p[j-1] == ".":
                    return rec(i+1, j) or rec(i+1, j+1)
                
                elif p[j-1] == s[i]:
                    return rec(i+1, j) or rec(i+1, j+1)
            
                return False
            
            if j+1<m and p[j+1] == "*":
                
                return rec(i, j+2)
                    
            return False
        
        return rec()
            
                
                
    
        