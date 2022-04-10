class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        o = 0
        x = 0
        
        for s in board :
            for char in s :
                if char == "O" :
                    o+=1
                elif char == "X" :
                    x += 1 
        
        if (o > x) or (x > o+1):
            return False
        
        l = [board[0][0]+board[0][1]+board[0][2],
        board[1][0]+board[1][1]+board[1][2],
        board[2][0]+board[2][1]+board[2][2],
        board[0][0]+board[1][0]+board[2][0],
        board[0][1]+board[1][1]+board[2][1],
        board[0][2]+board[1][2]+board[2][2],
        board[0][0]+board[1][1]+board[2][2],
        board[2][0]+board[1][1]+board[0][2]]
        
        winner_x = 0
        winner_o = 0
        for s in l :
            if s=="XXX":
                winner_x += 1
            elif s == "OOO" :
                winner_o += 1
        
        if winner_x == 0 and winner_o == 1 :
            return o==x
        
        if winner_x == 1 and winner_o == 0 :
            return o!=x
        
        if winner_x == winner_o == 0:
            return True
        
        if winner_x == 2 and winner_o == 0:
            return True
        
        return False