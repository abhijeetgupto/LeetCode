class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            flag = True
            for x, y in dr:
                r, c = (i + x), (j + y)
                if 0 <= r < n or 0 <= c < m:
                    if r == 0 or c == 0 or r == n - 1 or c == m - 1:
                        if grid[r][c] != 1:
                            flag = False
                    else:
                        if grid[r][c] == 0:
                            grid[r][c] = 1
                            if not dfs(r, c):
                                flag = False
                else:
                    flag = False
            return flag
        
        n = len(grid)
        m = len(grid[0])
        res = 0
        
        for i in range(1, n-1):
            for j in range(1, m-1):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    if dfs(i, j):
                        res+=1
        
        return res
        