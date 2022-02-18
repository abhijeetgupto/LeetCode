class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        if k==len(num):
            return "0"
        
        stack = []
        
        for number in num :
            
            while stack and stack[-1] > number and k>0 :
                k -= 1
                stack.pop()
            
            stack.append(number)
        
        
        if not stack:
            return "0"
        
        if k>0 :
            try : 
                return str(int("".join(stack[:-k])))
            except:
                return "0"
        
        return str(int("".join(stack)))
            
        