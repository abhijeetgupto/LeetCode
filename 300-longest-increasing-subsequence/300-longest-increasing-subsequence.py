class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0]*n
        dp[0] = 1
        
        for i in range(1, n) :
            res = 0
            for j in range(i-1,-1,-1) :
                if nums[j] < nums[i] :
                    res = max(res, dp[j])
            dp[i] = res + 1
        
        return max(dp)
            
            
          
                        
                