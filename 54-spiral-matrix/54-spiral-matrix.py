class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        nr = len(matrix)
        nc = len(matrix[0])
        
        res = []
        visited = set()
        def rec(i):
            
            #startrow = i
            #startcol = i
            
            #top row from left to right
            for c in range(i, nc-i):
                if (i,c) not in visited:
                    visited.add((i,c))
                    res.append(matrix[i][c])
            
            #right column from up to down
            for r in range(i+1, nr-i-1):
                if (r,nc-i-1) not in visited:
                    visited.add((r,nc-i-1))
                    res.append(matrix[r][nc-i-1])
            
            #bottom row from right to left
            for c in range(nc-i-1, i-1,-1):
                if (nr-i-1, c) not in visited:
                    visited.add((nr-i-1, c))
                    res.append(matrix[nr-i-1][c])
            
            #left column from bottom to up
            for r in range(nr-i-2, i,-1):
                if (r,i) not in visited:
                    visited.add((r,i))
                    res.append(matrix[r][i])
                
        for x in range(0, math.ceil(min(nr,nc)/2)):
            rec(x)
            
        return res
        
        
        
        