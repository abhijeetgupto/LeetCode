class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        
        idx1 = nums.index(min(nums))
        idx2 = nums.index(max(nums))
        
        if idx1 == idx2 :
            return 1
        
        m1 = max(idx1,idx2)+1
        m2 = max(len(nums)-idx1, len(nums)-idx2)
        
        m3 = idx1+1+len(nums)-idx2
        m4 = idx2+1+len(nums)-idx1
        
        return min(m1,m2,m3,m4)