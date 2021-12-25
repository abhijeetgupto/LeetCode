class Solution:
    def calculate(self, s: str) -> int:
        
        def eva(t):
            res = ""
            i = 0
            while (i < len(t)) and (t[i].isdigit() or (t[i] == " ")):
                if t[i] != " ":
                    res += t[i]
                i += 1

            res = int(res)
            while i < len(t):

                if t[i] == "*":
                    num2 = ""
                    idx = i + 1
                    while idx < len(t) and (t[idx].isdigit() or t[idx] == " "):
                        if t[idx] != " ":
                            num2 += t[idx]
                        idx += 1
                    i = idx
                    num2 = int(num2)
                    res *= num2

                elif t[i] == "/":
                    num2 = ""
                    idx = i + 1
                    while idx < len(t) and (t[idx].isdigit() or t[idx] == " "):
                        if t[idx] != " ":
                            num2 += t[idx]
                        idx += 1
                    i = idx
                    num2 = int(num2)
                    res = res // num2

                else:
                    i += 1
            return res
        
        l = s.split('+')
        l = [x.split('-') for x in l]
        
        res = 0
        
        for li in l :
            temp = eva(li[0])
            for i in range(1,len(li)) :
                temp -= eva(li[i])
            res += temp
        return res
                

        
        
        
        
        
        
        
        
        
        
        
#         curr = ""
#         start_idx = 0
#         l = {}
        
#         i = 0
#         while i<len(s) :
            
#             if s[i] == '*' :
#                 num1 = int(curr)
#                 num2 = ""
#                 idx = i
#                 while idx<len(s) and s[idx].isdigit() :
#                     num2 += s[idx]
#                     idx += 1
#                 i = idx
#                 num2 = int(num2)
#                 l[start_idx] = [num1*num2 , i]
#                 start_idx = idx+1
                
#             elif s[i] == '/' :
#                 num1 = int(curr)
#                 num2 = ""
#                 idx = i
#                 while idx<len(s) and s[idx].isdigit() :
#                     num2 += s[idx]
#                     idx += 1
#                 i = idx
#                 num2 = int(num2)
#                 l[start_idx] = [num1*num2 , i]
#                 start_idx = idx+1
                
#             elif s[i] == '+' :
            
#             elif s[i] == '-' :
            
#             elif s[i] != ' ' :
#                 curr += s[i]
#                 i += 1
#             else:
#                 i += 1
                
        