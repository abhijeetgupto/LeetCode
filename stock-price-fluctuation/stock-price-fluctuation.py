class StockPrice:

    def __init__(self):
        self.dic = {}
        self.time = -math.inf
        self.l = []

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.dic:
            self.l.remove(self.dic[timestamp])
            
        if timestamp > self.time:
            self.time = timestamp
            
        self.dic[timestamp] = price
        bisect.insort(self.l,price)
        

    def current(self) -> int:
        return self.dic[self.time]
        
    def maximum(self) -> int:
        return self.l[-1]

    def minimum(self) -> int:
        return self.l[0]
       


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()