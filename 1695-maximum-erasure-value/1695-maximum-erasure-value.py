class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        res = 0
        curr = 0
        start = 0
        l = set()
        for end in range(len(nums)):
            curr += nums[end]
            
            while nums[end] in l and end>=start:
                curr -= nums[start]
                l.remove(nums[start])
                start += 1
                
            l.add(nums[end])
            res = max(res, curr)
            
        return res
            
        