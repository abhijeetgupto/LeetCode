from functools import lru_cache
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        n = len(grid)
        
        @lru_cache(None)
        def rec(i, j):
    
            if i==n-1:
                return grid[i][j]
            
            count = math.inf
            for col in range(len(moveCost[grid[i][j]])):
                count = min(count, grid[i][j] + moveCost[grid[i][j]][col] + rec(i+1, col))
            
            return count
    
        res = math.inf
        for i in range(len(grid[0])):
            res = min(res, rec(0,i))
        
        return res
                
                
                
                
        