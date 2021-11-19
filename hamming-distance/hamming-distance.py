class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        xb=list(bin(x)[2:])
        yb=list(bin(y)[2:])
        
        if len(xb)>len(yb):
            while len(xb)!=len(yb):
                yb.insert(0,'0')
        elif len(xb)<len(yb):
            while len(xb)!=len(yb):
                xb.insert(0,'0')
               
        count=0
        for i in range(len(xb)):
            if xb[i]!=yb[i]:
                count+=1
        
        return count