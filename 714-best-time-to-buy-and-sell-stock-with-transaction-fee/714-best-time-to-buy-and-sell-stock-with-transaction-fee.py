class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        def rec(i=0, tc=fee, s=False, memo={}) :
            
            temp = (i,s) 
            if temp in memo:
                return memo[temp]
            
            if i>=n :
                return 0

            if not s :
                memo[temp] = max(rec(i+1,tc,True)-prices[i], rec(i+1,tc,False))
            else:
                memo[temp] = max(prices[i]-tc+rec(i+1,tc,False), rec(i+1,tc,True))
                
            return memo[temp]
                    
        return rec()
        