class Solution:
    def longestPrefix(self, s: str) -> str:
        
        res = ""
        curr1 = ''
        curr2 = ''
        i = 0
        j = len(s)-1
        
        
        while i<len(s) and j>0 :
            
            prefix = s[i]
            suffix = s[j]
            i += 1
            j -= 1
            
            curr1 += prefix
            curr2 = suffix + curr2
            
            if curr1 == curr2 :
                res = curr1

        return res
            
        