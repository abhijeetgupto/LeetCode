class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        

        res = ""
        last = 0
        
        for i in spaces :
            res += s[last : i]
            res += " "
            last = i
            
        res += s[last:]
        return res
        