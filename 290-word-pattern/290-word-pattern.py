class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        
        s = s.split()
        if len(s) != len(p) :
            return False
        
        dic1 = {}
        dic2 = {}
        
        for i in range(len(s)) :
            if p[i] not in dic1 :
                dic1[p[i]] = s[i]
            else:
                if dic1[p[i]] != s[i] :
                    return False
                
            if s[i] not in dic2 :
                dic2[s[i]] = p[i]
            else:
                if dic2[s[i]] != p[i] :
                    return False
                
                
        return True