class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        
        @lru_cache(None)
        def rec(i, j, k) :

            
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
                    return  rec(i+1,j,k+1) or  rec(i,j+1,k+1)
                    
                
                elif s1[i] == s3[k] :
                    return  rec(i+1,j,k+1)
                   
                
                elif s2[j] == s3[k] :
                    return rec(i,j+1,k+1)
                    
                else:
                    return False
                
        return rec(0,0,0)
                
            