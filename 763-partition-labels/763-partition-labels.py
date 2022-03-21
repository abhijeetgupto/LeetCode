class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        l = []
        i = 0
        n = len(s)
        
        while i < n :
            
            idx = s.rindex(s[i])
            
            if idx == i :
                l.append(1)
                i += 1
            
            else:
                j = i+1
                while j < idx and j < n :
                    x = s.rindex(s[j])
                    if x > idx :
                        idx = x
                    j+=1
                l.append(idx-i+1)
                i = idx+1
        return l
                
            
            
        