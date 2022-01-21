class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        s = prices[0]
        res = 0
        
        for i in range(1, len(prices)):
            if prices[i] < s :
                s = prices[i]
            elif prices[i] > s :
                res += prices[i]-s
                s = prices[i]

                
        return res
                
            
                
                
        