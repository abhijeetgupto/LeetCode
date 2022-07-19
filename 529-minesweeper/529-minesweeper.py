class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        n,m = len(board), len(board[0])
        
        def dfs(i, j):
            
            if board[i][j] == "M":
                board[i][j] = "X"
                return 
            
            count = 0
            dr = [(-1,-1), (-1, 0), (-1, 1), (0,-1), (0, 1), (1, -1), (1, 0), (1, 1)]
            
            for x,y in dr:
                if 0<=i+x<n and 0<=j+y<m:
                    if board[i+x][j+y] == "M":
                        count += 1
                        
            if count == 0:
                board[i][j] = "B"
                for x,y in dr:
                    if 0<=i+x<n and 0<=j+y<m:
                        if board[i+x][j+y] == "E":
                            dfs(i+x, j+y)
                return 
                
            else:
                board[i][j] = str(count)
                return 
                            
        dfs(click[0], click[1])
        return board
                    
                    
                    
            
        