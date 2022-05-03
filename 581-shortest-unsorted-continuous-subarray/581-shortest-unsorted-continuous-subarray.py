class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        temp = sorted(nums)
        start = None
        end = None
        
        for i in range(n) :
            
            if start is None :
                if nums[i] != temp[i] :
                    start = i
            
            else:
                if nums[i] != temp[i] :
                    end = i
        
        if start is None :
            return 0
        return end-start+1
            
        
        
        
        
        