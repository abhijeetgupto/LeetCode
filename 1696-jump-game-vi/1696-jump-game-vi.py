import sortedcontainers

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        
        m = dp[0]
        l = sortedcontainers.SortedList()
        l.add(dp[0])
        
        for i in range(1, min(k+1,len(nums))) :
            dp[i] = nums[i] + l[-1]
            l.add(dp[i])
        
        for i in range(k+1,len(dp)) :
            l.remove(dp[i-k-1])
            dp[i] = nums[i]+l[-1]
            l.add(dp[i])
        
        return dp[-1]
            