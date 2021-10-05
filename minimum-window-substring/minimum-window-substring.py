class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
    
        dic1 = dict(collections.Counter(t))
    
        dic2 = {}
        extras = {}
    
        left = 0
        right = None
        for i in range(len(s)):
            if s[i] in dic1:
                if s[i] not in dic2:
                    dic2[s[i]] = 1
    
                elif dic1[s[i]] > dic2[s[i]]:
                    dic2[s[i]] += 1
    
                else:
                    if s[i] in extras:
                        extras[s[i]] += 1
                    else:
                        extras[s[i]] = 1
            if dic1 == dic2:
                right = i
                break
    
        if right is None:
            return ""
        m = right - left + 1
        res = s[left : right+1]
        while left < len(s):
            if s[left] in dic2:
    
                if s[left] in extras:
                    if extras[s[left]] == 1:
                        extras.pop(s[left])
                    else:
                        extras[s[left]] -= 1
                else:
                    flag = False
                    for i in range(right + 1, len(s)):
                        if s[i] == s[left]:
                            flag = True
                            right = i
                            break
                        if s[i] in dic1:
                            if s[i] in extras:
                                extras[s[i]] += 1
                            else:
                                extras[s[i]] = 1
                    if not flag:
                        break
                left += 1
    
            else:
                left += 1
            if right - left + 1 < m :
                res = s[left : right+1]
                m = right - left + 1
        return res
                
            
         
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                    