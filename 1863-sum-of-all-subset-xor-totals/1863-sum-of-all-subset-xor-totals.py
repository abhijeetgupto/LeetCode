class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = []
        n = len(nums)
        
        def rec(i=0, curr=0):
            
            if i>=n:
                res.append(curr)
            
            else:
                rec(i+1, curr^nums[i])
                rec(i+1, curr)
        
        rec()
        return sum(res)
            
        