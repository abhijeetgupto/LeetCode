class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        if len(nums)<3:
            return 0
        
        res = []
        
        d = nums[1]-nums[0]
        curr = 2
        
        for i in range(2,len(nums)):
            
            if nums[i] == nums[i-1] + d :
                curr += 1
            
            else:
                if curr >= 3 :
                    res.append(curr)
                curr = 2
                d = nums[i]-nums[i-1]
                
        if curr>=3:
            res.append(curr)
        
        count = 0
        
        for n in res :
            count += ((n-1)*(n-2))//2
        
        return count
            
            
                
        