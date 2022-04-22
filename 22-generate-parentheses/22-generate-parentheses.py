class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = set()
        
        def rec(opened=0, closed=0, curr="") :
            
            if opened == n :
                if closed != n:
                    curr += ")"*(n-closed)
                res.add(curr)
            
            else :
                if opened == closed :
                    rec(opened+1, closed, curr+"(")
                
                else:
                    rec(opened+1, closed, curr+ "(")
                    rec(opened, closed+1, curr+")")
        rec()
        return list(res)
            
        