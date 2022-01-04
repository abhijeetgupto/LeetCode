class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
#         #iterative
        
#         dp = [0]*(amount+1)
#         for i in range(1, len(dp)) :
#             m = math.inf
#             for amt in coins :
#                 if i-amt >= 0 and dp[i-amt] >= 0 :
#                     m = min(m,dp[i-amt])
#             if m != math.inf : 
#                 dp[i] = 1+m
#             else:
#                 dp[i] = -1
#         return dp[-1]
        
        
        #recursive
        
        def rec(arr, target,memo={}, depth = 0) :
            
            if target in memo :
                return memo[target]
            
            elif target == 0 :
                return 0
            
            elif target < 0:
                return -1
            
            else:
                m = math.inf
                for num in arr :
                    x = rec(arr,target-num,memo)
                    if x >= 0 :
                        m = min(m,x)
                        
                if m!=math.inf :
                    memo[target] = 1+m
                    
                else:
                    memo[target] = -1
                    
                return memo[target]
            
        return rec(coins, amount)
                    
                    
                        
                