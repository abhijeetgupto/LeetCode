class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        rows = len(heights)
        cols = len(heights[0])
        if rows==cols==1:
            return 0
        
        if rows==1 :
            m = -math.inf
            for i in range(1,cols):
                m = max(m, abs(heights[0][i]-heights[0][i-1]))
            return m
        
        if cols==1 :
            m = -math.inf
            for i in range(1,rows):
                m = max(m, abs(heights[i][0] - heights[i-1][0]))
            return m
        
        def checker(k) :
            
            visited = set()
            queue = [(0,0)]
            while queue:
                nq = []
                for r,c in queue:
                    if r==rows-1 and c==cols-1:
                        return True
                    
                    if (r,c) not in visited:
                        
                        if r+1 < rows and abs(heights[r][c]-heights[r+1][c]) < k:
                            nq.append((r+1,c))
                        if r-1 >= 0 and abs(heights[r][c]-heights[r-1][c]) < k:
                            nq.append((r-1,c))
                        if c+1 < cols and abs(heights[r][c]-heights[r][c+1]) < k:
                            nq.append((r,c+1))
                        if c-1 >= 0 and abs(heights[r][c]-heights[r][c-1]) < k:
                            nq.append((r,c-1))

                            
                    visited.add((r,c))
                queue = nq
            
            return False
                        

        
        s = 0
        e = max(max(row) for row in heights) - min(min(row) for row in heights)
        res = e
        
        while s<=e :
            m = (s+e)//2
            if checker(m) :
                res = m
                e = m-1
            else:
                s = m+1
        
        return res-1
                
        
        
                    
                    
                
                
            
            
            
    
        