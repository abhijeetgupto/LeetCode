class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n = len(triangle)
        
        memo = {}
        def rec(i=0, j=0) :
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i==n-1 :
                return triangle[i][j]
            
            memo[(i,j)] = triangle[i][j] + min(rec(i+1,j),rec(i+1,j+1))
            return memo[(i,j)]
        
        return rec()
            
            
        