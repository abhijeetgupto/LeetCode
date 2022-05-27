class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx-1]<0:
                res.append(idx)
            else:
                nums[idx-1] *= -1
        return res