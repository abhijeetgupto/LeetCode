class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        res = 0 
        curr = 0 
        last = False
        
        for num in nums:
            
            if last:
                if num == 0:
                    curr += 1
                else:
                    last = False
                    res += (curr*(curr+1)//2)
            
            else:
                if num == 0:
                    curr = 1
                    last = True
        
        if last:
            res += (curr*(curr+1)//2)
        
        return res
                
                