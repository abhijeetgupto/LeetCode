from datetime import datetime

class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        
        l = list(set(timePoints))
        if len(l) < len(timePoints) :
            return 0
        
        l.sort()
        FMT = '%H:%M'
        m = math.inf
        
        for i in range(1, len(l)):
            s1 = l[i]
            s2 = l[i-1]
            x1 = (datetime.strptime(s1, FMT) - datetime.strptime(s2, FMT)).seconds//60
            x2 = 1440 -x1
            m = min(m, x1, x2)
        
        x1 = (datetime.strptime(l[0], FMT) - datetime.strptime(l[-1], FMT)).seconds//60
        x2 = 1440 -x1
        
        m = min(m,x1,x2)
        
        return m
        
            
            
        
        