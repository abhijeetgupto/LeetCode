class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        
        n = len(grid)
        m = len(grid[0])
        
        def rec(i, j, path) :
            
            if grid[i][j] == -1 :
                return 0
            
            if grid[i][j] == 2 :
                if len(path) == k :
                    return 1
                else:
                    return 0
            
            traverse = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            count = 0
            for r,c in traverse :
                if r>=0 and r<n and c>=0 and c<m and (r,c) not in path :
                    count += rec(r,c,path.union({(r,c)}))
            
            return count
                
        
        k = 0
        x = 0
        y = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != -1 :
                    k+=1
                if grid[i][j] == 1 :
                    x = i
                    y = j
        return rec(x,y,{(x,y)})
        
        