class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        n = len(s)
        res = []
        def rec(i=0, curr = []):
            
            if i>=n:
                res.append(" ".join(curr))
                return 
            
            temp = ""
            for j in range(i, n):
                temp += s[j]
                if temp in wordDict:
                    curr.append(temp)
                    rec(j+1, curr)
                    curr.pop()
            
            return 
        
        
        wordDict = set(wordDict)
        rec()
        return res
        