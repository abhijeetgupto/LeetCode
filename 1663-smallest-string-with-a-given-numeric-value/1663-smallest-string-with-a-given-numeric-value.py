class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        res = [0]*n
        for i in range(n) :
            
            # k - x = n-i-1
            x = k-n+i+1
            if x >= 26 :
                res[i] = 26
                k -= 26
                
            else:
                res[i] = x
                k -= x
        
        result = ""
        for i in range(n-1, -1, -1) :
            result += chr(96 + res[i])
        
        return result
            
                
        