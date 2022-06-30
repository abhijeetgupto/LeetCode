class Solution:
    def magicalString(self, n: int) -> int:
        
        if n==1:
            return 1
        
        l = [0]*(n+1)
        l[0] = 1
        l[1] = 2
        
        p1 = 0
        p2 = 0
        last = 2
        
        
        while p2<n:
            
            if l[p1] == 1:
                if last == 2:
                    l[p2] = 1
                else:
                    l[p2] = 2
                last = l[p2]
                p1 += 1 
                p2 += 1
            
            else:
                if last == 2:
                    l[p2] = 1
                    l[p2+1] = 1
                else:
                    l[p2] = 2
                    l[p2+1] = 2
                last = l[p2]
                p2+=2
                p1+=1
        
        return l[:n].count(1)
                    
                
                
                
                