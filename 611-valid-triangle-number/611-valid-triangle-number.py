class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        if len(nums)<3:
            return 0
        
        nums.sort()
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x = nums[i] + nums[j]
                idx = bisect.bisect_left(nums, x)
                if idx>j:
                    count += (idx-j-1)
                
        return count
        