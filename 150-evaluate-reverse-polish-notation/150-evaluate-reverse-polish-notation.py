class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for char in tokens:
            
            if char == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            
            elif char == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            
            elif char == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            
            elif char == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            
            else:
                stack.append(int(char))
                
        return stack[0]