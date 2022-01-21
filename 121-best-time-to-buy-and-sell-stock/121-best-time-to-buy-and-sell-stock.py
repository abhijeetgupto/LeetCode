class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        s = prices[0]
        
        for i in range(1,len(prices)) :
            if prices[i] < s :
                s = prices[i]
            else:
                res = max(res, prices[i]-s)
        
        return res
        