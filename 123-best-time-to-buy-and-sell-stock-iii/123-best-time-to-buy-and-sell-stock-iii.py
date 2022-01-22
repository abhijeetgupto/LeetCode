class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        def rec(i=0,count=0, s=False, memo={}) :
            
            temp = (i,s,count)
             
            if temp in memo:
                return memo[temp]
            
            if i>=n or count==2 :
                return 0

            
            if not s :
                memo[temp] = max(rec(i+1,count,True)-prices[i], rec(i+1,count,False))
            else:
                memo[temp] = max(prices[i] + rec(i+1,count+1,False), rec(i+1,count,True))
                
            return memo[temp]
        
        return rec()
        