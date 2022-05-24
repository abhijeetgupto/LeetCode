class Solution:
    def countTexts(self, s: str) -> int:
        
                
        s1 = []
        s2 = []
        m = 1000000007
        last = s[0]
        curr = 1
        
        for i in range(1, len(s)):
            if s[i] == last:
                curr+=1
            else:
                if last == '7' or last == '9' :
                    s2.append(curr)
                
                else:
                    s1.append(curr)
                    
                last = s[i]
                curr = 1
        
        if last == '7' or last == '9' :
            s2.append(curr)
                
        else:
            s1.append(curr)
        
        if s1:
            l1 = [0,1,2,4]
            while len(l1) <= max(s1):
                l1.append(l1[-1] + l1[-2] + l1[-3])
        
        if s2:
            l2 = [0,1,2,4,8]
            while len(l2) <= max(s2):
                l2.append(l2[-1] + l2[-2] + l2[-3] + l2[-4])
        
        
        res = 1
        for i in s1:
            res *= l1[i]%m
            res = res%m
            
        for i in s2:
            res *= l2[i]%m
            res = res%m

        
        return res
                 
                    
            
            
        