class Solution:
    
    def lengthOfLIS(self, nums : List[int]) -> int:
              
        def rec(i,memo) :
            
            if i in memo:
                return memo[i]

            else:
                m = 0
                for j in range(i+1,len(nums)) :
                    if nums[j] > nums[i] :
                        m = max(m, rec(j,memo))
                memo[i] = m+1
                return memo[i]
                        
        m = 0
        n = len(nums)
        
        memo = {}
        for i in range(n):
            if m >= n-i:
                break
            m = max(m,rec(i,memo))
            
        return m
            
            
          
                        
                