class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        
        n = len(m)
        memo = {}
        def rec(i, j) :
            
            if (i,j) in memo :
                return memo[(i,j)]
            
            if i == n-1 :
                return m[i][j]
            
            else:
                a = b =  math.inf
                
                if j-1>=0 :
                    a = rec(i+1,j-1)
                if j+1 < n :
                    b = rec(i+1,j+1)
    
                c = rec(i+1,j)
                memo[(i,j)] = m[i][j] + min(a, b, c)
                return memo[(i,j)]
            
        res = math.inf
        for x in range(n) :
            res = min(res, rec(0, x))
        return res
            
            
#         n = len(m)
#         for row in range(1,n) :
#             for col in range(n) : 
#                 if col == 0 :
#                     m[row][col] += min(m[row-1][col], m[row-1][col+1]) 
#                 elif col == n-1 :
#                     m[row][col] += min(m[row-1][col], m[row-1][col-1])
#                 else:
#                     m[row][col] += min(m[row-1][col], m[row-1][col-1], m[row-1][col+1])
                    
#         return min(m[-1])
        