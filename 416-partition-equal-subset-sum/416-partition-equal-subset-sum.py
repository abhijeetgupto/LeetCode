class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def rec(i, k, memo={}) :
            
            if (i,k) in memo:
                return memo[(i,k)]
            
            if k<0:
                return False
            
            if k==0 :
                return True
            
            if i>=len(nums):
                return False
            
            else:
                memo[(i,k)] = rec(i+1, k-nums[i]) or rec(i+1, k)
                return memo[(i,k)]
            
        s = sum(nums)
        if s%2 != 0 :
            return False
        
        target = s//2
        return rec(0,target)
        
        
            
            
        
        
        