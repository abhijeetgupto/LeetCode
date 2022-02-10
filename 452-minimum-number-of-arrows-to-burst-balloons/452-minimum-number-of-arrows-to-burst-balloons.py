class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        n = len(points)
        points.sort()
        last = points[0]
        count = 0
        i = 1
        
        while i<n :
            
            if last[1] >= points[i][0] :
                last = [points[i][0], min(last[1],points[i][1])]
            
            else:
                count += 1
                last = points[i]
            i+=1
                
        count+=1
        return count
        
            