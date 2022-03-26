class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        l = []
        for temp in grid :
            l += temp
        
        l.sort()
        re = l[0]%x
        
        for i in range(1, len(l)) :
            if l[i]%x != re :
                return -1
        
        n = l[len(l)//2]
        count = 0
        for num in l :
            count += abs(num - n)//x
        
        return count
            