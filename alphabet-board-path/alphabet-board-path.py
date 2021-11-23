class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        dic = {}
        for i in range(len(board)):
            for j in range(len(board[i])) :
                dic[board[i][j]] = [j,i]
        
        curr = [0,0]
        res = ''
        for char in target:
            temp = dic[char]
            if curr == temp:
                res += '!'
                
            elif char == 'z' :
                x = curr[0]
                res += 'L'*x
                y = 5-curr[1]
                res += 'D'*y
                res += '!'
               
            
            elif curr == [0,5] :
                y = 5 - temp[1]
                res += 'U'*y
                x = temp[0]
                res += 'R'*x
                res +='!'
            
            else:
                x = temp[0] - curr[0]
                y = temp[1] - curr[1]

                if x >= 0 and y >= 0:
                    res += 'R' * abs(x)
                    res += 'D' * abs(y)
                    res += '!'
                elif x <= 0 and y >= 0:
                    res += 'L' * abs(x)
                    res += 'D' * abs(y)
                    res += '!'
                elif x >= 0 and y <= 0:
                    res += 'R' * abs(x)
                    res += 'U' * abs(y)
                    res += '!'
                elif x <= 0 and y <= 0:
                    res += 'L' * abs(x)
                    res += 'U' * abs(y)
                    res += '!'
            curr = temp

                    
        return res
        
                
                
                
            