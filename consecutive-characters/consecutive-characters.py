class Solution:
    def maxPower(self, s: str) -> int:
        s=list(s)
        l=[]
        stack = []
        while len(s)!=0:         
            if not stack:
                stack.append(s[0])
                s.pop(0)      
            elif s[0] == stack[-1]:
                stack.append(s[0])
                s.pop(0)
            else:
                l.append(len(stack))
                stack = []
            
        l.append(len(stack))
        return max(l)
            
        