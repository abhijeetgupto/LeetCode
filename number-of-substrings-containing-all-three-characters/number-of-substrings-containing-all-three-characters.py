class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        start = 0
        end = 0
        
        count = 0
        dic = {'a':0,'b':0,'c':0}
        
        while end < len(s) :
            
            dic[s[end]] += 1
            
            
            while dic['a'] > 0 and dic['b'] > 0 and dic['c'] > 0 :
                 
                dic[s[start]] -= 1
                start += 1
                count += len(s)-(end)
            
            end += 1
            
        return count
            
                
            
            
            
        