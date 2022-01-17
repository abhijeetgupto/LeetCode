class Solution:
    def rob(self, houses: List[int]) -> int:
        
        def rec(i,nums,memo) :
            
            if i in memo :
                return memo[i]
            
            if i >= len(nums) :
                return 0
            
            else:
                memo[i] = max(nums[i]+rec(i+2,nums,memo), rec(i+1,nums,memo))
                return memo[i]
                
        return max(houses[0]+rec(0,houses[2:len(houses)-1],{}), rec(0,houses[1:],{}))
                    
        
        
        
        