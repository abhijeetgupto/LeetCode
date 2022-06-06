class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        
        n = len(s)
        if n > 12 or n<3:
            return []
        
        
        res = []
        
        def isValid(l):
          
            for s in l:
                if int(s) > 255:
                    return False
            return True
        
        def rec(curr=[], i=0):
            
            
            if len(curr) == 4:
                
                curr[-1] += s[i:]
                if len(curr[-1])>1 and curr[-1][0] == "0":
                    pass
                else:
                    if isValid(curr):
                        res.append(".".join(curr))
                    return 
            
            if i>=n:
                return 
            
            if not curr:
                rec([s[i]], i+1)
                return 
            
            else:
                if curr[-1] == "0":
                    rec(curr + [s[i]], i+1)
                    return 
                
                else:
                    rec(curr + [s[i]], i+1)
                    curr[-1] += s[i]
                    rec(curr, i+1)
        
        rec()
        return res
            