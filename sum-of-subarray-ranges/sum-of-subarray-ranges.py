class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        count = 0
        for i in range(len(nums)) :
            mini = nums[i]
            maxi = nums[i]
            for j in range(i+1,len(nums)) :
                if nums[j] > maxi :
                    maxi = nums[j]
                if nums[j] < mini :
                    mini = nums[j]
                
                count += maxi-mini
                
        return count
                    
        