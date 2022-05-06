class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        for char in s :
            if not stack :
                stack.append([char,1])
            
            elif stack[-1][0] == char :
                stack[-1][1] += 1
                
            else:
                stack.append([char,1])
            
            if stack[-1][1] == k :
                stack.pop()
        
        res = ""
        for char,i in stack:
            res += char*i
        
        return res
            
        