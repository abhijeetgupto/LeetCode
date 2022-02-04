class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n==2 :
            return 1
        
        if n==3 :
            return 2
        
        if n%3 == 0 :
            c = n//3
            return 3**c
        
        if n%3 == 1 :
            c = n//3
            return (3**(c-1))*(4)
        
        if n%3 == 2 :
            c = n//3
            return (3**c)*(2)