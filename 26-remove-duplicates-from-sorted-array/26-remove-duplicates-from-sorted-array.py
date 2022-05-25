class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        idx = 1
        last = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] != last :
                last = nums[i]
                nums[idx] = last
                idx += 1
                
        return idx
        