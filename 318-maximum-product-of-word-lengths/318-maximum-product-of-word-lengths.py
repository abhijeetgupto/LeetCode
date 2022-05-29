class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        new = []
        for i in range(len(words)):
            new.append(set(words[i]))
        
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not new[i].intersection(new[j]):
                       res = max(res, len(words[i])*len(words[j]))
        
        return res