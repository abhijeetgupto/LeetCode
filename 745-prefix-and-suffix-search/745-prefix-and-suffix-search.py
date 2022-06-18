class WordFilter:

    def __init__(self, words: List[str]):
        
        self.dic = {}
        for idx, word in enumerate(words):
            for i in range(len(word)+1):
                for j in range(len(word)+1):
                    self.dic[word[:i]+"#"+word[j:]] = idx
        
        
    def f(self, prefix: str, suffix: str) -> int:
        
        s = prefix + "#" + suffix
        if s in self.dic:
            return self.dic[s]
        
        return -1
        
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)