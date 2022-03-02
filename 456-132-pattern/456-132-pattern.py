from sortedcontainers import SortedList

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        prev = nums[0]
        temp = SortedList(nums)
        temp.remove(nums[0])
        
        for i in range(1,len(nums)):
            
            if nums[i] > prev :
                idx1 = bisect.bisect_left(temp, nums[i])
                idx2 = bisect.bisect_right(temp, prev)
                if idx2<idx1 :
                    return True
                
            else:
                prev = nums[i]
                
            temp.remove(nums[i])
                
        return False
                
                
            
        
        
            
                
                
                
        