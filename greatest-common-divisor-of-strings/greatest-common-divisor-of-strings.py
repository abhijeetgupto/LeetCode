class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if set(str1) != set(str2) :
            return ""
        
        s1 = min(str1,str2,key=len)
        s2 = max(str1,str2,key=len)
        
        res = ""
        for i in range(len(s1)) :
            temp = s1[:len(s1)-i]
            if s2.replace(temp,"") == "" and s1.replace(temp,"") == "" :
                return temp
        return ""
            
            