class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        res = 0
        count = 1
        last = nums[0]
        for i in range(1, len(nums)):
            
            if nums[i] == last+1:
                count+=1
                last = nums[i]
            else:
                res = max(res, count)
                count = 1
                last = nums[i]
        res = max(res, count)
        return res