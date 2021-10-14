class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setn = set(nums)
        if len(setn)==len(nums):
            return False
        
        return True
        