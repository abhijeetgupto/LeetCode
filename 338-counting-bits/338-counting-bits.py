class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def bits(k) :
            
            count = 0
            while k>0 :
                if k&1>0:
                    count+=1
                k = k>>1
            return count
        
        res = []
        for i in range(n+1) :
            res.append(bits(i))
        
        return res
        