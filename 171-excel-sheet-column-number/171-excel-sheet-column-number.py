class Solution:
    def titleToNumber(self, s: str) -> int:
        
        dic1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 
               'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
               'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 
               'Z': 26}   
        dic2 = {0: 1, 1: 26, 2: 676, 3: 17576, 4: 456976, 5: 11881376, 6: 308915776, 7: 8031810176}
        
        n = len(s)
        count = 0
        
        for i in range(n) :
            count += dic2[n-i-1]*dic1[s[i]]
        
        return count
        
        

        