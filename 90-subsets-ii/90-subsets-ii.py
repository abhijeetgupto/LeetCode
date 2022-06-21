class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        
        def rec(i=0, curr = []):
            
            if i>=n:
                if curr not in res:
                    res.append(curr.copy())
                return 
            
            curr.append(nums[i])
            rec(i+1, curr)
            curr.pop()
            rec(i+1, curr)
            return 
        
        nums.sort()
        rec()
        return res
            
        

            
                
                
                