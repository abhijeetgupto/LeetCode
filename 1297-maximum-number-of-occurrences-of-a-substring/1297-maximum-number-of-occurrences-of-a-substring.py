class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        dic = {}
        for i in range(len(s)-minSize+1) :
            for j in range(i+minSize-1, min(len(s), i+26)):
                if len(set(s[i:j+1])) <= maxLetters :
                    if s[i:j+1] not in dic :
                        dic[s[i:j+1]] = 0
                    dic[s[i:j+1]] += 1
        if not dic: return 0
        return max(dic.values())
                
                