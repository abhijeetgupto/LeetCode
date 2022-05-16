class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0]!=0:
            return -1
        
        n = len(grid)
        visited = set()
        visited.add((0,0))
        
        
        queue = [(0,0)]
        res = 1
        
        while queue :
            nq = []
            for i,j in queue:
                
                if i==j==n-1:
                    return res
                
                traverse = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1], [i, j + 1], [i + 1, j - 1], [i + 1, j],[i + 1, j + 1]]
                for r,c in traverse :
                    if r in range(n) and c in range(n) and grid[r][c] == 0 and (r,c) not in visited:
                        visited.add((r,c))
                        nq.append((r,c))
            queue = nq
            res += 1
            
        return -1
      
                    
        
        

        
        