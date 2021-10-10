class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        if len(nums)==2:
            n1,n2 = nums
            return [[n1,n2],[n2,n1]]
        
        else:
            l = []
            for i in range(len(nums)):
                temp = nums[:i]+nums[i+1:]
                for j in self.permute(temp):
                    l.append([nums[i]]+j)
            return l
        