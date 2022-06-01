class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        res = 0
        
        
        for i in range(n):
            m = grid[i][0]
            for j in range(n):
                m = max(grid[i][j], m)
                if grid[i][j] != 0:
                    res += 1
            res += m
        
        for col in range(n):
            m = grid[0][col]
            for row in range(n):
                m = max(m, grid[row][col])
            res+=m
        
        return res
        
        