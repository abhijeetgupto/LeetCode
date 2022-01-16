class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        s = 0
        for i in range(len(seats)) :
            if seats[i] == 1 :
                break
            s += 1
        e = 0
        for j in range(len(seats)-1,-1,-1) :
            if seats[j] == 1:
                break
            e += 1
            
        m = 0
        curr = 0
        for x in range(i+1,j+1) :
            if seats[x] == 1 :
                m = max(m,curr)
                curr = 0
            else:
                curr += 1
        
        if m%2 == 0 :
            temp = m//2
        else:
            temp = (m+1)//2
            
        
        if s>=e and s>=temp:
            return s
        
        if e>=s and e>=temp:
            return e
        
        else :
            return temp
        
        
        
        
        
                
                
        
        
        
        