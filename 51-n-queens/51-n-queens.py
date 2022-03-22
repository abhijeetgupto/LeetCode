import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["." for _ in range(n)] for _ in range(n)]
        def isValid(row,col) :
            
            for i in range(n) :
                if board[row][i] == 'Q' :
                    return False
            
            r=row-1
            c=col-1
            while r>=0 and c>=0 :
                if board[r][c] == "Q" :
                    return False
                r-=1
                c-=1
            
            r=row+1
            c=col-1
            while r<n and c>=0 :
                if board[r][c] == "Q" :
                    return False
                r+=1
                c-=1
            
            return True
            
        
        res = []
        def rec(col=0):
            
            if col == n :
                res.append(copy.deepcopy(board))
                return True
            
            for row in range(n) :
                
                if isValid(row, col) :
                    board[row][col] = 'Q'
                    rec(col+1)
                    board[row][col] = "."
                      
            return False
        
        rec()
        result = []
        for chess in res :
            temp = []
            for l in chess :
                temp.append("".join(l))
            result.append(temp)
            
        return result
        
                    
                
                
                
        
        
        
        
        