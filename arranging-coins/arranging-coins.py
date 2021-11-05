class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        count = 0
        while n>0:
            count += 1
            n -= i
            i += 1
        if n==0 :
            return count
        return count-1
            
        