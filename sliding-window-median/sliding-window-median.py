import sortedcontainers

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        temp = sortedcontainers.SortedList(nums[:k])
        res = []
        
        if k%2 == 0 :
            
            res.append((temp[k//2]+temp[(k//2)-1])/2)
            for i in range(1, len(nums)-k+1):
                temp.remove(nums[i-1])
                temp.add(nums[i+k-1])
                res.append((temp[k//2]+temp[(k//2)-1])/2)
        
        else: 
            
            res.append(temp[k//2])
            for i in range(1, len(nums)-k+1):
                temp.remove(nums[i-1])
                temp.add(nums[i+k-1])
                res.append(temp[k//2])
        
        return res
        
        
        