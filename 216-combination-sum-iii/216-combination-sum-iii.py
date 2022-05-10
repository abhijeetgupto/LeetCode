class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = list(range(1,10))
        res = []
        
        def rec(i=0, curr = []):
            
            if len(curr) == k and sum(curr) == n :
                res.append(curr.copy())
                return 
            
            if i>=9 or len(curr)>k:
                return 
                        
            rec(i+1, curr + [nums[i]])
            rec(i+1, curr)
            return 
        
        rec()
        return res