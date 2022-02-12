class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        
        for i in range(len(nums)) :
            n = len(res)
            for j in range(n) :
                x = res[j] + [nums[i]]
                res.append(x)
            
        
        return res
            
                    
            
 