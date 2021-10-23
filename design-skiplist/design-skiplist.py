class Skiplist:

    def __init__(self):
        self.dic = {}
        
    def search(self, target: int) -> bool:
        return target in self.dic
        
    def add(self, num: int) -> None:
        if num in self.dic:
            self.dic[num]+=1
        else:
            self.dic[num] = 1
        
    def erase(self, num: int) -> bool:
        
        if num in self.dic:
            if self.dic[num]==1:
                self.dic.pop(num)
            else:
                self.dic[num] -= 1
            return True
        return False
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)