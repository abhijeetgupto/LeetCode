class Solution:
    def removeCoveredIntervals(self, l: List[List[int]]) -> int:
        
        l.sort()
        i = 0
        
        while l and i<len(l) :
            
            if (i-1>=0 and l[i][0] >= l[i-1][0] and l[i][1] <=l[i-1][1]) or (i+1<len(l) and l[i][0] == l[i+1][0] and l[i][1] <= l[i+1][1]) :
                l.pop(i)      
                
            else:
                i += 1
                
        return len(l)