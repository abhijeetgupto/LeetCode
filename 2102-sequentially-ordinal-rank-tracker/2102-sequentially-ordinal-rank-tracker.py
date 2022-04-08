from sortedcontainers import SortedList

class SORTracker:

    def __init__(self):
        
        self.l = SortedList()
        self.dic = {}
        self.i = 0
        

    def add(self, name: str, score: int) -> None:
        
        self.l.add(score)
        if score not in self.dic :
            self.dic[score] = SortedList()
        self.dic[score].add(name)
        
    def get(self) -> str:
        
        self.i += 1
        k = self.i
        score = self.l[-k]
        right = len(self.l) - bisect.bisect_right(self.l, score) + 1
        idx = k-right
        # print(score, len(self.l), right, idx)
        # return "A"
        return self.dic[score][idx]
        
        
        
        
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()