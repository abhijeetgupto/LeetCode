class Solution:
    def minSwaps(self, s: str) -> int:
        
        s = list(s)
        k = len(s)-1
        o = 0
        c = 0
        swap = 0
        
        for i in range(len(s)) :
            if s[i] == "[" :
                o+=1
            else:
                c+=1
            
            if c > o :
                swap+=1
                o += 1
                c -= 1
                while k>0 :
                    if s[k] == "[":
                        s[k] = "]"
                        break
                    k -= 1
        return swap
            
        