class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:
            num = abs(num)
            if nums[num] < 0:
                return num
            nums[num] *= -1
        
        
        
        

        