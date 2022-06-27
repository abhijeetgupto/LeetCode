class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

        
        def findHashCode(s):
            n = len(s)-1
            hashCode = 0
            for char in s:
                hashCode += dic[char]*(10**n)
                n-=1
            return hashCode
        
        def checker(idx):
            for i in range(n):
                if needle[i] != haystack[i+idx]:
                    return False
            return True
        
        n = len(needle)
        target = findHashCode(needle)
        curr = findHashCode(haystack[:n])
        
        
        if curr == target and checker(0):
            return 0
        
        for i in range(1, len(haystack)-n+1):
            
            # include i+n-1
            # exclude i-1
            curr -= dic[haystack[i-1]]*(10**(n-1))
            curr *= 10
            curr += dic[haystack[n+i-1]]
            if curr == target and checker(i):
                return i
            
        return -1
        
        
                            
        
        