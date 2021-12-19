class Solution:
    def decodeString(self, s: str) -> str:
        
        if '[' not in s :
            return s
        
        while '[' in s :
            
            i1 = s.rindex('[')
            i2 = i1 + s[i1:].index(']')
            
            num = ""
            i = 1
            
            while True :
                try :
                    k = int(s[i1-i])
                    num = s[i1-i] + num
                    i += 1
               
                except :
                    break
                  
            k = int(num)       
            temp = s[i1+1 : i2]
            temp = temp*k
            s = s[ : i1-len(num)] + temp + s[i2+1:]
            
        return s
        
        