class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for char in s :
            if char == "(" :
                stack.append(char)
                
            elif char == "[" :
                stack.append(char)
                
            elif char == "{":
                stack.append(char)
                
            elif char == ")" :
                if stack and stack[-1] == "(" :
                    stack.pop()
                else:
                    return False
                
            elif char == "]" :
                if stack and stack[-1] == "[" :
                    stack.pop()
                else:
                    return False
                
            elif char == "}" :
                if stack and stack[-1] == "{" :
                    stack.pop()
                else:
                    return False
            
        if stack :
            return False
        return True
        