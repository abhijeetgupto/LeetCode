class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        res = []
        x = 2**(maximumBit) - 1
        
        xor = nums[0]
        xor_arr = [xor]
        
        for i in range(1,len(nums)) :
            xor = xor^nums[i]
            xor_arr.append(xor)
        
        while xor_arr :
            top = xor_arr.pop()
            res.append(top^x)
        
        return res
        
            