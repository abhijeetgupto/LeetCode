from sortedcontainers import SortedList

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        left_smallest = nums[0]
        right = SortedList(nums[1:])
        
        for i in range(1, len(nums)-1):
            if nums[i] > left_smallest :
                idx1 = bisect.bisect_left(right, nums[i])
                idx2 = bisect.bisect_right(right, left_smallest)
                if idx1>idx2:return True
                
            else:
                left_smallest = nums[i]
            right.remove(nums[i])
        return False
                
            
        
        
            
                
                
                
        