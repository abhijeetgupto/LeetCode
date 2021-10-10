class Solution:
    def combine(self, n: int, k: int) -> List[List[int]] : 
        
        def helper(nums,k):
            if k==1 :
                return [[num] for num in nums]
            
            else :
                l = []
                for i in range(len(nums)-k+1):
                    for lst in helper(nums[i+1 : ],k-1):
                        l.append([nums[i]]+lst)
                
                return l
        
        nums = list(range(1,n+1))
        return helper(nums,k)
        
        
        
        
        
            
                
        