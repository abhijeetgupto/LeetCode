import sortedcontainers

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        n = len(security)
        
        if time*2 >= n :
            return []
        
        if time==0 :
            return list(range(n))
        
        if len(set(security))==1:
            return list(range(time,n-time))
        
        l1 = sortedcontainers.SortedList(security[:time])
        l2 = sortedcontainers.SortedList(security[time+1: 2*time+1])
        
        window1 = collections.deque(reversed(security[:time]))
        window2 = security[time+1: 2*time+1]
        
        res = []
        
        if security[time] <= window2[0] and security[time] <= window1[0] and window1 == l1 and window2==l2:
            res.append(time)
            
        for i in range(time+1,n-time) :
            
            l1.remove(window1.pop())
            window1.appendleft(security[i-1])
            l1.add(security[i-1])
            
            l2.remove(window2.pop(0))
            window2.append(security[i+time])
            l2.add(security[i+time])
            
            if security[i] <= window2[0] and security[i] <= window1[0] and window1 == l1 and window2==l2:
                res.append(i)
        return res
        