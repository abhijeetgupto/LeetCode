class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        col = [matrix[i][0] for i in range(len(matrix))]
        idx = bisect.bisect_right(col, target)
        
        while idx<len(col) and col[idx] == target :
            idx += 1
            
        row = matrix[idx-1]
        idx = bisect.bisect_left(row, target)
        if idx >= len(row):
            return False
        
        return row[idx]==target
            
        
        