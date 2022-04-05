class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        
        
        self.keys = keys
        self.values = values
        
        self.map = {}        
        for i in range(len(keys)) :
            self.map[keys[i]] = values[i]
        
        self.encrypted = {}
        for word in dictionary :
            x = self.encrypt(word)
            if x!=0 :
                if x not in self.encrypted:
                    self.encrypted[x] = 0
                self.encrypted[x] += 1
            

    def encrypt(self, word1: str) -> str:
        
        res = ""
        for char in word1 :
            if char in self.map : 
                res += self.map[char]
            else:
                return 0
        return res
    
    def decrypt(self, word2: str) -> int:
        if word2 in self.encrypted : 
            return self.encrypted[word2]
        return 0
        
        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)