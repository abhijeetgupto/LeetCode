class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2)<len(s1):
            return False
        
        dic1 = dict(collections.Counter(s1))
        dic2 = dict(collections.Counter(s2[:len(s1)]))
                
        if dic1 == dic2 :
            return True
        
        for i in range(1,len(s2)-len(s1)+1) :
            if dic2[s2[i-1]] == 1:
                dic2.pop(s2[i-1])
            else:
                dic2[s2[i-1]] -= 1
            
            if s2[i+len(s1)-1] in dic2 :
                dic2[s2[i+len(s1)-1]] += 1
            else:
                dic2[s2[i+len(s1)-1]] = 1
            
            if dic1 == dic2:
                return True
        return False
                
                
        
        