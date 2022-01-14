class Solution:
    def myAtoi(self, s: str) -> int:
        s = list(s)
        i = ""
        while s and s[0] == ' ' :
            s.pop(0)
        while s :
            top = s.pop(0)
            if not i:
                if ord(top) in range(48,58) or top == "+" or top == "-" :
                    i += top
                else:
                    break
                    
            else:    
                if ord(top) in range(48,58) :
                        i += top
                else :
                    break
        if not i : return 0         
        try : i = int(i)
        except : return 0
        x = 2**31 
        if i > x-1:
            return x-1
        if i < -x :
            return -x
        else:
            return i
            
        
        