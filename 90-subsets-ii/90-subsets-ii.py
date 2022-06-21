class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        
        def rec(x=0, curr = []):
            
            res.append(curr.copy())
            for i in range(x,n):
                if i!=x and nums[i] != nums[i-1]:
                    curr.append(nums[i])
                    rec(i+1, curr)
                    curr.pop()
                elif i==x:
                    curr.append(nums[i])
                    rec(i+1, curr)
                    curr.pop()
            return
                    
            
        nums.sort()
        rec()
        return res
            
        

            
                
                
                