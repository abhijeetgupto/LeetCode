class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        m = 0
        bp = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < bp :
                bp = prices[i]
            else :
                m = max(m,prices[i]-bp)
        return m
                
             
        