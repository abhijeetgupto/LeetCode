class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return
        
                
        dic = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],
              '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        n = len(digits)
        res = []
        def rec(i=0, curr=""):
            
            if i >= n :
                res.append(curr)
                return 
            
            for char in dic[digits[i]]:
                rec(i+1, curr+char)
        
        rec()
        return res
                