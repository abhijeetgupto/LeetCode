class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        memo = {}
        
        def rec(i, curr) :
            
            if (i,curr) in memo :
                return memo[(i,curr)]
            
            if i == n :
                if curr == target :
                    return 1
                return 0
            
            else:
                memo[(i,curr)] =  rec(i+1, curr+nums[i]) + rec(i+1, curr-nums[i])
                return memo[(i,curr)]
        
        return rec(1, nums[0]) + rec(1, -nums[0])
            

            
            
        