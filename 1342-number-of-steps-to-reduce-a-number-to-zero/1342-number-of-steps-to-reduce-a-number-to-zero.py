class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        s = bin(num)[2:]
        return s.count('1')*2 - 1 + s.count('0') 