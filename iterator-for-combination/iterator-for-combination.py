class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        
        l = sorted(list(characters))
        self.p = list(itertools.combinations(l,combinationLength))
        
    def next(self) -> str:
        
        x = self.p.pop(0)
        return "".join(x)

    def hasNext(self) -> bool:
        
        if self.p :
            return True
        return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()