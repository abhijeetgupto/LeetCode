from sortedcontainers import SortedSet

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        main = SortedSet([1,2,3])
        extra = SortedSet()
        
        curr = [1,2,3]
        
        
        while len(main) < n :
            
            l1 = [curr[0]*2,curr[0]*3,curr[0]*5]
            l2 = [curr[1]*2,curr[1]*3,curr[1]*5]
            l3 = [curr[2]*2,curr[2]*3,curr[2]*5]
            
            for i in range(3) :
                extra.add(l1[i])
                extra.add(l2[i])
                extra.add(l3[i])
            
            a,b,c = extra.pop(0), extra.pop(0), extra.pop(0)
            main.add(a)
            main.add(b)
            main.add(c)
            
            curr = [a,b,c]
        return main[n-1]
        
            
                
            
            
            
            
            
        