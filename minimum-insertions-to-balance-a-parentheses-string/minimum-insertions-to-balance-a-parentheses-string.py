class Solution:
    def minInsertions(self, s: str) -> int:
        
        o = 0
        count = 0
        s = list(s)
        while s :
            top = s.pop(0)
            if top == "(" :
                o += 1
            
            else:
                if o > 0 :
                    if s :
                        if s[0] == ')' :
                            s.pop(0)
                            o -= 1
                        else :
                            count += 1
                            o -= 1
                    else :
                        count += 1
                        o -= 1
                else :
                    if s :
                        if s[0] == ')' :
                            s.pop(0)
                            count += 1
                        else:
                            count += 2
                    else:
                        count += 2
                    
        return count + (o*2)
                    
            
        
        