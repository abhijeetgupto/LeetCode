class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if num>0 :
            l = list(str(num))
            l.sort()
            res = ""
            z = 0
            i = 0
            
            while l[i] == "0" :
                i+=1
                z+=1
            
            res += l[i] + "0"*z
            res += "".join(l[i+1 : ])
            return int(res)
            
        
        else:
            num *= -1
            l = list(str(num))
            l.sort(reverse = True)
            res = "".join(l)
            res = int(res)*-1
            return res
            