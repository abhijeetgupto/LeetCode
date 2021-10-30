import sortedcontainers

class StockPrice:

    def __init__(self):
        self.dic = {}
        self.time = -math.inf
        self.l = sortedcontainers.SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.dic:
            self.l.remove(self.dic[timestamp])

        if timestamp > self.time:
            self.time = timestamp

        self.dic[timestamp] = price
        self.l.add(price)
        # bisect.insort(self.l,price)


    def current(self) -> int:
        return self.dic[self.time]

    def maximum(self) -> int:
        return self.l[-1]

    def minimum(self) -> int:
        return self.l[0]