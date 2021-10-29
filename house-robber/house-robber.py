class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <=  2 :
            return max(nums)
        
        if len(nums) == 3 :
            return max(nums[1],nums[0]+nums[2])
        
        dp = [0]*len(nums)
        dp[0],dp[1],dp[2] = nums[0],nums[1],max(nums[2]+nums[0],nums[1])
        
        
        for i in range(3, len(dp)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2], nums[i]+dp[i-3])
            
        return dp[-1]