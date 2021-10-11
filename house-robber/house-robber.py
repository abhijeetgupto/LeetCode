class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        if len(nums)==2:
            return max(nums)
        
        if len(nums) == 3 :
            return max(nums[1],nums[0]+nums[2])
        
        dp = [0]*len(nums)
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2,len(nums)):
            try :
                dp[i] = max(nums[i]+dp[i-2],dp[i-1],nums[i]+dp[i-3])
            except:
                 dp[i] = max(nums[i]+dp[i-2],dp[i-1],nums[i])
                
        return dp[-1]