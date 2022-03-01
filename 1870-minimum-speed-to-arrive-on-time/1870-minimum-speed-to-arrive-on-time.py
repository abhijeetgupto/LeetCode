class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def checker(k) :
            count = 0
            for i in range(0,len(dist)-1):
                count += math.ceil(dist[i]/k)
            
            count += dist[-1]/k
            return count <= hour
                
            
        s = 1
        e = 10**9
        res = -1
        
        while s <= e :
            
            m = (s+e)//2
            if checker(m) :
                res = m
                e = m-1
            
            else:
                s = m+1
            
        return res
        