class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        nums.sort()
        for i in range(len(nums)) :
            n = len(res)
            for j in range(n) :
                x = res[j] + [nums[i]]
                if x not in res:
                    res.append(x)
            
        return res
            
                
                
                