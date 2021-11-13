class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        
        res = [0]*len(t)
        stack = []
        for i in range(len(t)) :
            temp = t[i]
            while stack and temp > t[stack[-1]] :
                x = stack.pop()
                res[x] = i-x
            stack.append(i)
            
        return res