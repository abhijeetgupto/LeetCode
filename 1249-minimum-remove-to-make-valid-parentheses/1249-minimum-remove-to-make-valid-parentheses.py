class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        remove = set()
        
        for i in range(len(s)) :
            
            if s[i] == "(" :
                stack.append(["(", i])
            
            elif s[i] == ")" :
                if stack :
                    stack.pop()
                else:
                    remove.add(i)
        
        for _,i in stack :
            remove.add(i)
        
        res = ""
        for i in range(len(s)) :
            if i not in remove :
                res += s[i]
        
        return res
        