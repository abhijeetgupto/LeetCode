class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        if len(s)<k :
            return False
        
        count = 1
        memo = set()

        temp = s[:k]
        memo.add(temp)
        
        for i in range(1,len(s)-k+1):
            temp = temp[1:] + s[i+k-1]
            if temp not in memo :
                count += 1
                memo.add(temp)
        
        if count == 2**k:
            return True
        
        return False
        
        
        