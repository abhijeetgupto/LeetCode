class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        
        n = len(m)
        for row in range(1,n) :
            for col in range(n) : 
                if col == 0 :
                    m[row][col] += min(m[row-1][col], m[row-1][col+1]) 
                elif col == n-1 :
                    m[row][col] += min(m[row-1][col], m[row-1][col-1])
                else:
                    m[row][col] += min(m[row-1][col], m[row-1][col-1], m[row-1][col+1])
                    
        return min(m[-1])
        