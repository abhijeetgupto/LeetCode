class Solution:
    def makesquare(self, arr: List[int]) -> bool:
        
        arr.sort(reverse = True)
        n = len(arr)

        @lru_cache()        
        def rec(i=0, s1=0, s2=0, s3=0, s4=0):
            
            if s1==s2==s3==s4==target:
                return True
            
            if s1>target or s2>target or s3>target or s4>target or i>=n:
                return False
            
            return rec(i+1, s1+arr[i], s2, s3, s4) or rec(i+1, s1, s2+arr[i], s3, s4) or rec(i+1, s1, s2, s3+arr[i], s4) or rec(i+1, s1, s2, s3, s4+arr[i])
        
        s = sum(arr)
        target = s//4
        if s%4!=0 or max(arr) > target:
            return False
        
        return rec()
        
            
            
        
        
        