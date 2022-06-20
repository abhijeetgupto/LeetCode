class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        root = {}
        
        def addWord(word):
            curr_node = root
            for letter in word:
                if "*" in curr_node:
                    curr_node.pop("*")
                    
                if letter not in curr_node:
                    curr_node[letter] = {}
                    
                curr_node = curr_node[letter]
            
            curr_node["*"] = "*" 
            return 
        
        def search(word):
            
            curr_node = root
            for letter in word:
                curr_node = curr_node[letter]  
            
            return "*" in curr_node
            
        
        temp = []
        for word in set(words):
            temp.append(word[::-1])
            
        temp.sort(key=len)
        for word in temp:
            addWord(word)
        
        
        res = 0
        for word in temp:
            if search(word):
                res += len(word)+1
        
        return res
                
            