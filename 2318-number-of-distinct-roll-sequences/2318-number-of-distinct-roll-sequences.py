class Solution:
    def distinctSequences(self, n: int) -> int:
        
        @cache
        def rec(i, last, last_second):
            
            if i>=n:
                return 1
            
            count = 0
            for num in range(1, 7):
                if last!=num and num!=last_second and math.gcd(last, num)==1 :
                    count += rec(i+1, num, last)
                    count = count%m
            return count
        
        if n==1:
            return 6
        
        m = 10**9 +7
        res = 0
        for i in range(1,7):
            for j in range(1,7):
                if i!=j and math.gcd(i,j)==1:
                    res += rec(2,j,i)%m
                    
        return res%m
                    
                    
            
            
        