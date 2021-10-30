class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [None]*len(nums)
        dp[0] = 0
        j = 0 
        for i in range(len(nums)):
            for j  in range(i+1, min(len(dp),i+1+nums[i])) :
                if not dp[j] :
                    dp[j] = dp[i] + 1
                else:
                    dp[j] = min(dp[j], dp[i] + 1)
                    
        return dp[-1]
                    