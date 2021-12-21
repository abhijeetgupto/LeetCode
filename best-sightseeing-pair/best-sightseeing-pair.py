class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        res = 0
        m = values[0]
        for i in range(1,len(values)) :
            m -= 1
            res = max(res, values[i]+m)
            if m < values[i]:
                m = values[i]
        
        return res
            
        
        
            
                
            
        
        