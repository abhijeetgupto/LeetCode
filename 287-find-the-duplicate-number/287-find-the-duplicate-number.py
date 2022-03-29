class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums.sort()
        last = nums[0]
        for i in range(1,len(nums)) :
            if nums[i]==last:
                return nums[i]
            last = nums[i]
        
        