class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []   
        
        for top in s :
            
            if stack and top == stack[-1][0] :
                x = stack.pop()
                temp = x[1]+1
                if temp < k :
                    stack.append([x[0],temp])         
            
            else:
                stack.append([top,1])
                
        res = ""
        for l in stack :
            res += l[0]*l[1]
        
        return res
                
        