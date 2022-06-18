from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def rec(i=0, s = None):
            
            if i>=len(prices) :
                return 0
            
            else :
                if s is None :
                    return rec(i+1,prices[i])
                    
                else:
                    if prices[i] > s :
                        return  max(prices[i]-s+rec(i+2,None), rec(i+1,s))
                        
                    else:
                        return  rec(i+1, prices[i])
                        
                    
                    
        return rec()
        
        