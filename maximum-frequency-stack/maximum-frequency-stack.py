class FreqStack:

    def __init__(self):
        self.dic = {}
        self.heap = []
        self.count = 0
        heapq.heapify(self.heap)

    def push(self, val: int) -> None:
        
        self.count += 1
        if val not in self.dic :
            self.dic[val] = 1 
            
        else:
            self.dic[val] += 1
            
        temp = (-self.dic[val],-self.count, val)
        heapq.heappush(self.heap, temp)
            

    def pop(self) -> int:
        _,_, x = heapq.heappop(self.heap)
        self.dic[x] -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()