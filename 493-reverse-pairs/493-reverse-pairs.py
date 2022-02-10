import sortedcontainers
import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        temp = sortedcontainers.SortedList([])
        count = 0
        
        for i in range(len(nums)) :
            
            count += len(temp)-bisect.bisect_right(temp, 2*nums[i])
            temp.add(nums[i])
        
        return count