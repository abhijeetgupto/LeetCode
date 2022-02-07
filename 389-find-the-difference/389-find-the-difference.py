class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        dic1 = dict(collections.Counter(s))
        dic2 = dict(collections.Counter(t))
        for i in range(97,123) :
            char = chr(i)
            if char in dic1 and char in dic2 :
                if dic1[char]!=dic2[char] :
                    return char
            elif char in dic1 or char in dic2 :
                return char
            
        
        
        