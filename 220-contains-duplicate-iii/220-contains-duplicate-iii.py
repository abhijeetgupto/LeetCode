import sortedcontainers
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        k+=1
        temp = sortedcontainers.SortedList(nums[:k])
        for i in range(1,len(temp)):
            if temp[i]-temp[i-1] <= t :
                return True
        
        
        for i in range(1,len(nums)-k+1):
            
            num = nums[i+k-1]
            temp.remove(nums[i-1])
            temp.add(nums[i+k-1])
            idx = bisect.bisect_left(temp, num)
            
            if (idx-1 >= 0 and num-temp[idx-1]<=t) or (idx+1<k and temp[idx+1]-num<=t):
                return True
            
        return False
            
            
            