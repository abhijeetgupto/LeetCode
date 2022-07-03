class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        @cache        
        def rec(i, j, inc) :

            
            if i >= n :
                return 0
            
            if inc :
                if nums[i] > nums[j] :
                    return max(1+rec(i+1, i, False), rec(i+1, j, True))
                else:
                    return  rec(i+1, j, True)
            
            else:
                if nums[i] < nums[j] :
                    return  max(1+rec(i+1, i , True), rec(i+1, j, False))
                else:
                    return rec(i+1, j, False)

        
        res = 0
        for i in range(n):
            if res >= n-i :
                break
                
            res = max(res, 1+rec(i+1, i, True), 1+rec(i+1, i, False))
            
        
        return res
                    
                
            
            
        
                
        