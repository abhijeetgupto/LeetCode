import sortedcontainers

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        arr = sortedcontainers.SortedList(nums[:k])
        res = [arr[-1]]
        
        for i in range(1,len(nums)-k+1) :
            
            arr.remove(nums[i-1])
            arr.add(nums[i+k-1])
            res.append(arr[-1])
        
        return res
        