class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [0]*(amount+1)
        for i in range(1, len(dp)) :
            m = math.inf
            for amt in coins :
                if i-amt >= 0 and dp[i-amt] >= 0 :
                    m = min(m,dp[i-amt])
            if m != math.inf : 
                dp[i] = 1+m
            else:
                dp[i] = -1
        return dp[-1]
        

#         def rec(arr, target,memo={}, depth = 0) :
            
#             if target in memo :
#                 return memo[target]
            
#             elif target == 0 :
#                 return 1
            
#             elif target < 0:
#                 return 0
            
#             else:
#                 count = 0
#                 for num in arr :
#                     if rec(arr,target-num,memo) != 0 :
#                         count += 1
#                 memo[target] = count
#                 return memo[target]
            
#         return rec(coins, amount)
                    
                    
                        
                