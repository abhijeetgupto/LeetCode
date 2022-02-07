class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = list(range(1,10))
        res = []
        
        def rec(i=0, target=n, curr=[]):

            if target == 0 and len(curr) == k:
                res.append(curr)
                return

            if target < 0 or len(curr) > k or i >= 9:
                return

            else:
                rec(i + 1, target - nums[i], curr + [nums[i]])
                rec(i + 1, target, curr)
                return 
        
        rec()
        return res
        
        
        
        
        
        
        
        
        
        
        rec()
        return res
                
                
        