class Solution:
    def minimumMoves(self, s: str) -> int:
        
        count = 0
        s = list(s)
        while s :
            top = s.pop(0)
            if top == "X" :
                if len(s) >= 2 :
                    s.pop(0)
                    s.pop(0)
                    count += 1
                else:
                    count+=1
                    break
        return count
                
            
            
        