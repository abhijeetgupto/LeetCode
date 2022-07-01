class Solution:
    def getPermutation(self, n: int, k: int) -> str:
            
        @lru_cache(None)
        def fact(n):
            if n==1 or n==0:
                return 1
            
            return n*fact(n-1)

        
        l = list(range(1, n+1))
        k-=1
        res = ""
        while l :
            f = fact(len(l)-1)
            res += str(l.pop(k//f))
            k %= f


        res += "".join(l)
        return res
        
        