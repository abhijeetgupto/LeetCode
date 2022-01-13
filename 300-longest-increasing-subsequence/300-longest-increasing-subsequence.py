class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def rec(i,memo={}) :
            
            if i in memo:
                return memo[i]

            else:
                m = 0
                for j in range(i+1,len(nums)) :
                    if nums[j] > nums[i] :
                        m = max(m, rec(j))
                memo[i] = m+1
                return memo[i]
                        
        m = 0
        for i in range(len(nums)):
            m = max(m,rec(i))
        return m
                
            
          
                        
                