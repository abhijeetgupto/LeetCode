class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors)<3:
            return False
        a = 0
        b = 0
        for i in range(len(colors)):
            x = colors[i : i+3]
            if  x == 'AAA':
                a+=1
            elif x == 'BBB':
                b+=1
        if a>=b+1:
            return True 
        return False
        
                    
                
        
        