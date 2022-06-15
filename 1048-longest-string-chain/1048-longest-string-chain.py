class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dic = {}
        words.sort(key=len)
        
        res = 1
        
        for word in words:
            dic[word] = 1
            for i in range(len(word)):
                temp = word[:i] + word[i+1:]
                if temp in dic:
                    dic[word] = max(dic[word], 1+dic[temp])
            
            res = max(res, dic[word])
        
        return res
                
                
        
        
        
        
        
                    
                
        