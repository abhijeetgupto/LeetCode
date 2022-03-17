class Solution(object):
    def scoreOfParentheses(self, s):
        
        stack = []
        res = 0
        
        for char in s:
            if char == '(':
                stack.append(res)
                res = 0
            else:
                res = stack.pop() + max(1, res*2)
        
        return res