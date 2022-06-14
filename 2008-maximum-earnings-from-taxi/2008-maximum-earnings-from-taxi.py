from functools import lru_cache
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        rides.sort()
        @lru_cache(None)
        def rec(i=0) :
            
            if i>=len(rides):
                return 0
            
            start, end, tip = rides[i]
            a = end-start + tip + rec(bisect.bisect_left(stops, end))
            b = rec(i+1)
            return max(a,b)
            
        stops = [i for i,_,_ in rides]
        return rec()
        