class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def checker(k) :
            
            count = 0
            for num in time :
                count += k//num
            
            return count >= totalTrips
            
        
        
        s = 1
        e = max(time)*totalTrips
        res = e
        
        while s <= e :
            
            m = (s+e)//2
            
            if checker(m) :
                e = m-1
                res = m
                
            else:
                s = m+1
                
        return res
                