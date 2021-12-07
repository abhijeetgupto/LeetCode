import sortedcontainers
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        nums.reverse()
        l = []
        res = [0]*len(nums)
        
        for i in range(len(nums)) :
            idx = bisect.bisect_left(l,nums[i])
            l.insert(idx, nums[i])
            res[i] = idx
            
        res.reverse()
        return res
        