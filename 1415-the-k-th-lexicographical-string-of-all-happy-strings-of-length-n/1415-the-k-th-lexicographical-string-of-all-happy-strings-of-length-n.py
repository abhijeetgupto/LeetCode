class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        temp = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]
        if k>temp[n-1]:
            return ""
        
        res = []
        def rec(curr):
            
            if len(curr)==n:
                res.append(curr)
                return 
            
            if curr[-1] == "a":
                rec(curr+"b")
                rec(curr+"c")
                return 
                
            if curr[-1] == "b":
                rec(curr+"a")
                rec(curr+"c")
                return 
            
            if curr[-1] == "c":
                rec(curr+"a")
                rec(curr+"b")
                return 
        rec("a")
        if len(res)<k:
            rec("b")
        
        if len(res)<k:
            rec("c")
        
        res.sort()
        return res[k-1]
        
            
        

        
    
            
        