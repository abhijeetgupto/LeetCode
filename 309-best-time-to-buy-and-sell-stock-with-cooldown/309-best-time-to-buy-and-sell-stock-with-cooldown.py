class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def rec(i=0, s = None,memo={}):
            
            if (i,s) in memo :
                return memo[(i,s)]
            
            if i>=len(prices) :
                return 0
            
            else :
                if s is None :
                    memo[(i,s)] = rec(i+1,prices[i])
                    return memo[(i,s)]
                else:
                    if prices[i] > s :
                        memo[(i,s)] = max(prices[i]-s+rec(i+2,None),rec(i+1,s))
                        return memo[(i,s)]
                    else:
                        memo[(i,s)] =  max(rec(i+1, prices[i]), rec(i+1, s))
                        return memo[(i,s)]
        return rec()
        
        