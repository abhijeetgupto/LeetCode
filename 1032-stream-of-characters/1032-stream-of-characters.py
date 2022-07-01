class StreamChecker:

    def __init__(self, words: List[str]):
        
        def addWord(word):
            curr = self.root
            for char in word[::-1]:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr["*"] = "*"
            return 
            
        self.root = {}
        for word in words:
            addWord(word)
        
        self.curr_word = deque()
            

    def query(self, letter: str) -> bool:
        
        
        def checker(word):
            
            curr = self.root
            for i in range(len(word)-1,-1,-1):
                if word[i] in curr:
                    curr = curr[word[i]]
                    if "*" in curr:
                        return True
                else:
                    return False
                
            return False
                
                
        
        self.curr_word.append(letter)
        if len(self.curr_word) > 200:
            self.curr_word.popleft()
            
        return checker(self.curr_word)
           
        
        
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)