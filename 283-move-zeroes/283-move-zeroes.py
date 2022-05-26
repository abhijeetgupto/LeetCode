class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        idx = 0
        i = 0
        n = len(nums)
        z = 0
        
        while i<n:
            
            if nums[i] == 0:
                z+=1
            else:
                nums[idx] = nums[i]
                idx += 1
            i += 1
            
        for i in range(n-1, n-z-1, -1):
            nums[i] = 0
        
        
            
            
        