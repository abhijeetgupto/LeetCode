class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        n,m = len(matrix), len(matrix[0])
        @lru_cache(None)
        def rec(i,j):
            
            res = 1
            dv = [(1,0), (0,1), (-1,0), (0,-1)]
            for x,y in dv:
                if 0<=i+x<n and 0<=j+y<m and matrix[i+x][j+y] > matrix[i][j] :
                    res = max(res, 1+rec(i+x,j+y))
            return res
       
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, rec(i,j))
                
        return ans