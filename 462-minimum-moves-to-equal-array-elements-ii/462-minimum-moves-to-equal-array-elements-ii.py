class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()
        x = nums[n//2]
        count = 0
        
        for num in nums :
            count += abs(num - x)
        
        return count