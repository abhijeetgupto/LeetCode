class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def fun(i,j) :
            
            while i<=j :
                if s[i] != s[j] :
                    return False
                i+=1
                j-=1
                
            return True
            
        i = 0
        j = len(s)-1
        count = 0
        
        while i <= j :
            
            if s[i] != s[j] :
                return fun(i, j-1) or fun(i+1, j)
                    
            else:
                i+=1
                j-=1
                
        return True
                
        