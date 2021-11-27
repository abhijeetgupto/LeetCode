import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if nums.count(0) == 1:
            index = nums.index(0)
            nums.remove(0)
            total = math.prod(nums)
            l = [0]*len(nums)
            l.insert(index, total)
            return l  
        
        if nums.count(0) > 1 :
            return [0]*len(nums)
            
            
        total = math.prod(nums)
        l = []
        for num in nums :
            l.append(total//num)
        return l