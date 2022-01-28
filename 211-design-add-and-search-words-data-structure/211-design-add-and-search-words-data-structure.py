from collections import defaultdict
class WordDictionary:

    def __init__(self):
        self.data = defaultdict(list)
        
    def addWord(self, word: str) -> None:
        n = len(word)
        self.data[n].append(word)
            
    def search(self, word: str) -> bool:
        d = {}
        for i in range(len(word)):
            if word[i] != ".":
                d[i] = word[i]
                
        try :
            l = self.data[len(word)]
        except :
            return False
                
                
        if not d :
            for dic in l :
                if len(dic) == len(word) :
                    return True
            return False
            
        else :
            
            for dic in l :
                flag = True
                for key in d :
                    if d[key] != dic[key] :
                        flag = False
                        break
                if flag :
                    return True
            return False

