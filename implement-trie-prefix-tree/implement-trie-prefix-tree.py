class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.data.append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        return word in self.data

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for word in self.data :
            if len(word) >= len(prefix) :
                for i in range(len(prefix)):
                    flag = True
                    if prefix[i] != word[i]:
                        flag = False
                        break
                if flag :
                    return True
        return False

        