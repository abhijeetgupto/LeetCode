class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rec(i=n):
            
            if i==1:
                return "1"
            
            else:
                x = rec(i-1)
                res = ""
                last = x[0]
                count = 1
                for i in range(1, len(x)):
                    if x[i] == last:
                        count += 1
                    else:
                        res += str(count)+last
                        last = x[i]
                        count = 1
                res += str(count)+last
                return res
        return rec()