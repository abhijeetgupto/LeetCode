class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        for i in range(n):
            x = target - nums[i]
            if x >= nums[i]:
                idx = bisect.bisect_left(nums, x)
                if idx == i:
                    if nums[idx+1] == nums[i]:
                        return [i+1,i+2]
                        
                if idx<n and nums[idx] == x :
                    return [i+1,idx+1]
        
                    
                
        