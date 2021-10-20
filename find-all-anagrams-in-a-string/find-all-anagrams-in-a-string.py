class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p) :
            return []
        
        dic = dict(collections.Counter(p))
        window = dict(collections.Counter(s[:len(p)]))
        res = []
        if window == dic:
            res.append(0)
            
        for i in range(1, len(s)-len(p)+1) :
            if window[s[i-1]] ==  1 :
                window.pop(s[i-1])
            else:
                window[s[i-1]] -=  1
            
            if s[i+len(p)-1] in window :
                window[s[i+len(p)-1]] +=  1
            else:
                window[s[i+len(p)-1]] =  1
            
            if window == dic:
                res.append(i)
        return res
                
        
        
        