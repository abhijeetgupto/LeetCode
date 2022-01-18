class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def rec(lo=0, hi=len(nums)-1) :
            
            if hi == lo :
                return nums[hi]
            
            if hi-lo == 1 :
                return max(nums[hi],nums[lo])
            
            else:
                return max((nums[lo]+min(rec(lo+2,hi),rec(lo+1,hi-1))), nums[hi]+min(rec(lo+1,hi-1),rec(lo,hi-2)))
        
        s = sum(nums)
        return rec()>=s/2
        
        