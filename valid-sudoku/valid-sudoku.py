class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def helper(board) :
            for l in board :
                s = "".join(l)
                s = s.replace(".","")    
                if len(s) != len(set(s)):
                    return False
            return True

        bt = list(zip(*board))
        blocks = []
        
        for row in range(0,len(board),3):
            l1 = board[row][0:3] + board[row+1][0:3] + board[row+2][0:3]
            l2 = board[row][3:6] + board[row+1][3:6] + board[row+2][3:6]
            l3 = board[row][6:9] + board[row+1][6:9] + board[row+2][6:9]
            blocks.append(l1)
            blocks.append(l2)
            blocks.append(l3)
        
        return helper(board) and helper(bt) and helper(blocks)