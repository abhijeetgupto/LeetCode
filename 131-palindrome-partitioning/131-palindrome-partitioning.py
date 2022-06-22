class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        n = len(s)
        
        def rec(i=0, curr=[]):
            
            if len(curr)>=2 and curr[-2] != curr[-2][::-1]:
                return 
            
            if i>=n:
                if curr[-1] == curr[-1][::-1]:
                    res.append(curr.copy())
                return 
                    
            if not curr:
                rec(i+1, [s[i]])
                return 
                
            else:
                curr.append(s[i])
                rec(i+1, curr)
                curr.pop()
                
                curr[-1] += s[i]
                rec(i+1, curr)
                return 
            
        rec()
        return res
            
            
            
            