class Solution:
    def isValidSerialization(self, s: str) -> bool:
        
        if s=="#":
            return True
        
        l = s.split(",")
        if l[0] == "#" :
            return False
        
        stack = [[l.pop(0) ,0]]
        flag = True
        
        while l :
            top = l.pop(0)
            
            if top == "#" :
                if stack :
                    stack[-1][1] += 1
                    if stack[-1][1] == 2 :
                        stack.pop()
                else:
                    flag = False
                    break
            else:
                if stack :
                    stack[-1][1] += 1 
                    if stack[-1][1] == 2 :
                        stack.pop()
                    stack.append([top,0])
                else:
                    flag = False
                    break
        if stack :
            return False
        
        return flag
            
        
            
        
        