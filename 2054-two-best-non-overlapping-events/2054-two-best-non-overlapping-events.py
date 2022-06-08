from functools import lru_cache
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        n = len(events)
        
        @lru_cache(None)
        def rec(i=0, count=0):
            
            if i>=n or count==2:
                return 0
            
            
            a = events[i][2] + rec(bisect.bisect_left(startTime, events[i][1]+1), count+1)
            b = rec(i+1, count)
            return max(a,b)
            
            
        events.sort()
        startTime = [x for x,_,_ in events]
        return rec()
        
                    
                
                
            
        
        
        