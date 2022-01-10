class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def rec(s1, s2, s3, i, j, k, memo={}) :
            
            n1 = len(s1)
            n2 = len(s2)
            n3 = len(s3)
            
            if (i,j,k) in memo :
                return memo[(i,j,k)]
            
            if i >= n1 and j >= n2 and k >= n3 :
                return True
            
            elif i >= n1 and j <= n2 and k <= n3 :
                return s2[j:] == s3[k:]
            
            elif i >= n1 and j <= n2 and k >= n3 :
                return False
            
            elif i >= n1 and j >= n2 and k <= n3 :
                return False
            
            elif i <= n1 and j >= n2 and k >= n3 :
                return False
            
            elif i <= n1 and j >= n2 and k <= n3 :
                return s1[i:] == s3[k:]
            
            elif i <= n1 and j <= n2 and k >= n3 :
                return False
            
            else:
                
                if s1[i] == s3[k] and s2[j] == s3[k] :
                    memo[(i,j,k)] = rec(s1,s2,s3,i+1,j,k+1) or  rec(s1,s2,s3,i,j+1,k+1)
                    return memo[(i,j,k)]
                
                elif s1[i] == s3[k] :
                    memo[(i,j,k)] = rec(s1,s2,s3,i+1,j,k+1)
                    return memo[(i,j,k)]
                
                elif s2[j] == s3[k] :
                    memo[(i,j,k)] = rec(s1,s2,s3,i,j+1,k+1)
                    return memo[(i,j,k)]
                
                else:
                    return False
                
        return rec(s1,s2,s3,0,0,0)
                
            