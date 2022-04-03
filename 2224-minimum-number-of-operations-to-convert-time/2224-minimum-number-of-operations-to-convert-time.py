class Solution:
    def convertTime(self, curr: str, correct: str) -> int:
        
        curr = int(curr[:2])*60 + int(curr[3:])
        correct =  int(correct[:2])*60 + int(correct[3:])
        x = correct - curr
        l = [60, 15, 5, 1]
        i = 0
        count = 0
        
        while x != 0 :
                
            count += x//l[i]
            x = x%l[i]
            i += 1
        
        return count