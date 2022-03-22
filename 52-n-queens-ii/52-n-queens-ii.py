class Solution:
    def totalNQueens(self, n: int) -> int:
        
        board = [["." for _ in range(n)] for _ in range(n)]
        def isValid(row, col) :
            
            for i in range(n) :
                if board[row][i] == 'Q' :
                    return False
            
            r = row-1
            c = col-1
            while r>=0 and c>=0 :
                if board[r][c] == 'Q' :
                    return False
                r-=1
                c-=1
                
            r = row+1
            c = col-1
            while r<n and c>=0 :
                if board[r][c] == "Q" :
                    return False
                r+=1
                c-=1
            return True
            
    
        def rec(col=0) :
            
            if col == n :
                return 1
            
            count = 0
            for row in range(n) :
                if isValid(row,col) :
                    board[row][col] = "Q"
                    count += rec(col+1)
                    board[row][col] = "."
            return count
        
        return rec()
                    
                    
                