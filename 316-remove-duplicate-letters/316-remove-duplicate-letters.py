class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        dic = dict(collections.Counter(s))
        res = []
        
        for i in range(len(s)) :
            
            dic[s[i]] -= 1
            if s[i] not in res : 
                while res and dic[res[-1]] > 0 and s[i] < res[-1] : 
                    res.pop()

                res.append(s[i])
                
        
        return "".join(res)