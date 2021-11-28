class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) <= 2*k :
            return [-1]*len(nums)
        
        res = [-1]*(len(nums))
        curr = 0
        for i in range(2*k + 1) :
            curr += nums[i]
        
        res[k] = curr
        for i in range(k+1,len(nums)-k) :
            curr -= nums[i-k-1]
            curr += nums[i+k]
            res[i] = curr
        
        for i in range(k, len(nums)-k) :
            res[i] = res[i]//(2*k+1)
        
        return res