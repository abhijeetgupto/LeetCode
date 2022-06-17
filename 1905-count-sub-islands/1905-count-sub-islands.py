class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        m,n = len(grid1),len(grid1[0])
        dr = [(1,0), (-1,0), (0, 1), (0,-1)]
        
        def bfs(i,j):
            
            queue = [(i,j)]
            ans = 1
            while queue:
                nq = []
                for r,c in queue:
                    if grid1[r][c]==0:
                        ans = 0
                        
                    for dx,dy in dr:
                        if 0 <= r+dx < m and 0<=c+dy<n and grid2[r+dx][c+dy]==1 :
                            nq.append((r+dx,c+dy))
                            grid2[r+dx][c+dy] = 0
                queue = nq
            return ans
        
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == grid2[i][j] == 1  :
                    count += bfs(i,j)
        return count
                
            
        