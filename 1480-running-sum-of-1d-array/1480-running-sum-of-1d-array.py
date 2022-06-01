class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        for i,num in enumerate(nums):
            curr+=num
            nums[i]=curr
        
        return nums