import sortedcontainers

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        curr = nums[0]
        temp = sortedcontainers.SortedList(nums[1:])
        
        for i in range(1,len(nums)) :
            if nums[i] < curr :
                curr = nums[i]
                
            elif nums[i] > curr :
                if temp[-1] > nums[i] :
                    return True
            
            temp.remove(nums[i])
            
        return False
                
        
        
        