class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        l = [nums.pop(0)]
        
        for i in range(len(nums)):
            l.append(max(nums[i] , l[-1]+nums[i]))
        
        return max(l)
            
        