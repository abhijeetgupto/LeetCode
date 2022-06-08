from functools import lru_cache
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        n = len(profit)
        
        @lru_cache(None)
        def rec(i=0):
            
            if i>=n:
                return 0

            a = event[i][2] + rec(bisect.bisect_left(startTime, event[i][1]))
            b = rec(i+1)
            return max(a,b)
        
        event = []
        for i in range(n):
            event.append([startTime[i], endTime[i], profit[i]])
        
        event.sort()
        for i in range(n):
            startTime[i] = event[i][0]

        return rec()
        