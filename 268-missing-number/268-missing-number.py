class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s = sum(nums)
        a = len(nums)*(len(nums)+1)//2
        return a-s
        