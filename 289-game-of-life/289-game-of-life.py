class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                v = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
                count = 0
                for i,j in v:
                    if (r+i) in range(rows) and (c+j) in range(cols):
                        if board[(r+i)][(c+j)] == 1 or board[(r+i)][(c+j)] == 2:
                            count += 1
                
                if board[r][c] == 1:
                    if 2 <= count <= 3:
                        board[r][c] = 1
                    else:
                        board[r][c] = 2
                else:
                    if count == 3:
                        board[r][c] = 3
              
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                    
                elif board[i][j] == 3:
                    board[i][j] = 1
        
                        
                    