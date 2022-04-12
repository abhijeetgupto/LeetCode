class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        new = copy.deepcopy(board)
        rows = len(board)
        cols = len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                temp = [(i+1, j+1), (i-1,j-1), (i+1, j-1), (i-1, j+1), (i+1, j),(i-1,j), (i, j+1), (i, j-1)]
                count = 0
                for r,c in temp :
                    if r>=0 and r<rows and c>=0 and c<cols and board[r][c] == 1 :
                        count += 1
                
                if board[i][j] == 0 :
                    if count == 3 :
                        new[i][j] = 1
                
                else:
                    if count < 2 or count>3:
                        new[i][j] = 0
        board[:] = new
                        
                      