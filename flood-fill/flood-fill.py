class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def helper(mat,r,c,target,x) :
            traverse = [[r-1,c],[r+1,c],[r,c+1],[r,c-1]]
            mat[r][c] = x
            for t in traverse :
                row,col = t
                if row in range(len(mat)) and col in range(len(mat[0])) :
                    if mat[row][col] == target :
                        mat[row][col] = x
                        helper(mat,row,col,target,x)
            return mat
        if image[sr][sc] == newColor:
            return image
        return helper(image,sr,sc,image[sr][sc],newColor)
        