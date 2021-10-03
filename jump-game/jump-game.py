class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [0]*len(nums)
        dp[0] = 1
        
        for i in range(len(nums)) :
            if dp[i] != 0 :
                for j  in range(i+1, min(len(dp),i+1+nums[i])) :
                    dp[j] = 1
            if dp[-1] == 1 :
                return True
        
        return False
            
        