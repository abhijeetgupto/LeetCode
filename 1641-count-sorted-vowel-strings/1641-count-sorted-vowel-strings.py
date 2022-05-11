class Solution:
    
    def countVowelStrings(self, n: int) -> int:
                
        if n==1:
            return 5
        
        dp = [[1,1,1,1,1],[5,4,3,2,1]]
        
        total = sum(dp[-1])
        
        for _ in range(2,n):
            
            l = [total]
            curr = total
            for i in range(1,5) :
                x = l[-1] - dp[-1][i-1]
                curr += x
                l.append(x)
            dp.append(l)
            total = curr
            
        return total
    
            
            
        
