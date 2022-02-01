class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = {}
        
        def rec(i, j, inc) :
            
            if (i,j,inc) in memo :
                return memo[(i,j,inc)]
            
            if i >= n :
                return 0
            
            if inc :
                if nums[i] > nums[j] :
                    memo[(i,j,inc)] = max(1+rec(i+1, i, False), rec(i+1, j, True))
                else:
                    memo[(i,j,inc)] =  rec(i+1, j, True)
            
            else:
                if nums[i] < nums[j] :
                    memo[(i,j,inc)] = max(1+rec(i+1, i , True), rec(i+1, j, False))
                else:
                    memo[(i,j,inc)] = rec(i+1, j, False)
                 
            return memo[(i,j,inc)]
        
        res = 0
        for i in range(n):
            if res >= n-i :
                break
                
            res = max(res, 1+rec(i+1, i, True), 1+rec(i+1, i, False))
            
        
        return res
                    
                
            
            
        
                
        