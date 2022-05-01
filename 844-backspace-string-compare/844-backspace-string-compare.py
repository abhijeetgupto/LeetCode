class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        t1 = []
        for char in s :
            if char == "#" :
                if t1:
                    t1.pop()
            else:
                t1.append(char)
        
        t2 = []
        for char in t :
            if char == "#" :
                if t2:
                    t2.pop()
            else:
                t2.append(char)
        return t1 == t2