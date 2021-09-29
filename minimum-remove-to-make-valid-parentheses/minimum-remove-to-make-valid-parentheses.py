class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        res = []
        count = 0
        stack = 0 
        for i in range(len(s)) :
            char = s[i]
            
            if char == "(" :
                stack += 1
                res.append("*")
                
            elif char == ")" :
                if stack >= 1 :
                    count += 1
                    stack -= 1
                    res.append(char)         
            else :
                res.append(char)
                
        out = ""
        for char in res :
            if char == "*" and count > 0 :
                out += "("
                count -= 1
            elif char != "*" :
                out += char
        return out
        