from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        m = 0
        l = deque()
        for char in s:
            while char in l:
                l.popleft()
            l.append(char)
            m = max(m, len(l))
            
        return m