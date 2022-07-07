class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(None)
        def rec(i = 0, k = 0):
            
            if k==amount:
                return 1
            
            if k>amount or i>=n :
                return 0
            
            return rec(i, k + coins[i]) + rec(i+1, k)
        
        n = len(coins)
        return rec()
        
        

        
        
                
        
        
