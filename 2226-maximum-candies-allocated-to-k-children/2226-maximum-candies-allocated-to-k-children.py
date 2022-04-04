class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def checker(c) :
            
            count = 0
            for pile in candies :
                count += pile//c
            
            return count>=k
        
        
        s = 1
        e = sum(candies)//k
        
        res = 0
        
        while s<=e :
            
            m = (s+e)//2
            
            if checker(m) :
                res = m
                s = m+1
            else:
                e = m-1
        return res
                
            