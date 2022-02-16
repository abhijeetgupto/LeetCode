class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n1 = len(s)
        n2 = len(p)
        memo  = {}
        
        def rec(i=0, j=0) :
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i >= n1 and j >= n2:
                return True
            
            elif i>=n1 and j<n2:
                for x in range(j,n2) :
                    if p[x]!='*':
                        return False
                return True
            
            elif i<n1 and j>=n2 :
                return False
            
            else:
                if s[i] == p[j] :
                    memo[(i,j)] = rec(i+1, j+1)
                    return memo[(i,j)]
                
                else:
                    if p[j] == '?':
                        memo[(i,j)] =  rec(i+1, j+1)
                        return memo[(i,j)]
                    elif p[j] == '*' :
                        memo[(i,j)] = rec(i+1,j+1) or rec(i+1,j) or rec(i,j+1)
                        return memo[(i,j)]
                    else:
                        return False
        return rec()
                
                
        