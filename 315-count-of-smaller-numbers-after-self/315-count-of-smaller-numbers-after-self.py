class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        res = [0]*len(nums)
        l = sorted(nums)
        
        for i in range(len(nums)):
            idx = bisect.bisect_left(l,nums[i])
            l.pop(idx)
            res[i] = idx
            
        return res
        