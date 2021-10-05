class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s :
            return 0
        
        m = -math.inf
        l = []
        for char in s :
            while char in l:
                l.pop(0)
            l.append(char)
            m = max(m,len(l))
            
        return m
            
            
        
        