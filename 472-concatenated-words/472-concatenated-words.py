class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        root = {}
        def addWord(word):
            
            curr = root
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr["*"] = "*"
            
        
        def checker(word, x=0):
            
            if not word:
                return x>=2                
            
            curr = root
            for i, char in enumerate(word):
                
                if char in curr:
                    curr = curr[char]
                else:
                    return False
                
                if "*" in curr and checker(word[i+1: ], x+1):
                    return True
                
            return False
                    

        
        for word in words:
            addWord(word)
        
        res = []
        for word in words:
            if checker(word):
                res.append(word)
                
        return res
        
        
        
        